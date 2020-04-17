import os
import re
import json
import random
import hashlib
import time

from requests import request


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
    salt = random.randint(0,100)
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
    req = request(method="post", url="http://api.fanyi.baidu.com/api/trans/vip/translate", data=body)
    j = json.loads(req.content)
    arr = j["trans_result"]
    result = ""
    for dic in arr:
        result += dic["dst"]
    return result

if __name__ == '__main__':
    file_translation()
    pass