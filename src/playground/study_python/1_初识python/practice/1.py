# description: 1
# date: 2021/1/6 5:08 下午
# author: objcat
# version: 1.0


"""
学习使用turtle在屏幕上绘制图形。
说明：turtle是Python内置的一个非常有趣的模块，特别适合对计算机程序设计进行初体验的小伙伴，它最早是Logo语言的一部分，Logo语言是Wally Feurzig和Seymour Papert在1966发明的编程语言。
"""

import turtle

turtle.pensize(10)
turtle.pencolor('red')

turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

turtle.mainloop()