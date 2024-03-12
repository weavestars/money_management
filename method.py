class budget():
    def __init__(self):
        self.current_budget=0
        self.f_in_=[]
        self.f_out_=[]
        self.in_=[]
        self.out_=[]
        self.inReasonBig=["용돈","투자","장학금","기타"]
        self.outReasonBig=["여가","투자","식비","기타"]

    def editCurrentBudget(self):
        self.current_budget=input("현재 자산을 입력하세요.\n")

    def inputData(self, destination1, destination2, string): 
        """destintion1: 대분류리스트, destination2: f_in 등"""
        temporaryList=[]
        count=1

        print(f"===========")
        for v in destination1:
            temp=f"{str(count)}. "+v
            print(temp)
            count+=1
        print(f"==========")

        sel=input("대분류를 선택하세요. (숫자 입력)\n")
        temporaryList.append(destination1[int(sel)])

        sel=input("소분류를 입력하세요.\n")
        temporaryList.append(sel)

        sel=input("금액을 입력하세요\n")
        temporaryList.append(str(sel))

        sel=input(f"{string} 발생 월일을 입력하세요. (02월 17일: 0217)")
        temporaryList.append(sel)

        while True:
            if temporaryList in destination2:
                choice=str(input("이미 동일하게 입력하신 항목이 있습니다. 계속하시겠습니까? (Y/N)\n")).upper()
                if choice=='Y':
                    destination2.append(temporaryList)
                    print("성공적으로 입력되었습니다.")
                    break

                elif choice =='N':
                    print("성공적으로 취소되었습니다.")
                    break

                else:
                    print("정확히 입력하십시오. (Y/N 중 하나 입력)")
            else:
                destination2.append(temporaryList)
                print("성공적으로 입력되었습니다.")
                break

    def __str__(self):
        total_f_in=self.getTotalValue(self.f_in_)
        total_f_out=self.getTotalValue(self.f_out_)
        total_out=self.getTotalValue(self.out_)
        total_in=self.getTotalValue(self.in_)
        
        return f"""
현재 자산:{self.current_budget}
고정수입합계:{total_f_in}
고정지출합계:{total_f_out}
"""
    def getTotalValue(self,destination):
        temp=0
        if len(destination)==0:
            return 0
        else:
            for v in destination:
                temp+=int(v[2])
            return temp

"""이번 달 수입(변동):{total_in}
이번 달 지출(변동):{total_out}
이번 달 손익:{total_f_in+total_in-total_f_out-total_out}
"""