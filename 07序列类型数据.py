"""
============================
Author:柠檬班-木森
Time:2020/2/8   11:19
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
序列类型的数据：数据内部的元素是有顺序的（有下标）

序列类型的数据：字符串类型、列表类型、元组类型

序列类型数据的共同特性：
1、可以通过下标取值
[下标]
2、可以进行切片操作
[起始位置:终止位置]:左闭右开


"""

# s = "python"
# li = ["aaa", "bbb", "ccc"]
# tu = (123, "222", "999")
#
# # 下标取值：通过下标获取数据内的元素
# # 从前往后数下标:从0开始
# print(s[3])
# print(li[1])
# print(tu[2])
# # 从后往前数下标:从-1开始
# print(s[-3])
# print(li[-2])
# print(tu[-1])

# 切片操作：获取数据中的某一段数据
li = [11, 22, 33, 44, 55, 66, 77, 88]
res = li[0:4]
print(res)
print(li[2:5])