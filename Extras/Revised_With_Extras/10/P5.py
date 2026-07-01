from random import randint

class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, From, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {From} to {to}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getFare(self, From, to):
        print(f"Ticket fare in train no: {self.trainNo} from {From} to {to} is {randint(222, 9999)}")
    
    def getCoach(self, coach):
        print(f"Coach selection: {coach}")

t = Train(12334)
t.book("Rampur", "Delhi")
t.getStatus()
t.getFare("Rampur", "Delhi")
t.getCoach("AC")