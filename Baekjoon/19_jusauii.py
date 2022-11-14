# 1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.
# 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
# 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
# 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.
# 예를 들어, 3개의 눈 3, 3, 6이 주어지면 상금은 1,000+3×100으로 계산되어 1,300원을 받게 된다. 또 3개의 눈이 2, 2, 2로 주어지면 10,000+2×1,000 으로 계산되어 12,000원을 받게 된다. 3개의 눈이 6, 2, 5로 주어지면 그중 가장 큰 값이 6이므로 6×100으로 계산되어 600원을 상금으로 받게 된다.
# 3개 주사위의 나온 눈이 주어질 때, 상금을 계산하는 프로그램을 작성 하시오.
# 입력
# 첫째 줄에 3개의 눈이 빈칸을 사이에 두고 각각 주어진다.
# 출력
# 첫째 줄에 게임의 상금을 출력 한다.

dice_a, dice_b, dice_c = map(int, input("3개의 주사위의 나온 눈을 입력바랍니다람쥐 :").split())


if dice_a == dice_b == dice_c:
    print(10000 + (dice_a*1000))

elif dice_a == dice_b != dice_c or dice_a != dice_b == dice_c or dice_b != dice_a == dice_c:
    if dice_a == dice_b != dice_c or dice_c == dice_a != dice_b:
        print(1000 + (dice_a*100))

    elif dice_a != dice_b == dice_c:
        print(1000 + (dice_b*100))

elif dice_a != dice_b != dice_c:
    if dice_a >= dice_b and dice_a >= dice_c:
        print(dice_a*100)

    elif dice_b >= dice_a and dice_b >= dice_c:
        print(dice_b*100)

    elif dice_c >= dice_b and dice_c >= dice_a:
        print(dice_c*100)

# 베스트 풀이

dice_d = sorted(list(map(int, input().split()))) # list, sortes 사용해서 오름차순으로 정리 

if len(set(dice_d)) is 1: # set은 집합으로 만들어주고 중복따위 없어, 즉 저렇게 하면 3개다 같은 수라서 len의 값이 1이 되는거
    print(10000 + dice_d[0]*1000)
elif len(set(dice_d)) is 2: # len의 값이 2개일때 (즉 중복이 2개 나와서 set으로 중복은 없어져서 2개가 됨)
    print(1000 + dice_d[1]*100)  
else:
    print(dice_d[2]*100) # 그외 값

# 생각보다 list를 활용을 잘못하는것 같아서.. 자주 써보기!!
# sort가 중요한 이유 : 점수 높은순으로 배열시켜줭, 이름순으로 배열해줘 이런거 유용...
# 여기서 sort()와 sorted()차이
# 1. sort()는 기존 리스트의 순서를 변경하는거임.
# 2. sorted()는 기존 리스트는 두고 새롭게 데이터 만드는거.
# 그래서 둘이 쓸때도, sort()는 해당 list변수에 변수명.sort()이렇게 쓰면 되는데, 
# sorted()는 변수명1 = sorted(변수명2) 이렇게 해서 변수명1 을 사용하는교,,,
# 즉 데이터를 변경할땐 sort()사용하고, 기존 데이터는 유지하고 새롭게 만들고 싶은거면 sorted() 사용하기!!
# 굳이 장황하게 쓰지말고 최대한 간결하게 수학적 접근으로 다가가기.
