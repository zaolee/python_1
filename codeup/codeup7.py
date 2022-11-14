#  3 6 9 게임은? 여러 사람이 순서를 정한 후, 순서대로 수를 부르는 게임이다.
# 만약 3, 6, 9 가 들어간 수를 자신이 불러야 하는 상황이라면, 수를 부르는 대신 "박수(X)" 를 쳐야 한다.
# 33과 같이 3,6,9가 두 번 들어간 수 일때, "짝짝"과 같이 박수를 두 번 치는 형태도 있다. 
# 1 부터 그 수까지 순서대로 공백을 두고 수를 출력하는데, 3 또는 6 또는 9가 포함 되어있는 수인 경우, 그 수 대신 영문 대문자 X 를 출력한다.

# 해결방법 : 해당 숫자에 3,6,9가 들어가면 X로 출력 ? 나머지들은 그대로 출력

sam69 = int(input("30 보다 작은 정수 1개를 입력하시와요,,"))

for i in range(1, sam69+1):
    if ((i % 10 == 3 ) or (i % 10 == 6 ) or (i % 10 == 9 )):
        print("X",end=" ")
    else:
        print(i,end=" ")



# 3,4,6, = 나머지가 3,6,9,가 나오는걸 선택하면 돼!!    <- 이 공식을 생각해 내는게 강권    

        



