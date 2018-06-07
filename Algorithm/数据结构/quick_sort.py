'''
快速排序期望复杂度O(nlogn)
期望时间复杂度下应该是最快的排序算法
最坏的情况也能够达到O(n^2)
'''

def quick_sort(a):
    if len(a) <= 1: return a
    return quick_sort([it for it in a[1:] if it < a[0]]) + \
           [it for it in a if it == a[0]] + \
           quick_sort([it for it in a[1:] if it > a[0]])

if __name__ == '__main__':
    test = list(range(10))
    print(quick_sort(test))
