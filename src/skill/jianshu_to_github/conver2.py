import os
import re
import requests

path = u"/Users/objcat/markdown/objcat_blog_markdown/markdown/Python/[Python] import自定义类"

"""
将简书markdown转换成github (古老版本: 废弃)
主要功能为下载图片后替换markdown中的路径为绝对路径 

使用方法
                            img 存放图片
建立文件夹结构 文章名(文件夹) 
                            md 存放md
                            
单个文章: 使用 download_replace 方法来指定单个文章文件夹
多个文章: 一个大文件夹包含多个文章文件夹目录 使用 batch 方法给定大目录即可

"""


# 下载图片 替换文章
def download_replace(dir_path):
    md_path = dir_path + "/md"
    img_path = dir_path + "/img"
    for filename in os.listdir(md_path):
        md = md_path + "/" + filename
        f = open(md)
        content = f.readlines()
        f.close()
        f = open(md)
        content2 = f.read()
        f.close()
        i = 1
        for url in content:
            if "https://upload-images" in url:
                pattern = re.compile(r"]\((.*?)\)")
                item = re.findall(pattern, url)
                print(item[0])
                result = requests.get(item[0])
                with open(img_path + "/" + str(i) + ".png", "wb") as f2:
                    f2.write(result.content)
                content2 = content2.replace(url, "![](" + "../img/" + str(i) + ".png" + ")" + "\n")
                i += 1
        # 生成新文档
        with open(md_path + "/new.md", "w") as f2:
            f2.write(content2)


def batch(root_path):
    for filename in os.listdir(root_path):
        target_path = root_path + "/" + filename
        if os.path.isdir(target_path):
            for filename2 in os.listdir(target_path):
                target_path2 = target_path + "/" + filename2
                if os.path.isdir(target_path2):
                    print("开始处理: " + filename2)
                    download_replace(target_path2)


if __name__ == '__main__':
    # download_replace(path)
    batch("/Users/objcat/markdown/objcat_blog_markdown/markdown")
