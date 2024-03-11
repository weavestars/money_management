"""
Made to practice python.
Will be used to manage my budget.
"""
from method import budget

myBudget=budget()


while True:
    sel=input(
"""
무엇을 하시겠습니까?
1. 현재 보유 자산 수정
2. 고정 수입 수정/추가
3. 고정 지출 수정/추가
4. 현재 입력 정보 확인
5. 나가기
""")
    if sel=='1':
        myBudget.setNewBudget()

    elif sel=='2':
        myBudget.setIncome()

    elif sel=='3':
        myBudget.setOutcome()

    elif sel=='4':
        print(myBudget)

    elif sel=='5':
        print("종료되었습니다.")


