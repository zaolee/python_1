# KOI 전자에서는 건강에 좋고 맛있는 훈제오리구이 요리를 간편하게 만드는 인공지능 오븐을 개발하려고 한다. 인공지능 오븐을 사용하는 방법은 적당한 양의 오리 훈제 재료를 인공지능 오븐에 넣으면 된다. 그러면 인공지능 오븐은 오븐구이가 끝나는 시간을 분 단위로 자동적으로 계산한다.
# 또한, KOI 전자의 인공지능 오븐 앞면에는 사용자에게 훈제오리구이 요리가 끝나는 시각을 알려 주는 디지털 시계가 있다.
# 훈제오리구이를 시작하는 시각과 오븐구이를 하는 데 필요한 시간이 분단위로 주어졌을 때, 오븐구이가 끝나는 시각을 계산하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에는 현재 시각이 나온다. 현재 시각은 시 A (0 ≤ A ≤ 23) 와 분 B (0 ≤ B ≤ 59)가 정수로 빈칸을 사이에 두고 순서대로 주어진다. 두 번째 줄에는 요리하는 데 필요한 시간 C (0 ≤ C ≤ 1,000)가 분 단위로 주어진다.
# 출력
# 첫째 줄에 종료되는 시각의 시와 분을 공백을 사이에 두고 출력한다. (단, 시는 0부터 23까지의 정수, 분은 0부터 59까지의 정수이다. 디지털 시계는 23시 59분에서 1분이 지나면 0시 0분이 된다.)

A, B = map(int, input("지금 몇시여! : ").split())
C = int(input("요리하는데 필요한 시간을 입력하시오 : "))

B = B + C

if (B >= 60) and (0 <= A < 23):
    mok = B // 60
    B = B % 60
    if (A+mok >= 24):
        A = A+mok
        A -= 24
    else:
        A = A + mok
    print(A, B)

elif (B >= 60) and (A == 23):
    mok = B // 60
    B = B % 60
    if (A+mok >= 24):
        A = A+mok
        A -= 24
    print(A, B)

elif (B < 60):
    print(A, B)


# 일단, 60을 넘으면 +1을 하라는 아주 단순한 생각..., c의 범위가 넓기 때문에 60으로 나누어진 몫과 나머지를 활용해야됨!!
# 마지막에 '시'가 24시를 넘으면 0을 리셋되기 때문에 조건문 사용해서 -24하고 아니면 그냥 '시' 와 몫 합해주는걸로 걸어줘야됨!!
# 나름 기초적인 문제인데 나누기 60을 생각조차 하지 못했다...

h, m = map(int, input().split()) # 시, 분 입력 
t = h*60+m+int(input()) # 시를 분으로 환산하고 추가 시간 입력해서 다합하기 = t
print(t//60 % 24, t % 60) # t 나누기 60의 몫 을 24로 나눴을때 나머지 = 시, t 나누기 60의 나머지가 분....

# 다른분 풀이인데, 그저 감탄뿐;;