'''
利用之前学的写个小游戏吧：
规则如下: 程序会随机生成一个数,  然后用户手动输入自己猜的数字
程序会根据你猜的数字和目标数字的大小做出提示
'''
import random

targetNumber = random.randint(0, 100)    #生成一个[0, 100] 之间的随机数
while True:
    num = (int)(input())    #input() 函数读入会返回一个str,  (int)(input()) 就是对输入进行强制转换成整数
    #假设控制台输入的不是一个合法的整数, 那么就会进行报错, 比如输入 we 或者 12.5
    if -1 == num:
        print('See you next time!')
        break
    if num == targetNumber:
        print('Bingo!')
        break
    if num < targetNumber:
        print('Too Small!')
    else:
        print('Too Big!')

'''
output:
12
Too Small!
50
Too Big!
35
Too Big!
36
Too Big!
27
Too Small!
30
Too Big!
28
Too Small!
29
Bingo!
'''
