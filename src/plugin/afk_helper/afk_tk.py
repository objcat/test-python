# description: afk_tk
# date: 2020/5/31 13:11
# author: objcat
# version: 1.0

import tkinter as tk
from plugin.afk_helper.afk import afk
import threading


def treading_it(func, *args):
    t = threading.Thread(target=func, *args)
    t.setDaemon(True)
    t.start()


window = tk.Tk()
window.title('afk assistant')
window.geometry('500x400')

show_screen_btn = tk.Button(window, text='展示屏幕', width=15, height=2, command=lambda: treading_it(afk.show_screen),
                            bg="white").pack()


auto_challenge_2_btn = tk.Button(window, text='自动挑战2.0', width=15, height=2,
                                 command=lambda: treading_it(afk.auto_challenge2), bg="white").pack()

auto_challenge_tower = tk.Button(window, text='自动爬塔', width=15, height=2,
                                 command=lambda: treading_it(afk.auto_challenge_king_tower), bg="white").pack()

stop_all = tk.Button(window, text='终止所有操作', width=15, height=2,
                                 command=lambda: treading_it(afk.auto_challenge_king_tower), bg="white").pack()


window.mainloop()
