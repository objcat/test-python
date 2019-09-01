"""
 description: qq农场自动收菜种菜
 time: 2019/8/22 16:34
 author: objcat
 verson: 1.0
"""

import requests
from bs4 import BeautifulSoup
from tools.tool import sleep_5_do, sleep_1_print

headers = {
    'cache-control': "no-cache",
    "Cookie": "手机qq空间app -> 小游戏 -> qq农场wap",
    "User-Agent": "QZONEJSSDK/8.3.6.1 QQJSSDK/1.2 Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_4 like Mac OS X) AppleWebKit/605.1.15"
}

place = "0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23"


def harvest():
    """
    收获
    :return:
    """
    url = "http://mcapp.z.qq.com/nc/cgi-bin/wap_farm_harvest"
    querystring = {"sid": "", "B_UID": "0", "place": place, "g_ut": "3", "time": "-2147483648"}
    payload = ""
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    log(response)


def fer():
    """
    施肥
    :return:
    """
    url = "http://mcapp.z.qq.com/nc/cgi-bin/wap_farm_harvest"
    querystring = {"sid": "", "g_ut": "3", "act": "fer",
                   "place": place, "random": "242596"}
    payload = ""
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    log(response)


def dig():
    """
    铲地
    :return:
    """
    url = "http://mcapp.z.qq.com/nc/cgi-bin/wap_farm_dig"
    querystring = {"sid": "c", "g_ut": "3", "place": place, "cropStatus": "7"}
    payload = ""
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    log(response)


def clear_weed():
    """
    除草
    :return:
    """
    url = "http://mcapp.z.qq.com/nc/cgi-bin/wap_farm_opt"
    querystring = {"sid": "c", "B_UID": "237631497", "act": "clearWeed", "place": place, "g_ut": "3",
                   "name": "", "time": "-2147483648"}
    payload = ""
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    log(response)


def spraying():
    """
    杀虫
    :return:
    """
    url = "http://mcapp.z.qq.com/nc/cgi-bin/wap_farm_opt"
    querystring = {"sid": "", "B_UID": "0", "act": "spraying", "place": place, "g_ut": "3", "name": "",
                   "time": "-2147483648%20"}
    payload = ""
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    log(response)


def water():
    """
    浇水
    :return:
    """
    url = "http://mcapp.z.qq.com/nc/cgi-bin/wap_farm_opt"
    querystring = {"sid": "c", "B_UID": "237631497", "act": "water", "place": place, "g_ut": "3",
                   "name": "", "time": "-2147483648"}
    payload = ""
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    log(response)


def plant():
    """
    种植牧草
    :return:
    """
    url = "http://mcapp.z.qq.com/nc/cgi-bin/wap_farm_plant"
    querystring = {"sid": "c", "g_ut": "3", "v": "0", "cid": "40", "landid": place}
    payload = ""
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    log(response)


def log(response):
    soup = BeautifulSoup(response.content, features="html.parser")
    # print(soup.prettify())
    arr = soup.find_all("p")
    for p in arr:
        try:
            index = p['class'].index("txt-warning2")
            if index >= 0:
                for string in p.strings:
                    print(string.strip().replace(" ", ""))
        except Exception as e:
            pass


def do_nc():
    # response = requests.request("GET", "http://mooc.egivesoft.cn/static/wechat/enterprise/index.html")
    # soup = BeautifulSoup(response.content, features="html.parser")
    # print(soup.prettify())

    print("***** 农场伴侣v1.0 ***** author:objcat")
    sleep_1_print("正在浇水...")
    sleep_5_do(water)
    sleep_1_print("正在杀虫...")
    sleep_5_do(spraying)
    sleep_1_print("正在除草...")
    sleep_5_do(clear_weed)
    sleep_1_print("正在收获作物...")
    sleep_5_do(harvest)
    sleep_1_print("正在清理地块...")
    sleep_5_do(dig)
    sleep_1_print("正在种植牧草...")
    sleep_5_do(plant)
