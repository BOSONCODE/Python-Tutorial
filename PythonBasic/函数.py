'''
函数调用分为调用库的, 和自己写的, 其实本质上都是一样的
都是已经有人写好的, 这也体现出python模块化的优势

对于库的话要正确使用, 所以在使用之前先要了解怎么使用, 可以去查看官方文档
比如说输入的参数, 返回值类型什么的
'''
#调用库的
#求一个数的绝对值
a = -5
print(abs(a))
#output: 5

#求一组数的最大值
print(max(2, 3, 1, -5))
#output: 3

#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
calABS = abs
print(calABS(a))
#output: 5

#自定义函数
#比如要实现一个函数求解一个list里面整型数的最大值
def ListMax(lst):
    INF = 10000000000 
    ans = -INF          #初始化为负无穷
    for item in lst:
        if False == isinstance(item, int): #判断item是不是一个整型数
            raise RuntimeError('这个list不合法') #如果不是就抛出异常
        ans = max(ans, item) #求出两个数当中比较大的数, 更新答案
    return ans

def EmptyFunction(): #空函数
    pass

if __name__ == '__main__': #这一行的目的是表示运行在当前模块的主函数中 \
    #只要路径正确(或者同一目录下, 可以直接调用ListMax函数, 而不会运行当前文件中main中的内容)
    lst = [1, 2, 0, -9, 8]
    lst2 = [1, 2, 'aa', 9]
    print(ListMax(lst))
    #output: 8
    print(ListMax(lst2))
    #output: 会抛出异常

