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

def Send():
    window=Toplevel(root)
    window.title("Send")
    window.geometry('450x560+500+200')
    window.resizable(False,False)
    
    def select_file():
        global filename
        filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select Image File",
                                            filetype=(('file_type','*.txt'),('all files','*.*')))
        
    def sender():
        s=socket.socket()
        host=socket.gethostname()
        port=8080
        s.bind((host,port))
        s.listen(1)
        print(host)
        print("Waiting for any incoming connections....")
        conn,addr=s.accept()
        file=open(filename,'rb')
        file_data=file.read(1024)
        conn.send(file_data)
        print("Data has been transmitted successfully....")
    #icon
    image_icon1= PhotoImage(file = "Images/send.png")
    window.iconphoto(False,image_icon1)
    
    Sbackground = PhotoImage(file="Images/sender.png")
    Label(window,image=Sbackground).place(x=-2,y=0)
    
    Mbackground= PhotoImage(file="Images/id.png")
    Label(window,image=Mbackground,bg='#f4fdfe').place(x=100,y=260)
    
    host=socket.gethostname()
    Label(window,text=f'ID:{host}',bg="white",fg="black").place(x=140,y=290)
    
    Button(window,text="+ Select file",width=10,height=1,font="arial 14 bold",bg="#fff",fg = "#000" ,command=select_file).place(x=160,y=150)
    Button(window,text="SEND",width=10,height=1,font="arial 14 bold",bg="#000",fg = "#fff" ,command=sender).place(x=300,y=150)
    window.mainloop()
def Receive():
    main=Toplevel(root)
    main.title("Send")
    main.geometry('450x560+500+200')
    main.resizable(False,False)
    
    def receiver():
        ID=SenderID.get()
        filename1=incomingFile.get()
        
        s=socket.socket()
        port=8080
        s.connect((ID,port))
        file=open(filename1, 'wb')
        file_data = s.recv(1024)
        file.write(file_data)
        file.close()
        print("File has been received succesfully...")
    
    #icon
    image_icon1= PhotoImage(file = "Images/receive.png")
    main.iconphoto(False,image_icon1)
    
    Hbackground=PhotoImage(file = "Images/receiver.png")
    Label(main,image=Hbackground).place(x=-2,y=0)
    
    logo=PhotoImage(file = "Images/profile.png")
    Label(main,image=logo,bg="#f4fdfe").place(x=10,y=250)
    
    Label(main,text="Receive",font=('arial',20),bg="#f4fdfe").place(x=100,y=280)
    
    Label(main,text="Input sender id ",font=('arial',10 ,"bold"),bg="#f4fdfe").place(x=20,y=340)
    SenderID= Entry(main,width=25,fg="black",border=2,bg="white",font=('arial',15))
    SenderID.place(x=20,y=370)
    SenderID.focus()
    
    Label(main,text="file name for incoming file:",font=('arial',10 ,"bold"),bg="#f4fdfe").place(x=20,y=420)
    incomingFile= Entry(main,width=25,fg="black",border=2,bg="white",font=('arial',15))
    incomingFile.place(x=20,y=450)
    
    imageicon=PhotoImage(file="Images/arrow.png")
    rr=Button(main,text="Receive",compound=LEFT,image=imageicon,width=130,bg="#39c790",font="arial 14 bold",command=receiver)
    rr.place(x=20,y=500)
    
    
    main.mainloop()
    
#icon
image_icon = PhotoImage(file = "Images/icon.png")
root.iconphoto(False,image_icon)

Label(root , text="File Tranfer" ,font=('Arial',20 ,'bold'),bg="#f4fdfe").place(x=20 ,y=30)
Frame(root,width=400,height=2,bg ="#f3f5f6").place(x=25 ,y=80)

sendImage = PhotoImage (file = "Images/send.png")
send = Button(root ,image=sendImage ,bg="#f4fdfe",bd = 0,command=Send)
send.place(x=60 ,y=100)

receiveImage = PhotoImage (file = "Images/receive.png")
receive = Button(root , image = receiveImage ,bg="#f4fdfe",bd = 0,command=Receive)
receive.place(x=300 ,y=100)

#label 
Label(root,text ="Send", font=('acumin Variable Concept' , 17 ,'bold'),bg="#f4fdfe").place(x = 70 , y = 200)
Label(root,text ="Receive", font=('acumin Variable Concept' , 17 ,'bold'),bg="#f4fdfe").place(x =300 , y = 200)

background = PhotoImage(file ="Images/background.png")
Label(root ,image = background).place(x=-2 , y =323)

root.mainloop()