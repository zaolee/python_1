# 99dan 만들기. 싸야되는거 = 중첩 for문

# i * j = 값 즉 i도 반복(2부터 9) j도 반복(1부터 9)

for i in range(2,9+1) :
    for j in range(1,9+1):
        # print("{} * {} = {}".format(i,j,i*j))
          print(f"{i} X {j} = {i*j}", end = "\t")
        #format 활용하기!!