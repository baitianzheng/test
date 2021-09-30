"""
============================
Author:柠檬班-木森
Time:2020/2/8   10:53
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
字符串的常用方法：



"""

# count方法：查找字符串中某个字符串的个数
# s1 = "123aaa123bbb123ccc567890pokjhgghjkl"
# res = s1.count("bbb")
# print(res)

# find:查找字符串中某个字符串出现的第一个下标（索引）位置
# s2 = "abcdefgbb"
# res = s2.find("b")
# print(res)


# replace:替换字符串中的某个字符串
# s3 = "python 12 3 456 php 123 123"
# res3 = s3.replace("123", "666", 2)
# print(res3)


# upper:将字符串中的小写字母变成大写
# s4 = "python9999PHP"
# res4 = s4.upper()
# print(res4)

# lower：将字符串中的大写字母变成小写
# s5 = "PHP000000java"
# res5 = s5.lower()
# print(res5)

# split:字符串分割的方法
s6 = "python111java111php"
res6 = s6.split("111")
print(res6)

# 字符串分割之后得到的数列表类型的数据：['python', 'java', 'php']
# join:字符串拼接
# s7 = "111".join(("python","java","php"))
s7 = "111".join(['python', 'java', 'php'])
print(s7)

# ("python","java","php")
# ['python', 'java', 'php']