import datetime
import os

class TimingFunction():
    """These Functions are for Loading"""
    def loading(self,time):
        timeset=datetime.datetime.now()+datetime.timedelta(seconds=time)
        while datetime.datetime.now()<timeset:
            continue

    def pause(self):
        temp=input("계속하시려면 아무 버튼이나 누르세요....\n")
        if type(temp)==type(""):
            return
    
class DateFunction():
    """This Function Returns Selected Date, YMD Seperated By Selected 'type'"""
    def __init__(self):
        self.edittype=""
        self.c_str=""
    
    def getfDate(self):
        
        while True:
            datacheck=[]
            checklist=[str(v) for v in range(10)]
            data=input("\n발생 월일을 입력하세요.\n=>2024년 02월 17일: 240217\n매년, 매월 발생하는 경우 해당 항목을 00으로 입력하세요.\n=>")

            for v in data:
                if v not in checklist:
                    datacheck.append('f')
            if ('f' in datacheck) | len(data)!=6:
                print("잘못입력하셨습니다! 다시 입력하세요.\n=>",end="")
            
            else:
                break

        if ((data[0]=='0') & (data[1]=='0')):
            date=f"RR/{data[2:4]}/{data[4:]}"
            return date

        elif((data[2]=='0') & (data[3]=='0')):
            date=f"{data[:2]}/RR/{data[4:]}"
            return date
                
        else:
            date=datetime.datetime(int(f"20{data[0]}{data[1]}"),int(f"{data[2]}{data[3]}"),int(f"{data[4]}{data[5]}")).strftime("%x")
            return date

class SaveFunction():
    """This Function is for Saving"""
    def SaveData(self,data0,data1,data2,data3,data4,data5):
        f=open(os.getcwd()+"/log.txt","w")
        """자산입력"""
        f.write("비유동자산\n")
        f.write(str(data0))
        f.write("\n")
        f.write("=\n")

        f.write("유동자산\n")
        f.write(str(data1))
        f.write("\n")
        f.write("=\n")

        """데이터1 저장"""
        f.write("고정지출\n")
        self.SaveFunction(f,data2)
        f.write("=\n")

        """데이터2 저장"""
        f.write("고정수입\n")
        self.SaveFunction(f,data3)
        f.write("=\n")

        """데이터3 저장"""
        f.write("변동지출\n")
        self.SaveFunction(f,data4)
        f.write("=\n")

        """데이터4 저장"""
        f.write("변동수입\n")
        self.SaveFunction(f,data5)
        f.write("=\n")

        f.close()

    
    def SaveFunction(self,destination,data):
        for v in data:
            tempdata=""
            for j in v:
                tempdata+=str(j)+"+"
            tempdata=tempdata[:len(tempdata)-1]
            destination.write(tempdata+"\n")

class LoadFunction():
    """This Function is for Loading"""
    def LoadData(self,type1,str):
        f=open(os.getcwd()+"/log.txt","r")
        while True:
            tempdata=f.readline().strip()
            if tempdata==str:
                changed_data=self.LoadFunction(f,type1)

            elif tempdata=="":
                break
        f.close()
        return changed_data



    def LoadFunction(self,destination,data):
        if type(data)==type([]):
            for i in range(len(data)):del data[i]

        temp=destination.readline().strip()
        while len(temp)>4:
            if temp=="=":
                break

            elif type(data)==type(""):
                data=temp
            else:
                data.append(temp.split("+"))
            temp=destination.readline().strip()
        return data
            
class LetterTransFunction():
    """This Function is for changing value including korean to pure number or the other direction."""
    def GetOrChangeValue(self, choice)->str:
        """If there are letters that does not match the condition it will add false to checklist.
            if checklist contains f it asks for another input."""
        
        if choice==1:
            tt="0"
            o="0"
            while True:
                templist=",".join(input("\n금액을 입력하세요.\n=>").replace(" ","")).split(",")

                if '만' in templist:
                    templist[templist.index('만')]="-2"

                if '원' in templist:
                    templist[templist.index('원')]="-1"
            
                ite=[str(v) for v in range(-2,10)]

                checklist=[]
                
                for j in templist:
                    if j not in ite:
                        checklist.append("f")
                    else:
                        checklist.append("t")

                if "f" in checklist:
                    os.system("cls")
                    print("잘못된 형식으로 입력하셨습니다!\n다시 입력하세요.")

                else:
                    break
                
            if '-2' not in templist:
                templist.insert(0,"-2")

            if '-1' not in templist:
                templist.append("-1")

            for v in templist[:templist.index("-2")]:
                tt+=v
            for v in templist[templist.index("-2")+1:templist.index("-1")]:
                o+=v

            returnnum=str(int(tt)*10000+int(o))
            return returnnum
    
        elif choice==2:
            """숫자로만 된 경우 한글(str)형 반환"""
            pass
    
class DisplayFunction():
    #This Function Displays the Selected Data(List) with Good Display Format
    def showList(self,data,type,*data_k):
        if type=='f':
            print(f"{str(data_k[0]):<10}{str(data_k[1]):<25}{str(data_k[2]):<25}{str(data_k[3]):<20}{str(data_k[4]):<20}{str(data_k[5]):<20}{str(data_k[6]):<15}")
            if len(data)==0:
                print("없음")
            for v in data:
                print(f"{data.index(v)+1:<10}{v[0]:<25}{v[1]:<25}{v[2]:<20}{v[3]:<20}{v[4]:<20}{v[5]:<15}")

