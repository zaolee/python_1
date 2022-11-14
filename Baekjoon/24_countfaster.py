# # 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# # 입력
# # 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# # 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# # 출력
# # 각 테스트 케이스마다 A+B를 출력한다.

# import sys


# TC = sys.stdin.readline()
# TC = int(TC)
# for i in range(0, TC):
#     A, B = sys.stdin.readline().split()
#     A = int(A)
#     B = int(B)
#     print(A + B)

def get_yearly_revenue(monthly_revenue):
    monthly_revenue * 12


def get_yearly_expenses(monthly_expenses):
    monthly_expenses * 12


def get_tax_amount(profit):
    if(profit > 100,000):
        profit * 0.25
    else:
        profit * 0.15
    


def apply_tax_credits(tax_amount, tax_credits):
    tax_amount * tax_credits  

# Don't touch anthing below this line 🙅🏻‍♂️🙅🏻‍♀️

monthly_revenue = 5500000
monthly_expenses = 2700000
tax_credits = 0.01

profit = get_yearly_revenue(monthly_revenue) - get_yearly_expenses(monthly_expenses)

tax_amount = get_tax_amount(profit)

final_tax_amount = tax_amount - apply_tax_credits(tax_amount, tax_credits)

print(f"Your tax bill is: ${final_tax_amount}")


