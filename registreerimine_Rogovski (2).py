from tkinter import *

user_pass={}
pass_user={}
file = open ("users.txt", 'r', encoding="utf-8")
for line in file:
    k, v=line.strip().split('-')
    user_pass[k] = v
    pass_user[v] = k
file.close()

user_mail={}
file = open ("users_gmail.txt", 'r', encoding="utf-8")
for line in file:
    k, v=line.strip().split('-')
    user_mail[k] = v
file.close()

print(user_mail,user_pass)

def rootmain():
    rootmain=Tk()
    rootmain.geometry("1000x1000")
    rootmain.title("Reg ja auto")

    lblname=Label(rootmain,text="Tere tulemast!",font="Arial 30")
    log_btn=Button(rootmain,text="autoriseerimise",font="Arial 30",command=logpage)
    reg_btn=Button(rootmain,text="registreerimine",font="Arial 30",command=regpage)
    mainmut=Button(rootmain,text="Nime või parooli muutmine",font="Arial 30",command=changepassname)
    mainunus=Button(rootmain,text="Unustanud parooli taastamine",font="Arial 30",command=forgotpass)

    ob=[lblname,log_btn,reg_btn,mainmut,mainunus]
    for item in ob:
        item.pack()



    rootmain.mainloop()

def regpage():
        

        main.destroy()
        aken=Tk()
        aken.geometry("1000x1000")
        aken.title("registreerimine")

       
        lbl=Label(aken,text="registreerimine",font="Quicksand 45")
        reg_nimi=Entry(aken,bg="lightblue",width=15,font="Quicksand 24",justify=LEFT)
        reg_nimi.insert(0, "name..")
        def clearall(event):
            reg_nimi.delete(0,END)
        reg_nimi.bind("<Button-1>",clearall)
        reg_pass=Entry(aken,bg="lightblue",width=15,font="Quicksand 24",justify=LEFT)
        reg_pass.insert(0, "password...")
        def clearall1(event):
            reg_pass.delete(0,END)
        reg_pass.bind("<Button-1>",clearall1)
        btn_login=Button(aken,text="Login")
        reg_gmail=Entry(aken,bg="lightblue",width=15,font="Quicksand 24",justify=LEFT)
        reg_gmail.insert(0, "gmail...")
        def clearall2(event):
            reg_gmail.delete(0,END)
        reg_gmail.bind("<Button-1>",clearall2)
        def proverka():
            pass
        btn_login=Button(aken,text="Registreerimine",font="Arial 30",command=proverka)

        btn_taga=Button(aken,text="Main",command=rootmain,font="Arial 12")

        reg_nimi.bind("<Return>")#enter

        ob=[lbl,reg_nimi,reg_pass,reg_gmail,btn_login,btn_taga]
        for item in ob:
            item.pack()
        aken.mainloop()

def logpage():
        main.destroy()
        login=Tk()
        login.geometry("1000x1000")
        login.title("auto")

        lognimi=StringVar()
        logpass=StringVar()

        lbl=Label(login,text="autoriseerimise",font="Quicksand 45")
        log_nimi=Entry(login,bg="lightblue",width=15,font="Quicksand 24",justify=LEFT,textvariable=lognimi)
        log_nimi.insert(0, "name..")
        def clearall(event):
            log_nimi.delete(0,END)
        log_nimi.bind("<Button-1>",clearall)
        log_pass=Entry(login,bg="lightblue",width=15,font="Quicksand 24",justify=LEFT,textvariable=logpass)
        log_pass.insert(0, "password...")
        def clearall1(event):
            log_pass.delete(0,END)
        log_pass.bind("<Button-1>",clearall1)
        def autoresermine(event):
            if lognimi == "aleks" and logpass == "12345678":
                succes=Tk()
                succes.geometry("1000x1000")
                succes.title("succesful")
                lbl=Label(succes,text="SUCCESSFUL").pack()

        btn_login=Button(login,text="Login")
        btn_login.bind("<Button-1>",autoresermine)

        btn_taga=Button(login,text="Main",command=rootmain,font="Arial 12")
        

        ob=[lbl,log_nimi,log_pass,btn_login,btn_taga]
        for item in ob:
            item.pack()
        login.mainloop()

def changepassname():
    main.destroy()
    changing=Tk()
    changing.geometry("1000x1000")
    changing.title("Changepassname")

    lbl=Label(changing,text="Nime või parooli muutmine",font="Arias 30")
    lbl1=Label(changing,text="Sisesta sinu konto nimi ja parool:",font="Arial 30")
    vana_gmail=Entry(changing,bg="lightblue",width=15,font="Quicksand 24",justify=LEFT)
    vana_gmail.insert(0, "nimi...")
    def clearall2(event):
        vana_gmail.delete(0,END)
    vana_gmail.bind("<Button-1>",clearall2)
    vana_pass=Entry(changing,bg="lightblue",width=15,font="Quicksand 24",justify=LEFT)
    vana_pass.insert(0, "password...")
    def clearall1(event):
        vana_pass.delete(0,END)
    vana_pass.bind("<Button-1>",clearall1)

    lbl2=Label(changing,text="Sisesta sinu uus konto nimi ja parool:",font="Arial 30")
    uus_gmail=Entry(changing,bg="lightblue",width=15,font="Quicksand 24",justify=LEFT)
    uus_gmail.insert(0, "nimi...")
    def clearall3(event):
        uus_gmail.delete(0,END)
    uus_gmail.bind("<Button-1>",clearall3)
    uus_pass=Entry(changing,bg="lightblue",width=15,font="Quicksand 24",justify=LEFT)
    uus_pass.insert(0, "password...")
    def clearall4(event):
        uus_pass.delete(0,END)
    uus_pass.bind("<Button-1>",clearall4)
    btn_login=Button(changing,text="Sisesta",font="Arial 30")

    btn_taga=Button(changing,text="Main",command=rootmain,font="Arial 12")

    ob=[lbl,lbl1,vana_gmail,vana_pass,lbl2,uus_gmail,uus_pass,btn_login,btn_taga]
    for item in ob:
        item.pack()
    changing.mainloop()

def forgotpass():
    main.destroy()
    forgot=Tk()
    forgot.geometry("1000x1000")
    forgot.title("Forgotpass")

    lbl=Label(forgot,text="Unustanud parooli taastamine",font="Arial 30")
    lbl1=Label(forgot,text="Sisesta sinu konto gmail:",font="Arial 30")
    unus_gmail=Entry(forgot,bg="lightblue",width=15,font="Quicksand 24",justify=LEFT)
    unus_gmail.insert(0, "gmail...")
    def clearall2(event):
        unus_gmail.delete(0,END)
    unus_gmail.bind("<Button-1>",clearall2)
    btn_login=Button(forgot,text="Saada",font="Arial 30")

    btn_taga=Button(forgot,text="Main",command=rootmain,font="Arial 12")

    ob=[lbl,lbl1,unus_gmail,btn_login,btn_taga]
    for item in ob:
        item.pack()
    forgot.mainloop()

main=Tk()
main.geometry("1000x1000")
main.title("Reg ja auto")

lblname=Label(main,text="Tere tulemast!",font="Arial 30")
var=IntVar()
log_btn=Button(main,text="autoriseerimise",font="Arial 24",command=logpage,bg="Lightblue")
reg_btn=Button(main,text="registreerimine",font="Arial 24",command=regpage,bg="Lightblue")
mainmut=Button(main,text="Nime või parooli muutmine",font="Arial 24",command=changepassname,bg="Lightblue")
mainunus=Button(main,text="Unustanud parooli taastamine",font="Arial 24",command=forgotpass,bg="Lightblue")

ob=[lblname,log_btn,reg_btn,mainmut,mainunus]
for item in ob:
    item.pack()



main.mainloop()



#https://metanit.com/python/tkinter/2.4.php