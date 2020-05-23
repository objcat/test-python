import os
import time


def start():
    path = r"C:/Users/objcat/Desktop/photos"
    rename_photo(path)

dic = {}

def rename_photo(path):
    list = os.listdir(path)
    for item in list:
        item_path = path + "/" + item
        if os.path.isdir(item_path):
            # 文件夹
            rename_photo(item_path)
            pass
        else:
            # 修改时间
            t = time.localtime(os.path.getmtime(item_path))
            if "_ZYIMG" not in item_path:
                i = rename(path, item_path, t)
            else:
                print("发现已命名文件")
                print(item_path)


def rename(path, item_path, t):
    ymd = time.strftime("%Y%m%d", t)
    hs = time.strftime("_%H%S")
    i = 1
    if dic.__contains__(ymd):
        i = dic[ymd]
    ymd_hs_i = ymd + hs + "_" + str(i)
    target_path = path + "/" + ymd_hs_i + "_ZYIMG" + file_ext_name(item_path)

    if os.path.exists(target_path):
        i += 1
        dic[ymd] = i
        rename(path, item_path, t)
    else:
        print(item_path, target_path)
        os.rename(item_path, target_path)
        i += 1
        dic[ymd] = i
        return i


def file_ext_name(path):
    return os.path.splitext(path)[1]


if __name__ == '__main__':
    start()
