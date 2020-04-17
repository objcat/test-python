
import re
import json
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
        # print(line)
    # print(fo)
    fo.close()


def file_translation():
    body = {
        "query": "要是正、要重点点検項目がありますが、社内指示が既に最大数書き込みされているため、\n 要是正、要重点点検内容が社内指示に自動反映できません。",
        "from": "jp",
        "to": "zh",
        "transtype": "translang",
        "sign": "700785.938560",
        "token": "0b4df204801214eefb2ea604b334cfeb",
        "domain": "common"

    }
    header = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"
    }

    req = request(method="post", url="https://fanyi.baidu.com/v2transapi?from=jp&to=zh", data=body, headers=header)
    print(req.content)


if __name__ == '__main__':
    file_translation()
    pass