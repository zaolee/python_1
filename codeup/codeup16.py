# 같은 날 동시에 가입한 3명의 사람들이 온라인 채점시스템에 들어와 문제를 푸는 날짜가 매우 규칙적이라고 할 때, 다시 모두 함께 문제를 풀게 되는 그날은 언제일까?
# 예를 들어 3명이 같은 날 가입/등업하고, 각각 3일마다, 7일마다, 9일마다 한 번씩 들어온다면, 처음 가입하고 63일 만에 다시 3명이 함께 문제를 풀게 된다.

# 해결 : input으로 3명 수 호출 -> while문으로 해서 반복 ㄱㄱ 하고 3개가 0이아니면 하루가 지나고 총3개가 1이 되면 그 날을 출력해주세요!!

a, b, c = input("3명의 응시자가 응시할 주기를 차례대로 입력해주세요!!:").split()

a = int(a)
b = int(b)
c = int(c)
d = 1 
while (d % a != 0) or (d % b != 0) or (d % c != 0):  
    # d 에서 a를 나눈 나머지가 0이 아니거나 d 에서 b를 나눈 나머지가 0이 아니거나 d 에서 c를 나눈 나머지가 0이 아니면
    d += 1 # d에다가 1을 더해주세요.
    # 즉 d에서 a, b, c를 각각 나눈 값의 나머지가 모두 0이면 stop하는 반복문
   
   
print("세명의 응시자가 다함께 만나는 날은:", d)