menu = {"아이스 아메리카노" : 3000, "아메리카노" : 2500, "아이스 라떼" : 4000, "라떼" : 3500, "아이스크림" : 8000}

# 차가운 메뉴, 따듯한 메뉴로 구분해서 출력하기.
# for문 활용해야돼 continue문?
ice_menu = {} # dictionary 생성
hot_menu = {}
for i, j in menu.items() :
    if i[0:3] == "아이스":
       ice_menu[i] = j
    else :
       hot_menu[i] = j   
print(ice_menu)
for i, j in ice_menu.items():
    print("제품명 : {}, 가격 : {}".format(i,j))

print(hot_menu)
for i, j in hot_menu.items():
    print("제품명 : {}, 가격 : {}".format(i,j))    