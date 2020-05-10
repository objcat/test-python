import os
from requests import request
import threading
import time
import hashlib
from urllib.parse import urlparse


class MyThread(threading.Thread):
    """
    创建多线程进行下载 提高下载速度
    """

    def __init__(self, line, download_path):
        threading.Thread.__init__(self)
        self.line = line
        self.download_path = download_path

    def run(self) -> None:
        download(self.line, self.download_path)


def analysis_m3u8_file_and_download(m3u8_path, download_path, domain):
    """
    解析m3u8文件并进行下载
    :param m3u8_path: m3u8文件本地路径
    :param download_path: 文件下载路径
    :param domain: 域名
    :return:
    """

    f = open(m3u8_path)
    lines = f.readlines()
    f.close()
    total = len([line for line in lines if "ts" in line])
    i = 1
    for line in lines:
        if "ts" in line:
            new_file_path = download_path + os.path.basename(line.strip())
            if os.path.exists(new_file_path):
                i += 1
                continue
            time.sleep(1)
            download_url = domain + line
            print("开始下载:" + download_url.strip())
            print("下载进度" + str(i) + " / " + str(total))
            i += 1
            MyThread(download_url, download_path).start()


def download(download_url, download_path):
    """
    下载文件
    :param download_url: 下载地址
    :param download_path: 下载路径
    :return:
    """

    new_file_path = download_path + os.path.basename(download_url.strip())
    try:
        res = request(url=download_url.strip(), method="get", timeout=20)
        with open(new_file_path, "wb") as video:
            video.write(res.content)
    except Exception as e:
        print("连接断开正在重试 " + download_url)
        print(e)
        download(download_url, download_path)


def mkdir(path):
    """
    创建文件夹
    :param path:
    :return:
    """
    exist = os.path.exists(path)
    if not exist:
        os.makedirs(path)
    return path


def mix(m3u8_path, download_path):
    """
    制作合成脚本
    因为m3u8下载后是一个个的ts文件 所以需要脚本来合成为一个视频文件
    :param m3u8_path: m3u8的文件路径
    :param download_path: 下载路径
    :return:
    """

    cmd = "copy/b"
    arr = list()
    f = open(m3u8_path)
    line = f.readline()
    while line:
        if "ts" in line:
            arr.append(os.path.basename(line.strip()))
        line = f.readline()
    f.close()
    count = arr.__len__()
    for line in arr:
        if arr.index(line) == 0:
            cmd = cmd + " " + line
        elif arr.index(line) == count - 1:
            cmd = cmd + " " + "mix.ts"
        else:
            cmd = cmd + "+" + line
    with open(download_path + "run.bat", "w") as bat:
        bat.write(cmd)


def download_m3u8_file(url):
    """
    下载m3u8文件
    :param url: m3u8文件url
    :return:
    """

    file_name = hashlib.md5(url.encode()).hexdigest()
    download_path = mkdir(base_path + "/" + file_name) + "/"
    m3u8_path = base_path + "/" + file_name + "/" + file_name + ".m3u8"
    exist = os.path.exists(m3u8_path)
    parse = urlparse(url)
    # 获取域名
    domain = parse[0] + "://" + parse[1]

    print("\n")
    print("--------------------")
    print("域名:\n" + domain)
    print("m3u8文件目录:\n" + m3u8_path)
    print("下载路径:\n" + download_path.strip())
    print("--------------------")
    print("\n")

    if not exist:
        try:
            req = request(method="get", url=url)
            fo = open(m3u8_path, "w", encoding="utf-8")
            fo.write(req.content.decode())
            fo.close()
            print("m3u8文件下载成功:" + m3u8_path)
            return m3u8_path, download_path, domain
        except Exception as e:
            print(e)
    else:
        return m3u8_path, download_path, domain


# 下载根路径 设置成 "." 则为当前目录
base_path = "D:/video"
m3u8_url = "https://www.xxxx.com/xxx.m3u8"


def start():
    # 下载m3u8文件
    m3u8_path, download_path, domain = download_m3u8_file(m3u8_url)
    # 解析文件并下载ts
    analysis_m3u8_file_and_download(m3u8_path, download_path, domain)
    # 生成自动合成脚本
    mix(m3u8_path, download_path)


if __name__ == '__main__':
    start()
