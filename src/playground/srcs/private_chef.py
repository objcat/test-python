# description: private_chef
# date: 2021/2/9 22:13
# author: objcat
# version: 1.0

from PIL import Image
from PIL import ImageFilter


class Privatechef:
    name = None
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"您的私人厨师 {name} 上线了! 年龄: {age}")

    def make_luosifen(self):
        print("厨师做出一碗香喷喷的螺蛳粉端到了你面前")

    def qe(self):
        print("请问有什么需要帮助的吗")
        a = input()
        if a == "我饿了":
            print("我去给你做一碗螺丝粉吧!")

    # 素描
    def p_picture(self):
        square = Image.open("./1.jpg")
        square1 = square.filter(ImageFilter.EDGE_ENHANCE_MORE)  # 选择轮廓效果
        square1.save("./2.jpg")
        print("照片制作完成")


if __name__ == '__main__':
    # 创建厨师
    srcs = Privatechef("中华小当家", 18)
    # 素描
    srcs.p_picture()
