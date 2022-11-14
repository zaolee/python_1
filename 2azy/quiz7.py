

def b(num,*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)


b(10, 20, 30)        