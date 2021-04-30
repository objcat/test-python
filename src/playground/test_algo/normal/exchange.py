# description: exchange
# date: 2021/4/30 1:36 下午
# author: objcat
# version: 1.0

def exchange(a, b):
    temp = a
    a = b
    b = temp
    print(a)
    print(b)

if __name__ == '__main__':
    a = 1
    b = 2
    exchange(a, b)
    print(a)
    print(b)