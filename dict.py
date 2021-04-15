#创建一个空字典
my_dict1 = {}
my_dict2 = dict()
print("my_dict1:{}".format(my_dict1))
print("my_dict2:{}".format(my_dict2))

#3种形式创建字典
my_dict3 = {'id':1,1:100,(20,30):40}
my_dict4 = dict(id=1,age=20)

my_list1 = [('id',20),('age',30)]
my_list2 = [['id',20],['age',30]]
my_list3 = (('id',20),('age',30))
my_list4 = (['id',20],['age',30])
my_dict5 = dict(my_list1)
my_dict6 = dict(my_list2)
my_dict7 = dict(my_list3)
my_dict8 = dict(my_list4)


print("my_dict3:{}".format(my_dict3))
print("my_dict4:{}".format(my_dict4))
print("my_dict5:{}".format(my_dict5))
print("my_dict6:{}".format(my_dict6))
print("my_dict7:{}".format(my_dict7))
print("my_dict8:{}".format(my_dict8))


#通过key访问value(1.key, 2.函数）
print("'id'对应的数值是：{}".format(my_dict4['id']))
print("'id'对应的数值是：{}".format(my_dict4.get('id')))
#print("[]访问不存在的key的返回结果是：{}".format(my_dict4['hahaha']))
print("get()访问不存在的key的返回结果是：{}".format(my_dict4.get('hahaha')))

#对字典进行增删改（1.key，2.函数）
my_dict4['score']=90
print("my_dict4:{}".format(my_dict4))
my_dict4.update({'id':21,'age':100})
print("my_dict4:{}".format(my_dict4))
my_dict4.pop('score')
print("my_dict4:{}".format(my_dict4))
my_dict4.__delitem__('age')
print("my_dict4:{}".format(my_dict4))
my_dict4.clear()
print("my_dict4:{}".format(my_dict4))







