# -*- coding: utf-8 -*-
# Python version: 3.9
# @DATE 2022-12-23
# 正如你所见 这是一个敷衍的注释
# 如果是妹子的话，不妨加个微信哟~
# @WECHAT TUBUG_CN


import requests
import sys
# openid = 'oWRkU0d****************mGoEU'
openid = input('请输入openid:')

headers = {
    "Content-Type": "application/json",
    "imprint": openid,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}

get_id = requests.request(
    'post',
    'https://a.welife001.com/getUser',
    data='{"openid":"' + openid + '"}',
    headers=headers
)

_id = get_id.json()["currentUser"]["child_class_list"][0]["_id"]
cid = get_id.json()["currentUser"]["child_class_list"][0]["cid"]
member_id = get_id.json()["currentUser"]["child_class_list"][0]["member_id"]

get_homework = requests.request(
    'get',
    'https://a.welife001.com/info/getParent?type=-1&members='+member_id+'&page=0&size=10&date=-1&hasMore=true&isRecent=true',
    headers=headers
)
print('你有'+str(len(get_homework.json()["data"]))+'项作业未完成:')
for subject_num in range(len(get_homework.json()["data"])):
    print(get_homework.json()["data"][subject_num-1]["title"])
choose = input('请输入你要抄的作业：[1-'+str(len(get_homework.json()["data"]))+']：')
try:
    homework_id = get_homework.json()["data"][int(choose)-1]["_id"]
except IndexError:
    print('看看你输入的什么？')
    sys.exit(0)

# print(get_homework.json()["data"][4]["_id"])

url = requests.request(
    'post', 'https://a.welife001.com/applet/notify/check4teacher',
    data='''
    {
      "extra": 1,
      "cid": "'''+cid+'''",
      "cls_ts": 1671750618852,
      "daka_day": "",
      "member_id": "'''+member_id+'''",
      "_id": "'''+homework_id+'''",
      "page": 0,
      "size": 10,
      "trial": false
    }
    ''',
    headers=headers
)

abcd = ['A', 'B', 'C', 'D']

for i in range(len(url.json()["data"]["notify"]["attach"]["subjects"])):
    try:
        for a in range(4):
            if url.json()["data"]["notify"]["attach"]["subjects"][i]["details"][a]["right"] == 'y':
                print('第' + str(i + 1) + '选' + abcd[a])
    except IndexError:
        print('第'+str(i+1)+'是大题，自己写！')

print('-----END-----')
# print(len(url.json()["data"]["notify"]["attach"]["subjects"]))
# print(url.json()["data"]["notify"]["attach"]["subjects"][11]["details"][2]["right"])