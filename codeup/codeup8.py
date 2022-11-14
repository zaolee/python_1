# 빨강(red), 초록(green), 파랑(blue) 빛을 섞어 여러 가지 다른 색 빛을 만들어 내려고 한다.
# 빨강(r), 초록(g), 파랑(b) 각 빛의 가짓수가 주어질 때, 주어진 rgb 빛들을 섞어 만들 수 있는 모든 경우의 조합(r g b)과 만들 수 있는 색의 가짓 수를 계산해보자.  
# 모니터, 스마트폰과 같은 디스플레이에서 각 픽셀의 색을 만들어내기 위해서 r, g, b 색을 조합할 수 있다. 픽셀(pixel)은 그림(picture)을 구성하는 셀(cell)에서 이름이 만들어졌다.
 
 # 해결 : input 써서 수 호출해 3개 입력해서 split르호 값 3개 나오게 하기. 각 r, g, b의 값을 -> 주사위 던지기랑 동일 -> 중첩 for문 쓰기?



r, g, b = input("red값, green값, blue값을 차례대로 넣어주세요,,!!").split()
r = int(r) 
g = int(g)
b = int(b)

for i in range(0, r):
    for j in range(0, g):
        for z in range(0, b):
            count = r * g * b 
            print(i, j, z)
print(count)


# 굿.