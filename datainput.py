"""This File is Only For Inputting Data. Other Methods are in methods.py"""
import methods
    
class budget():
    def __init__(self):
        self.current_budget=""
        self.f_in_=[]
        self.f_out_=[]
        self.in_=[]
        self.out_=[]
        self.inReasonBig=["용돈","투자","장학금","기타"] 
        self.outReasonBig=["여가","투자","식비","기타"]

    def changeValue(self, num, choice):
        if choice==1:
            tt="0"
            o="0"
            while True:
                templist=",".join(num.replace(" ","")).split(",")
                if '만' in templist:
                    templist[templist.index('만')]="-2"

                if '원' in templist:
                    templist[templist.index('원')]="-1"
            
                ite=[str(v) for v in list(range(-2,10))]
                for j in templist:
                    if (j not in ite):
                        templist=",".join(input("올바른 형식이 아닙니다! 다시 입력하세요.\n").replace(" ","")).split(",")
                        if '만' in templist:
                            templist[templist.index('만')]="-2"

                        if '원' in templist:
                            templist[templist.index('원')]="-1"
                        j=templist[0]
                        continue

                if '-2' not in templist:
                    templist.insert(0,"-2")
                if '-1' not in templist:
                    templist.append("-1")

                for v in templist[:templist.index("-2")]:
                    tt+=v
                for v in templist[templist.index("-2")+1:templist.index("-1")]:
                    o+=v
                break
            returnnum=str(int(tt)*10000+int(o))
            return returnnum
    
        elif choice==2:
            yi=int(int(num)/100000000)
            wan=int((int(num)-yi)/10000)
            down=int(num)-yi-wan
            """숫자로만 된 경우 한글(str)형 반환"""
            return str(yi)+"억"+str(wan)+"만"+str(down)
                    
    
    def editCurrentBudget(self):
        self.current_budget=self.changeValue(input("현재 자산을 입력하세요.\n예:\n500000:50만원\n302567:30만2567원\n"),1)

    def inputData(self, destination1, destination2, string): 
        for v in destination2:
            print(v)
            
        selection=input("새로 입력하시려면 n, 수정하시려면 e, 삭제하시려면 x, 첫 화면으로 돌아가시려면 c를 입력하세요.\n\n")

        if selection=='n':
            """destintion1: 대분류리스트, destination2: f_in 등"""
            temporaryList=[]
            count=1

            print(f"{"=":=^40}")
            for v in destination1:
                temp=f"{str(count)}. "+v
                print(temp)
                count+=1
            print(f"{"=":=^40}")

            sel=input("대분류를 선택하세요. (숫자 입력)\n")
            temporaryList.append(destination1[int(sel)-1])

            sel=input("소분류를 입력하세요.\n")
            temporaryList.append(sel)

            sel=self.changeValue(input("금액을 입력하세요\n"),1)
            temporaryList.append(sel)

            date=methods.DateFunction()
            temporaryList.append(date.inputData(string))

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
                    today=methods.DateFunction()
                    temporaryList.append(today.getfDate("now"))
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
                sel=input("몇 번 항목을 수정하시겠습니까?\n")
                print(destination2[int(sel)-1])

                sel2=input("어떤 항목을 수정하시겠습니까?\n0:대분류\n1:소분류\n2:금액\n3:발생월일\n")
                if sel2=='0':
                    for v in destination1:
                        temp=f"{str(count)}. "+v
                        print(temp)
                        count+=1
                    temp_edit=input("어떤 항목으로 수정하시겠습니까?\n")
                    destination2[int(sel)-1][0]=destination1[int(temp_edit)-1]
                    print("성공적으로 수정되었습니다!")

                else:
                    
                    temp_edit=input("새로 입력하실 내용을 작성하세요.\n")
                    destination2[int(sel)-1][int(sel2)]=temp_edit
                    print("성공적으로 수정되었습니다!")
                    
        elif selection=='x':
            if len(destination2)==0:
                print("삭제할 항목이 없습니다!")
                methods.pause()
                return
            
            else:
                for v in range(0,len(destination2)):
                    print(f"{v+1}. {destination2[v]}")
                sel=int(input("몇 번 항목을 삭제하시겠습니까?\n"))
                temp = destination2[sel-1]
                del destination2[sel-1]
            
                print(f"{temp}가 성공적으로 삭제되었습니다.")
                methods.pause()
        
        elif selection=='c':
            return
        
    def Save(self):
        save=methods.Save()
        save.SaveData(self.current_budget,self.f_out_,self.f_in_,self.out_,self.in_)
        print("성공적으로 저장되었습니다!\n")

    def Load(self):
        load=methods.Load()
        self.current_budget=load.LoadData(self.current_budget,"자산")
        self.f_in_=load.LoadData(self.f_in_,"고정수입")
        self.f_out_=load.LoadData(self.f_out_,"고정지출")
        self.in_=load.LoadData(self.in_,"변동수입")
        self.out_=load.LoadData(self.out_,"변동지출")
        print("성공적으로 불러왔습니다!")

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