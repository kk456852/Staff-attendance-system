"""声明出现错误时的异常类，和它包含的错误代码。

"""


class RequestError(Exception):
    """所有请求类的基类"""

    def err_msg(self):
        return self.__doc__

    def err_num(self):
        return self.eno


class UserNotFoundError(RequestError):
    """没有找到该用户"""
    eno = 50000


class NoLoginError(RequestError):
    """用户没有登录"""
    eno = 50001


class NoPermissionError(RequestError):
    """用户没有足够的权限"""
    eno = 50002


class PasswordNotCorrectError(RequestError):
    """用户名或密码错误"""
    eno = 50003
