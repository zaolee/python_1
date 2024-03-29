# 1부터 입력한 정수까지 1씩 증가시켜 출력하는 프로그램을 작성하되, 3의 배수인 경우는 출력하지 않도록 만들어보자.
# 예를 들면, 1 2 4 5 7 8 10 11 13 14 ...와 같이 출력하는 것이다.

# 해결 : input써서 값하나 입력하게 한다. 반복문 사용할꺼 for문 if 3으로 나눈 % 가 0이라면 pass(continue) 그렇지 않으면 출력

sam = int(input("원하는 수 하나 입력해보세요 ->"))

for i in range(1, sam+1):
    if i % 3 == 0:
        continue
    print(i)

# continue문을 쓰면 간단하게 해결가능함
# 조건문이나 반복문의 안에서 continue 가 실행되면, 반복 블록 안에 있는 나머지 부분을 실행하지 않고, 다음 반복 단계로 넘어감.
# 즉, 반복 블록의 나머지 부분은 실행되지 않고, 다음 단계의 반복을 계속(continue)하는 것이다.
# 여기서 3의 배수들은 if조건식에 해당되서 print까지 안가고 다음 반복 단계로 넘어가는교..