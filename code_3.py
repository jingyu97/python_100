#
#1.编写一个程序，查找所有此类数字，它们可以被7整除，但不能是5的倍数（在2000和3200之间（均包括在内））
# 获得的数字应以逗号分隔的顺序打印在一行上
#
list = []
j=0
for i in range(2000,3201):
    if i%7 == 0 and i%5 != 0:
        list.append(i)
print(list)


#
#2.编写一个程序，可以计算给定数字的阶乘，结果应以逗号分隔的顺序打印在一行上。
# 假设向程序提供了以下输入：8然后，输出应为：40320
#
n = int(input("please enter number:>"))
def fun(n):
    if n == 1:
        return n
    return n*fun(n-1)
result = fun(n)
print("{}的阶乘是{}".format(n,result))



#
#3.用户输入一个数值，打印{1:1,2:4,3:9,4:16}
#
#获取用户输入的数值
number = int(input("please enter number:>"))
#定义一个空字典
my_dict = {}
#填充字典
for i in range(1,number+1):
    my_dict[i] = i*i
#打印字典
print(my_dict)
