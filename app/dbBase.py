from flask_sqlalchemy import SQLAlchemy, Model, BaseQuery
from sqlalchemy.ext.declarative import DeclarativeMeta
import json


class JsonModel(Model):
    __exclude__ = ['password', 'password_hash']  # to_dict 排除敏感字段
    __include__ = []  # 包含字段
    __exclude_foreign__ = False  # 排除外键

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
        if self.__exclude_foreign__:
            fields = fields - set(self.__foreign_column__())
        fields = fields - set(self.__exclude__)
        fields = set(list(fields) + self.__include__)
        return fields