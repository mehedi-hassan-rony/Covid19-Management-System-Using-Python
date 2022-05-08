
from  tkinter import  *
from tkinter import ttk


import  pymysql
from tkinter import messagebox




class covid19:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Covid Test Management System")
        self.root.configure(bg='#ffcb82')




        #========== Variables================



        # ========================= search sector =======================
        #####   next page transform

        def change():
            root.destroy()

        ##____________________________________________

        #===--------==-=-=-=- Button Frame +==============-----------

        btn_Frame=Frame(self.root,bg="#ffffff")
        btn_Frame.place(x=0,y=0,width=1920,height=87)
        lbl=Label(btn_Frame,bg='black',width=129,height=120)
        lbl.place(x=0,y=0)

        btn=Button(lbl,text ="hey",command=lambda: change()).pack()









        mainloop()




root=Tk()
ob=covid19(root)
root.mainloop()
