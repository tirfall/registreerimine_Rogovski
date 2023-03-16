from tkinter import *

clicks = 0


def regpage():

        
        aken=Tk()
        aken.geometry("500x500")
        aken.title("reg")

        lbl=Label(aken,text="Reg",font="Quicksand 45")
        log_nimi=Entry(aken,bg="lightblue",width=15,font="Quicksand 24",justify=LEFT)
        log_nimi.insert(0, "name..")
        def clearall(event):
            log_nimi.delete(0,END)
        log_nimi.bind("<Button-1>",clearall)
        log_pass=Entry(aken,bg="lightblue",width=15,font="Quicksand 24",justify=LEFT)
        log_pass.insert(0, "password...")
        def clearall1(event):
            log_pass.delete(0,END)
        log_pass.bind("<Button-1>",clearall1)
        btn_login=Button(aken,text="Login")


        log_nimi.bind("<Return>")#enter

        sf.pack(fill=X)
        log_btn.pack(side=RIGHT)
        reg_btn.pack(side=RIGHT)

        lbl.pack()

        log_nimi.pack()
        log_pass.pack()
        btn_login.pack()
        aken.mainloop()


def loginpage():
    
        login=Tk()
        login.geometry("500x500")
        login.title("auto")
        
        lbl=Label(login,text="Login",font="Quicksand 45")
        log_nimi=Entry(login,bg="lightblue",width=15,font="Quicksand 24",justify=LEFT)
        log_nimi.insert(0, "name..")
        def clearall(event):
            log_nimi.delete(0,END)
        log_nimi.bind("<Button-1>",clearall)
        log_pass=Entry(login,bg="lightblue",width=15,font="Quicksand 24",justify=LEFT)
        log_pass.insert(0, "password...")
        def clearall1(event):
            log_pass.delete(0,END)
        log_pass.bind("<Button-1>",clearall1)
        btn_login=Button(login,text="Login")


        log_nimi.bind("<Return>")#enter

        sf.pack(fill=X)
        log_btn.pack(side=RIGHT)
        reg_btn.pack(side=RIGHT)

        lbl.pack()

        log_nimi.pack()
        log_pass.pack()
        btn_login.pack()
        login.mainloop()



main=Tk()
main.geometry("1440x1024")
main.title("Reg ja auto")

sf=Frame(main,bg="lightblue")
log_btn=Button(sf,text="Login",command=loginpage)
reg_btn=Button(sf,text="register",command=regpage)


sf.pack(fill=X)
log_btn.pack(side=RIGHT)
reg_btn.pack(side=RIGHT)


main.mainloop()

#https://metanit.com/python/tkinter/2.4.php