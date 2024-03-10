class budget():
    def __init__(self):
        self.budget=input("현재 총 자산을 입력하세요.\n")
        self.income={}
        self.outcome={}

    def setNewBudget(self):
        self.butdget=input("현재 총 자산을 새로 입력하세요.\n")

    def setIncome(self,count):
        for value in range(0,count):
            self.income[len(self.income)+value+1]=[input("현재 고정 수입 값을 작성하세요.\n"),input("수입 원인을 작성하세요.\n")]

    def setOutcome(self,count):
        for value in range(0,count):
            self.outcome[len(self.income)+value+1]=[input("현재 고정 지출 값을 작성하세요.\n"),input("지출 원인을 작성하세요.\n")]

    def __str__(self):
        print("현재 총 자산은 {0} 입니다.".format(self.budget))
 