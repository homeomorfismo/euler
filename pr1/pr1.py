def get_mult(bound,mlist):
    mult = [] # Empty list
    for n in range(1000):
        for j in range(len(mlist)):
            if n%mlist[j] == 0:
                mult.append(n)
                break
    return mult # Return list

def sum_list(l):
    s = 0
    for i in range(len(l)):
        s = s + l[i]
    return s

print(sum_list(get_mult(1000,[3,5])))
