"""
 description: 爬取1688榴莲
 time: 2019/8/31 00:33
 author: objcat
 version: 1.0
"""
import json
import re
import requests
import urllib3
from tools.tool import write_to_file

# 去掉ssl警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

header = {
    # 自己上浏览器抓去
    'cookie': 'cna=7Kz7FmCAB3UCAXbNMUPo/NNs; cookie2=1aa72e8ad93e0829ed1f1a9c41de5c98; t=0f1f4770e437bbab849022bdf5cde95d; _tb_token_=7ba3887e6e3e5; cookie1=B0Tw40p%2Bnr9QRkktsAYh8Lle6sMmXp65dnQQMDBr1Q4%3D; cookie17=UoewCLQXAHssrw%3D%3D; sg=%E6%A2%B302; csg=5d90609a; lid=%E6%A2%B3%E5%A4%B4%E7%9A%84%E6%9C%A8%E6%A2%B3; unb=1648546690; uc4=nk4=0%40qzbdiJKrqH2c0xDcrHgPqJ7xcSn%2F&id4=0%40UO%2B2s806mFvtVbeDQi3V4ehF0o4d; __cn_logon__=true; __cn_logon_id__=%E6%A2%B3%E5%A4%B4%E7%9A%84%E6%9C%A8%E6%A2%B3; ali_apache_track=c_mid=b2b-1648546690|c_lid=%E6%A2%B3%E5%A4%B4%E7%9A%84%E6%9C%A8%E6%A2%B3|c_ms=1; ali_apache_tracktmp=c_w_signed=Y; _nk_=%5Cu68B3%5Cu5934%5Cu7684%5Cu6728%5Cu68B3; last_mid=b2b-1648546690; _csrf_token=1587203660700; UM_distinctid=1718cb40d1d12e-0b3255933b5ffa-376b4502-1fa400-1718cb40d1e5e4; CNZZDATA1253659577=211053041-1587201783-%7C1587201783; taklid=a9e5da548de6439797a1fe43d7a3c616; _is_show_loginId_change_block_=b2b-1648546690_false; _show_force_unbind_div_=b2b-1648546690_false; _show_sys_unbind_div_=b2b-1648546690_false; _show_user_unbind_div_=b2b-1648546690_false; __rn_alert__=false; alicnweb=touch_tb_at%3D1587202444192%7Clastlogonid%3D%25E6%25A2%25B3%25E5%25A4%25B4%25E7%259A%2584%25E6%259C%25A8%25E6%25A2%25B3; x5sec=7b226c61707574613b32223a223532613138343036626366356463643133373962313539633333653632643631434a2b65362f51464550337378757a4e37592f4662786f4d4d5459304f4455304e6a59354d447378227d; JSESSIONID=8140863E13769A6407B85DCA5C45A7AD; l=eBMXE79IQ4oSnOCkBOfNdfR-jLQOIIRAgu-N2kJJiT5POl6e588VWZXaeqtwCnGVhssJJ3rEQAfvBeYBqIYoLjD5jrfiLYHmn; isg=BN7ecaJ6DJOqb1h3cV54_EzrL3Qgn6IZJxeukohnRCEcq36F8Sv1KF1Jp7enk5ox'
}


def get_json(page):
    res = requests.get(
        'https://data.p4psearch.1688.com/data/ajax/get_premium_offer_list.json?beginpage=1&keywords=%E6%B3%B0%E5%9B%BD%E6%A6%B4%E8%8E%B2&sortType=&descendOrder=&province=&city=&priceStart=&priceEnd=&dis=&spm=a312h.2018_new_sem.dh_001.1.283e7778w1R94P&cosite=baidujj_pz&location=re&trackid=%7Btrackid%7D&keywordid=%7Bkeywordid%7D&provinceValue=%E6%89%80%E5%9C%A8%E5%9C%B0%E5%8C%BA&p_rs=true&pageid=596f52d5pnced2&p4pid=11ad02b8be3b43519b098472625b50c1&asyncreq='.format(
            page), headers=header, verify=False)
    print(res.text)
    analysis_json(res.text)


def analysis_json(j):
    r = json.loads(j)
    l = list()
    for d in r['data']['content']['offerResult']:
        d2 = {
            'title': d['title'],
            'companyName': d['attr']['company']['name'],
            'url': d['eurl'],
            'imgUrl': d['imgUrl'],
            'price': d['priceMoney']['amount']
        }
        # if 'https' not in d2['url'] and '新鲜' in d2['title']:
        l.append(d2)

    print(l)
    for dic in l:
        get_html('https:' + dic['url'], dic)


def get_html(url, dic):
    # 'https://detail.1688.com/offer/589913568703.html'
    res = requests.get(url, headers=header, verify=False)
    analysis_html(res.text, dic)


def analysis_html(h, dic):
    pattern = re.compile(r'<td class="name">.*?<span>(.*?)</span>.*?'
                         r'<td class="price">.*?<em class="value">(.*?)</em>.*?'
                         r'<td class="count">.*?<em class="value">(.*?)</em>.*?'
                         , re.S)

    items = re.findall(pattern, h)
    l = list()
    for item in items:
        try:
            d = {
                'name': item[0],
                'price': item[1],
                'num': item[2],
                'companyName': dic['companyName'],
                'url': 'https' + dic['url']
            }
            l.append(d)
        except Exception as e:
            print(e)
            continue

    if len(l) > 0:
        # 打印数组
        print(l)
        # 写入result.txt文件
        write_to_file(path="./result2.txt", content=json.dumps(l, ensure_ascii=False) + "\n")
        # 写入数据库
        # save_to_mongo(MONGO_TABLE_LIULIAN_NAME, l)
        # 打印3-4斤榴莲价格以及公司
        # for dic in l:
        #     if '3-4' in dic['name']:
        #         print(dic)


def main():
    # for i in range(1, 6):
    #     get_json(i)
    get_json(1)


if __name__ == '__main__':
    main()
