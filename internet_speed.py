from ast import Raise
from tkinter import *
import speedtest 

def speedcheck():
    sp = speedtest.Speedtest() 
    sp.get_servers()
    down =str(round(sp.download()/(10**6),3))+"Mbps"
    up =str(round(sp.upload()/(10**6),3))+"Mbps"
    lab_dv.config(text=down)
    lab_uv.config(text=up)







st=Tk()
st.title("Internet speed app")
st.geometry("500x700")
st.config(bg="cyan")

lab =Label(st,text="Internet speed Test",font=("Time New Roman",30,"bold"),bg="cyan",fg="blue")
lab.place(x=60,y=40,height=50,width=380)

lab_d =Label(st,text="Download speed",font=("Time New Roman",30,"bold"),bg="cyan",fg="blue")
lab_d.place(x=60,y=130,height=50,width=380)

lab_dv =Label(st,text="00",font=("Time New Roman",30,"bold"),bg="cyan",fg="magenta")
lab_dv.place(x=60,y=200,height=50,width=380)

lab_u =Label(st,text="Upload speed ",font=("Time New Roman",30,"bold"),bg="cyan",fg="blue")
lab_u.place(x=55,y=290,height=50,width=380)

lab_uv =Label(st,text="00",font=("Time New Roman",30,"bold"),bg="cyan",fg="magenta")
lab_uv.place(x=55,y=360,height=50,width=380)

button =Button(st,text="CHECK" ,font=("Time New Roman",30,"bold"),relief=RAISED,bg="blue",fg="yellow",command=speedcheck)
button.place(x=55,y=460,height=50,width=380)




st.mainloop()