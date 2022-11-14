def plus(a=0,b=0):
    print("{} 더하기 {}는 {}이다".format(a,b,(a+b)))

def minus(a=0,b=0):
    print("{} 빼기 {}는 {}이다".format(a,b,(a-b)))  

def multiple(a=0,b=0):
    print("{} 곱하기 {}는 {}이다".format(a,b,(a*b)))

def division(a=0,b=0):
    print("{} 나누기 {}는 {}이다".format(a,b,(a/b)))

def remainder(a=0,b=0):
    print("{} 나누기 {}의 나머지는 {}이다".format(a,b,(a%b)))

def share(a=0,b=0):
    print("{} 나누기 {}의 몫은 {}이다".format(a,b,(a%b)))    

def power(a=0):
    print("{}의 제곱은 {}이다".format(a,(a*a)))     
   #print(f"{a}의 제곱은 {a*a}이다") 

plus()                
minus(2,1)
multiple(1,1)
division(2,1)
remainder(1,1)
share(2,2)
power()


