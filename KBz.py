import tkinter as tk
from tkinter import ttk

import webbrowser

from tkinter import messagebox as mbox
import collections
from collections import OrderedDict
from tkinter import * 
import mysql.connector as mysql
import sqlite3

import pandas as pd

#Connect database
conn = sqlite3.connect('database1.db')


# Combobox for Antibiotics
def getSelectedComboItem():
	return Antibiotic.get()

# Creates Combobox for culture
def getSelectedComboItem():
	return Culture.get()

# Creates Entry box of ZOI
def getInputBoxValue():
	userInput = zoi.get()
	return userInput

# Creates output button
def btnClickFunction():
	print('Interpret')

# Creates exit button
def ask_quit():
    if tkMessageBox.askokcancel("Quit", "You want to quit now?"):
        root.destroy()

#Create 



# Creates hyperlink
def openweb():
    webbrowser.open('https://asm.org/getattachment/2594ce26-bd44-47f6-8287-0657aa9185ad/Kirby-Bauer-Disk-Diffusion-Susceptibility-Test-Protocol-pdf.pdf')

# Create popup
def popupmsg():
    popup=tk.Tk()
    
    def leavemini():
        popup.destroy()
    popup.wm_title("About")
    label= ttk.Label(popup,text="Made by Namstaxk (Naman Devadiga) Application available as open source in .....",font='Helvitica')
    label.pack(side="top",fill="x",pady=60,padx=60)
    B1=ttk.Button(popup,text="Okay",command=leavemini,padx=10,pady=20)
    B1.pack()
    popup.mainloop

    
#Creates widget
root = Tk()

#Asign variable to OrderedDic
od=OrderedDict()


#Creates submit button
Button(root, text='Interpret', bg='#F0F8FF', font=('calibri', 12, 'bold')).place(x=350, y=230)
Button(root, text='Experiment procedure', bg='#F0F8FF', font=('calibri', 12, 'bold'), command=openweb).place(x=105, y=230)




# This is the section of code which creates the main window
root.geometry('650x475')
root.resizable(0,0)
root.configure(background='white')
root.title('KBz - Interpretator')

# Creates title of input
Antibiotic= Label(text="Antibiotic Disk",bg="white",font=("calibri",12)).place(x=40,y=42.5)
Culture = Label(text="Culture type",bg="white", font=("calibri",12)).place(x=40,y=112)
length = Label(text="Lenght of ZOI (in mm)",bg="white", font=("calibri",12)).place(x=40,y=177)
mm= Label(text="mm",bg="white",font=("calibri",12)).place(x=410,y=177) 

# Creates internal value of Combobox
Antibiotic= ttk.Combobox(root,state="readonly",values=['---Select One---',"Amikacin (30 ug)","Ampillicin (10 ug)","Cefoperazone (75 ug)","Cefotaxime (30 ug)","Cefazolin (30 ug)","Clindamycin (2 ug)","Erythromycin (15 ug)","Gentamicin (10 ug)","Oxacillin (3 ug)","Penicillin G (10 ug)","Piperacillin (100 ug)","Tetracylin (30 ug)","Ticarcillin (75 ug)","Tobramycin (10 ug)","Trimethoprinm (5 ug)","Vancomycin (30 ug)"], font=('calibri', 12, 'normal'), width=30)
Antibiotic.place(x=190, y=40)
Antibiotic.current(0)

Culture= ttk.Combobox(root,state="readonly",values=['---Select Micro-organinsm---',"Staphylococcus species","Pseudomonas aeruginosa and other non-fermenting Gram Negative rod",'E.coli and other enteric Gram Negative rods',], font=('calibri', 12, 'normal'), width=50)
Culture.place(x=190, y=110)
Culture.current(0)

# Takes input
zoi=Entry(root,bd=3,font=(3))
zoi.place(x=220, y=175)


 

menu = Menu(root) 
root.config(menu=menu) 
filemenu = Menu(menu,tearoff=False) 
menu.add_cascade(label='About',command=popupmsg)
helpmenu = Menu(menu,tearoff=False) 
menu.add_cascade(label='Help', menu=helpmenu)
menu.add_cascade(label='Exit',command=root.destroy)
helpmenu.add_command(label='Experiment guide',command=openweb)
helpmenu.add_command(label='Kirby Bauer chart',command=openweb)


root.mainloop()

