"""
============================
Author:柠檬班-木森
Time:2020/2/12   10:54
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

print("--------------------------第1题-----------------------------")
"""
一、现在有一个列表 li2=[1，2，3，4，5]，
     第一步：请通过三行代码将上面的列表，改成这个样子 li2 = [0，1，2，3，66，5，11，22，33]，
     第二步：对列表进行升序排序 （从小到大）
     第三步：将列表复制一份进行降序排序（从大到小）
"""
li2 = [1, 2, 3, 4, 5]
# 第一步
li2.insert(0, 0)  # 在最前面加入0
li2[4] = 66
li2.extend([11, 22, 33])  # 在最后加入三个元素

print(li2)
# 第二步：从小到大排序
li2.sort()
print(li2)
# 第三步：从大到小排序
li3 = li2.copy()
li3.sort(reverse=True)
print(li3)

print("--------------------------第2题-----------------------------")
"""
二、定义一个空列表user=[],   分别提示用户输入，姓名，年龄，身高，用户输入完之后，
将输入的信息作为添加的列表中保存，然后按照一下格式输出：
    用户的姓名为：xxx,年龄为：xxx,  身高为：xxx  ,请仔细核对

"""
user = []
name = input("请输入姓名：")
age = input("请输入年龄：")
height = input("请输入身高：")
user.extend([name, age, height])
print('用户的姓名为：{},年龄为：{},身高为：{:.2f},请仔细核对'.format(name, age, float(height)))

print("--------------------------第3题-----------------------------")
"""
三、
1、现在有一个字符串 s = 'abcdefghijk',
    要求一：通过切片获取: defg
    要求二：通过切片获取：cgk
    要求三：通过切片获取：jhf

2、现在有一个列表li = [1,2,3,4,5,6,7,8,9] 请通过切片得出结果 [3,6,9] 
"""
s = 'abcdefghijk'
# 要求一
s1 = s[3:7]
print(s1)

# 要求二
s2 = s[2::4]
print(s2)

# 要求三
s3 = s[-2:-7:-2]
print(s3)

# 、切片得出结果 [3,6,9]
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s4 = li[2::3]
print(s4)
