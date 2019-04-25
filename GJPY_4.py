dic1={
    "name" :"王大锤",
    "age"  :    54,
    "id"   :   1,
}
print(dic1["age"])#获取不到值就报错
print(dic1.get("a","000"))#获取字典信息，没有找到默认返回none,设置返回值就返回设定的值
i=0
while i<8:
    print('#'*i)
    i=i+1
print("循环结束")

for A in range(1,4):
    print(A)

lis_num1 =[1,2,3,4,5,6]
lis_num2 =[7,8,9,10,11]
for num1 in lis_num1:
    for num2 in lis_num2:
        print(f'({num1},{num2})')
#二维列表
dim_1=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
print(dim_1[0][2])
dim_1[0][0]=133
print(dim_1)
for item in dim_1:
    for row in item:#tiem也是一个列表
        print(row)


