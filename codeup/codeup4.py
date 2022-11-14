# 1, 2, 3 ... 을 계속 더해 나갈 때, 그 합이 입력한 정수(0 ~ 1000)보다 같거나 작을 때까지만 계속 더하는 프로그램을 작성해보자.
# 즉, 1부터 n까지 정수를 계속 더해 나간다고 할 때 어디까지 더해야 입력한 수보다 같거나 커지는 지를 알아보고자하는 문제이다.

# 해결방안 : input-> 수를 하나 정해줘. for문 1부터 해당 수까지 더해, IF 그 수보다 작아? 또 더해, else 멈춰 print 마지막으로 더한 수 출력해줘.


gabojago = int(input("0부터 1000까지의 숫자중 마음에 드는거 하나 골라보슈"))

total = 0 #합한 값

mola = 0 #1씩 늘어나는 수

for i in range(0 , gabojago+1):

    if total < gabojago:
       
       total += i
       mola += 1
       

    else:  
        break

print(mola-1)    

