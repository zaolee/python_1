from random import randint, random


print("SY카지노에 오신것을 환영합니다. 게임을 시작할게요. 100점으로 시작합니다.")

pc_choice = randint(1,100)

playing = True

score = 100

while playing:
    user_choice = int(input("1부터 100까지의 수 중에서 원하는 수를 입력하세요. ->"))
    if pc_choice > user_choice:
        print("수를 더 크게 입력하세요. -5점")
        score -=5

    elif pc_choice < user_choice:
        print("수를 더 작게 입력하세요. -5점")  
        score -=5

    elif pc_choice == user_choice:
        print("정답입니다! 총 {}점을 획득했습니다.".format(score))
        playing = False

    
