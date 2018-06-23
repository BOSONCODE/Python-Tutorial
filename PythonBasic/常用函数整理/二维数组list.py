'''
funciton: 用list开一个相当于C++中的二维数组
'''
#先来一个正确的姿势
#这个函数是定义一个dim维n*m的张量
def GetArrayn(n, m, dim):
    '''matrix = [[0 for i in range(n)] for i in range(n)]
    return matrix
    '''
    if dim == 1:
        raise Exception('维度至少是2')
    if dim == 2:
        return [[0 for i in range(m)] for i in range(n)]
    return [GetArrayn(n, m, dim - 1) for i in range(n)]

def GetVectorn(n, m, dim):
    if dim == 1:
        raise Exception('维度至少是2')
    if dim == 2:
        return [[] for i in range(n)]
    return [GetArrayn(n, m, dim - 1) for i in range(n)]

if __name__ == '__main__':
    #定义一个n*m的二维数组只需要调用 GetArrayn(n, m, 2)
    n = 3; m = 2;
    matrix = GetArrayn(n, m, 2)
    print(matrix)
