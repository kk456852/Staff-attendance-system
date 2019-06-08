from enum import IntEnum


class Role(IntEnum):
    """职务

    使用数值枚举类，该类是int的子类
    """
    STAFF = 1
    CHARGE = 2
    MANAGER = 3
