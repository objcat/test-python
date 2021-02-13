# description: deaes
# date: 2021/2/13 19:11
# author: objcat
# version: 1.0

from glob import glob
import os
import sys


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


def str_to_hex(s):
    return ' '.join([hex(ord(c)).replace('0x', '') for c in s])


if __name__ == '__main__':

    if len(sys.argv) < 3:
        print("参数错误: ts文件路径 key路径")
        exit()

    # 获取文件夹路径
    dir_path = sys.argv[1]
    # 获取key路径
    key_path = sys.argv[2]

    # 取出16进制key
    f = open(key_path, 'r')
    key = str_to_hex(f.read()).replace(" ", "")
    f.close()
    # 获取文件列表
    files = glob(dir_path + "\\*.ts")
    output_path = os.path.join(dir_path, "output")
    mkdir(output_path)

    # 遍历文件解密
    for file_path in files:
        basename = os.path.basename(file_path)
        print(file_path)
        str = f"openssl aes-128-cbc -d -in {file_path} -out {os.path.join(dir_path, 'output', basename)} -nosalt -iv 00000000000000000000000000000000 -K {key}"
        print(str)
        os.system(str)
    print("转换成功")

    pass
