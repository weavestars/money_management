import datetime

"""This Functions are for Loading"""
def loading(time):
    timeset=datetime.datetime.now()+datetime.timedelta(seconds=time)
    while datetime.datetime.now()<timeset:
        continue

def pause():
    temp=input("계속하시려면 아무 버튼이나 누르세요....\n")
    if type(temp)==type(""):
        return
    
"""This Function Returns Selected Date, YMD Seperated By Selected 'type'"""
class DateFunction():
    def __init__(self):
        self.edittype=""
        self.c_str=""

    """You Can Just Use First Function for Inputting Data"""
    def inputData(self,string):
        self.edittype=string

        sel=input(f"{self.edittype} 발생 월일을 입력하세요.\n (2024년 02월 17일: 240217)\n매년, 매월 발생하는 경우 해당 항목을 00으로 입력하세요.\n")

        return self.getfDate(sel)

    
    def getfDate(self,data):
        if data=='now':
            date=datetime.datetime.now().strftime("%x")
            return date

        elif len(data)==6:
            if ((data[0]=='0') & (data[1]=='0')) | ((data[2]=='0') & (data[3]=='0')):
                pass
            
            date=datetime.datetime(int(f"20{data[0]}{data[1]}"),int(f"{data[2]}{data[3]}"),int(f"{data[4]}{data[5]}")).strftime("%x")
            return date

        else:
            print("잘못된 형식입니다! 다시 입력해주세요.\n")
            self.inputData(self.c_str,self.edittype)

class Save():
    def SaveData(self,data1,data2,data3,data4,data5):
        f=open("d:/Programming/Money_V1.0/money_v1.0/log1.txt","w")
        """자산입력"""
        f.write("자산\n")
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
            

class Load():

    def LoadData(self,type1,str):
        f=open("d:/Programming/Money_V1.0/money_v1.0/log1.txt","r")

        while True:
            tempdata=f.readline().strip()
            if tempdata==str:
                changed_data=self.LoadFunction(f,type1)

            elif tempdata=="":
                break
        f.close()
        return changed_data



    def LoadFunction(self,destination,data):
        for i in range(len(data)):
            del data[i]

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
            
            
    
"""This Function Displays the Selected Data with Good Display Format"""
def showfList(data):
    print(f"{"대분류":<7}{"소분류":<15}{"금액":<15}{"날짜":<10}{"입력날짜":<10}")
    
    