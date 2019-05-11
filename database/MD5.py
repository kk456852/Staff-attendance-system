# md5加密
import hashlib
md5 = hashlib.md5()
str = "test"  # 来自前端输入的用户密码串？
str_bytes_utf8 = str.encode(encoding="utf-8")
md5.update(str_bytes_utf8)
encrypted = md5.hexdigest()  # 将加密后的串存储在数据库中
print("经过MD5加密后的加密串是：%s" % encrypted)
