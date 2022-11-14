# 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 
# 입력
# 두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)
# 출력
# 첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.

A, B = map(int, input("정수 A와 B를 입력하시오 : ").split())
 
plus = A + B
 
minus = A - B

mul = A * B

div = A // B

remainder = A % B

print(f"{plus}\n{minus}\n{mul}\n{div}\n{remainder}")