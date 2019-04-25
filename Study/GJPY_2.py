# name = "小王"
# age =50
# school ="蓝翔学校"
# p_per =[name,age,school] #List 列表功能，存储一组列表数据
# #         0   1    3
# #        -3   -2   -1
# print(p_per[-1])#访问列表中的元素
# print(p_per.index(school))#取所在位置
#
# #slice切片
# print(p_per[0:2])#slice切片操作，[1:4]4切下1到3的元素，[1:]切下1开始到后面所有的
# p_per[0] = "王小丫"
# print(p_per)

P_list_1 = ["GG","KK","AA","YY","BB","CC","DD","AA","YY"]
P_list_2 = [1,2,3,4,5,6,9,4,5,8]
print(P_list_1)
print(P_list_2)
# #extend将B列表加到A列表之后
# P_list_1.extend(P_list_2)
# print(P_list_1)
#append将一个元素加到列表最后面
P_list_1.append("HH")
#insert将一个元素插入到指定位置
P_list_1.insert(0,"JJ")
#remove删除列表中的额元素
P_list_1.remove("BB")
print(P_list_1)
# #clear清空列表所有元素
# P_list_1.clear()
# print(P_list_1)
#POP清空指定的元素，不给参数默认删除最后一个
P_list_1.pop(0)
print(P_list_1)
print(P_list_1.index("CC"))
#count在列表中有多少个该值
print(P_list_1.count("YY"))
#sort排序，将列表按照字母顺序和数字大小进行排序
P_list_1.sort()
P_list_2.sort()
print(P_list_1,P_list_2)
#reverse,将列表数据按照原有的顺序逆序排列
print(P_list_1,P_list_2)
P_list_2.reverse(),P_list_1.reverse()
print(P_list_1,P_list_2)
#copy列表拷贝操作,讲列表拷贝后赋值给一个新的列表
P_list_3 =P_list_2.copy()
print(P_list_3)
#元组，Tuple不允许修改，元素固定，不可变，其他同列表，中括号变成小括号即为元祖
P_list = ("GG","KK","AA","YY","BB","CC","DD","AA","YY")
print(P_list)
