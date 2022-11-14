# 1부터 30까지의 수 중에서 3의 배수들의 합을 구하쎄yo!! for문 사용할꺼.

# 1. for문으로 1부터 30까지의 수 중 3의 배수를 찾는다.. (리스트로 출력? range 함수??) 2. 나온 수를 합산하는 공식을 만든다...
sum = 0
for i in range(3, 30+1, 3) : #step이용하면 더 이득
   # if i % 3==0 :
        print("{} + {}=".format(sum,i),  end = "")
        sum += i
print(sum) # 이건 if절이 아니니까 for문에 둬야됨.
