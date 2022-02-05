def even_fib(limit):
    an = 1
    an1 = 1
    fib_list = []
    while (an1 < limit):
        if (an1%2 == 0):
            fib_list.append(an1)
        tmp = an
        an = an1
        an1 = an + tmp
    return fib_list

def sum_list(l):
    S = 0
    for i in range(len(l)):
        S += l[i]
    return S

print(sum_list(even_fib(4000000)))
