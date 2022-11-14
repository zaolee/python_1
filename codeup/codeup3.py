# 영문 소문자 'q'가 입력될 때까지
# 입력한 문자를 계속 출력하는 프로그램을 작성해보자.

# 해결방안 -> input 써서 입력하세요!! 하고 for문안에 if구절 만약 q가 맞다면 -> 그레잇!!  else -> 다시하세요 (return? 이려나??) 

def qqq() :
    while True:  
        q = input("여왕이란 의미로 _ueen에서 밑줄에 들어갈 스펠링은??(소문자로 기재해주세요) : ")
        if q == "q" :
            return("정답입니다!! 그뤠잇!!")
        else:
            print("땡!!! 다시해주세요ㅜㅜ ")  
            
print (qqq())   



# for문 대신 while문쓰기