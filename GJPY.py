#这是我的python程序！
name ="小ABCDEF"
age = 99
print( "\"name[0]\"\nname[1]")
print(name+"我的家人")
print(name *3 )
print("K" in name )
print(name.upper().isupper())#转换字母为大写，并判断是不是大写，是则输出true
print(name.islower())#判断是不是大写，是则输出true
print(name.index("DEF"))#返回某个特定字符或者字符串的位置
print(name.replace("ABC","YYY"))#替换函数，可以方便的替换需要替换的内容
print(name.isdigit())#判断是不是数值
print(name.isalpha())#判断是否为字符串
print(2.5e2,2.5e+2,2.5e-2,2**5)#代表次方运算，2.5e2=2.5*10^2,2**5=2^5
print(3%2)#取余数
print(str(7)+"我喜欢这个数字")#字符串转换，未转换的情况下是不可进行字符串操作的
print(abs(-8.1))#取绝对值
print(pow(2,4))#次方运算2^4
print(max(2,3,4,5))#取最大值，min()取最小值
print(round(4.51))#四舍五入
from math import *#导入外部模块，math有大量的函数
print(sqrt(5))#导入math才可运行
msg =f'以前有个人，他叫{name},他{age}了'#字符串格式化f''
print(msg)
name2 = input("请输入你的姓名")#输入函数，获取用户输入信息
print(f'{name2}欢迎来到我的家')