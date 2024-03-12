"""
Made to practice python.
Will be used to manage my budget.
"""
from method import budget
from os import system

myBudget=budget()
system("cls")

while True:
    
    sel=input(
"""
무엇을 하시겠습니까?
1. 현재 보유 자산 수정
2. 고정 수입 수정/추가
3. 고정 지출 수정/추가
4. 변동 수입 수정/추가
5. 변동 지출 수정/추가
6. 현재 정보 출력
7. 저장
8. 불러오기 (입력하신 정보가 덮어씌워집니다!))
9. 화면 지우기
10. 나가기
""")
    if sel=='1':
        myBudget.editCurrentBudget()

    elif sel=='2':
        myBudget.inputData(myBudget.inReasonBig, myBudget.f_in_, "수입")

    elif sel=='3':
        myBudget.inputData(myBudget.outReasonBig, myBudget.f_out_, "지출")

    elif sel=='4':
        myBudget.inputData(myBudget.inReasonBig, myBudget.in_, "수입")

    elif sel=='5':
        myBudget.inputData(myBudget.outReasonBig, myBudget.out_, "지출")
    
    elif sel=='6':
        print(myBudget)

    elif sel=='7':
        pass

    elif sel=='8':
        pass

    elif sel=='9':
        system("cls")

    elif sel=='10':
        print("종료되었습니다.")
        break

