"""
============================
Author:柠檬班-木森
Time:2020/2/8   10:44
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
字符串的转义：
\表示转义
\t:制表符
\n:换行符
\\:表示\
# 如何关闭字符串转义
字符串：r表达式


"""

# s1 = "python\thello"
# s2 = "python\nppppp"
# 使用字符串r表达式关闭转义
s1 = r"python\thello"
s2 = r"python\nppppp"
print(s1)
print(s2)

file_path = r"C:\project\py27_class\py27_03day\task_02day.py"

print(file_path)