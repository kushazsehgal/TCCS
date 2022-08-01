from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("S E L E C T  R O L E")
root.geometry("350x500")
root.configure(background='#000d33')
def cmd2():
    w=Tk()
    root.destroy()
    w.geometry('350x500')
    w.title(' L O G I N ')
    w.resizable(0,0)


    #Making gradient frame
    j=0
    r=10
    for i in range(100):
        c=str(222222+r)
        Frame(w,width=10,height=500,bg="#"+c).place(x=j,y=0)   
        j=j+10                                                  
        r=r+1

    Frame(w,width=250,height=400,bg='white').place(x=50,y=50)


    l1=Label(w,text='Username',bg='white')
    l=('Consolas',13)
    l1.config(font=l)
    l1.place(x=80,y=130)

    #e1 entry for username entry
    e1=Entry(w,width=20,border=0)
    l=('Consolas',13)
    e1.config(font=l)
    e1.place(x=80,y=160)

    l2=Label(w,text='Password',bg='white')
    l=('Consolas',13)
    l2.config(font=l)
    l2.place(x=80,y=210)
    #e2 entry for password entry
    e2=Entry(w,width=20,border=0,show='*')
    e2.config(font=l)
    e2.place(x=80,y=240)

    ###lineframe on entry

    Frame(w,width=180,height=2,bg='#141414').place(x=80,y=262)
    Frame(w,width=180,height=2,bg='#141414').place(x=80,y=182)


    #Command
    def cmd():
        if e1.get()=='shivam' and e2.get()=='shivam':
            messagebox.showinfo("LOGIN SUCCESSFULLY", "         W E L C O M E        ")
            q=Tk()
            #destroy window w.
            w.destroy()
            q.mainloop()
            
        else:
            messagebox.showwarning("LOGIN FAILED","        PLEASE TRY AGAIN        ")

    def bttn(x,y,text,ecolor,lcolor):
        def on_entera(e):
            myButton1['background'] = ecolor #ffcc66
            myButton1['foreground']= lcolor  #000d33

        def on_leavea(e):
            myButton1['background'] = lcolor
            myButton1['foreground']= ecolor

        myButton1 = Button(w,text=text,
                    width=20 ,
                    height=2,
                    fg=ecolor,
                    border=0,
                    bg=lcolor,
                    activeforeground=lcolor,
                    activebackground=ecolor,
                        command=cmd)
                    
        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x,y=y)

    bttn(100,280,'L O G I N','white','#994422')
    #Signup button
    bttn(100,310,'S I G N U P','white','#994422')

    w.mainloop()

#Making gradient frame
j=0
r=10
for i in range(100):
    c=str(222222+r)
    Frame(root,width=10,height=500,bg="#"+c).place(x=j,y=0)   
    j=j+10                                                  
    r=r+1

Frame(root,width=250,height=400,bg='white').place(x=50,y=50)

def bttn(x,y,text,ecolor,lcolor):
    def on_entera(e):
        myButton1['background'] = ecolor #ffcc66
        myButton1['foreground']= lcolor  #000d33

    def on_leavea(e):
        myButton1['background'] = lcolor
        myButton1['foreground']= ecolor

    myButton1 = Button(root,text=text,
                width=20,
                height=2,
                fg=ecolor,
                border=0,
                bg=lcolor,
                activeforeground=lcolor,
                activebackground=ecolor,
                    command=cmd2)
                
    myButton1.bind("<Enter>", on_entera)
    myButton1.bind("<Leave>", on_leavea)

    myButton1.place(x=x,y=y)


#create 3 buttons: Customer, Employee, Manager
bttn(100,150,'C U S T O M E R','white','#994422')
bttn(100,200,'E M P L O Y E E','white','#994422')
bttn(100,250,'M A N A G E R','white','#994422')

root.mainloop()