# (세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.
#         0 0 0 (1)
#         0 0 0 (2)
# --------------
#         0 0 0 (3)
#       0 0 0 0 (4)
#     0 0 0 0 0 (5)
# --------------
#   0 0 0 0 0 0 (6)
# (1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.
# 출력
# 첫째 줄부터 넷째 줄까지 차례대로 (3), (4), (5), (6)에 들어갈 값을 출력한다.

first = int(input("곱할 세자리 수 a를 입력하세용!"))
second = input("곱할 세자리 수 b를 입력하세용!")

second1 = second[-1]
second2 = second[-2]
second3 = second[-3]
second1 = int(second1)
second2 = int(second2)
second3 = int(second3)
third = second1 * first 
forth = second2 * first 
fifth = second3 * first
sixth = third + (forth*10) + (fifth*100)

print(f"{third}\n{forth}\n{fifth}\n{sixth}")

# 다른 방법
A = int(input())
B = input()

print(A*int(B[2]), A*int(B[1]), A*int(B[0]), A*int(B), sep='\n')

# 여기서 sep='\n' 사용하면 각 항목마다 줄바꿔줌..!!
# int형 형변환이랑 []순서 같이 사용하는게 더 간결함.

