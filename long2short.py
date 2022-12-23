from flask import Flask, request
import requests
app = Flask(__name__)

openid = "oWRkU0djwGt7sra2Ey2K3nxmGoEU"
headers = {
    "Content-Type": "application/json",
    "imprint": openid,
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E217 MicroMessenger/6.8.0(0x16080000) NetType/WIFI Language/en Branch/Br_trunk MiniProgramEnv/Mac"
}


def long2short(url_):

    long2short_req = requests.request(
        'post',
        'https://a.welife001.com/applet/long2shortByToken',
        headers=headers,
        data='{"link":"' + url_ + '","type":0,"day":0}'
    )
    return long2short_req.json()["data"]


@app.route('/l2s', methods=['GET', 'POST'])
def long2short_web():
    url = request.args.get('url')
    if url is None:
        return 'ERROR!<br/>格式：/l2s?url=https://xxxx.com'
    return long2short(url_=url)


if __name__ == '__main__':
    app.run()
