# description: guozhi
# date: 2021/1/9 9:54
# author: objcat
# version: 1.0


import requests
from bs4 import BeautifulSoup
from win32com.client import Dispatch
import pathlib
import os

class download:

    @classmethod
    def parse_url(cls):
        baseurl = "http://2018.emu618.net:6180"
        for page in range(53, 125):
            print(f"开始爬取第 {page} 页")
            res = requests.get(f"http://2018.emu618.net:6180/index.php?controller=site&action=pro_list&cat=23&page={page}")
            # 转换编码 乱码的时候需要转换
            res.encoding = "utf-8"
            main_page = BeautifulSoup(res.text, "html.parser")
            target = main_page.find("div", class_="games_list").find_all("a", class_="p_name")
            for a in target:
                child_res = requests.get(baseurl + a.get("href"))
                child_page = BeautifulSoup(child_res.text, "html.parser")
                child_a = child_page.find("div", class_="detail_down_adress_con_bottom_left_part2_con").find("a")
                child_download_btn_url = baseurl + child_a.get("href")
                download_res = requests.get(child_download_btn_url)
                download_page = BeautifulSoup(download_res.text, "html.parser")
                download_url = download_page.find("div", class_="download").find("a").get("href")
                print(download_url)
                cls.download_ftp(download_url)

            # exit()

    @staticmethod
    def download_ftp(download_url):
        # 调用迅雷下载
        o = Dispatch("ThunderAgent.Agent64.1")
        # AddTask("下载地址", "另存为文件名", "保存目录", "任务注释", "引用地址", "开始模式", "只从原始地址下载", "从原始地址下载线程数")
        o.AddTask(download_url)
        o.CommitTasks()


if __name__ == '__main__':
    download.parse_url()
