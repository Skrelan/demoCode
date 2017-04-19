def amazing_number(num):
    k = len(num)
    shift = [0] * k
    for i, n in enumerate(num):
        print 'i',i,'n',n
        if n >= k:
            continue
        elif n <= 0:
            print'9:elif n <= 0: '
            shift[0] += 1
        elif n > i:
            print '12:elif n > i:'
            shift[i + 1] += 1
            if n > i + 1: 
                shift[i + k - n + 1] -= 1
        else:
            print '17:else'
            shift[0] += 1
            shift[i - n + 1] -= 1
            if i != k - 1:
                shift[i + 1] += 1
        print shift
    total = 0
    index = 0
    max_number = 0
    for i, s in enumerate(shift):
        total += s
        if total > max_number:
            max_number = total
            index = i
    print index
    return index

# num = [0, 1, 2, 3]
# assert amazing_number(num) == 0

num = [1, 0, 0]
assert amazing_number(num) == 1

# num = [5, 3, 8, 7, 2]
# assert amazing_number(num) == 2

# num = [4, 0, 1, 2, -1]
# assert amazing_number(num) == 1
