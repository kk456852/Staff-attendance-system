from flask import Flask
from operation import *

def test_print():
    # print(UserInfo().findAll())
    print(UserInfo().getInfoByUserName('test1'))
    # print(WorkArrangementInfo().findAll())
    # print(DepartmentInfo().findAll())

def test_insert():
    pass

if __name__ == '__main__':
    test_print()
