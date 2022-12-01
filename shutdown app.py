from tkinter import * 
import os 

def Restart ():
    os.system("shutdown /r /t 1 ")

def Restart_time ():
    os.system("shutdown /r /t 20 ")

def Logout ():
    os.system("shutdown -1")

def shutdown ():
    os.system("shutdown /s  /t 1")




st=Tk()
st.title("shutDown app")
st.geometry("500x500")
st.config(bg="cyan")

r_button = Button(st,text="Restart",font=("Time New Roman" ,20 ,"bold"),relief=RAISED,cursor="plus",command=Restart)
r_button.place(x=150,y=60,height=50,width=200)

rt_button = Button(st,text="Restart time",font=("Time New Roman" ,20 ,"bold"),relief=RAISED,cursor="plus",command=Restart_time)
rt_button.place(x=150,y=170,height=50,width=200)

lo_button = Button(st,text="Log-out",font=("Time New Roman" ,20 ,"bold"),relief=RAISED,cursor="plus",command=Logout)
lo_button.place(x=150,y=270,height=50,width=200)

sd_button = Button(st,text="Shut-Down",font=("Time New Roman" ,20 ,"bold"),relief=RAISED,cursor="plus",command=shutdown)
sd_button.place(x=150,y=370,height=50,width=200)














st.mainloop()
