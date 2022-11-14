# print(max_min_search(15, 30, 4, 60, 7, 80, 32)) 해서 출력값이 (80,4) 나오게하기

# 첫번째 출력값은 최대가 나와야되고, 두번째 출력값은 최소가 나와야됨.

def max_min_search(*args1):
    return(max(args1),min(args1))

print(max_min_search(15, 30, 4, 60, 7, 80, 32)) 
