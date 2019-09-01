import time


def sleep_5_do(f):
    time.sleep(5)
    f()


def sleep_1_print(str):
    time.sleep(1)
    print(str)