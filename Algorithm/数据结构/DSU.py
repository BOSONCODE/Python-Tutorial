'''
并查集(Disjoint Set Union)
平均时间:
init 操作 O(n)
find(路径压缩): O(logn)
Unite(合并操作): O(logn)
这里的实现不是最快的, 但是对于一般OJ够了
理论最快的实现是按秩合并需要再增加一个rank数组
那样最坏复杂度能够达到
init 操作 O(n)
find(路径压缩): O(\alpha(n))
Unite(合并操作): O(\alpha(n))
通常来讲\alpha(n) <= 4
详细的计算和理论讲解请查看论文, 这里只是一个大致说明
主要是代码的实现:
'''
#初始化
def init(n):
   fa = list(range(n + 1))
   return fa

#路径压缩
def find(x, fa):
    if fa[x] == x:
        return fa[x]
    else:
        return find(fa[x], fa)

#合并操作
def Unite(x, y, fa):
    fx = find(x, fa)
    fy = find(y, fa)
    if fx == fy:
        return
    fa[fx] = fy

'''
test case
input:
1 2
2 3
3 4
2

output:

'''

def test():
    fa = init(5)
    print(fa)
    for i in range(3):
        try:
            x, y = map(int, input().strip().split())
        except EOFError:
            break
        Unite(x, y, fa)
    tar = int(input())
    print('the topFather of %d is %d.'%(tar, find(tar, fa)))

if __name__ == '__main__':
    test()
        
    
    
