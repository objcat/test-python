# description: test_lambda
# date: 2020/6/1 5:06 下午
# author: objcat
# version: 1.0

# lambda其实是一种函数的缩写

# 1，lambda 函数不能包含命令，
# 2，包含的表达式不能超过一个。

# 1.基本使用

# 加法
p = lambda x, y: x + y
print(p(1, 2))

# 乘法
p2 = lambda x: x * x
print(p2(3))

# 2.结合map使用

m = map(lambda x: x ** x, [1, 2, 3, 4, 5])

print(m)


