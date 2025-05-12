from breezypythongui import EasyFrame

class GUI(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self,title='window')
        self.setSize(500,500)
        self.setResizable(False)
        self.label1=self.addLabel(text="Hiii",row=0,column=0,sticky='EWNS')
        self.enter=self.addIntegerField(value=0,row=1,column=0,sticky='EW')
        self.t1=self.addTextField(text='',row=3,column=0,sticky='EW')
        self.b1=self.addButton(text="submit",row=4,column=0,command=self.clicked)

    def clicked(self):
        v1=self.enter.getNumber()
        v2=self.t1.getValue()
        self.label1["text"]=str(v1)+v2

if __name__=='__main__':
    GUI().mainloop()