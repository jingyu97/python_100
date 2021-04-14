
def index():
    for i in range(len(my_tupple)):
        print("索引分别为：{}".format(i))
    print('\n')

def data():
    for i in my_tupple:
        print("数值分别为：{}".format(i))
    print('\n')


def index_data():
    for i in range(len(my_tupple)):
        print("索引是：{},索引对应的数值是：{}".format(i,my_tupple[i]))
    print('\n')



my_tupple=(1,2,3,4)
index()
data()
index_data()
