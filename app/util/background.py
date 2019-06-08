"""保存所有的后台任务。这些将在首次请求被调用之前添加进线程池。
详见app/__init__.py

TODO: 完成在下班前通知员工的操作。
"""

from time import sleep
from ..model import User


def print_number():
    i = 0
    while True:
        sleep(1)
        print(i)
        i = i + 1
