
from  tkinter import  *
from tkinter import ttk

import pymysql
from tkinter import messagebox
class covid19:
    def __init__(self,root):
        self.root=root
        self.root.geometry("2350x700+0+0")
        self.root.title("Covid Test Management System")
        self.root.configure(bg='#f0f2f5')

        title=Label(self.root,text="Covid Test Management System",
                    font=("times new roman",40,"bold"),bd=10,relief=GROOVE,fg='#f0f2f5',bg='#1877f2')
        title.pack(side=TOP,fill=X)


        #========== Variables================

        self.id_var=StringVar()
        self.name_var = StringVar()
        self.age_var = StringVar()
        self.gender_var=StringVar()
        self.location_var=StringVar()
        self.phone_var= StringVar()
        self.result_var=StringVar()
        self.full_address_var=StringVar()

        self.search_by=StringVar()
        self.search_text = StringVar()


#============Manage Frames==================================
        Manage_Frame= Frame(self.root,bd=1,relief=RIDGE,bg='#ffffff')
        Manage_Frame.place(x=40,y=100,width=460,height=560)

        m_title = Label(Manage_Frame,text="  Patient Details", bg='#ffffff',font=("times new roman",20))
        m_title.grid(row=0,columnspan=2,pady=10)

        lbl_Id=Label(Manage_Frame,text="patient Id:", padx=15, bg='#ffffff',font=("times new roman",15,))
        lbl_Id.grid(row=1,column=0,sticky="w")

        text_Id=Entry(Manage_Frame,textvariable=self.id_var,font=("times new roman",15,))
        text_Id.grid(row=1,column=1 ,pady=7,padx=20,sticky="w")

        lbl_Name = Label(Manage_Frame, text="patient Name :", padx=15, bg='#ffffff',font=("times new roman", 15,))
        lbl_Name.grid(row=2, column=0, sticky="w")

        text_Name = Entry(Manage_Frame,textvariable=self.name_var, font=("times new roman", 15,))
        text_Name.grid(row=2, column=1,pady=7, padx=20, sticky="w")

        lbl_Age = Label(Manage_Frame, text="Age :",padx=15, bg='#ffffff', font=("times new roman", 15,))
        lbl_Age.grid(row=3, column=0, sticky="w")

        text_Age = Entry(Manage_Frame, textvariable=self.age_var,font=("times new roman", 15,))
        text_Age.grid(row=3, column=1, pady=7,padx=20, sticky="w")

        lbl_Gender = Label(Manage_Frame, text="Gender :", padx=15,bg='#ffffff', font=("times new roman",15,))
        lbl_Gender.grid(row=4, column=0, sticky="w")

        text_Gender = Entry(Manage_Frame,textvariable=self.gender_var, font=("times new roman", 15,))
        text_Gender.grid(row=4, column=1, pady=7,padx=20, sticky="w")

        lbl_Location = Label(Manage_Frame, text="Location :",padx=15, bg='#ffffff', font=("times new roman", 15,))
        lbl_Location.grid(row=5, column=0, sticky="w")

        text_Location = Entry(Manage_Frame,textvariable=self.location_var, font=("times new roman", 15,))
        text_Location.grid(row=5, column=1, pady=7,padx=20, sticky="w")

        lbl_Phone = Label(Manage_Frame, text="Phone Number :",padx=15,  bg='#ffffff',font=("times new roman", 15,))
        lbl_Phone.grid(row=6, column=0, sticky="w")

        text_Id = Entry(Manage_Frame, textvariable=self.phone_var,font=("times new roman", 15,))
        text_Id.grid(row=6, column=1, pady=7,padx=20, sticky="w")

        lbl_Result = Label(Manage_Frame, text="Covid Result:",padx=15, bg='#ffffff', font=("times new roman", 15,))
        lbl_Result.grid(row=7, column=0, sticky="w")

        combo_Result=ttk.Combobox(Manage_Frame, textvariable=self.result_var,  font=("times new roman", 13),state='readonly')
        combo_Result['values']=("Positive","Negative")
        combo_Result.grid(row=7,column=1 ,pady=7)

        lbl_Full_address = Label(Manage_Frame, text="Full Address :",padx=15, bg='#ffffff', font=("times new roman", 15,))
        lbl_Full_address.grid(row=8, column=0, sticky="w")

        self.text_Full_address=Text(Manage_Frame,width=25,height=5)
        self.text_Full_address.grid(row=8, column=1,pady=7, )


        #===--------==-=-=-=- Button Frame +==============-----------

        btn_Frame=Frame(Manage_Frame,bg="#ffffff")
        btn_Frame.place(x=10,y=450,width=420)

        addbtn = Button(btn_Frame,text="Add",font=("times new roman",15,"bold"),bg='#1877f2',fg='#ffffff',width=6,command=self.add_patients).grid(row=0,column=1,padx=10,)
        updatebtn = Button(btn_Frame, text="Update", font=("times new roman",15,"bold"),bg='#1877f2',fg='#ffffff',width=6,command=self.update).grid(row=0, column=2, padx=10, )
        deletebtn = Button(btn_Frame, text="Delete",font=("times new roman",15,"bold"),bg='#1877f2',fg='#ffffff',width=6,command=self.delete).grid(row=0, column=3, padx=10, )
        clearbtn = Button(btn_Frame, text="Clear", font=("times new roman",15,"bold"),bg='#1877f2',fg='#ffffff',width=6,command=self.clear,).grid(row=0, column=4,padx=10, )


        #====================Right frame=======================


        Right_Frame = Frame(self.root,  relief=RIDGE, bg='#f0f2f5')
        Right_Frame.place(x=520, y=100, width=700, height=560)

        #========================= search sector =======================

        lbl_search=Label(Right_Frame,text="Search By :", font=("times new roman",16,))
        lbl_search.grid(row=0,column=0,pady=10,padx=10,sticky="w")

        combo_Search = ttk.Combobox(Right_Frame,textvariable=self.search_by,width=10, font=("times new roman", 13), state='readonly')
        combo_Search['values'] = ("Id","Result ","Location")
        combo_Search.grid(row=0, column=1, pady=10)

        text_Search = Entry(Right_Frame,textvariable=self.search_text, font=("times new roman", 13,),width=14)
        text_Search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchbtn = Button(Right_Frame, text="Search",  font=("times new roman",11,"bold"),bg='#b358ca',fg='#ffffff',width=6,command=self.search_data).grid(row=0, column=3, padx=10, )
        showbtn = Button(Right_Frame, text="Show All", font=("times new roman",11,"bold"),bg='#b358ca',fg='#ffffff',width=6,command=self.fetch_data).grid(row=0, column=4, padx=10, )

        #======================= table form  =====================================

        Table_frame=Frame(Right_Frame, relief=RIDGE, bg='#ffffff')
        Table_frame.place(x=30, y=80, width=650, height=450)

        scroll_x=Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_frame, orient=VERTICAL)
        self.covid19_table=ttk.Treeview(Table_frame,columns=("id","name","age","gender","location","phone","result","full_address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.covid19_table.xview)
        scroll_y.config(command=self.covid19_table.yview)
        self.covid19_table.heading("id", text="Patient ID")
        self.covid19_table.heading("name", text="Name")
        self.covid19_table.heading("age", text="Age")
        self.covid19_table.heading("gender", text="Gender")
        self.covid19_table.heading("location", text="Location")
        self.covid19_table.heading("phone", text="Phone")
        self.covid19_table.heading("result", text="Covid Result")
        self.covid19_table.heading("full_address", text="Full Adress")
        self.covid19_table['show']='headings'

        self.covid19_table.column("id",width=100)
        self.covid19_table.column("name", width=100)
        self.covid19_table.column("age", width=100)
        self.covid19_table.column("gender", width=100)
        self.covid19_table.column("location", width=100)
        self.covid19_table.column("phone", width=100)
        self.covid19_table.column("result", width=100)
        self.covid19_table.column("full_address", width=100)

        self.covid19_table.pack(fill=BOTH,expand=1)
        self.covid19_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()



    def add_patients(self):
        if self.id_var.get()=="" or self.name_var.get()=="" :
            messagebox.showerror("Error","All Fields Are Required !!!")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="covid19")
            cur=con.cursor()
            cur.execute("insert into patients values ( %s,%s,%s,%s,%s,%s,%s,%s)",(self.id_var.get(),
                                                                                 self.name_var.get(),
                                                                                 self.age_var.get(),
                                                                                 self.gender_var.get(),
                                                                                 self.location_var.get(),
                                                                                 self.phone_var.get(),
                                                                                 self.result_var.get(),
                                                                                 self.text_Full_address.get('1.0',END)
                                                                                 ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Great ","Record has Been inserted  :)")

    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="covid19")
        cur = con.cursor()
        cur.execute("select * from patients")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.covid19_table.delete(*self.covid19_table.get_children())
            for row in rows:
                    self.covid19_table.insert('',END,values=row)
            con.commit()
        con.close()


    def clear(self):
        self.id_var.set("")
        self.name_var.set(""),
        self.age_var.set(""),
        self.gender_var.set(""),
        self.location_var.set(""),
        self.phone_var.set(""),
        self.result_var.set(""),
        self.text_Full_address.delete("1.0",END)


    def get_cursor(self,ev):
        cursor_row=self.covid19_table.focus()
        contents=self.covid19_table.item(cursor_row)
        row=contents['values']
        self.id_var.set(row[0])
        self.name_var.set(row[1]),
        self.age_var.set(row[2]),
        self.gender_var.set(row[3]),
        self.location_var.set(row[4]),
        self.phone_var.set(row[5]),
        self.result_var.set(row[6]),
        self.text_Full_address.delete("1.0", END)
        self.text_Full_address.insert(END,row[7])



        #==================update================

    def update(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="covid19")
        cur = con.cursor()
        cur.execute("update patients set name=%s,age=%s,gender=%s,location=%s,phone=%s,result=%s,full_address=%s where id=%s",(
                                                                               self.name_var.get(),
                                                                               self.age_var.get(),
                                                                               self.gender_var.get(),
                                                                               self.location_var.get(),
                                                                               self.phone_var.get(),
                                                                               self.result_var.get(),
                                                                               self.text_Full_address.get('1.0', END),
                                                                               self.id_var.get()
                                                                               ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("Great ", "Record has Been Updated  :)")


    def delete(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="covid19")
        cur = con.cursor()
        cur.execute("delete from patients where id=%s",self.id_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
        messagebox.showinfo("Deleted","Data has been sucessfully deleted !!!")

#===================search data===========================

    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="covid19")
        cur = con.cursor()
        cur.execute("select * from patients where "+str(self.search_by.get())+" LIKE '%"+str(self.search_text.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.covid19_table.delete(*self.covid19_table.get_children())
            for row in rows:
                self.covid19_table.insert('',END,values=row)
            con.commit()
        con.close()




root=Tk()
ob=covid19(root)
root.mainloop()