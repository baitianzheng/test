"""
============================
Author:柠檬班-木森
Time:2020/2/7   14:35
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

# 1、写一段代码，运行的时候在控制台依次提示提输入姓名，年龄、性别
# 最终在控制台按照以下格式输出

# 用户输入
name = input("请输入姓名：")
age = input("请输入年龄：")
gender = input("请输入性别：")
# 输出到控制台
print("********************")
print("姓名：", name)
print("年龄：", age)
print("性别：", gender)
print("********************")

# 2、使用随机数模块生成一个5到10之间的浮点数，输出到控制台
import random
a1 = random.random()
a2 = random.randint(5, 9)
number = a2 + a1
print(number)

# 扩展:实现方式:random.uniform()
print(random.uniform(5, 10))



# 3、有5个数 a1=100，a2 =300,a3=400，b=180 、c=1000,
# 要求一、请使用逻辑运算符和比较运算符去  比较c大于 a1、a2、a3是否全部成立。
# 要求二、请使用逻辑运算符和比较运算符去 比较b大于 a1、a2、a3至少1个成立。
a1 = 100
a2 = 300
a3 = 400
b = 180
c = 1000
# 要求1
print(c > a1 and c > a2 and c > a3)
# 要求2
print(b > a1 or b > a2 or b > a3)

# 4、运算符的应用：
#   1、计算 5的三次方，除以15的余数
b1 = (5 ** 3) % 15
print(b1)
#   2、比较989除以57取余的结果，是否大于17
print((989 % 57) > 17)
