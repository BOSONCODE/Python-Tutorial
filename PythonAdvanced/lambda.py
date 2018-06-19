if __name__ == '__main__':
    a = [5]
    b = a
    print(id(b), id(a))
    a[0] = 6
    print(a, b)
