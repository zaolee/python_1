# 1, 2, 3 ... 을 순서대로 계속 더해 합을 만드는데, 그 합이 입력한 정수보다 작을 동안만 계속 더하는 프로그램을 작성해보자.
# 즉, 1부터 n까지 정수를 하나씩 더해 합을 만드는데, 어디까지 더해야 입력한 수보다 같거나 커지는지 알아보고자 하는 문제이다.
# 하지만, 이번에는 그 때 까지의 합을 출력해야 한다. 
# 예를 들어, 57을 입력하면 1+2+3+...+8+9+10=55에서 그 다음 수인 11을 더해 66이 될 때, 그 값 66이 출력되어야 한다.

# 해결 : input()함수 써서 수 하나를 입력하게 한다. 반복문(while) 사용해서 다 더하게 함. 여기서 if 그 합이 내가 입력한 수보다 작으면 계속 더하고 else라면 출력하기

plus = int(input("마음에 드는 수 하나만 입력 부탁!!"))
total = 0 # 총합
hagisilta = 0 # 1씩 늘어나는 수

for i in range(1, plus+1):
    if total < plus:

        total += i
       
    else:
        break    


print(total)