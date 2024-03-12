
    
class budget():
    def __init__(self):
        self.current_budget=0
        self.f_in_=[]
        self.f_out_=[]
        self.in_=[]
        self.out_=[]
        self.inReasonBig=["용돈","투자","장학금","기타"]
        self.outReasonBig=["여가","투자","식비","기타"]

    def changeValue(self, num, choice):
        if choice==1:
            wan=num[:int(num.find("만"))]
            down=num[int(num.find("만"))+1:int(num.find("원"))]

            if wan=='':
                wan='0'
            if down=='':
                down='0'

            return str(int(wan)*10000+int(down))
    
        if choice==2:
            yi=int(int(num)/100000000)
            wan=int((int(num)-yi)/10000)
            down=int(num)-yi-wan
            return str(yi)+"억"+str(wan)+"만"+str(down)
    
    def editCurrentBudget(self):
        self.current_budget=self.changeValue(input("현재 자산을 입력하세요.\n"),1)

    def inputData(self, destination1, destination2, string): 
        selection=input("새로 입력하시려면 n, 수정하시려면 e를 입력하세요.\n")

        if selection=='n':
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

            sel=input(f"{string} 발생 월일을 입력하세요.\n (02월 17일: 0217)\n매월 발생하는 경우 월을 00으로 입력하세요.\n")
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
        elif selection=='e':
            count=0
            if len(destination2)==0:
                print("수정할 값이 없습니다!")
                return
            else:
                for v in range(0,len(destination2)):
                    print(f"{v+1}. {destination2[v]}")
                sel=input("무엇을 수정하시겠습니까?\n")
                print(destination2[sel-1])

                sel2=input("어떤 항목을 수정하시겠습니까?\n0:대분류\n1:소분류\n2:금액\n3:발생월일\n")
                if sel2=='0':
                    for v in destination1:
                        temp=f"{str(count)}. "+v
                        print(temp)
                        count+=1
                    temp_edit=input("어떤 항목으로 수정하시겠습니까?\n")
                    destination2[sel-1][0]=destination1[int(temp_edit)-1]
                    print("성공적으로 수정되었습니다!")

                else:
                    temp_edit=input("새로 입력하실 내용을 작성하세요.\n")
                    destination2[sel-1][int(sel2)]=temp_edit
                    print("성공적으로 수정되었습니다!")

                


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