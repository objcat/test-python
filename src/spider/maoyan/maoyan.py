"""
 description: 爬取猫眼电影top100
 time: 2019/9/1 10:33
 author: objcat
 version: 1.0
"""
import json
import re
import requests
from multiprocessing import Pool
from requests.exceptions import RequestException
from tools.tool import write_to_file, save_to_mongo
from configs.config import MONGO_TABLE_MAOYAN_NAME


def get_html(url):
    """使用requests库获取html
    :param url: url
    :return: html
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def analysis_html(html):
    """解析html
    :param html: html字符串
    :return: dictionary
    """
    pattern = re.compile(r'class="board-index.*?>(\d+)</i>.*?'
                         r'title="(.*?)".*?'
                         r'class="image-link".*?data-src="(.*?)".*?'
                         r'class="star">(.*?)</p>.*?'
                         r'class="releasetime">(.*?)</p>.*?'
                         r'class="integer">(.*?)</i>.*?'
                         r'class="fraction">(.*?)</i>.*?'
                         , re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'title': item[1],
            'image': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }


def parse_with_offset(offset):
    url = 'https://maoyan.com/board/4?offset=' + str(offset)
    html = get_html(url)
    items = analysis_html(html)
    for item in items:
        # 打印item
        print(item)
        # 写入到result.txt
        # write_to_file(json.dumps(item, ensure_ascii=False) + '\n')
        # 保存到mongodb
        # save_to_mongo(MONGO_TABLE_MAOYAN_NAME, item)


def main():
    # 多线程 并发速度快 但是无序
    pool = Pool()
    pool.map(parse_with_offset, [i * 10 for i in range(10)])
    # 单线程 队列 速度慢 但是有序
    # for i in range(10):
    #     parse_with_offset(i * 10)


if __name__ == '__main__':
    main()
