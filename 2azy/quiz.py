#if문 quiz
domain = input("웹사이트 주소를 입력해주세요.>")
a = domain.split(".")
if a[-1] == "kr" :
    print("한국")
elif a[-1] == "uk":
    print("영국")
elif a[-1] == "com":
    print("기업용")
elif a[-1] == "org":
    print("기관")
else :
    print("해당사항이 없습니다.")                