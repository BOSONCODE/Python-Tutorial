'''
if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
    <执行3>
else:
    <执行4>
'''

s = eval(input('birth:'))
if s < 2000:
    print('00前')
elif s >= 2000 and s < 2010:
    print('00后10前')
else:
    print('10后')

#input: 1997
#output: 00前

#input: 2008
#output: 00后10前

#input: 2015
#output: 10后
