import datetime

today=datetime.date.today()
class setBudgetReason():
    """
    수입/지출 대분류 리스트
    """
    def __init__(self):
        self.IncomeReasonList=['용돈','아르바이트','투자','장학금', '기타']
        self.OutcomeReasonList=['여가', '식비', '교통비', '투자', '기타']

    """
    수입 대분류 지정 
    리턴값: str
    """
    def setIncomeReasonBig(self):
        print(
"""
=======대분류=======
1. 용돈
2. 아르바이트
3. 투자
4. 장학금
5. 기타
====================

""")
        a=input("해당하는 번호를 입력하세요.")
        return self.IncomeReasonList[a]
        
    """
    지출 대분류 지정
    리턴값: str
    """
    def setOutcomeReasonBig(self):
        print(
"""
=======대분류=======
1. 용돈
2. 아르바이트
3. 투자
4. 장학금
====================

""")
        a=input("해당하는 번호를 입력하세요.")
        return self.IncomeReasonList[a]
        

class budget(setBudgetReason):
    """자산 정보 목록"""
    def __init__(self):
        self.budget=input("현재 총 자산을 입력하세요.\n")
        self.f_income=[]
        self.f_outcome=[]

    """현재 자산 새로 설정(계산값과 실제 값이 다를 때 사용)"""
    def setNewBudget(self):
        self.budget=input("현재 총 자산을 새로 입력하세요.\n")

    def setIncome(self):
        sel=input(
"""
======고정 수입 설정======
1. 신규
2. 수정
3. 제거
=========================
""")
        if sel=='1':
            temp=[]
            temp.append(setBudgetReason.setIncomeReasonBig())
            temp.append(input("소분류를 입력하세요:"))
            temp.append(input("금액을 입력하세요:"))
            self.f_income.append(temp)

        elif sel=='2':
            count=1
            for value in self.f_income:
                print(f"{count}"+str(value))
                count+=1

            choice=input("어떤 항목을 수정하시겠습니까?")
            self.f_income[choice-1][0]=setBudgetReason.setIncomeReasonBig()
            self.f_income[choice-1][1]=input("소분류를 입력하세요:")
            self.f_income[choice-1][2]=input("금액을 입력하세요:")

        elif sel=='3':
            count=1
            for value in self.f_income:
                print(f"{count}"+str(value))
                count+=1

            choice=input("어떤 항목을 삭제하시겠습니까?")

            del self.f_income[choice]
            for value in self.f_income:
                print(value)
            print("성공적으로 삭제되었습니다!")


    def setOutcome(self):
        sel=input(
"""
======고정 지출 설정======
1. 신규
2. 수정
3. 제거
=========================
""")
        if sel==1:
            temp=[]
            temp.append(setBudgetReason.setOutcomeReasonBig())
            temp.append(input("소분류를 입력하세요:"))
            temp.append(input("금액을 입력하세요:"))
            self.f_income.append(temp)

        elif sel==2:
            count=1
            for value in self.f_outcome:
                print(f"{count}"+str(value))
                count+=1

            choice=input("어떤 항목을 수정하시겠습니까?")
            self.f_outcome[choice-1][0]=setBudgetReason.setOutcomeReasonBig()
            self.f_outcome[choice-1][1]=input("소분류를 입력하세요:")
            self.f_outcome[choice-1][2]=input("금액을 입력하세요:")

        elif sel==3:
            count=1
            for value in self.f_outcome:
                print(f"{count}"+str(value))
                count+=1

            choice=input("어떤 항목을 삭제하시겠습니까?")

            del self.f_outcome[choice]
            for value in self.f_outcome:
                print(value)
            print("성공적으로 삭제되었습니다!")

    def __str__(self):
        print(f"현재 총 자산은 {self.budget} 입니다.")
        print("고정 수입은 다음과 같습니다.")

        if(len(self.f_income)>0):
            for value in self.f_outcome:
                print(value)
        else:
            print("없음")

        print("고정 지출은 다음과 같습니다.")

        if(len(self.f_outcome)>0):
            for value in self.f_outcome:
                print(value)
        else:
            print("없음")

            

class budgetSet(budget):
    def __init__(self):
        super()

    

 