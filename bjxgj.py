"""
必备模块方便以后扩展
"""


# 检查配置文件是否存在
def check_config():
    import os
    if not os.path.exists('config.ini'):
        with open('./config.ini', 'w') as file:
            file.write('[User]\nopenid=xxx\nuserid=1')
        file.close()


# 读取配置文件
def read_config(file='config.ini'):
    import configparser
    file = file
    con = configparser.ConfigParser()
    con.read(file, encoding='utf-8')
    items = dict(con.items('User'))
    return items


# 获取一下必要的id
def get_id(openid, headers):
    import requests
    get_id_requests = requests.request(
        'post',
        'https://a.welife001.com/getUser',
        data='{"openid":"' + openid + '"}',
        headers=headers
    )
    _id = get_id_requests.json()["currentUser"]["child_class_list"][int(read_config()['userid']) - 1]["_id"]
    cid = get_id_requests.json()["currentUser"]["child_class_list"][int(read_config()['userid']) - 1]["cid"]
    member_id = get_id_requests.json()["currentUser"]["child_class_list"][int(read_config()['userid']) - 1]["member_id"]
    return _id, cid, member_id


def get_homework(headers, member_id):
    import requests
    import sys
    get_homework_requests = requests.request(
        'get',
        'https://a.welife001.com/info/getParent?type=-1&members=' + member_id + '&page=0&size=10&date=-1&hasMore=true&isRecent=true',
        headers=headers
    )
    # print('你有' + str(len(get_homework_requests.json()["data"])) + '项作业未完成:')
    # for subject_num in range(len(get_homework_requests.json()["data"])):
    #     print(get_homework_requests.json()["data"][subject_num]["title"])
    # choose = input('请输入你要抄的作业：[1-' + str(len(get_homework_requests.json()["data"])) + ']：')
    # try:
    #     homework_id = get_homework_requests.json()["data"][int(choose) - 1]["_id"]
    # except IndexError:
    #     print('看看你输入的什么？')
    #     sys.exit(0)
    return get_homework_requests


def get_answer(cid, member_id, homework_id, headers):
    import requests
    url = requests.request(
        'post', 'https://a.welife001.com/applet/notify/check4teacher',
        data='''
        {
          "extra": 1,
          "cid": "''' + cid + '''",
          "cls_ts": 1671750618852,
          "daka_day": "",
          "member_id": "''' + member_id + '''",
          "_id": "''' + homework_id + '''",
          "page": 0,
          "size": 10,
          "trial": false
        }
        ''',
        headers=headers
    )
    return url


def homework_photo(headers, homework_id):
    import requests
    steal_homework = requests.request(
        'post',
        'https://a.welife001.com/applet/notify/check4teacherList',
        headers=headers,
        data='''
        {
            "_id": "''' + homework_id + '''",
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
    return steal_homework
