import hashlib
import os
import re

import requests

from tools import tool

# path = u"/Users/objcat/markdown/objcat_blog_markdown/markdown/Python/[Python] import自定义类"

"""
将简书个人中心下载的markdown转换成github
"""


# 下载图片 替换文章
def download_replace(file_path):
    # 当前文件夹目录
    current_path = os.path.dirname(file_path)
    file_name = os.path.basename(file_path).replace(".md", "")
    file_name = hashlib.md5(file_name.encode()).hexdigest()
    img_path = tool.mkdir(current_path + "/" + "images" + "/" + file_name)

    print("开始下载:" + "\n" + file_path)

    # 逐行读取文章
    f = open(file_path, encoding='utf-8')
    content = f.readlines()
    f.close()

    # 全篇读取文章
    f = open(file_path, encoding='utf-8')
    content2 = f.read()
    f.close()

    i = 1
    # 逐行读取
    for url in content:
        if "https://upload-images" in url or "http://upload-images" in url:
            pattern = re.compile(r"\[(.*?)]\((.*?)\)")
            item = re.findall(pattern, url)
            print(url)
            print(item)
            img_file_path = img_path + "/" + str(i) + ".png"
            if not os.path.exists(img_file_path):
                result = requests.get(item[0][1])
                with open(img_path + "/" + str(i) + ".png", "wb") as f2:
                    f2.write(result.content)
                print("开始替换")
                # new_url = "![" + item[0][0] + "](" + "./images/" + file_name + "/"  + str(i) + ".png" + ")" + "\n"
                new_url = "![](" + "./images/" + file_name + "/" + str(i) + ".png" + ")" + "\n"
                print(url + "替换成" + new_url)
                content2 = content2.replace(url, new_url)
            i += 1
    # 生成新文档
    with open(file_path, "w") as f2:
        f2.write(content2)


def batch(root_path):
    for filename in os.listdir(root_path):
        target_path = root_path + "/" + filename
        if os.path.isdir(target_path):
            for filename2 in os.listdir(target_path):
                if filename2.__contains__(".md"):
                    target_path2 = target_path + "/" + filename2
                    if not os.path.isdir(target_path2):
                        download_replace(target_path2)
                        # time.sleep(1)


def make_article_list(root_path):
    """
    生成文章列表HTML(未完成)
    :param root_path:
    :return:
    """
    for filename in os.listdir(root_path):
        target_path = root_path + "/" + filename
        if os.path.isdir(target_path):
            for filename2 in os.listdir(target_path):
                if filename2.__contains__(".md"):
                    target_path2 = target_path + "/" + filename2
                    if not os.path.isdir(target_path2):
                        print(target_path2)


def start():
    # 遍历文章下载图片
    batch("/Users/macmini/Downloads/user-2194379-1588927139")


if __name__ == '__main__':
    start()
