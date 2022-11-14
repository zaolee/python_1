# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 출력
# 각 테스트 케이스마다 A+B를 출력한다.

import sys

star = ""

TC = sys.stdin.readline()
TC = int(TC)
for i in range(0, TC):
    star += "*"
    print(star.rjust(TC))


# .rjust() -> 왼쪽으로 정렬, 괄호안에 왼쪽으로 몇칸 옮길지 넣으면 됨.

# 다른사람들은 .rjust()사용 안하고 " "*(TC-1) 하고 * 사용, (TC-1)만큼 공백주고 *입력하겠단 뜻