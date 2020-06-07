# description: 封装线程管理类
# date: 2020/5/31 16:00
# author: objcat
# version: 1.0

import threading
import inspect
import ctypes

treadings = {}


def run(func):
    t = threading.Thread(target=func)
    t.setDaemon(True)
    t.start()


def add(func_name, func):
    t = threading.Thread(target=func)
    try:
        # 防止重复插入相同名字的方法
        func_name = treadings[func_name]
        return
    except:
        treadings[func_name] = t

    t.setDaemon(True)
    t.start()


def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)


def stop_all():
    """终止所有线程的操作
    :return:
    """
    # 终止所有线程
    for key in treadings:
        try:
            stop_thread(treadings[key])
        except Exception as e:
            pass
    # 清空所有线程
    treadings.clear()
