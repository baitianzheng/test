"""
============================
Author:柠檬班-木森
Time:2020/2/13   20:11
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
字典：dict类型

字典的定义：{}表示字典，
字典中的元素是有键值对(key:value)组成的，每个元素也是逗号隔开
键就是该数据的索引（字典没有下标）

字典中的相关规范：
1、字典中的键不能重复
2、字典中的键只能使用不可变类型的数据（通常是用字符串）

3、字典中键对应的值可以是任何的数据类型



不可变类型的数据：数值类型、字符串、元组

可变类型的数据：列表、字典、集合

可变类型的数据，定义了之后可以进行修改（对元素支持增删查改的操作）
"""

stu = ["小明", "18", "13811223344"]

# stu.append("男")
# stu.append("1")
# stu.append("湖南长沙")


# print(stu)
# print(stu[0])

# name = "musen"
# age = 18


# 字典的定义
dic = {"name": "小明", "age": 18, "phone": "13309877890"}

print(dic["name"])
print(dic["age"])

# print(type(dic))

# 错误示范
# dic2 = {"a": 11, "a": 111, "a": 11112}
# print(dic2)
