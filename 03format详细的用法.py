"""
============================
Author:柠檬班-木森
Time:2020/2/8   10:24
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
format的使用

注意点：input输入的，不管你输的是什么，都会保存为字符串
"""

# name = input("输入名字:")
# info = input("输入费用信息：")
# money = float(input("输入金额："))
# print("money的类型：",type(money))

# 通过索引来控制填充的位置
# print("今天收到{2}，交来{1}{1}.开此收据为凭证".format(name, info, money))

# 保留指定小数位数
# print("今天收到{}，交来{},￥:{:.3f}开此收据为凭证".format(name, info, 999.222222223332))

# 指定占位的字符串长度
# 默认左对齐
# print("python:{:10}AAAAAAAAAAAAAAAA".format("123"))
# # 左对齐
# print("python:{:<10}AAAAAAAAAAAAAAAA".format("123"))
# # 右对齐
# print("python:{:>10}AAAAAAAAAAAAAAAA".format("123"))
# # 居中对齐
# print("python:{:^10}AAAAAAAAAAAAAAAA".format("123"))

# 指定内容填充
# print("python:{:q<10}AAAAAAAAAAAAAAAA".format("123"))

# 百分比显示效果
print("百分比为：{:.3%}".format(0.2))
