# 최소값과 최대값을 입력받고 그사이에 있는 홀수와 짝수 리스트 만들기
# 순서 : 1. 최소값 최대값 입력(input함수 이용) 2.if문으로 그 사이 수들이 짝수라면? 그리고 그게 아니라면??(else) 3. while문으로 그안에 있는 수를 출력해주세요!! 4. 끝

# 1
Max_Num = int(input("최대값을 입력해주시와요,,"))
Min_Num = int(input("최소값을 입력해주시와요,,"))

# A = 짝수 리스트 B = 홀수 리스트
A_List = []
B_List = []

Num = Min_Num

# 2
if Min_Num < Max_Num :
    while Num < Max_Num:
        if Num % 2 == 0:
             A_List.append(Num)
        else:
             B_List.append(Num)
        Num += 1
    print("{}부터 {}까지의 짝수는 {}입니다람쥐.".format(Min_Num, Max_Num, A_List))
    print("{}부터 {}까지의 홀수는 {}입니다리미.".format(Min_Num, Max_Num, B_List))
else :    print("최소값{}이 최대값{}보다 커용" .format(Min_Num,Max_Num))

