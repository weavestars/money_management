#This File is Only For Inputting Data. Other Methods are in methods.py
from methods import *
import numpy as np
import os

class budget(TimingFunction, SaveFunction, LoadFunction, LetterTransFunction, DateFunction, DisplayFunction):
    def __init__(self):
        super().__init__()
        self.current_budget=["0","0"]
        self.f_in_=[]
        self.f_out_=[]
        self.in_=[]
        self.out_=[]
        self.Reasons=np.array([["Pin Money","Investment","Scholarship","Others"], ["여가","투자","식비","기타"]])

    def inputData(self, reason, destination, string): 
        os.system('cls')
        print(f"{string}입력 내역:")
        DisplayFunction.showList(self,destination,'f',"Order","Classification(L)","Classification(s)","Price","Date","Date(Input)","Appl. Status")
        
        print(f"{"=":=<120}")
        selection=input("\n새로 입력하시려면 n, 수정하시려면 e, 삭제하시려면 x, 돌아가시려면 아무버튼이나 입력하세요.\n=>")
        os.system("cls")

        if selection=='n':
            temporaryList=[]
            count=1
            os.system('cls')

            print(f"{"=":=^40}")
            for v in reason:
                temp=f"{str(count)}. "+v
                print(temp)
                count+=1
            print(f"{"=":=^40}")

            sel=input("\n대분류를 선택하세요.\n=>")
            temporaryList.append(reason[int(sel)-1])

            sel=input("\n소분류를 입력하세요.\n=>")
            temporaryList.append(sel)

            sel=LetterTransFunction.GetOrChangeValue(self,1)
            temporaryList.append(sel)

            date=DateFunction()
            temporaryList.append(date.getfDate())

            while True:
                if temporaryList in destination:
                    os.system('cls')
                    choice=str(input("이미 동일하게 입력하신 항목이 있습니다. 계속하시겠습니까? (Y/N)\n")).upper()
                    if choice=='Y':
                        destination.append(temporaryList)
                        os.system('cls')
                        print("성공적으로 입력되었습니다.")
                        break

                    elif choice =='N':
                        print("성공적으로 취소되었습니다.")
                        break

                    else:
                        print("정확히 입력하십시오. (Y/N 중 하나 입력)")
                else:
                    temporaryList.append(datetime.datetime.now().strftime("%x"))
                    temporaryList.append("U")
                    destination.append(temporaryList)
                    print("성공적으로 입력되었습니다.")
                    break

        elif selection=='e':
            count=0
            if len(destination)==0:
                print("수정할 값이 없습니다!")
                return
            else:
                DisplayFunction.showList(self,destination,'f',"Order","Classification(L)","Classification(s)","Price","Date","Date(Input)","Appl. Status")
                sel=input("몇 번 항목을 수정하시겠습니까?\n=>")
                print(f"{"=":=<135}")

                while True:
                    if type(sel) != type(""):
                        sel=input("잘못된 형식으로 입력하셨습니다! 다시 입력하세요.\n=>")
                    elif len(destination)<int(sel):
                        sel=input("항목이 존재하지 않습니다! 다시 입력하세요.\n=>")
                    else:
                        break
                print(destination[int(sel)-1])

                sel2=input("어떤 항목을 수정하시겠습니까?\n1:대분류\n2:소분류\n3:금액\n4:발생월일\n=>")
                if sel2=='1':
                    for v in reason:
                        temp=f"{str(count)}. "+v
                        print(temp)
                        count+=1
                    temp_edit=input("어떤 항목으로 수정하시겠습니까?\n")
                    destination[int(sel)-1][0]=reason[int(temp_edit)-1]
                    print("성공적으로 수정되었습니다!")

                else:
                    
                    temp_edit=input("새로 입력하실 내용을 작성하세요.\n")
                    destination[int(sel)-1][int(sel2)-1]=temp_edit
                    print("성공적으로 수정되었습니다!")
                    
        elif selection=='x':
            if len(destination)==0:
                print("삭제할 항목이 없습니다!")
                TimingFunction.pause()
                return
            
            else:
                for cnt, v in enumerate(destination):
                    print(f"{cnt+1}. {destination[cnt]}")
                sel=input("몇 번 항목을 삭제하시겠습니까?\n")
                while True:
                    if type(sel) != type(""):
                        sel=input("잘못된 형식으로 입력하셨습니다! 다시 입력하세요.\n=>")
                    elif len(destination)<int(sel):
                        sel=input("항목이 존재하지 않습니다! 다시 입력하세요.\n=>")
                    else:
                        break

                temp = destination[int(sel)-1]
                del destination[int(sel)-1]
            
                print(f"{temp}가 성공적으로 삭제되었습니다.")
                TimingFunction.pause(self)  
        else:
            return
    
    def editCurrentBudget(self):
        #This Function Changes 만, 원 Value To Number Needed. If the format doesn't match it asks for another input.
        while True:
            choice=input(f"어떤 항목을 수정하시겠습니까?\n#1. 비유동자산:{self.current_budget[0]}\n#2. 유동자산:{self.current_budget[1]}\n=>")
            if choice=='1':
                self.current_budget[0]=LetterTransFunction.GetOrChangeValue(self,1)
                
                print("성공적으로 입력되었습니다.")
                TimingFunction.loading(self,1)
                break

            elif choice=='2':
                self.current_budget[1]=LetterTransFunction.GetOrChangeValue(self,1)
                print("성공적으로 입력되었습니다.")
                TimingFunction.loading(self,1)
                break
            else:
                print("잘못 입력하셨습니다!")
                TimingFunction.loading(self,1)
                break

        

    def Save(self):
        save=SaveFunction()
        save.SaveData(self.current_budget[0],self.current_budget[1],self.f_out_,self.f_in_,self.out_,self.in_)
        print("성공적으로 저장되었습니다!\n")

    def Load(self):
        load=LoadFunction()
        self.current_budget[0]=load.LoadData(self.current_budget[0],"비유동자산")
        self.current_budget[1]=load.LoadData(self.current_budget[1],"유동자산")
        self.f_in_=load.LoadData(self.f_in_,"고정수입")
        self.f_out_=load.LoadData(self.f_out_,"고정지출")
        self.in_=load.LoadData(self.in_,"변동수입")
        self.out_=load.LoadData(self.out_,"변동지출")
        print("성공적으로 불러왔습니다!")

    def __str__(self):
        totalfin=self.getTotalValue(self.f_in_)
        totalfout=self.getTotalValue(self.f_out_)
        totalout=self.getTotalValue(self.out_)
        totalin=self.getTotalValue(self.in_)
        
        return f"""
현재 자산:{self.current_budget}
고정수입합계:{totalfin}
고정지출합계:{totalfout}
변동수입합계:{totalin}
변동지출합계:{totalout}
"""
    def getTotalValue(self,destination):
        temp=0
        if len(destination)==0:
            return 0
        else:
            for v in destination:
                temp+=int(v[2])
            return temp
