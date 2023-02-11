from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import sendmsg as sm

def send_msgg():
    if phoneEntry.get()=='' or msgEntry.get()=='':
        messagebox.showerror('Error', 'All Field Are Required')
    else:
        sm.message(phoneEntry.get(),msgEntry.get())
        login_window.destroy()
    
login_window=Tk()
login_window.geometry('990x660+50+50')#use with place
login_window.resizable(0,0)
login_window.title('Login Page')
bgImage=ImageTk.PhotoImage(file='background.jpg')

bgLable=Label(login_window,image=bgImage)
bgLable.place(x=0,y=0)

heading=Label(login_window,text='Send messages through us!',font=('Microsoft Yahei UI Light',18,'bold'),bg='DeepSkyBlue',fg='black')
heading.place(x=60,y=125)

frame=Frame(login_window,bg='cornflowerblue')
frame.place(x=33,y=200)

phoneLabel=Label(frame,text='Enter phone number',font=('Microsoft Yahei Ui Light',15,'bold'),bg='cornflowerblue',fg='white')
phoneLabel.grid(row=1,column=0,sticky='w',padx=2,pady=(10,0))

phoneEntry=Entry(frame,width=40,font=('Microsoft Yahei Ui Light',9,'bold'),fg='black',bg='white')
phoneEntry.grid(row=2,column=0,sticky='w',padx=35)
phoneEntry.insert(0,'+91')

frame2=Frame(login_window,bg='cornflowerblue')
frame2.place(x=33,y=300)

msgLabel=Label(frame2,text='Enter message',font=('Microsoft Yahei Ui Light',15,'bold'),bg='cornflowerblue',fg='white')
msgLabel.grid(row=3,column=0,sticky='w',padx=2,pady=(10,0))

msgEntry=Entry(login_window,width=40,font=('Microsoft Yahei Ui Light',9,'bold'),fg='black',bg='cornflowerblue')
msgEntry.place(x=60,y=350,width=335,height=120)

phoneEntry.bind('<FocusIn>',phoneEntry)

frame3=Frame(login_window,bg='cornflowerblue')
frame3.place(x=150,y=500)

sendButton=Button(frame3,text='Send',font=('Open Sans',16,'bold'),bd=0,bg='cornflowerblue',fg='darkblue',width=10,command=send_msgg)
sendButton.grid(row=5,column=0,padx=4)

login_window.mainloop()