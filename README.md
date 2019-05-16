# Staff-attendance-system

要求 Python 3.5 以上。

### 构建

推荐使用Python虚拟环境如果当前目录下没有虚拟环境，用以下方式创建：
```
python3 -m venv venv
```

之后安装所需要的依赖：
```
pip install -r requirements.txt
```

如果已经添加新包，请在提交前执行以下命令：
```
pip freeze > requirements.txt
```

注意，如果正在使用mysql数据库，请添加.env文件，并额外加入以下行：
```
SQLALCHEMY_DATABASE_URI=mysql+mysqlconnector://root:1234@127.0.0.1:3306/sys_db?charset=utf8
```
之后运行：
```
flask run
```
就可以开启服务器。

可以交互式地调试程序。调用`flask ipy`可以进入带有flask上下文的IPython环境。推荐在交互式环境下编程！

### 数据库生成
可以使用`flask init-db`命令生成一个数据库模型。

### 单元测试
单元测试极其重要。当写出新的代码时，请写一段简单的测试函数确保你的类/函数是可以正常工作的！在做任何修改之后，请运行单元测试确保修改没有影响到之前的结果。

这里使用Python标准库内置单元测试框架unittest。见：[unittest — 单元测试框架 — Python 3.7.3 文档](https://docs.python.org/zh-cn/3/library/unittest.html)

运行单元测试只需要运行：
```
flask test
```

在Flask中，对数据库和路由的测试必须在Flask上下文中。在测试数据库时，请记得在测试运行前后清理数据。

### 代码规范
应遵守 PEP 8 代码风格，推荐使用 autopep8 配合 pylint 插件。


### 提示
在.vscode文件夹中的`settings.json`中添加这一行：
```json
"python.linting.pylintArgs": ["--load-plugins", "pylint_flask"]
```
就可以开启数据库提示支持。
