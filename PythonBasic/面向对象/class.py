'''
OOP: object-oriented programming
面向对象是一种方法, 这个说起来是软件工程里面的长篇大论
这里粗略简单地来说的话就是 物以类聚
比如说 芒果、苹果、香蕉 这些都是一个一个的对象 这些可以归为一类就是水果
然后水果之间又有一些关系, 比如说长在树上的可以分为一类, 长在地上的分为一类, 那么
这些又是继承于水果这一个类
水果类专业术语叫做基类  生长环境类又叫做 派生类
多态就是基类的不同行为
'''
#私有变量不可以直接访问只能由当前类访问
#protected 派生类可以访问 但是不可以直接由对象访问, 对象不可以直接访问
#public 基类、派生类和对象都可以直接访问

class BaseClass:
    __privateVar = "I'm the private Variable"
    _protectedVar = "I'm the protected Variable"
    publicVar = "I'm the public Variable"

    def getPrivateVar(self):
        return self.__privateVar

    def __str__(self):
        '''return self.__privateVar \
         + self._protectedVar \
        + self.publicVar'''
        return "I'm the Base Class"

class DerivedClass(BaseClass):  #继承
    def __init__(self):
        print(BaseClass.publicVar)
        print(BaseClass._protectedVar)
        #print(BaseClass.__privateVar) 如果这么写就会报错
    def printPrivateVar(self):
        #print(BaseClass())
        print(self.getPrivateVar()) #这么访问私有变量就没问题
        #output: I'm the private Variable

    def __str__(self):
        return "I'm the Derived Class"

def polymorphic(obj):
    print(obj)

if __name__ == '__main__':
    test = DerivedClass()
    test2 = BaseClass()
    polymorphic(test)
    #output:I'm the Derived Class
    polymorphic(test2)
    #output: I'm the Base Class
    test.printPrivateVar()
'''
I'm the public Variable
I'm the protected Variable
Traceback (most recent call last):
  File "F:\python\PythonBasic\面向对象\class.py", line 23, in <module>
    test = DerivedClass()
  File "F:\python\PythonBasic\面向对象\class.py", line 20, in __init__
    print(BaseClass.__privateVar)
AttributeError: type object 'BaseClass' has no attribute '_DerivedClass__privateVar'
'''
        
        
