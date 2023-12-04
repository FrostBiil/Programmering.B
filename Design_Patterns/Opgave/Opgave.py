from tkinter import *  
from abc import ABC, abstractmethod 

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class SetBlackBackground(Command):
    def __init__(self):
        super()
        


    def execute(self):
        root.configure(background='black')

class SetGreenBackground(Command):
    def __init__(self):
        super().__init__()

    def execute(self):
        root.configure(background='green')


setBlack = SetBlackBackground()
setGreen = SetGreenBackground()

#Lav et tkinter vindue
root = Tk()              
 
#Åben vinduet
root.geometry('500x500') 

#Lav en knap
btnBlack = Button(root, text = 'Sort baggrund !', bd = '5', command = setBlack.execute) 
 
# Sæt positionen af knap på vindue   
btnBlack.pack(side = 'top')    
 
btnGreen = Button(root, text = 'Grøn Baggrund !', bd = '5', command = setGreen.execute)

btnGreen.pack(side = 'top')

root.mainloop()

