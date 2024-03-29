# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 출력
# 첫째 줄에 A+B를 출력한다.
A, B = input("정수 A와 B를 입력하시오 : ").split()
A = int(A)
B = int(B) 
sum = A + B
print(sum)

# map 함수 : 여러요소에 하나의 함수를 한꺼번에 대응 시키는거.
# 형식 : 저장한 변수 = map(함수이름, 대응할 일련의 요소)
# 장점 : 여러개의 요소를 하나씩 함수에 적용하지 않고 한번에 이용가능, 가독성, 간결해져
# input()함수와 함께 사용하는 경우 많음.(input은 기본적으로 str형태로 나오걸랑) )
# list로 표현할때도 요긴하게 쓰임

# 두 정수 C와 D를 입력받은 다음, C-D를 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 C와 D가 주어진다. (0 < C, D < 10)
# 출력
# 첫째 줄에 C-D를 출력한다.

C, D = map(int, input("정수 C와 D를 입력하시오 : ").split())
 
minus = C - D
print(minus)

# 두 정수 E와 F를 입력받은 다음, E×F를 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 E와 F가 주어진다. (0 < E, F < 10)
# 출력
# 첫째 줄에 E×F를 출력한다.

E, F = map(int, input("정수 E와 F를 입력하시요 :").split())

mul = E * F
print(mul)

# 두 정수 M과 N을 입력받은 다음, M/N를 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 M과 N이 주어진다. (0 < M, N < 10)
# 출력
# 첫째 줄에 M/N를 출력한다. 실제 정답과 출력값의 절대오차 또는 상대오차가 10-9 이하이면 정답이다.

M, N = map(float,input("정수 M과 N을 입력하시오 :").split())

div = M / N
print(M/N)