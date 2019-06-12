from flask_sqlalchemy import SQLAlchemy, Model, BaseQuery
from sqlalchemy.ext.declarative import DeclarativeMeta
import json

from flask.json import JSONEncoder
import datetime


class BaseModel(Model):
    __exclude__ = ['password', 'password_hash']  # to_dict 排除敏感字段
    __include__ = []  # 包含字段
    __exclude_foreign__ = False  # 排除外键

    # 查询方法
    @classmethod
    def All(cls):
        return cls.query.all()

    @classmethod
    def ByID(cls, ID):
        return cls.query.get(ID)

    # 新建方法
    @classmethod
    def new(cls, profile: dict):
        """
        根据一个字典，新建一个对象并保存。
        """
        cls(**profile).update_db()

    # 修改方法
    def update(self, data):
        """修改自身属性。

        :data 属性字典
        :param 具名参数
        """
        for x in self.dict().keys():
            if x in data.keys():
                self.__setattr__(x, data[x])

        self.update_db()

    def update_db(self):
        """将修改后的对象，或者新增的对象添加/修改到数据库中。
        失败时抛出异常。

        :raise InvalidRequestError
        """
        self.query.session.add(self)
        self.query.session.commit()

    # 删除方法
    def delete(self):
        """删除数据库中该对象对应的行。
        失败时抛出异常。

        :raise InvalidRequestError
        """
        self.query.session.delete(self)
        self.query.session.commit()

    def dict(self):
        """返回一个数据库模型所有的属性组成的字典

        :return dict
        """
        data = {}
        for field in self.__fields__():
            value = getattr(self, field)  # value
            if isinstance(value.__class__, DeclarativeMeta):
                data[field] = value.dict()
            elif hasattr(value, '__call__'):
                pass
            elif not hasattr(value, '__func__') and not isinstance(value, BaseQuery):
                try:
                    data[field] = value
                except TypeError:
                    data[field] = None
        return data

    def json(self):
        data = {}
        for field in self.__fields__():
            value = getattr(self, field)  # value
            if isinstance(value.__class__, DeclarativeMeta):
                data[field] = value.dict()
            elif hasattr(value, '__call__'):
                pass
            elif not hasattr(value, '__func__') and not isinstance(value, BaseQuery):
                try:
                    json.dumps(value)
                    data[field] = value
                except TypeError:
                    try:
                        data[field] = str(value)
                    except Exception as e:
                        data[field] = None
        return json.dumps(data, ensure_ascii=False)

    def __foreign_column__(self):
        data = []
        for column in self.__table__.columns:
            if getattr(column, 'foreign_keys'):
                data.append(column.key)
        return data

    def __fields__(self):
        # 选择数据库中的每一列
        # 去掉前置下划线，得到真正的@property属性名
        fields = set(x.name.lstrip("_") for x in self.__table__.columns)
        if not self.__exclude_foreign__:
            fields.update(self.__foreign_column__())
        fields = fields - set(self.__exclude__)
        fields = set(list(fields) + self.__include__)
        return fields
