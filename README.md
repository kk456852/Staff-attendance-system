# Staff-attendance-system

要求 Python 3.5 以上。

## 用例完成情况
@Mahaoqu
- [x] 登录、登出

@kk456852
- [ ] 添加、删除、管理用户信息
- [ ] 任命主管
- [ ] 创建临时性加班

@XuKaiyue-959
- [ ] 进行考勤记录
- [ ] 更新自己的账户信息
- [ ] 查看员工的上班状况

@JimmyMoo
- [ ] 查看自己的工作班次
- [ ] 进行请假和销假
- [ ] 申请加班和审批

@CharleyZhao123
- [ ] 调整员工的工作班次
- [ ] 为本部门安排工作班次
- [ ] 展示某一部门的工作班次


## 编码要求
* 撰写详细设计文档
* 设计前后端交互接口
* 确定并修改用到的数据库模型
* 通过交互式操作确定操作流程
* 实现功能，完成路由接口
* 撰写测试用例
* 执行变更
* 申请提交
---
编码规范如下：

### 交互环境编码
每次写出一行代码都应该在shell中交互式地验证逻辑是否正确。推荐使用iPython Shell。

### 用异常而不应该检查返回值
每个服务对应一个HTTP请求，在路由最外层捕获异常并打印日志。中间传递过程默认能够成功。

### 提交代码前通过测试
`flask test`确保当前的修改不会影响已有的功能。在提交一个功能时需要写对应的测试用例。

### 使用规范的文档和注释格式
标清参数、返回值、抛出异常的类型和含义。确保文档和注释格式规范。使用autopep8修正代码格式。

### 使用不同分支
开发一项新功能时请开启一个新的branch，在完成功能时提出Pull Request合并到master上。

在开发过程中需要及时从master中合并最新的紧急修改。使用`git merge master`


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
