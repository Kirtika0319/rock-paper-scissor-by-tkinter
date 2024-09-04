from tkinter import*
import random
top=Tk()
top.geometry("700x300")
Your_Select=""
Comp_Select=""
Your_Score=0
Comp_Score=0

def choice_to_number(choice):
    rps = {'rock':0,'paper':1,'scissor':2}
    return rps[choice]
def number_to_choice(number):
    rps={0:'rock',1:'paper',2:'scissor'}
    return rps[number]

def random_computer_choice():
    return random.choice(['rock','paper','scissor'])

def result(human_choice,comp_choice):
    global Your_Score
    global Comp_Score
    your=choice_to_number(human_choice)
    comp=choice_to_number(comp_choice)
    if(your==comp):
       heading4.config(text=" TIE!")
    elif((your-comp)%3==1):
       heading4.config(text=" YOU WIN")
       Your_Score+=1
    else:
        heading4.config(text=" COMPUTER WIN")
        Comp_Score+=1

    update_labels()
    
def update_labels():
    heading5.config(text=f"Your Selected: {Your_Select}")
    heading6.config(text=f"Computer Selected: {Comp_Select}")
    heading7.config(text=f"Your Score: {Your_Score}")
    heading8.config(text=f"Computer Score: {Comp_Score}")        

def rock():
    global Your_Select
    global Comp_Select
    Your_Select='rock'
    Comp_Select=random_computer_choice()
    result(Your_Select,Comp_Select)
def paper():
    global Your_Select
    global Comp_Select
    Your_Select='paper'
    Comp_Select=random_computer_choice()
    result(Your_Select,Comp_Select)
def scissor():
    global Your_Select
    global Comp_Select
    Your_Select='scissor'
    Comp_Select=random_computer_choice() 
    result(Your_Select,Comp_Select)
        

heading = Label(top, text = "Rock Paper Scissor",font=20,fg="grey")
heading.place(x = 300,y = 10)  
heading1 = Label(top, text = "Let's Start the Game...",fg="green")
heading1.place(x = 320,y = 38)
heading3=Label(top,text="Your Options:",fg="grey")
heading3.place(x=100,y=65)

btn1=Button(top,text="Rock",bg="pink",font=3,command=rock)
btn1.place(x=230,y=70)
btn2=Button(top,text="Paper",bg="grey",font=3,command=paper)
btn2.place(x=310,y=70)
btn3=Button(top,text="Scissor",bg="light blue",font=3,command=scissor)
btn3.place(x=400,y=70)

heading4=Label(top,text="Score:",fg="grey")
heading4.place(x=100,y=120)
heading5=Label(top,text="Your Selected:---",fg="grey")
heading5.place(x=120,y=160)

heading6=Label(top,text="Computer Selected:---",fg="grey")
heading6.place(x=120,y=200)



heading7=Label(top,text="Your Score:---",fg="grey")
heading7.place(x=400,y=160)
heading8=Label(top,text="Computer Score:---",fg="grey")
heading8.place(x=400,y=200)
top.mainloop()
