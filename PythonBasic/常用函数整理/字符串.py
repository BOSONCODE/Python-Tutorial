class StrFunction:
    '''
    python是不可以直接修改字符串中某一个字符的
    所以可以采用下面这个方法,利用list修改, join函数创建一个新的字符串
    '''
    def ReplaceChar(self, s, index, targetChar):
        s = list(s)
        s[index] = targetChar
        s = ''.join(s)
        return s


if __name__ == '__main__':
    test = StrFunction()
    teststr = 'abc'
    print(test.ReplaceChar(teststr, 1, 'g'))
