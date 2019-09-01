"""
 description: 爬取1688榴莲
 time: 2019/8/31 00:33
 author: objcat
 verson: 1.0
"""
import json
import re
import requests
import urllib3
from tools.tool import write_to_file

# 去掉ssl警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

header = {
    'cookie': '自己填'
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
        write_to_file(json.dumps(l, ensure_ascii=False) + "\n")
        # 打印3-4斤榴莲价格以及公司
        # for dic in l:
        #     if '3-4' in dic['name']:
        #         print(dic)


def main():
    for i in range(1, 6):
        get_json(i)


if __name__ == '__main__':
    main()
