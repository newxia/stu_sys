


import random
dom=[[],[],[]]
names=['a','b','c','d','e','f']
for name in names:
    index=random.randint(0,2)
    dom[index].append(name)
i=1
for temp in dom:
    print('宿舍%d的人数为：%d'%(i,len(temp)))
    i+=1
    for name in temp:
        print('%s'%name,end='')
    print("\n")

dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

dict['Age'] = 8  # 更新 Age

print("dict['Age']: ", dict['Age'])
print(dict)

del dict['Name']
print(dict)
print(dict.keys())
print(dict.items())
for key,value in dict.items():
    print((key,value),end='')
    print()













# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁,weight is : %d。" % (self.name, self.age,self.__weight))
def a(people):
    print("%s 说: 我 %d 岁。" % (people.name, people.age))

# 实例化类
p = people('runoob', 10, 30)

p.speak()
a(p)




for x in range(1, 11):
    print('{0:2} {2:4} {1:6}'.format(x, x*x, x*x*x))

print('\n')
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name, number in table.items():

    print('{1:<4} ==> {0:10}'.format(name, number))

table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print('{0[Runoob]:^4d};{0[Google]:^4d};{0[Taobao]:^4d}'.format(table))

table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print('{^10};{^10};{^10}'.format(**table))

