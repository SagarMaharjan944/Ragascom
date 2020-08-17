from tkinter import *
import math, random
from tkinter import messagebox 
class online:
    def __init__(self,gui):
        self.gui=gui
        self.gui.geometry("1920x1080+0+0")
        self.gui.title("Menu and billing")
        bg_color="#C67CFF"
        title = Label(self.gui,text="RESTRO",bd=10,bg="#C67CFF",font=("Arial",30,"bold"),relief=GROOVE,fg="white",pady=2).pack(fill=X) 
        ##############---Variables---##############
        #Hot drinks
        self.americano = IntVar()
        self.latte = IntVar()
        self.cappuccino = IntVar()
        self.black_tea = IntVar()
        self.green_tea = IntVar()

        #Cold drinks
        self.pepsi = IntVar()
        self.coke = IntVar()
        self.choco_shakes = IntVar()
        self.lassi = IntVar()
        self.lemonade = IntVar()

        #Hard drinks
        self.JD = IntVar()
        self.OD = IntVar()
        self.BL = IntVar()
        self.mt8848 = IntVar()
        self.vodka = IntVar()

        #total
        self.gtot=StringVar()
        self.tot=StringVar()
        self.tax=StringVar()
        self.dis=StringVar()
        self.bill=StringVar()
        a=random.randint(100,9999)
        self.bill.set(str(a))

        #############---bottom---############
        bot=LabelFrame(self.gui,bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg="#C67CFF")
        bot.place(x=0,y=710,relwidth=1,height=75)
       
        tot=Label(bot,text="Total Price",bg="#C67CFF",fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=12)
        tot_box=Entry(bot,width=16,textvariable=self.tot,font=("arial",10,"bold"),bd=5,relief=SUNKEN)
        tot_box.place(x=150,y=9)

        tax=Label(bot,text="Total Tax",bg="#C67CFF",fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=120,pady=1)
        tax_box=Entry(bot,width=16,textvariable=self.tax,font=("arial",10,"bold"),bd=5,relief=SUNKEN)
        tax_box.place(x=400,y=9)

        dis=Label(bot,text="Total discount",bg="#C67CFF",fg="white",font=("times new roman",18,"bold")).grid(row=0,column=3,padx=30,pady=1)
        dis_box=Entry(bot,width=16,textvariable=self.dis,font=("arial",10,"bold"),bd=5,relief=SUNKEN)
        dis_box.place(x=700,y=9)

        tat=Button(bot,width=5,text="Total",font=("arial",10,"bold"),bd=5,relief=GROOVE,command=self.gtotal)
        tat.place(x=830,y=5)

        #############---Menu---##############
        B1=LabelFrame(self.gui,text="Hot Drinks",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg="#86b9f0")
        B1.place(x=0,y=80,width=900,height=200)

        americano=Entry(B1,width=5,textvariable=self.americano,font=("Arial",14,"bold"),bd=5,relief=SUNKEN)
        americano.place(x=80,y=120)

        latte=Entry(B1,width=5,textvariable=self.latte,font=("Arial",14,"bold"),bd=5,relief=SUNKEN)
        latte.place(x=240,y=120)

        cappuccino=Entry(B1,width=5,textvariable=self.cappuccino,font=("Arial",14,"bold"),bd=5,relief=SUNKEN)
        cappuccino.place(x=400,y=120)

        black_tea=Entry(B1,width=5,textvariable=self.black_tea,font=("Arial",14,"bold"),bd=5,relief=SUNKEN)
        black_tea.place(x=560,y=120)

        green_tea=Entry(B1,width=5,textvariable=self.green_tea,font=("Arial",14,"bold"),bd=5,relief=SUNKEN)
        green_tea.place(x=720,y=120)

        m2=LabelFrame(self.gui,text="Cold Drinks",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg="#fc7cf6")
        m2.place(x=0,y=290,width=900,height=200)

        pepsi=Entry(m2,width=5,textvariable=self.pepsi,font=("Arial",14,"bold"),bd=5,relief=SUNKEN)
        pepsi.place(x=80,y=120)

        coke=Entry(m2,width=5,textvariable=self.coke,font=("Arial",14,"bold"),bd=5,relief=SUNKEN)
        coke.place(x=240,y=120)

        lassi=Entry(m2,width=5,textvariable=self.lassi,font=("Arial",14,"bold"),bd=5,relief=SUNKEN)
        lassi.place(x=400,y=120)

        choco_shakes=Entry(m2,width=5,textvariable=self.choco_shakes,font=("Arial",14,"bold"),bd=5,relief=SUNKEN)
        choco_shakes.place(x=560,y=120)

        lemonade=Entry(m2,width=5,textvariable=self.lemonade,font=("Arial",14,"bold"),bd=5,relief=SUNKEN)
        lemonade.place(x=720,y=120)
        
        d3=LabelFrame(self.gui,text="Hard Drinks",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg="#fc7c7c")
        d3.place(x=0,y=500,width=900,height=200)

        JD=Entry(d3,width=5,textvariable=self.JD,font=("Arial",14,"bold"),bd=5,relief=SUNKEN)
        JD.place(x=80,y=120)

        OD=Entry(d3,width=5,textvariable=self.OD,font=("Arial",14,"bold"),bd=5,relief=SUNKEN)
        OD.place(x=240,y=120)

        BL=Entry(d3,width=5,textvariable=self.BL,font=("Arial",14,"bold"),bd=5,relief=SUNKEN)
        BL.place(x=400,y=120)

        mt8848=Entry(d3,width=5,textvariable=self.mt8848,font=("Arial",14,"bold"),bd=5,relief=SUNKEN)
        mt8848.place(x=560,y=120)

        vodka=Entry(d3,width=5,textvariable=self.vodka,font=("Arial",14,"bold"),bd=5,relief=SUNKEN)
        vodka.place(x=720,y=120)
        
        
        ##############---Calculation---############
        cal=LabelFrame(self.gui,bd=10,relief=GROOVE,bg="gold")
        cal.place(x=915,y=500,width=600,height=200)

        cal_btn=Frame(cal,bd=10,relief=GROOVE)
        cal_btn.place(x=7,width=567,height=180)
        
        gen_bill1=Button(cal_btn,command=self.bill_area,text="Generate Bill",bg="#299AF4",bd=5,fg="white",pady=20,width=12,height=3,font=("times new roman",16,"bold")).grid(row=0,column=0,padx=10,pady=10)
        gen_bill2=Button(cal_btn,command=self.reset,text="Reset",bg="#80ED70",bd=5,fg="white",pady=20,width=12,height=3,font=("times new roman",16,"bold")).grid(row=0,column=1,padx=10,pady=12)
        gen_bill3=Button(cal_btn,command=self.Exit,text="Exit",bg="#F44329",bd=5,fg="white",pady=20,width=12,height=3,font=("times new roman",16,"bold")).grid(row=0,column=2,padx=10,pady=12)
        self.gtotal()
        ##############---Billing---#############
        bill=Frame(self.gui,bd=10,relief=GROOVE)
        bill.place(x=915,y=80,width=600,height=410)
        bill_title=Label(bill,text="Billing",font=("times new roman",12,"bold"),bd=6,relief=GROOVE).pack(fill=X)
        scroll=Scrollbar(bill,orient=VERTICAL)
        self.textarea=Text(bill,yscrollcommand=scroll.set)
        scroll.pack(side=RIGHT,fill=Y)
        scroll.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        self.welcome_area()
    def gtotal(self):
        self.a_p=self.americano.get()*40
        self.l_p=self.latte.get()*40
        self.cap_p=self.cappuccino.get()*40
        self.b_p=self.black_tea.get()*40
        self.g_p=self.green_tea.get()*40
        self.p_p=self.pepsi.get()*40
        self.co_p=self.coke.get()*40
        self.ch_p=self.choco_shakes.get()*40
        self.le_p=self.lemonade.get()*40
        self.la_p=self.lassi.get()*40
        self.J_p=self.JD.get()*40
        self.O_p=self.OD.get()*40
        self.BL_p=self.BL.get()*40
        self.m_p=self.mt8848.get()*40
        self.v_p=self.vodka.get()*40
        self.grand_total=float(
                             self.a_p+
                             self.l_p+
                             self.cap_p+
                             self.b_p+
                             self.g_p+
                             self.p_p+
                             self.co_p+
                             self.ch_p+
                             self.le_p+
                             self.la_p+
                             self.J_p+                                 
                             self.O_p+
                             self.BL_p+
                             self.m_p+
                             self.v_p
                             )
        self.tot.set("Rs."+str(self.grand_total))
        self.t_tax=round((self.grand_total*0.08),2)
        self.tax.set("Rs."+str(self.t_tax))
        self.d_dis=round((self.grand_total*0.01),2)
        self.dis.set("Rs."+str(self.d_dis))
        self.gtot=round(float(self.grand_total + self.t_tax - self.d_dis),2)
    
    def welcome_area(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\t                   Welcome to Restro")
        self.textarea.insert(END,f"\n\n\tBill number: {self.bill.get()}")
        self.textarea.insert(END,f"\n\n*********************************************************************")
        self.textarea.insert(END,f"\n Drinks\t\t\t\tQuantity\t\t\t      Price")
        self.textarea.insert(END,"\n*********************************************************************")
    def bill_area(self):
        self.welcome_area()
        if self.americano.get()!=0:
            self.textarea.insert(END,f"\n Americano\t\t\t\t{self.americano.get()}\t\t\t      {self.a_p}")
        if self.latte.get()!=0:
            self.textarea.insert(END,f"\n Latte\t\t\t\t{self.latte.get()}\t\t\t      {self.l_p}")
        if self.cappuccino.get()!=0:
            self.textarea.insert(END,f"\n Cappuccino\t\t\t\t{self.cappuccino.get()}\t\t\t      {self.cap_p}")
        if self.black_tea.get()!=0:
            self.textarea.insert(END,f"\n Black Tea\t\t\t\t{self.black_tea.get()}\t\t\t      {self.b_p}")    
        if self.green_tea.get()!=0:
            self.textarea.insert(END,f"\n Green Tea\t\t\t\t{self.green_tea.get()}\t\t\t      {self.g_p}")
        if self.pepsi.get()!=0:
            self.textarea.insert(END,f"\n Pepsi\t\t\t\t{self.pepsi.get()}\t\t\t      {self.p_p}")
        if self.coke.get()!=0:
            self.textarea.insert(END,f"\n Coke\t\t\t\t{self.coke.get()}\t\t\t      {self.co_p}")
        if self.choco_shakes.get()!=0:
            self.textarea.insert(END,f"\n Choco Shakes\t\t\t\t{self.choco_shakes.get()}\t\t\t      {self.ch_p}")
        if self.lemonade.get()!=0:
            self.textarea.insert(END,f"\n Lemonade\t\t\t\t{self.lemonade.get()}\t\t\t      {self.le_p}")
        if self.lassi.get()!=0:
            self.textarea.insert(END,f"\n Lassi\t\t\t\t{self.lassi.get()}\t\t\t      {self.la_p}")
        if self.JD.get()!=0:
            self.textarea.insert(END,f"\n Jack Daniels\t\t\t\t{self.JD.get()}\t\t\t      {self.J_p}")
        if self.OD.get()!=0:
            self.textarea.insert(END,f"\n Old Durbar\t\t\t\t{self.OD.get()}\t\t\t      {self.O_p}")
        if self.mt8848.get()!=0:
            self.textarea.insert(END,f"\n Mt 8848\t\t\t\t{self.mt8848.get()}\t\t\t      {self.m_p}")
        if self.BL.get()!=0:
            self.textarea.insert(END,f"\n Black Label\t\t\t\t{self.BL.get()}\t\t\t      {self.BL_p}")
        if self.vodka.get()!=0:
            self.textarea.insert(END,f"\n Vodka\t\t\t\t{self.vodka.get()}\t\t\t      {self.v_p}")
        self.textarea.insert(END,f"\n\n---------------------------------------------------------------------")
        self.textarea.insert(END,f"\n Total Tax\t\t\t\t\t\t\t     {self.tax.get()}")
        self.textarea.insert(END,f"\n Total Discount\t\t\t\t\t\t\t     {self.dis.get()}")
        self.textarea.insert(END,"\n---------------------------------------------------------------------")
        self.textarea.insert(END,f"\n Grand Total\t\t\t\t\t\t\t    Rs. {self.gtot}")
    def reset(self):
         #Hot drinks
        self.americano.set(0)
        self.latte.set(0)
        self.cappuccino.set(0)
        self.black_tea.set(0) 
        self.green_tea.set(0) 

        #Cold drinks
        self.pepsi.set(0)
        self.coke.set(0) 
        self.choco_shakes.set(0) 
        self.lassi.set(0) 
        self.lemonade.set(0) 

        #Hard drinks
        self.JD.set(0) 
        self.OD.set(0) 
        self.BL.set(0) 
        self.mt8848.set(0) 
        self.vodka.set(0)

        #total
        self.tot.set("")
        self.tax.set("")
        self.dis.set("")
        self.bill.set("")
        a=random.randint(100,9999)
        self.bill.set(str(a))
        self.welcome_area()
               
    def Exit(self):
        ex=messagebox.askyesno("Exit","Do you want to exit?")
        if ex>0:
            self.gui.destroy()

gui = Tk()
obj = online(gui)
gui.mainloop()