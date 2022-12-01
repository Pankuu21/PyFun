from time import *
import random as r



def mistake(partest,usertest):
    error =0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error =error + 1

        except :
            error=error + 1
    return error
            
def speed_time(time_s,time_e,userinput):
    time_delay =time_e-time_s
    time_R= round(time_delay,2)
    speed= len(userinput)/time_R
    return round(speed)

if __name__=='__main__':

    while(True):
        ck=input("ready to test y/n")
        if ck=="y" :
            test=["If you have gained enough knowledge about the Python programming language","In this Python project for beginners in Hindi, you will learn critical skills that will make you sharp in Python"," Python is one of the most used languages currently, and the demand for programmers in the market is not slowing down."]
            test1=r.choice(test)
            print("        ****** typing speed *****")
            print()
            print()
            print(test1)
            print()
            print()
            time_1=time()
            testinput=input("Enter : ")
            time_2 =time()

            print('speed :',speed_time(time_1,time_2,testinput)," w/sec")
            print("error: ",mistake(test1,testinput))
        elif ck=="n":
            print("thankyou")
            break
        else:
            print("erong input")

