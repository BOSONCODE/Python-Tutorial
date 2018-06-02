'''
python的数据类型有:
整数: int
浮点数: float
布尔型: bool(True, False)
空值: None
字符串

python定义一个变量非常简单, 并不需要像C语言之类的 要定义类型
具体的使用看代码
'''
a = 12345678910111213141516
b = a * 2
print(a*b, type(b))
#output: 304831575503129583142940443235931715685556512 <class 'int'>
'''
知识点:
type(变量): type是一个函数用来查看当前变量的类型的
int: 可以支持大整数的运算, 通过我造的数字可以知道了, +, -, * 问题不大都是普通用法
'''

a = 2
b = 3
print(a**b)
#output: 8
'''这是python的求幂运算, a**b 表示 pow(a, b)'''

a = 5
b = 2
print(a/b, a//b, type(a/b), type(a//b))
#output: 2.5 2 <class 'float'> <class 'int'>
'''
*知识点: 除法非常重要容易被坑
a/b: 表示精确除,是浮点数
a//b: 整除是双斜杠
'''



