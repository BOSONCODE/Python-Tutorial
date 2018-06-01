'''
kmp 是一个字符串匹配算法
时间复杂度: O(n + m)
空间复杂度: O(n)
'''

def GetNxt(s, lens):
    i = 0; j = -1;
    nxt = list(range(lens + 1))
    nxt[0] = -1
    while i < lens:
        if -1 == j or s[i] == s[j]:
            i = i + 1; j = j + 1;
            nxt[i] = j
        else:
            j = nxt[j]
    return nxt

#求解字符串s和模式串pattern的最大公共子串
#max_{k}{s[i: i + k] = pattern}
def kmp(s, pattern):
    lens = len(s)
    lenpa = len(pattern)
    nxt = GetNxt(pattern, lenpa)
    i = 0; j = 0; ans = 0;
    while i < lens and j < lenpa:
        if -1 == j or s[i] == pattern[j]:
            i = i + 1
            j = j + 1
        else:
            j = nxt[j]
        ans = max(ans, j)
    return ans

def test():
    s = 'aabbabd'
    pattern = 'abbabd'
    print(kmp(s, pattern))

if __name__ == '__main__':
    test()
    
