# try:
#     L=int(input("请输入一个数"))
# except ValueError:
#     print("不能输入非数值")
# except ZeroDivisionError:
#     print("不能为0")
# except FileNotFoundError:
#     print("找不到文件")
# try:
#     P=2/L
# except ValueError:
#        print("不能输入非数值")
# except ZeroDivisionError:
#        print("不能为0")
# except NameError:
#        print("找不到文件")
# except SyntaxError:
#     print("111")
# try:
#     print(P)
# except NameError:
#        print("访问一个不存在的变量时抛出的异常")

#文件读取操作
# -*- coding: UTF-8 -*-
# fileRE = open("mystory.txt","r")
# fileRE.write("我想回家")
# filered=fileRE.read() #读取所有，加入参数则读取多少字符
# filered=fileRE.readline()#读一行，加入参数则读取一行的第几个

# filered = fileRE.write("\n我骑着小猪上学")
# filered=fileRE.readlines() #读取列表.加入参数则读取第几行列表值
# print(filered[1])
# for line in filered:
#     print(line)
# fileRE.close()

class stdent:
    def __init__(self,name,age,sex):
        self.__name =name #  "__" 加上可以防止被外部修改
        self.__age =age
        self.__sex =sex
    def Who_am_I(self):
        print(f'我是一个学生{self.__name}{self.__age}岁{self.__sex}')
    def Get_name(self):
        return self.__name
    def Set_name(self,name):
        self.__name =name
    def Get_age(self):
        return self.__age
    def Set_age(self,age):
        self.__age =age
    def Get_sex(self):
        return self.__sex
    def Set_sex(self,sex):
        self.__sex =sex



class Teacher(stdent):
    def Who_am_I(self):
        print(f'我是一个老师{self.Get_name()}')
# Teacher.set_name("春天"
# XM=stdent("小明",26,"男")
# XM.Who_am_I()
# print(GJ.age,XM.name)
# AA=Teacher("魅力",22,"男")
# AA.Who_am_I()
if(__name__=="__main__"): #下面的内容只在当前模块运行，被其他模块导入则不运行，当nane值不是main时不运行
    print("——————————1212121")
    print("————验证一下喽")

print(f'我的名字是",{__name__}')