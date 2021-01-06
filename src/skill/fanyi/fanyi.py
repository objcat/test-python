import os
import re
import json
import random
import hashlib
import time

from requests import request

"""
目前在做日文iOS项目 所以写一个程序来翻译文本中的日文
原理是调用百度翻译的免费api进行翻译
"""


def strings_to_file():
    pattern = re.compile(r'"(.*?)" = "(.*?)";', re.S)
    fo = open("./Localizable.strings", "r")
    newFile = open("./1.txt", "w")

    for line in fo.readlines():
        items = re.findall(pattern, line)
        for item in items:
            newFile.write(item[0] + "," + item[1] + "\n")
            print(item[0])
            print(item[1])
    fo.close()


def file_translation():
    fo = open("./1.txt", "rb")
    f2 = open("./2.txt", "w", encoding="utf-8")

    for line in fo.readlines():
        s = line.decode()
        a = s.split(',')
        r = request_baidu(a[1])
        r = r.replace("\n", "")
        s = a[0] + "|" + r + "|" + a[1]
        print(s)
        f2.write(s)
        time.sleep(1)
    fo.close()
    f2.close()


def request_baidu(q):
    salt = random.randint(0, 100)
    appid = "20200417000423061"
    signStr = appid + q + str(salt) + "80Klm6_i5EIZcSIPVNI8"
    body = {
        "q": q,
        "from": "jp",
        "to": "zh",
        "appid": appid,
        "salt": salt,
        "tts": "1",
        "dict": "1",
        "action": "0",
        "sign": hashlib.md5(signStr.encode()).hexdigest()
    }
    print(q)
    req = request(method="post", url="http://api.fanyi.baidu.com/api/trans/vip/translate", data=body)
    j = json.loads(req.content)
    print(j)
    arr = j["trans_result"]

    result = ""
    for dic in arr:
        result += dic["dst"]
    return result


def translation2():
    f1 = open("./FC00I21CheckItemCheckData.txt", encoding="utf-8")
    f3 = open("./3.txt", "a", encoding="utf-8")
    arr = f1.readlines()
    result = []
    dic = {}
    i = 1
    for line in arr:

        if line.__contains__("@property") or line.__contains__(" * "):

            if line.__contains__("@property"):
                index1 = line.index("*")
                index2 = line.index(";")
                line = line[index1 + 1:index2]
                line = line.strip()
                dic['name'] = line

            if line.__contains__(" * "):
                line = line.replace("*", "")
                line = line.strip()
                dic['jp'] = line
                # 进行翻译
                tr = request_baidu(line)
                dic['tr'] = tr

            if i % 2 == 0:
                # f3.write(dic['name'] + "|" + dic['jp'] + "\n")
                f3.write(dic['name'] + "|" + dic['tr'] + "|" + dic['jp'] + "\n")
                time.sleep(1)
                print(dic)
                result.append(dic)

            i += 1

    s = json.dumps(result)
    a = s.encode('utf-8').decode('unicode_escape')
    print(a)


def start():
    # file_translation()
    translation2()


if __name__ == '__main__':
    start()
    pass
