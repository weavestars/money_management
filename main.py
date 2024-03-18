"""
Made to practice python.
Will be used to manage my budget.
Page1/3 (Main Page)
"""
from datainput import budget
from os import system
from methods import pause,loading

myBudget=budget()
while True:
    system("cls")
    sel=input(
f"""
{"자산관리시스템":=^40}

{"1.":<10}{" 현재 보유 자산 수정":<40}
{"2.":<10}{" 고정 수입 수정/추가/삭제":<40}
{"3.":<10}{" 고정 지출 수정/추가/삭제":<40}
{"4.":<10}{" 변동 수입 수정/추가/삭제":<40}
{"5.":<10}{" 변동 지출 수정/추가/삭제":<40}
{"6.":<10}{" 현재 정보 출력":<40}
{"7.":<10}{" 저장":<40}
{"8.":<10}{" 불러오기":<40}
{"9.":<10}{" 화면 지우기":<40}
{"10.":<10}{" 나가기":<40}

{"=":=^47}
""")
    if sel=='1':
        system("cls")
        myBudget.editCurrentBudget()
        pause()

    elif sel=='2':
        system("cls")
        myBudget.inputData(myBudget.inReasonBig, myBudget.f_in_, "수입")
        pause()

    elif sel=='3':
        system("cls")
        myBudget.inputData(myBudget.outReasonBig, myBudget.f_out_, "지출")
        pause()

    elif sel=='4':
        system("cls")
        myBudget.inputData(myBudget.inReasonBig, myBudget.in_, "수입")

    elif sel=='5':
        system("cls")
        myBudget.inputData(myBudget.outReasonBig, myBudget.out_, "지출")
        pause()
    
    elif sel=='6':
        system("cls")
        print(myBudget)
        pause()

    elif sel=='7':
        system("cls")
        myBudget.Save()
        pause()

    elif sel=='8':
        system("cls")
        myBudget.Load()
        pause()

    elif sel=='9':
        system("cls")

    elif sel=='10':
        system("cls")
        print("종료되었습니다.")
        break

