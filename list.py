def index():
    for i in range(len(my_list)):
        print("索引是：{}".format(i))
    print('\n')

def data():
    for i in my_list:
        print("数值是：{}".format(i))
    print('\n')

def index_data():
    for i in range(len(my_list)):
        print("索引是：{},索引对应的数值是：{}".format(i,my_list[i]))
my_list=[1,2,3,4,5]
index()
data()
index_data()