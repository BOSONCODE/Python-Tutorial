import heapq

def heapq_int():
    heap = []
    heapq.heappush(heap, 10) #堆的push操作 heappush(heapname, item)
    heapq.heappush(heap, 1) 
    heapq.heappush(heap, 5)
    [heapq.heappush(heap, i)for i in range(10)]
    [heapq.heappush(heap, 10-i) for i in range(10)]
    print(heapq.nlargest(10, heap)) #nlargest ==> 大顶堆的top操作
    print([heapq.heappop(heap) for i in range(len(heap))]) #heappop(heapname) 去掉堆顶的元素并且返回

#output:
'''
[10, 10, 9, 9, 8, 8, 7, 7, 6, 6]
[0, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]
'''
if __name__ == '__main__':
    heapq_int()
