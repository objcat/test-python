# description: study
# date: 2021/1/7 10:06 上午
# author: objcat
# version: 1.0


# 使用变量保存数据并进行加减乘除运算

a = 1
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a / b)

#使用type检测变量类型

a = 100
b = 12.345
c = 1 + 5j
d = 'hello, world'
e = True
print(type(a))    # <class 'int'>
print(type(b))    # <class 'float'>
print(type(c))    # <class 'complex'>
print(type(d))    # <class 'str'>
print(type(e))    # <class 'bool'>

"""
使用input()函数获取键盘输入(字符串)
使用int()函数将输入的字符串转换成整数
使用print()函数输出带占位符的字符串
"""

# 把输入的字符串转化成整数
"""
这里会存在一个问题 当输入的字符串带有小数的时候 程序便会报错
int()函数不能处理小数字符串的转换 会抛出异常
ValueError: invalid literal for int() with base 10: '1.5'
需要先用float把字符串转化成数字然后在用int()转化成整数即可
a = int(float(input('a = ')))
"""

a = int(input('a = '))
b = int(input('b = '))

# 使用百分号来拼接返回结果
print('%d + %d = %d' % (a, b, a + b))
# 使用f和花括号来拼接返回结果
print(f'{a} + {b} = {a + b}')
# 如果拼接字符中需要用到特殊符号 输入一个会报错 比如 % 输入两个才会完整输出 % 字符
print('%d %% %d = %d' % (a, b, a % b))
# 使用f拼接法 这个就不需要输入两个%了 因为f拼接法不是包含在字符串内的 很先进!
print(f'{a} % {b} = {a % b}')

"""
运算符	描述
[] [:]	下标，切片
**	指数
~ + -	按位取反, 正负号
* / % //	乘，除，模，整除
+ -	加，减
>> <<	右移，左移
&	按位与
^ |	按位异或，按位或
<= < > >=	小于等于，小于，大于，大于等于
== !=	等于，不等于
is is not	身份运算符
in not in	成员运算符
not or and	逻辑运算符
= += -= *= /= %= //= **= &= `	= ^= >>= <<=`
"""

flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not (1 != 2)
print('flag0 =', flag0)    # flag0 = True
print('flag1 =', flag1)    # flag1 = True
print('flag2 =', flag2)    # flag2 = False
print('flag3 =', flag3)    # flag3 = False
print('flag4 =', flag4)    # flag4 = True
print('flag5 =', flag5)    # flag5 = False



