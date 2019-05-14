# **数据库**

## 1、结构

```
database.py 数据库表定义
config.py   数据库环境配置
operation.py  数据库操作定义在该文件中
management_database.py  测试文件
```

## 2、配置方法

在本地创建mysql数据库并修改config.py参数，运行database.py，生成数据库表。

## 3、方法引用

目前仅有简单的查询，通过调用operation.py中的方法进行调用，返回查询结果