from tkinter import *



aken=Tk()
aken.geometry("1000x1000")
aken.title("Reg ja auto")

sf=Frame(aken,bg="lightblue")
log_btn=Button(sf,text="Login")
reg_btn=Button(sf,text="register")

lbl=Label(aken,text="Login",font="Quicksand 24")
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


log_nimi.bind("<Return>")#enter

sf.pack(fill=X)
log_btn.pack(side=RIGHT)
reg_btn.pack(side=RIGHT)

lbl.pack()

log_nimi.pack()
log_pass.pack()

aken.mainloop()

#https://metanit.com/python/tkinter/2.4.php