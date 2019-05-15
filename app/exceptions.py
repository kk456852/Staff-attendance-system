"""声明出现错误时的异常类，和它包含的错误代码。

"""


class NoLoginError(Exception):
    """用户没有登录"""

    def __init__(self):
        self.eno = 50000


class NoPermissionError(Exception):
    """用户没有足够的权限"""

    def __init__(self):
        self.eno = 50001
