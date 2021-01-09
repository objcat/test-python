# description: life
# date: 2021/1/7 5:02 下午
# author: objcat
# version: 1.0

import functools
import random
import time

# 生命
life = 18250
# 计数
count = 1
# 是否为正常死亡
normal_die = True


# 方法钩子
def hook(func):
    @functools.wraps(func)
    def new_func(*args, **kwargs):
        # 随机发生意外
        accident(func)
        # 检测是否活着
        check_life()
        time.sleep(1)
        return func(*args, **kwargs)

    return new_func


# 检测是否活着及后续处理
def check_life():
    # 如果生命值归0 死亡
    if life <= 0:
        burial()
        exit()


# 发生意外
def accident(func):
    global life
    global normal_die
    number = random.randint(0, 20)
    if number == 0:
        # 发生意外非正常死亡
        life = 0
        normal_die = False
        print(f"{func.__name__} 发生意外")


@hook
def getup():
    # 起床
    print(f"第{count}次 起床")


@hook
def goto_work():
    # 去上班
    print(f"第{count}次 上班")


@hook
def work():
    # 工作
    print(f"第{count}次 工作")


@hook
def eat_breakfast():
    # 吃早餐
    print(f"第{count}次 吃早饭")


@hook
def eat_lunch():
    # 吃午饭
    print(f"第{count}次 吃午饭")


@hook
def eat_dinner():
    # 吃晚饭
    print(f"第{count}次 吃晚饭")


@hook
def after_work():
    # 下班
    print(f"第{count}次 下班回家")


@hook
def think_life():
    # 思考人生
    print(f"第{count}次 思考人生")


@hook
def sleep():
    # 睡觉
    global life
    global count
    print(f"第{count}次 睡觉")
    # 生命流逝
    life -= 1
    # 天数增加
    count += 1
    print(f"准备进入第 {count} 天...")


def burial():
    # 安葬
    print(f"游戏结束, 生存{count}天")
    if normal_die is True:
        print("入土为安, 度过了平凡的一生!")
    else:
        print("发生意外, 呜呼哀哉!")


while (life > 0):
    # 起床
    getup()
    # 上班
    goto_work()
    # 吃早饭
    eat_breakfast()
    # 工作
    work()
    # 吃午饭
    eat_lunch()
    # 工作
    work()
    # 下班回家
    after_work()
    # 吃晚饭
    eat_dinner()
    # 思考人生
    think_life()
    # 睡觉
    sleep()
    pass

burial()
