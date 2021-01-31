import os
from requests import request
import threading
import time
import hashlib
from urllib.parse import urlparse
import glob

# 下载最大线程数
max_thread = 30
# 当前下载线程数
count_thread = 0
# ts总文件数
ts_count = 0


class MyThread(threading.Thread):
    """
    创建多线程进行下载 提高下载速度
    """

    def __init__(self, line, download_path, progress):
        threading.Thread.__init__(self)
        self.line = line
        self.download_path = download_path
        self.progress = progress

    def run(self) -> None:
        download(self.line, self.download_path, self.progress)


def analysis_m3u8_file_and_download(m3u8_path, download_path, domain):
    """
    解析m3u8文件并进行下载
    :param m3u8_path: m3u8文件本地路径
    :param download_path: 文件下载路径
    :param domain: 域名
    :return:
    """
    global count_thread
    global ts_count
    f = open(m3u8_path)
    lines = f.readlines()
    f.close()
    ts_count = len([line for line in lines if "ts" in line])
    total_lines = len(lines)
    # 计数
    i = 0
    # 进度
    progress = 1
    while True:

        # 判断循环是否到头
        if i < total_lines:
            line = lines[i]
            i += 1
        else:
            break

        if "ts" in line:
            new_file_path = download_path + os.path.basename(line.strip())
            if os.path.exists(new_file_path):
                progress += 1
                continue

            # time.sleep(2)
            # 限制最大线程数
            if count_thread < max_thread:
                download_url = build_download_url(domain, line)
                print("加入下载队列:" + download_url.strip())
                print("进度 " + str(progress) + " / " + str(ts_count))
                progress += 1
                count_thread += 1
                MyThread(download_url, download_path, progress).start()
            else:
                # print(f"下载队列已达到 {max_thread} 等待中...")
                # 如果线程满了这一次循环就作废
                i -= 1
                time.sleep(2)
                continue

    while True:
        if (count_thread):
            print(f"等待下载完成, 当前线程数目 {count_thread} ")
            time.sleep(2)
        else:
            if check_file_count(download_path):
                print("总进度 " + str(ts_count) + " / " + str(ts_count) + " 下载完成!")
                break
            else:
                print("将开始下载...")
                analysis_m3u8_file_and_download(m3u8_path, download_path, domain)
                break


def check_file_count(download_path):
    """
    对比本地文件数与m3u8中实际文件数确保完整
    :param download_path:
    :return:
    """
    number = glob.glob(download_path + "*.ts")
    count = len(number)
    print("下载结束, 正在检测文件是否有遗漏")
    if count == ts_count:
        print(f"恭喜你文件很完整")
        return True
    else:
        print(f"检测到文件遗漏 已下载 {count} 个 剩余 {ts_count - count} 个")
        return False
    pass


def build_download_url(domain, line):
    filename = os.path.basename(m3u8_url)
    download_base_url = m3u8_url.replace(filename, "")
    return download_base_url + line
    # 不同的拼接方式
    # return domain + line


def download(download_url, download_path, progress):
    """
    下载文件
    :param download_url: 下载地址
    :param download_path: 下载路径
    :return:
    """
    global count_thread
    new_file_path = download_path + os.path.basename(download_url.strip())
    try:
        res = request(url=download_url.strip(), method="get", timeout=20, headers=http_header)
        with open(new_file_path, "wb") as video:
            video.write(res.content)
        count_thread -= 1
    except Exception as e:
        print(f"进度 {progress} 下载失败, 继续进行下一个")
        count_thread -= 1
        # time.sleep(2)
        # download(download_url, download_path)


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
            cmd = cmd + " " + "0.ts"
        else:
            cmd = cmd + "+" + line
    with open(download_path + "0.bat", "w") as bat:
        bat.write(cmd)


def download_m3u8_file():
    """
    下载m3u8文件
    :param url: m3u8文件url
    :return:
    """

    url = m3u8_url
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
            print(http_header)
            req = request(method="get", url=url, headers=http_header)
            fo = open(m3u8_path, "w", encoding="utf-8")
            fo.write(req.content.decode())
            fo.close()
            print("m3u8文件下载成功:" + m3u8_path)
            return m3u8_path, download_path, domain
        except Exception as e:
            print(e)
    else:
        return m3u8_path, download_path, domain


http_header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"
}

# 下载根路径 设置成 "." 则为当前目录
base_path = "D:/video"
m3u8_url = "https://www.xxxx.com/xxx.m3u8"


def start():
    # 下载m3u8文件
    m3u8_path, download_path, domain = download_m3u8_file()
    # 解析文件并下载ts
    analysis_m3u8_file_and_download(m3u8_path, download_path, domain)
    # 生成自动合成脚本
    mix(m3u8_path, download_path)


if __name__ == '__main__':
    start()
