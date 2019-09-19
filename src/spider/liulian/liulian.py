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
from tools.tool import write_to_file, save_to_mongo
from configs.config import MONGO_TABLE_LIULIAN_NAME

# 去掉ssl警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

header = {
    # 自己上浏览器抓去
    'cookie': 'cna=aGPUFc2JbU4CAdOh9TQWQHdb; lid=%E6%A2%B3%E5%A4%B4%E7%9A%84%E6%9C%A8%E6%A2%B3; ali_apache_track=c_mid=b2b-1648546690|c_lid=%E6%A2%B3%E5%A4%B4%E7%9A%84%E6%9C%A8%E6%A2%B3|c_ms=1; UM_distinctid=16cdd5f0ea6445-0819ffdb3d4e3e-5373e62-1fa400-16cdd5f0ea7897; ptid=aGPUFc2JbU4CAdOh9TQWQHdb; last_mid=b2b-1648546690; cookie2=14b1588e647c71777c520d5ae0bdae42; t=4e420ecfb1f640e8a33a80df3d3575c6; _tb_token_=e3bb66661ee8d; cookie1=B0Tw40p%2Bnr9QRkktsAYh8Lle6sMmXp65dnQQMDBr1Q4%3D; cookie17=UoewCLQXAHssrw%3D%3D; sg=%E6%A2%B302; csg=28dfbe7e; unb=1648546690; uc4=id4=0%40UO%2B2s806mFvtVbeDQiMgJjEVW1%2BF&nk4=0%40qzbdiJKrqH2c0xDcrHbyQOtrH7ge; __cn_logon__=true; __cn_logon_id__=%E6%A2%B3%E5%A4%B4%E7%9A%84%E6%9C%A8%E6%A2%B3; ali_apache_tracktmp=c_w_signed=Y; _nk_=%5Cu68B3%5Cu5934%5Cu7684%5Cu6728%5Cu68B3; _csrf_token=1567343093873; _is_show_loginId_change_block_=b2b-1648546690_false; _show_force_unbind_div_=b2b-1648546690_false; _show_sys_unbind_div_=b2b-1648546690_false; _show_user_unbind_div_=b2b-1648546690_false; __rn_alert__=false; l=cBS9vZvrqFDdR3-EXOCw5uI8Uh7OSIRAguPRwdxvi_5Kx1Y_zD_Oklja7ev6VjWd9fLB4ezvPZ99-etliZe_Ch7x5tVf.; isg=BOrqSTLpQ85RuM8uYeLwSazqO1BM82zG41EAx3Sjlj3Ip4phXOu-xTCVM5MeV-ZN; alicnweb=touch_tb_at%3D1567343096008%7Clastlogonid%3D%25E6%25A2%25B3%25E5%25A4%25B4%25E7%259A%2584%25E6%259C%25A8%25E6%25A2%25B3'
}


def get_json(page):
    res = requests.get(
        'https://data.p4psearch.1688.com/data/ajax/get_premium_offer_list.json?'
        'beginpage=1&asyncreq={}&keywords=%E9%87%91%E6%9E%95%E5%A4%B4%E6%A6%B4%E8%8E%B2&'
        'sortType=price&descendOrder=false&province=&city=&priceStart=40&priceEnd=200&'
        'dis=&spm=a312h.2018_new_sem.dh_003.2.57256ac1KWWuzY&cosite=baidujj_pz&location=re&'
        'trackid=%7Btrackid%7D&keywordid=%7Bkeywordid%7D&'
        'provinceValue=%E6%89%80%E5%9C%A8%E5%9C%B0%E5%8C%BA&pageid=78e86ac1q210bK&p4pid=397'
        '06c77a4ca42db859a324ac7ddb0ae'.format(
            page), headers=header, verify=False)
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
        if 'https' not in d2['url'] and '新鲜' in d2['title']:
            l.append(d2)

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
        # write_to_file(json.dumps(l, ensure_ascii=False) + "\n")
        # 写入数据库
        # save_to_mongo(MONGO_TABLE_LIULIAN_NAME, l)
        # 打印3-4斤榴莲价格以及公司
        # for dic in l:
        #     if '3-4' in dic['name']:
        #         print(dic)


def main():
    for i in range(1, 6):
        get_json(i)


if __name__ == '__main__':
    main()
