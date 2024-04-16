
#Made to practice python.
#Will be used to manage my budget.

from datainput import budget
from os import system
from methods import *

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
{"9.":<10}{" 입력내용 적용":<40}
{"10.":<10}{" 나가기":<40}

{"="*47}
""")
    if sel=='1':
        system("cls")
        myBudget.editCurrentBudget()
        TimingFunction.pause(myBudget)

    elif sel=='2':
        system("cls")
        myBudget.inputData(myBudget.Reasons[0], myBudget.f_in_, "수입")
        TimingFunction.pause(myBudget)

    elif sel=='3':
        system("cls")
        myBudget.inputData(myBudget.Reasons[1], myBudget.f_out_, "지출")
        TimingFunction.pause(myBudget)

    elif sel=='4':
        system("cls")
        myBudget.inputData(myBudget.Reasons[0], myBudget.in_, "수입")
        TimingFunction.pause(myBudget)

    elif sel=='5':
        system("cls")
        myBudget.inputData(myBudget.Reasons[1], myBudget.out_, "지출")
        TimingFunction.pause(myBudget)
    
    elif sel=='6':
        system("cls")
        print(myBudget)
        TimingFunction.pause(myBudget)

    elif sel=='7':
        system("cls")
        myBudget.Save()
        TimingFunction.pause(myBudget)

    elif sel=='8':
        system("cls")
        myBudget.Load()
        TimingFunction.pause(myBudget)

    elif sel=='9':
        system('cls')
        myBudget.Apply()

    elif sel=='10':
        system("cls")
        print("종료되었습니다.")
        break

