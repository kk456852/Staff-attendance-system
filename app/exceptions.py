"""声明出现错误时的异常类，和它包含的错误代码。

"""


class UserNotFoundException(Exception):
    pass


class RequestError(Exception):
    def err_num(self):
        return self.eno


class DepartmentError(Exception):
    """部门缺少主管"""
    def __init__(self):
        print("部门缺少主管")
        

class NoLoginError(RequestError):
    """用户没有登录"""

    def __init__(self):
        self.eno = 50000


class NoPermissionError(RequestError):
    """用户没有足够的权限"""

    def __init__(self):
        self.eno = 50001

