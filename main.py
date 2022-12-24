# -*- coding: utf-8 -*-
# Python version: 3.9
# @DATE 2022-12-23
# 正如你所见 这是一个敷衍的注释
# 如果是妹子的话，不妨加个微信哟~
# @WECHAT TUBUG_CN


import requests
import sys
import configparser

# 读取配置文件
file = 'config.ini'
con = configparser.ConfigParser()
con.read(file,encoding='utf-8')
items = dict(con.items('User'))
# 读取配置文件 END

# openid = 'oWRkU0djwGt7sra2Ey2K3nxmGoEU'
openid = items['openid']

# 这里是请求头
headers = {
    "Content-Type": "application/json",
    "imprint": openid,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}

# 向小管家发请求（这里只是或许一些必要的id
get_id = requests.request(
    'post',
    'https://a.welife001.com/getUser',
    data='{"openid":"' + openid + '"}',
    headers=headers
)
print('您现在是：'+str(get_id.json()["currentUser"]["child_class_list"][int(items['userid'])-1]['name']))
_id = get_id.json()["currentUser"]["child_class_list"][int(items['userid'])-1]["_id"]
cid = get_id.json()["currentUser"]["child_class_list"][int(items['userid'])-1]["cid"]
member_id = get_id.json()["currentUser"]["child_class_list"][int(items['userid'])-1]["member_id"]
# 获取必要id END

# 这里是获取作业（如果上面的东西报错建议下面的东西就跑不了了
get_homework = requests.request(
    'get',
    'https://a.welife001.com/info/getParent?type=-1&members='+member_id+'&page=0&size=10&date=-1&hasMore=true&isRecent=true',
    headers=headers
)

print('你有'+str(len(get_homework.json()["data"]))+'项作业未完成:')
for subject_num in range(len(get_homework.json()["data"])):
    print(get_homework.json()["data"][subject_num]["title"])
choose = input('请输入你要抄的作业：[1-'+str(len(get_homework.json()["data"]))+']：')
try:
    homework_id = get_homework.json()["data"][int(choose)-1]["_id"]
except IndexError:
    print('看看你输入的什么？')
    sys.exit(0)
# 获取作业列表 END
# print(get_homework.json()["data"][4]["_id"])
# 获取答案
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

steal_homework = requests.request(
    'post',
    'https://a.welife001.com/applet/notify/check4teacherList',
    headers=headers,
    data='''
    {
        "_id": "'''+homework_id+'''",
        "sortType": "shijiandaoxu",
        "selectType": "quanbu",
        "page": 0,
        "size": 10,
        "last_accId": "",
        "isNew": "nextId",
        "extra": 1
    }
    '''
)


'''
curl 'https://a.welife001.com/applet/notify/check4teacherList' \
-X POST \
-H 'Host: a.welife001.com' \
-H 'Accept: */*' \
-H 'Accept-Language: zh-CN,zh-Hans;q=0.9' \
-H 'Connection: keep-alive' \
-H 'Referer: https://servicewechat.com/wx23d8d7ea22039466/1802/page-frame.html' \
-H 'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E217 MicroMessenger/6.8.0(0x16080000) NetType/WIFI Language/en Branch/Br_trunk MiniProgramEnv/Mac' \
-H 'Content-Length: 144' \
-H 'Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVuaWQiOiJvV1JrVTBkandHdDdzcmEyRXkySzNueG1Hb0VVIiwidW5pb25pZCI6Im90Z3pwdjU2T3pBcUNXVGpfSE9qTklVY09uNGciLCJwbGF0Zm9ybSI6Im1pbmkiLCJleHAiOjE2NzY3OTI4NjMwMjQsImlhdCI6MTY3MTYwODg2M30.x-afJTAo6hfaNm5x6HGDQyDiNK_AtnMu9FQ6rC-sOGw' \
-H 'imprint: oWRkU0djwGt7sra2Ey2K3nxmGoEU' \
-H 'Content-Type: application/json' \
-d '{"_id":"63a2cb999d775ec3c7d2f773","sortType":"shijiandaoxu","selectType":"quanbu","page":0,"size":10,"last_accId":"","isNew":"nextId","extra":1}' \
--proxy http://localhost:9090
'''

abcd = ['A', 'B', 'C', 'D']

for i in range(len(url.json()["data"]["notify"]["attach"]["subjects"])):
    try:
        for a in range(4):
            if url.json()["data"]["notify"]["attach"]["subjects"][i]["details"][a]["right"] == 'y':
                print('第' + str(i + 1) + '题选' + abcd[a])
    except IndexError:
        for good_baby in range(len(steal_homework.json()['data'])):
            print(steal_homework.json()['data'][good_baby]['name'])
        who_homework = input('请输入你要抄谁的作业[1-'+str(len(steal_homework.json()['data']))+']:')
        for photo_list in range(len(steal_homework.json()['data'][int(who_homework)-1]['attach']['subjects'][i]['answers'])):
            print('https://img.banjixiaoguanjia.com/'+steal_homework.json()['data'][int(who_homework) - 1]['attach']['subjects'][i]['answers'][photo_list])
        # print(steal_homework.json()['data'][int(who_homework)-1]['attach']['subjects'][i]['answers'])
        print('第'+str(i+1)+'题是大题，看链接！')
# 获取答案 END

input('请按任意键退出...')
# print(len(url.json()["data"]["notify"]["attach"]["subjects"]))
# print(url.json()["data"]["notify"]["attach"]["subjects"][11]["details"][2]["right"])
