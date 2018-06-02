'''
Python 的内置数据类型有很多种 这里主要讲讲list, tuple
list: 列表 tuple: 元组
'''
#list
fruit = ['mango', 'apple', 'orange']
print(fruit, type(fruit))
#output: ['mango', 'apple', 'orange']  <class 'list'>

#len(listName)
print('The length of the list is: ', len(fruit))
#output: The length of the list is:  3

#listName.insert(pos, value) insert value in index pos
fruit.insert(2, 'banana')
print(fruit)
#output:['mango', 'apple', 'banana', 'orange']

#listName.append(value) insert value in the end
fruit.append('watermelon')
print(fruit)
#output:['mango', 'apple', 'banana', 'orange', 'watermelon']

#listName[pos]
print(fruit[2])
#output:banana

#倒着遍历只要在前面加一个符号 比如说要遍历倒数第2个数
print(fruit[-2])
#output: orange

#tuple
'''
tuple和list很相似, 只是tuple一旦初始化就不能修改了
'''
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)
#output: ('Michael', 'Bob', 'Tracy')

'''
举个特殊的栗子
'''
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
#output:('a', 'b', ['X', 'Y'])
'简单的解释就是tuple所指向的对象内存是不变的, 内存存储的内容可以改变, list可变所以可以这么操作'






