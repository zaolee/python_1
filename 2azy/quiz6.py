# 끝말잇기 함수 만들기

# 1. input 써서 물어보기 2. if 끝말이 맞다면? 끝말을 이어주세용 else? 끝말이 이어지지않아용가리 3. 반복 (return값??)

# 만약 호출한 끝말과 내가 적은 첫말이 같다면?


def game(str1) :
    while True:
        print(str1)
        str2 = input("끝말을 이어주세용 >")
        if str1[-1] == str2[0]:
            str1 = str2 # str1에 str2를 넣어라!!
        else :
            print("끝말2 이어지지 않아용,,,ㅜㅜ !!")
            break    
game("표범")            