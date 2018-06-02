'''
字符串是以单引号'或双引号"括起来的任意文本

I'm "OK"!
目标:
1.讲解一下引号的混合使用和转义字符的使用
'''
print('I\'m "OK"!')
#output: I'm "OK"!
#print('I'm "OK"!') 这样写就会编译错误 因为输出的内容会被分成两部分
#'I', 然后最后一个'会出现不匹配 所以会编译错误

#所以转移字符 \ 的作用就是消除这种歧义性
print("I'm \"OK\"!")
#output: I'm "OK"!

#那么这个时候肯定就会有人问了, 那我非要是输出\怎么办
print('\\')
#output: \

#一句话总结一下: 当字符串出现歧义性的时候就可以使用转义字符\

#python也提供了 r'' 保证引号内字符串默认不转义 这样写起来就方便多了
print(r'I\'m "OK"!')
#output:I\'m "OK"!

'''
python的格式化输出
%d: 整数
%f: 浮点数
%s: 字符串
%x: 十六进制整数
'''
str1 = 'world'
n = 1000
#使用 %
print("hello, %s, today is %d"%(str1, n))
#output: hello, world, today is 1000

#使用format 采用从0开始的编号输出 稍微麻烦了点
print('hello, {0}, today is {1}'.format(str1, n))
#output: hello, world, today is 1000

