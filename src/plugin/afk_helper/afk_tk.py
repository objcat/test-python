# description: afk_tk
# date: 2020/5/31 13:11
# author: objcat
# version: 1.0

import tkinter as tk
from plugin.afk_helper import ztr
from plugin.afk_helper.afk import afk
from plugin.afk_helper.adb import adb

window = tk.Tk()
window.title('afk assistant')
window.geometry('500x400')


def stop_all():
    adb.log("终止所有操作")
    ztr.stop_all()


show_screen_btn = tk.Button(window, text='展示屏幕', width=15, height=2, command=lambda: ztr.run('显示屏幕', afk.show_screen),
                            bg="white").pack()

make_line_sift_btn = tk.Button(window, text='绘制特征线', width=15, height=2, command=lambda: ztr.run('绘制特征线', afk.make_line),
                            bg="white").pack()

get_distance_btn = tk.Button(window, text='打印特征', width=15, height=2, command=lambda: ztr.run('打印特征', afk.log_sift_distance),
                            bg="white").pack()

auto_challenge_2_btn = tk.Button(window, text='自动挑战2.0', width=15, height=2,
                                 command=lambda: ztr.run('自动挑战2.0', afk.auto_challenge2), bg="white").pack()

auto_challenge_tower_btn = tk.Button(window, text='自动爬塔', width=15, height=2,
                                     command=lambda: ztr.run('自动爬塔', afk.auto_challenge_king_tower), bg="white").pack()

stop_all_btn = tk.Button(window, text='终止所有操作', width=15, height=2,
                         command=stop_all, bg="white").pack()

window.mainloop()
