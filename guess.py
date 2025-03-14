from breezypythongui import EasyFrame
import random
class Guess(EasyFrame):

    def __init__(self):
        EasyFrame.__init__(self,title="HII")
        self.setSize(300,300)
        self.setResizable(False)
        self.guess = random.randint(1, 100)
        self.heading=self.addLabel(text="Guess a random number between 1 and 100 !",row=0,column=4,columnspan=2,sticky="WENS")
        self.input=self.addIntegerField(value=0,row=4,column=4,sticky="EW")
        self.submit=self.addButton(text="Check",row=6,column=4,command=self.buttonClicked)
        self.count=0

    def buttonClicked(self):
        user = self.input.getNumber()
        self.count+=1
        if self.guess < user:
            self.heading["text"] = "Bit Lower!"
        elif self.guess > user:
            self.heading["text"] = "Bit Higher!"
        elif self.guess == user:
            self.heading["text"] = f"WOW!!! Correct in {self.count} tries"


if __name__=="__main__":
    Guess().mainloop()