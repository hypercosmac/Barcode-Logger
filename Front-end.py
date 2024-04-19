import csv
from tkinter import *

overallarr = []
#output = "my"
with open('barcodes.csv') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
#        if row[1] == output:
        overallarr.append([row[1], row[0]])
top = Tk()
class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Attendence Register")        
        text = Text(master, width = 53, fg = 'black')
        for counter in overallarr:
            text.insert(END, counter[0])
            text.insert(END, "\n")
            text.insert(END, counter[1])
            text.insert(END, "\n")
        text.pack()
        
gui = GUI(top)
top.mainloop()
