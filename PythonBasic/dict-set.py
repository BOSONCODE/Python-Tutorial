'''
dict就是一个map, <key, value>的一个映射关系 之所以叫做字典是因为它内部也采用了类似查字典的算法查询很快
请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。

和list比较，dict有以下几个特点：

查找和插入的速度极快，不会随着key的增加而变慢；
需要占用大量的内存，内存浪费多。
而list相反：

查找和插入的时间随着元素的增加而增加；
占用空间小，浪费内存很少。
所以，dict是用空间来换取时间的一种方法。

set就是集合, 和数学定义中的集合一样, 不能含有重复相同的元素
更多用法可以参考: https://blog.csdn.net/it_yuan/article/details/23170891
'''
dic = {} #声明一个字典dic dic[key] = value 
for i in range(10):
    dic[i] = i
#比如要查找8这个数字的下标位置
print(dic[8])
print(dic.get(8))
#output: 8
#[], get() 这两种方法都能达到效果, 但是假设这个key值不在字典内
'''
if 10 not in dic:
    print(dic[10])
raceback (most recent call last):
  File "F:\python\PythonBasic\dict-set.py", line 26, in <module>
    print(dic[10])
KeyError: 10
'''

if 10 not in dic:
    print(dic.get(10))
#output: none
#或者可以指定一个返回值表示不存在
if 10 not in dic:
    print(dic.get(10, 'tangent90'))
#output:tangent90

#pop(key) 可以删除键值为key的映射
dic.pop(5)
print(dic.get(5, '这个元素已经被删了'))
#output: 这个元素已经被删了

'''
稍微进阶的部分:
dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。

这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。

要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：
'''
'''
key = [1, 2, 3]
d = {}
d[key] = 'a list'
print(d)
Traceback (most recent call last):
  File "F:\python\PythonBasic\dict-set.py", line 57, in <module>
    d[key] = 'a list'
TypeError: unhashable type: 'list'
'''


#set需要一个list作为输入
s = set([1, 1, 3, 2, 2])
print(s)
#output: {1, 2, 3}
s.add(4)
print(s)
#output:{1, 2, 3, 4}
s.remove(4)
print(s)
#output:{1, 2, 3}

#set的操作
#求交集 s1 & s2
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
#output: {2, 3}

#求并集 s1 | s2
print(s1 | s2)
#output: {1, 2, 3, 4}
