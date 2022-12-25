# -*- coding: utf-8 -*-
# Python version: 3.9
# @DATE 2022-12-23
# 正如你所见 这是一个敷衍的注释
# 如果是妹子的话，不妨加个微信哟~
# @WECHAT TUBUG_CN
import sys
from tkinter import ttk, INSERT, Text, messagebox as tk, Tk, Button
import random
import bjxgj

win = Tk()

openid = bjxgj.read_config()['openid']

headers = {
    "Content-Type": "application/json",
    "imprint": openid,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}

win.title('班级小管家学霸版v1.1.0')
# win.iconbitmap('logo.ico')
# win.geometry('759x484')
try:
    _id = bjxgj.get_id(openid=openid, headers=headers)[0]
except KeyError:
    tk.showerror(title='ERROR', message='请检查config.ini')
    sys.exit(0)
cid = bjxgj.get_id(openid=openid, headers=headers)[1]
member_id = bjxgj.get_id(openid=openid, headers=headers)[2]

text = Text(win, font=('System', 16))
text.grid(row=2, column=1, columnspan=3)
cmb = ttk.Combobox(win)
cmb.grid(row=1, column=1, columnspan=2)
text.insert(INSERT,
            '你有' + str(len(bjxgj.get_homework(headers=headers, member_id=member_id).json()["data"])) + '项作业未完成:\n')
hw_list = ['请选择你要完成的学科']
for subject_num in range(len(bjxgj.get_homework(headers=headers, member_id=member_id).json()["data"])):
    text.insert(INSERT, bjxgj.get_homework(headers=headers, member_id=member_id).json()["data"][subject_num]["title"] +
                '\n')
    hw_list = hw_list + bjxgj.get_homework(headers=headers, member_id=member_id).json()["data"][subject_num][
        "title"].split('\n')
    cmb['value'] = hw_list
cmb.current(0)


def hw_list_():
    homework_id = bjxgj.get_homework(headers=headers, member_id=member_id).json()["data"][hw_list.index(cmb.get()) - 1][
        "_id"]
    get_answer = bjxgj.get_answer(cid=cid, member_id=member_id, homework_id=homework_id, headers=headers)
    data = bjxgj.homework_photo(headers=headers, homework_id=homework_id).json()['data']
    if get_answer.json()['data']['notify']['feedback_type'] == 24:
        text.delete(1.0, "end")
        data = bjxgj.homework_photo(headers=headers, homework_id=homework_id).json()['data']
        num = len(bjxgj.homework_photo(headers=headers, homework_id=homework_id).json()['data'])
        chooses = random.randint(1, num)
        for photo_num in range(len(data[int(chooses) - 1]['feedback_photo'])):
            text.insert(INSERT, 'https://img.banjixiaoguanjia.com/' + data[int(chooses) - 1]['feedback_photo'][
                photo_num] + '\n')
            # print('https://img.banjixiaoguanjia.com/' + data[int(chooses) - 1]['feedback_photo'][photo_num])
    elif get_answer.json()['data']['notify']['feedback_type'] == -1:
        text.delete(1.0, "end")
        abcdefg = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        _data = bjxgj.get_answer(cid=cid, headers=headers, homework_id=homework_id, member_id=member_id).json()['data']
        for i in range(len(_data["notify"]["attach"]["subjects"])):
            try:
                for a in range(len(_data["notify"]["attach"]["subjects"][0]["details"])):
                    if _data["notify"]["attach"]["subjects"][i]["details"][a]["right"] == 'y':
                        text.insert(INSERT, '第' + str(i + 1) + '题选' + abcdefg[a] + '\n')
                        # print('第' + str(i + 1) + '题选' + abcdefg[a])
            except IndexError:
                who_homework = 1
                for photo_list in range(
                        len(data[int(who_homework) - 1]['attach']['subjects'][i]['answers'])):
                    text.insert(INSERT, '第' + str(i + 1) + '题是大题，看链接！\n')
                    text.insert(INSERT, 'https://img.banjixiaoguanjia.com/' +
                                data[int(who_homework) - 1]['attach']['subjects'][i]['answers'][
                                    photo_list] + '\n')
                    # print('https://img.banjixiaoguanjia.com/' +
                    #       data[int(who_homework) - 1]['attach']['subjects'][i]['answers'][
                    #           photo_list])
                # print(steal_homework.json()['data'][int(who_homework)-1]['attach']['subjects'][i]['answers'])
    print(homework_id)


def about():
    tk.showinfo(title='关于我...', message='小管家学霸版\n版本：v1.1.0\n\nCopyright © 2022-2022 TUBUG.\nAll rights reserved')


def _exit():
    sys.exit(1)


button = Button(win, text='确认', command=hw_list_).grid(row=1, column=3)
about = Button(win, text='关于', command=about).grid(row=3, column=1, padx=5, pady=5)
exit_ = Button(win, text='退出', command=_exit).grid(row=3, column=3, padx=5, pady=5)

win.mainloop()
