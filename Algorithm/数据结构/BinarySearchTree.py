'''
BinarySearchTree: 二叉搜索树
Property(性质):
对于当前节点node有,
node.val > node.lchild.val
node.val < node.rchild.val
所以中序遍历的结果就是一个有序的数组
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.lchild = None
        self.rchild = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def Insert(self, val):
        p = self.root
        if None == p:
            self.root = Node(val)
            return
        fa = None
        while p != None:
            fa = p
            if p.val < val:
                p = p.rchild
            else:
                p = p.lchild
        if val < fa.val:
            fa.lchild = Node(val)
        else:
            fa.rchild = Node(val)

    def Search(self, val):
        p = self.root
        fa = None
        while p != None:
            if p.val == val:
                #print('This value has been found!')
                return p, fa
            if p.val < val:
                fa = p
                p = p.rchild
            else:
                fa = p
                p = p.lchild
        #print('This value is not found!')
        return None, None

    def Delete(self, val):
        p, fa = self.Search(val)
        if p == None:
            print('Sorry, there is no such node!')
            return
        if fa == None:      #考虑删除根的情况
            fap = None
            pp = p.rchild
            if pp == None:
                self.root = p.lchild
                return
            while pp.lchild != None:
                fap = pp
                pp = pp.lchild
            pp.lchild = p.lchild
            pp.rchild = p.rchild
            self.root = pp
            fap.lchild = None
            return 
        if p.lchild == None:    #考虑没有左儿子
            if p.val < fa.val:
                fa.lchild = p.rchild
            else:
                fa.rchild = p.rchild
        elif p.rchild == None:  #考虑没有右儿子
            if p.val < fa.val:
                fa.lchild = p.lchild
            else:
                fa.rchild = p.lchild
        else:                   #考虑有两个儿子
            fap = p
            pp = p.rchild
            while pp.lchild != None:
                fap = pp
                pp = pp.lchild
            fap.lchild = None
            if p.val < fa.val:
                fa.lchild = pp
                pp.lchild = p.lchild
                pp.rchild = p.rchild
            else:
                fa.rchild = pp
                pp.lchild = p.lchild
                pp.rchild = p.rchild

    def InOrder(self, p):
        if p.lchild != None:
            self.InOrder(p.lchild)
        print(p.val)
        if p.rchild != None:
            self.InOrder(p.rchild)

if __name__ == '__main__':
    test = BinarySearchTree()
    for i in range(5):
        test.Insert(10 - i)
    test.Delete(10)
    test.InOrder(test.root)
