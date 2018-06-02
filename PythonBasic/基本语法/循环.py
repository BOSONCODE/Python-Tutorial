'''
循环: for, while
关键字: continue, break
'''

lst = range(5) #生成[0, 1, 2, 3, 4]
for item in lst:
    print(item)
'''
0
1
2
3
4
'''

#len() 返回lst的长度
#range(st, en)表示遍历[st, en)

for index in range(len(lst)):
    print(lst[index])
'''
0
1
2
3
4
'''
st = 0; en = len(lst)-1;
while st <= en:
    print(lst[st])
    #++st; 或者 st++; 注意 这是个错误的写法
    #++st; st本身不会发生改变, st++会直接报错 python中尽量不要用自增运算
    st = st + 1
'''output:
0
1
2
3
4
'''
#输出[0, 3]所有的奇数
for i in range(4):
    if i % 2 == 0:
        continue #意思执行到这一步的时候就接着循环, 不执行下面的步骤了
    print(i)
'''
output:
1
3
'''

#输出[0, 3]中所有的数
flag = -1
for i in range(100):
    if i >= 4:
        flag = i
        break #执行到这一步的时候 就直接跳出循环
    print(i)
if -1 == flag:
    print("嘿嘿, 我把区间都遍历完了")
else:
    print("我在%d位置提前跳出来了"%flag)
'''
0
1
2
3
我在4位置提前跳出来了
'''
    

