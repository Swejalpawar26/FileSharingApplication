from tkinter import *
import socket
from tkinter import filedialog
from tkinter import messagebox
import os

root = Tk()
root.title("ShareMe")
root.geometry("450x560+500+200")
root.configure(bg="#f4fdfe")
root.resizable(False,False)
#icon
image_icon = PhotoImage(file = "Images/icon.png")
root.iconphoto(False,image_icon)

Label(root , text="File Tranfer" ,font=('Arial',20 ,'bold'),bg="#f4fdfe").place(x=20 ,y=30)
Frame(root,width=400,height=2,bg ="#f3f5f6").place(x=25 ,y=80)

sendImage = PhotoImage (file = "Images/send.png")
send = Button(root ,image=sendImage ,bg="#f4fdfe",bd = 0)
send.place(x=60 ,y=100)

receiveImage = PhotoImage (file = "Images/receive.png")
receive = Button(root , image = receiveImage ,bg="#f4fdfe",bd = 0)
receive.place(x=300 ,y=100)

#label 
Label(root,text ="Send", font=('acumin Variable Concept' , 17 ,'bold'),bg="#f4fdfe").place(x = 70 , y = 200)
Label(root,text ="Receive", font=('acumin Variable Concept' , 17 ,'bold'),bg="#f4fdfe").place(x =300 , y = 200)

background = PhotoImage(file ="Images/background.png")
Label(root ,image = background).place(x=-2 , y =323)

root.mainloop()