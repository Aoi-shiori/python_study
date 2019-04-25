#函数 function
#def函数声明
#关键字 keywords
# P_list_4 =[3,4,5,2,6,7,8,9,0]
# P_list_5 =["小王","小明"]
# P_list_4[] =input('请输入一组数字')
# P_list_5[] =input('请输入姓名')

def getyushu(A,B,C):
    j=A%B
    h=j+B
    return ((C+"所得余数是"+str(j)+"abc其他值是"+str(h)).upper())

def littlefun():
    P_list_5=[]
    #is_dig =True
    for i in range(5): #一个for循环
        strn = input ("请输入一组内容:")
        P_list_5.append(strn)
    P_list_5.sort()#重新按大小排序
    if P_list_5[2].isdigit():#判断是不是数值
        return P_list_5
    else:
        return str(P_list_5)

A=[]
B=[]
print("请输入A列表数据")
A =littlefun()
print("请输入B列表数据")
B=littlefun()
print(A,B)

if int(A[3])>=int(A[1]) or int(A[0])>=1 :#等于需要双==
    print(getyushu(int(A[0]),int(A[3]),B[1]))
print(A[0])


# # getyushu(P_list_4[-2],P_list_4[5],P_list_5[0])
# print(getyushu(P_list_4[-5],P_list_4[5],P_list_5[0]))

