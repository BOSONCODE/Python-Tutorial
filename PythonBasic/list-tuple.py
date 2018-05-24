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

#tuple


