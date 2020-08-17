from tkinter import *
from tkinter import ttk
import os


app = Tk()
app.iconbitmap('favicon.ico')
app.title('Liquor Detailer')
app.configure(background='#7d161a')
app.geometry('1300x1000+0+0')

c = Canvas(app, height=475, width=700, bg='#7d161a')

c.pack()



verifycali = PhotoImage(file='verify.png')

c.create_image(230,430, image=verifycali, anchor=NW)

titlecali = PhotoImage(file='one.png')
c.create_image(350,50, image=titlecali, anchor=CENTER)

bargif = PhotoImage(file='Bar BG.gif')
c.create_image(350, 250, image=bargif, anchor=CENTER)


class Beginning:

   def __init__(self, root):
      myFrame = Frame(root)
      myFrame.pack()

      self.b1 = Button(app, text="ABOVE 21", font=('Exceptional Experience', 12), bg='green', bd=10, relief=GROOVE, padx=53, pady=3, command=self.Register)
      self.b2 = Button(app, text="BELLOW 21", font=('Exceptional Experience', 12), bg='red', bd=10, relief=GROOVE, padx=50, pady=3,  command=self.myClick)

      self.b1.pack()
      self.b2.pack()
   

   def Register_User(self):
           Username_info = Username.get()
           Password_info = Password.get() 

           try:

                file=open(Username_info+".txt", "w")
                file.write(Username_info+"\n")
                file.write(Password_info)
                        
                        
           except:
                print ("sorry file error.")
           finally:
                file.close()        

           Username_entry.delete(0, END)
           Password_entry.delete(0, END)   

           Label(register, text="*Registration successful*", fg='white', bg='maroon', font = ("calibri", 12)).pack()

   def Register(self):
           global register 
           register = Toplevel()        
           register.title("Register")
           register.resizable(False, False)
           register.geometry("600x250")
           register.configure(background='maroon')

           global Username
           global Password
           global Username_entry
           global Password_entry

           Username = StringVar()
           Password = StringVar()

           Label(register, text="Please enter details below", bg="grey", width=600, height=2, font=("Roman_bold", 20)).pack()
           Label(register, text="").pack
           Label(register, text="Username * ", padx=30, bg='maroon').pack()
           Username_entry = Entry(register, textvariable=Username)
           Username_entry.pack()
           Label(register, text="Password * ", padx=30, bg='maroon').pack()
           Password_entry = Entry(register, textvariable=Password)
           Password_entry.pack()
           Label(register, text="", bg='maroon').pack()
           Button(register, text="Register", height=1, width=10, command=lambda:[self.Register_User(), self.Welcome()]).pack()

   def login(self):
           print("Login session stared")

   def myClick(self):
           myLabel = Label(app, text="You are not eligible to access this Application", bg='#7d161a')
           myLabel.pack( padx=25, pady=2)

           button_quit = Button(app, text="Exit Program", command=app.quit)
           button_quit.pack()

 # firstpage of products

  
   def Welcome(self):
           top = Toplevel()
           top.geometry('1400x1400+0+0')
           top.title('Know your price')
           top.configure(bg='#2C1503')

    
           c1 = Canvas(top, height=50, width=1400, bg='maroon')
           c1.pack()


           #WHISKY  

           whisky = PhotoImage(file='whisky time.png')

           bwhisky = Button( top, image=whisky, command=WHISKY)
           bwhisky.pack()
           bwhisky.place(bordermode=OUTSIDE, height=150, width=130, x=65, y=115)

           lbl = Label(top, text="Whisky")
           lbl.pack()
           lbl.place(bordermode=OUTSIDE, height=50, width=130, x=65, y=280)

           #RUM   

           rum = PhotoImage(file='rum.png')

           brum = Button(top, image=rum, command=RUM )
           brum.pack()
           brum.place(bordermode=OUTSIDE, height=150, width=130, x=260, y=115)

           lblrum = Label(top, text="Rum")
           lblrum.pack()
           lblrum.place(bordermode=OUTSIDE, height=50, width=130, x=260, y=280)
    
           #GIN   

           gin = PhotoImage(file='gin.png')

           bgin = Button(top, image=gin, command=GIN )
           bgin.pack()
           bgin.place(bordermode=OUTSIDE, height=150, width=130, x=455, y=115)

           lblgin = Label(top, text="Gin")
           lblgin.pack()
           lblgin.place(bordermode=OUTSIDE, height=50, width=130, x=455, y=280)

           #CHAMPAGNE

           Champagne = PhotoImage(file='champagne.png.png')

           bchampagne = Button(top, image=Champagne)
           bchampagne.pack()
           bchampagne.place(bordermode=OUTSIDE, height=150, width=130, x=650, y=115)

           lblchampagne = Label(top, text="Champagne")
           lblchampagne.pack()
           lblchampagne.place(bordermode=OUTSIDE, height=50, width=130, x=650, y=280)

           #WINE

           wine = PhotoImage(file='wine icon.png')

           bwine = Button(top, image=wine, command=WINE )
           bwine.pack()
           bwine.place(bordermode=OUTSIDE, height=150, width=130, x=845, y=115)

           lblwine = Label(top, text="Wine")
           lblwine.pack()
           lblwine.place(bordermode=OUTSIDE, height=50, width=130, x=845, y=280)

           #VODKA

           vodka = PhotoImage(file='vodka.png')

           bvodka = Button(top, image=vodka, command=VODKA )
           bvodka.pack()
           bvodka.place(bordermode=OUTSIDE, height=150, width=130, x=1040, y=115)

           lblvodka = Label(top, text="Vodka")
           lblvodka.pack()
           lblvodka.place(bordermode=OUTSIDE, height=50, width=130, x=1040, y=280)

           #BEER

           beer = PhotoImage(file='beer.png.png')

           bbeer = Button(top, image=beer, command=BEER )
           bbeer.pack()
           bbeer.place(bordermode=OUTSIDE, height=150, width=130, x=455, y=350)

           lblbeer = Label(top, text="Beer")
           lblbeer.pack()
           lblbeer.place(bordermode=OUTSIDE, height=50, width=130, x=455, y=515)

           #TEQUILA


           tequila = PhotoImage(file='tequila.png')

           btequila = Button(top, image=tequila, command=TEQUILA )
           btequila.pack()
           btequila.place(bordermode=OUTSIDE, height=150, width=130, x=650, y=350)

           lbltequila = Label(top, text="Tequila")
           lbltequila.pack()
           lbltequila.place(bordermode=OUTSIDE, height=50, width=130, x=650, y=515)



    
           photo1 = PhotoImage(file='one.png')

           c1.create_image(670,30, image=photo1, anchor=CENTER).pack()
           top.mainloop()
    

b = Beginning(app)

#PRODUCTS   
def WHISKY():
        scotch = Toplevel()
        scotch.geometry('1400x1400+0+0')
        scotch.title('Gentleman drink')
        scotch.configure(bg='#2C1503')

        c2 = Canvas(scotch, height=50, width=1400, bg='maroon')
        c2.pack()
        

        johnniewalker = PhotoImage(file='johnniewalker.png')

        bjohnniewalker = Button(scotch, image=johnniewalker, command=JOHNNIEWALKER)
        bjohnniewalker.pack()
        bjohnniewalker.place(bordermode=OUTSIDE, height=210, width=210, x=65, y=100)

        jackdaniels = PhotoImage(file='jackdaniels.png')

        bjackdaniels = Button(scotch, image=jackdaniels, command=JACKDANIELS)
        bjackdaniels.pack()
        bjackdaniels.place(bordermode=OUTSIDE, height=210, width=210, x=65, y=360)


        chivasregal = PhotoImage(file='chivasregal.png')

        bchivasregal = Button(scotch, image=chivasregal, command=CHIVASREGAL)
        bchivasregal.pack()
        bchivasregal.place(bordermode=OUTSIDE, height=210, width=210, x=325, y=100)



        Glenfiddich = PhotoImage(file='Glenfiddich.png')

        bGlenfiddich = Button(scotch,image=Glenfiddich, command=GLENFIDDICH)
        bGlenfiddich.pack()
        bGlenfiddich.place(bordermode=OUTSIDE, height=210, width=210, x=325 , y=360)

        
        olddurbar = PhotoImage(file='olddurbar.png')

        bolddurbar = Button(scotch,image=olddurbar, command=OLDDURBAR)
        bolddurbar.pack()
        bolddurbar.place(bordermode=OUTSIDE, height=210, width=210, x=585 , y=100)


        goldenoak= PhotoImage(file='goldenoak.png')
        

        bgoldenoak = Button(scotch,image=goldenoak)
        bgoldenoak.pack()
        bgoldenoak.place(bordermode=OUTSIDE, height=210, width=210, x=585 , y=360)


        j89 = PhotoImage(file='j89.png')

        bj89 = Button(scotch,image=j89)
        bj89.pack()
        bj89.place(bordermode=OUTSIDE, height=210, width=210, x=845 , y=100)

        

        virgin = PhotoImage(file='virgin.png')

        bvirgin = Button(scotch,image=virgin)
        bvirgin.pack()
        bvirgin.place(bordermode=OUTSIDE, height=210, width=210, x=845 , y=360)
    
        photo1 = PhotoImage(file='WHISKY.png')

        c2.create_image(670,30, image=photo1, anchor=CENTER)
        c2.pack()
        

        scotch.mainloop()

def JOHNNIEWALKER():
        jw = Toplevel()
        jw.geometry('1400x1400+0+0')
        jw.title('Gentleman drink')
        jw.configure(bg='#2C1503')


        cjw = Canvas(jw, height=50, width=1400, bg='maroon')
        cjw.pack()
        

        redlabel = PhotoImage(file='redlabel.png')

        lblredlabel = Label(jw, image=redlabel)
        lblredlabel.pack()
        lblredlabel.place(bordermode=OUTSIDE, height=200, width=120, x=65, y=100)

        lblredlabel1 = Label(jw, text="1L")
        lblredlabel1.pack()
        lblredlabel1.place(bordermode=OUTSIDE, height=20, width=120, x=65, y=305)

        lblredlabel2 = Label(jw, text="Price: Rs. 5,965")
        lblredlabel2.pack()
        lblredlabel2.place(bordermode=OUTSIDE, height=20, width=120, x=65, y=330)




        blacklabel = PhotoImage(file='blacklabel.png')

        lblblacklabel = Label(jw, image=blacklabel)
        lblblacklabel.pack()
        lblblacklabel.place(bordermode=OUTSIDE, height=200, width=120, x=215, y=100)

        lblblacklabel1 = Label(jw, text="1L")
        lblblacklabel1.pack()
        lblblacklabel1.place(bordermode=OUTSIDE, height=20, width=120, x=215, y=305)

        lblblacklabel2 = Label(jw, text="Price: Rs. 7,600")
        lblblacklabel2.pack()
        lblblacklabel2.place(bordermode=OUTSIDE, height=20, width=120, x=215, y=330)



        greenlabel = PhotoImage(file='greenlabel.png')

        lblgreenlabel = Label(jw, image=greenlabel)
        lblgreenlabel.pack()
        lblgreenlabel.place(bordermode=OUTSIDE, height=200, width=120, x=365, y=100)


        lblgreenlabel1 = Label(jw, text="1L")
        lblgreenlabel1.pack()
        lblgreenlabel1.place(bordermode=OUTSIDE, height=20, width=120, x=365, y=305)

        lblgreenlabel2 = Label(jw, text="Rs. 8,000")
        lblgreenlabel2.pack()
        lblgreenlabel2.place(bordermode=OUTSIDE, height=20, width=120, x=365, y=330)


        doudleblack = PhotoImage(file='doudleblack.png')

        lbldoudleblack = Label(jw, image=doudleblack)
        lbldoudleblack.pack()
        lbldoudleblack.place(bordermode=OUTSIDE, height=200, width=120, x=535, y=100)

        lbldoudleblack1 = Label(jw, text="1L")
        lbldoudleblack1.pack()
        lbldoudleblack1.place(bordermode=OUTSIDE, height=20, width=120, x=535, y=305)

        lbldoudleblack2 = Label(jw, text="Rs. 8,440")
        lbldoudleblack2.pack()
        lbldoudleblack2.place(bordermode=OUTSIDE, height=20, width=120, x=535, y=330)


        #  = PhotoImage(file='.png')

        # lbl = Label(jw, image=)
        # lbl.pack()
        # lbl.place(bordermode=OUTSIDE, height=210, width=210, x=65, y=100)


        #  = PhotoImage(file='.png')

        # lbl = Label(jw, image=)
        # lbl.pack()
        # lbl.place(bordermode=OUTSIDE, height=210, width=210, x=65, y=100)







        jw.mainloop()

def JACKDANIELS():
        jd = Toplevel()
        jd.geometry('1400x1400+0+0')
        jd.title('Gentleman drink')
        jd.configure(bg='#2C1503')


        cjd = Canvas(jd, height=50, width=1400, bg='maroon')
        cjd.pack()
        

        jackdaniels1l = PhotoImage(file='jackdaniels1l.png')

        lbljackdaniels1l = Label(jd, image=jackdaniels1l)
        lbljackdaniels1l.pack()
        lbljackdaniels1l.place(bordermode=OUTSIDE, height=200, width=120, x=65, y=100)

        lbljackdaniels1l1 = Label(jd, text="1L")
        lbljackdaniels1l1.pack()
        lbljackdaniels1l1.place(bordermode=OUTSIDE, height=20, width=120, x=65, y=305)

        lbljackdaniels1l2 = Label(jd, text="Price: Rs. 6,700")
        lbljackdaniels1l2.pack()
        lbljackdaniels1l2.place(bordermode=OUTSIDE, height=20, width=120, x=65, y=330)




        jdhoney = PhotoImage(file='jdhoney.png')

        lbljdhoney = Label(jd, image=jdhoney)
        lbljdhoney.pack()
        lbljdhoney.place(bordermode=OUTSIDE, height=200, width=120, x=215, y=100)

        lbljdhoney1 = Label(jd, text="1L")
        lbljdhoney1.pack()
        lbljdhoney1.place(bordermode=OUTSIDE, height=20, width=120, x=215, y=305)

        lbljdhoney2 = Label(jd, text="Price: Rs. 7,050")
        lbljdhoney2.pack()
        lbljdhoney2.place(bordermode=OUTSIDE, height=20, width=120, x=215, y=330)



        # greenlabel = PhotoImage(file='greenlabel.png')

        # lblgreenlabel = Label(jd, image=greenlabel)
        # lblgreenlabel.pack()
        # lblgreenlabel.place(bordermode=OUTSIDE, height=200, width=120, x=365, y=100)


        # lblgreenlabel1 = Label(jd, text="1L")
        # lblgreenlabel1.pack()
        # lblgreenlabel1.place(bordermode=OUTSIDE, height=20, width=120, x=365, y=305)

        # lblgreenlabel2 = Label(jd, text="Rs. 8,000")
        # lblgreenlabel2.pack()
        # lblgreenlabel2.place(bordermode=OUTSIDE, height=20, width=120, x=365, y=330)


        # doudleblack = PhotoImage(file='doudleblack.png')

        # lbldoudleblack = Label(jd, image=doudleblack)
        # lbldoudleblack.pack()
        # lbldoudleblack.place(bordermode=OUTSIDE, height=200, width=120, x=535, y=100)

        # lbldoudleblack1 = Label(jd, text="1L")
        # lbldoudleblack1.pack()
        # lbldoudleblack1.place(bordermode=OUTSIDE, height=20, width=120, x=535, y=305)

        # lbldoudleblack2 = Label(jd, text="Rs. 8,440")
        # lbldoudleblack2.pack()
        # lbldoudleblack2.place(bordermode=OUTSIDE, height=20, width=120, x=535, y=330)


        # #  = PhotoImage(file='.png')

        # # lbl = Label(jw, image=)
        # # lbl.pack()
        # # lbl.place(bordermode=OUTSIDE, height=210, width=210, x=65, y=100)


        # #  = PhotoImage(file='.png')

        # # lbl = Label(jw, image=)
        # # lbl.pack()
        # # lbl.place(bordermode=OUTSIDE, height=210, width=210, x=65, y=100)







        jd.mainloop()

def CHIVASREGAL():
        cr = Toplevel()
        cr.geometry('1400x1400+0+0')
        cr.title('Gentleman drink')
        cr.configure(bg='#2C1503')


        ccr = Canvas(cr, height=50, width=1400, bg='maroon')
        ccr.pack()
        

        chivasregal12 = PhotoImage(file='chivasregal12.png')

        lblchivasregal12 = Label(cr, image=chivasregal12)
        lblchivasregal12.pack()
        lblchivasregal12.place(bordermode=OUTSIDE, height=200, width=120, x=65, y=100)

        lblchivasregal121 = Label(cr, text="1L")
        lblchivasregal121.pack()
        lblchivasregal121.place(bordermode=OUTSIDE, height=20, width=120, x=65, y=305)

        lblchivasregal122 = Label(cr, text="Price: Rs. 7,500")
        lblchivasregal122.pack()
        lblchivasregal122.place(bordermode=OUTSIDE, height=20, width=120, x=65, y=330)




        chivasregal18 = PhotoImage(file='chivasregal18.png')

        lblchivasregal18 = Label(cr, image=chivasregal18)
        lblchivasregal18.pack()
        lblchivasregal18.place(bordermode=OUTSIDE, height=200, width=120, x=215, y=100)

        lblchivasregal181 = Label(cr, text="1L")
        lblchivasregal181.pack()
        lblchivasregal181.place(bordermode=OUTSIDE, height=20, width=120, x=215, y=305)

        lblchivasregal182 = Label(cr, text="Price: Rs. 14,500")
        lblchivasregal182.pack()
        lblchivasregal182.place(bordermode=OUTSIDE, height=20, width=120, x=215, y=330)



        # greenlabel = PhotoImage(file='greenlabel.png')

        # lblgreenlabel = Label(cr, image=greenlabel)
        # lblgreenlabel.pack()
        # lblgreenlabel.place(bordermode=OUTSIDE, height=200, width=120, x=365, y=100)


        # lblgreenlabel1 = Label(cr, text="1L")
        # lblgreenlabel1.pack()
        # lblgreenlabel1.place(bordermode=OUTSIDE, height=20, width=120, x=365, y=305)

        # lblgreenlabel2 = Label(cr, text="Rs. 8,000")
        # lblgreenlabel2.pack()
        # lblgreenlabel2.place(bordermode=OUTSIDE, height=20, width=120, x=365, y=330)

        cr.mainloop()
        
def GLENFIDDICH():
        gd = Toplevel()
        gd.geometry('1400x1400+0+0')
        gd.title('Gentleman drink')
        gd.configure(bg='#2C1503')


        cgd = Canvas(gd, height=50, width=1400, bg='maroon')
        cgd.pack()
        

        glenfiddich12 = PhotoImage(file='glenfiddich12.png')

        lblglenfiddich12 = Label(gd, image=glenfiddich12)
        lblglenfiddich12.pack()
        lblglenfiddich12.place(bordermode=OUTSIDE, height=200, width=120, x=65, y=100)

        lblglenfiddich121 = Label(gd, text="1L")
        lblglenfiddich121.pack()
        lblglenfiddich121.place(bordermode=OUTSIDE, height=20, width=120, x=65, y=305)

        lblglenfiddich122 = Label(gd, text="Price: Rs. 7,500")
        lblglenfiddich122.pack()
        lblglenfiddich122.place(bordermode=OUTSIDE, height=20, width=120, x=65, y=330)




        glenfiddich18 = PhotoImage(file='glenfiddich18.png')

        lblglenfiddich18 = Label(gd, image=glenfiddich18)
        lblglenfiddich18.pack()
        lblglenfiddich18.place(bordermode=OUTSIDE, height=200, width=120, x=215, y=100)

        lblglenfiddich181 = Label(gd, text="1L")
        lblglenfiddich181.pack()
        lblglenfiddich181.place(bordermode=OUTSIDE, height=20, width=120, x=215, y=305)

        lblglenfiddich182 = Label(gd, text="Price: Rs. 12,500")
        lblglenfiddich182.pack()
        lblglenfiddich182.place(bordermode=OUTSIDE, height=20, width=120, x=215, y=330)



        # greenlabel = PhotoImage(file='greenlabel.png')

        # lblgreenlabel = Label(cr, image=greenlabel)
        # lblgreenlabel.pack()
        # lblgreenlabel.place(bordermode=OUTSIDE, height=200, width=120, x=365, y=100)


        # lblgreenlabel1 = Label(cr, text="1L")
        # lblgreenlabel1.pack()
        # lblgreenlabel1.place(bordermode=OUTSIDE, height=20, width=120, x=365, y=305)

        # lblgreenlabel2 = Label(cr, text="Rs. 8,000")
        # lblgreenlabel2.pack()
        # lblgreenlabel2.place(bordermode=OUTSIDE, height=20, width=120, x=365, y=330)

        cr.mainloop()

def OLDDURBAR():
        od = Toplevel()
        od.geometry('1400x1400+0+0')
        od.title('Gentleman drink')
        od.configure(bg='#2C1503')

        twocontinents1l = PhotoImage(file='twocontinents1l.png')

        lbltwocontinents1l=Label(od, image=twocontinents1l)
        lbltwocontinents1l.pack()
        lbltwocontinents1l.place(bordermode=OUTSIDE, height=200, width=120, x=65, y=100)

        lbltwocontinents1l1 = Label(od, text="Two Continents 1L")
        lbltwocontinents1l1.pack()
        lbltwocontinents1l1.place(bordermode=OUTSIDE, height=20, width=120, x=65, y=305)

        lbltwocontinents1l2 = Label(od, text="Price: Rs. 7,500")
        lbltwocontinents1l2.pack()
        lbltwocontinents1l2.place(bordermode=OUTSIDE, height=20, width=120, x=65, y=330)

        twocontinents750ml = PhotoImage(file='twocontinents750ml.png')

        lbltwocontinents750ml = Label(od, image=twocontinents750ml)
        lbltwocontinents750ml.pack()
        lbltwocontinents750ml.place(bordermode=OUTSIDE, height=200, width=120, x=215, y=100)

        lbltwocontinents750ml1 = Label(od, text="Two Continents 750ml")
        lbltwocontinents750ml1.pack()
        lbltwocontinents750ml1.place(bordermode=OUTSIDE, height=20, width=120, x=215, y=305)

        lbltwocontinents750ml2 = Label(od, text="Price: Rs. 2,230")
        lbltwocontinents750ml2.pack()
        lbltwocontinents750ml2.place(bordermode=OUTSIDE, height=20, width=120, x=215, y=330)



        greenlabel = PhotoImage(file='greenlabel.png')

        lblgreenlabel = Label(cr, image=greenlabel)
        lblgreenlabel.pack()
        lblgreenlabel.place(bordermode=OUTSIDE, height=200, width=120, x=365, y=100)


        lblgreenlabel1 = Label(cr, text="1L")
        lblgreenlabel1.pack()
        lblgreenlabel1.place(bordermode=OUTSIDE, height=20, width=120, x=365, y=305)

        lblgreenlabel2 = Label(cr, text="Rs. 8,000")
        lblgreenlabel2.pack()
        lblgreenlabel2.place(bordermode=OUTSIDE, height=20, width=120, x=365, y=330)

# RUM product page

def RUM():
        rum = Toplevel()
        rum.geometry('1400x1400+0+0')
        rum.title('Rum')
        rum.configure(bg='#2C1503')

        c3 = Canvas(rum, height=50, width=1400, bg='maroon')
        c3.pack()


   

        bacardi = PhotoImage(file='Bacardi.png')

        bbacardi = Button(rum, image=bacardi)
        bbacardi.pack()
        bbacardi.place(bordermode=OUTSIDE, height=210, width=210, x=65, y=100)



        captainmorgan = PhotoImage(file='captainmorgan.png')

        bcaptainmorgan = Button(rum, image=captainmorgan)
        bcaptainmorgan.pack()
        bcaptainmorgan.place(bordermode=OUTSIDE, height=210, width=210, x=65, y=360)


        malibu = PhotoImage(file='malibu.png')

        bmalibu = Button(rum, image=malibu)
        bmalibu.pack()
        bmalibu.place(bordermode=OUTSIDE, height=210, width=210, x=325, y=100)


        havanaclub = PhotoImage(file='havanaclub.png')

        bhavanaclub = Button(rum, image=havanaclub)
        bhavanaclub.pack()
        bhavanaclub.place(bordermode=OUTSIDE, height=210, width=210, x=325, y=360)


        oldmonk = PhotoImage(file='oldmonk.png')

        boldmonk = Button(rum,image=oldmonk)
        boldmonk.pack()
        boldmonk.place(bordermode=OUTSIDE, height=210, width=210, x=585 , y=100)

        khukuri = PhotoImage(file='khukuri.png')

        bkhukuri = Button(rum,image=khukuri)
        bkhukuri.pack()
        bkhukuri.place(bordermode=OUTSIDE, height=210, width=210, x=585 , y=360)


        # = PhotoImage(file='.png')

        # b = Button(,image=)
        # b.pack()
        # b.place(bordermode=OUTSIDE, height=210, width=210, x=845 , y=100)


        # = PhotoImage(file='.png')

        # b = Button(,image=)
        # b.pack()
        # b.place(bordermode=OUTSIDE, height=210, width=210, x=845 , y=360)

    
        photo1 = PhotoImage(file='rum cali.png')

        c3.create_image(670,30, image=photo1, anchor=CENTER)
        c3.create_image.pack()

        rum.mainloop()

# RUM product page

def GIN():
        gin = Toplevel()
        gin.geometry('1400x1400+0+0')
        gin.title('Gin')
        gin.configure(bg='#2C1503')

        c4 = Canvas(gin, height=50, width=1400, bg='maroon')
        c4.pack()


   

        beefeater = PhotoImage(file='beefeater.png')

        bbeefeater = Button(gin, image=beefeater)
        bbeefeater.pack()
        bbeefeater.place(bordermode=OUTSIDE, height=210, width=210, x=65, y=100)



        gordon = PhotoImage(file='gordon.png')

        bgordon = Button(gin, image=gordon)
        bgordon.pack()
        bgordon.place(bordermode=OUTSIDE, height=210, width=210, x=65, y=360)


        bombaysapphire = PhotoImage(file='bombaysapphire.png')

        bbombaysapphire = Button(gin, image=bombaysapphire)
        bbombaysapphire.pack()
        bbombaysapphire.place(bordermode=OUTSIDE, height=210, width=210, x=325, y=100)


        hendricksgin = PhotoImage(file='hendricksgin.png')

        bhendricksgin = Button(gin, image=hendricksgin)
        bhendricksgin.pack()
        bhendricksgin.place(bordermode=OUTSIDE, height=210, width=210, x=325, y=360)


        snowman = PhotoImage(file='snowman.png')

        bsnowman = Button(gin,image=snowman)
        bsnowman.pack()
        bsnowman.place(bordermode=OUTSIDE, height=210, width=210, x=585 , y=100)


        blueriband = PhotoImage(file='blueriband.png')

        bblueriband = Button(gin,image=blueriband)
        bblueriband.pack()
        bblueriband.place(bordermode=OUTSIDE, height=210, width=210, x=585 , y=360)


        vogue = PhotoImage(file='vogue.png')

        bvogue = Button(gin,image=vogue)
        bvogue.pack()
        bvogue.place(bordermode=OUTSIDE, height=210, width=210, x=845 , y=100)


        bluediamond = PhotoImage(file='bluediamond.png')

        bbluediamond = Button(gin,image=bluediamond)
        bbluediamond.pack()
        bbluediamond.place(bordermode=OUTSIDE, height=210, width=210, x=845 , y=360)



    
        photo1 = PhotoImage(file='gin cali.png')

        c4.create_image(670,30, image=photo1, anchor=CENTER)
        c4.create_image.pack()

        gin.mainloop()

# WINE product page

def WINE():
        shiraz = Toplevel()
        shiraz.geometry('1400x1400+0+0')
        shiraz.title('Wine drink')
        shiraz.configure(bg='#2C1503')

        c3 = Canvas(shiraz, height=50, width=1400, bg='maroon')
        c3.pack()




   

        lindemans = PhotoImage(file='lindemans.png')

        blindemans = Button(shiraz, image=lindemans)
        blindemans.pack()
        blindemans.place(bordermode=OUTSIDE, height=210, width=210, x=65, y=100)



        jacobscreek = PhotoImage(file='jacobscreek.png')

        bjacobscreek = Button(shiraz, image=jacobscreek)
        bjacobscreek.pack()
        bjacobscreek.place(bordermode=OUTSIDE, height=210, width=210, x=65, y=360)


        jpchenet = PhotoImage(file='jpchenet.png')

        bjpchenet = Button(shiraz, image=jpchenet)
        bjpchenet.pack()
        bjpchenet.place(bordermode=OUTSIDE, height=210, width=210, x=325, y=100)




        hardys = PhotoImage(file='hardys.png')

        bhardys = Button(shiraz, image=hardys)
        bhardys.pack()
        bhardys.place(bordermode=OUTSIDE, height=210, width=210, x=325, y=360)


        bigmaster = PhotoImage(file='bigmaster.png')

        bbigmaster = Button(shiraz,image=bigmaster)
        bbigmaster.pack()
        bbigmaster.place(bordermode=OUTSIDE, height=210, width=210, x=585 , y=100)


        hinwa = PhotoImage(file='hinwa.png')

        bhinwa = Button(shiraz,image=hinwa)
        bhinwa.pack()
        bhinwa.place(bordermode=OUTSIDE, height=210, width=210, x=585 , y=360)


        divine = PhotoImage(file='divine.png')

        bdivine = Button(shiraz,image=divine)
        bdivine.pack()
        bdivine.place(bordermode=OUTSIDE, height=210, width=210, x=845 , y=100)


        canvas = PhotoImage(file='canvas.png')

        bcanvas = Button(shiraz,image=canvas)
        bcanvas.pack()
        bcanvas.place(bordermode=OUTSIDE, height=210, width=210, x=845 , y=360)



    
        photo1 = PhotoImage(file='wine cali.png')

        c3.create_image(670,30, image=photo1, anchor=CENTER)
        c3.create_image.pack()
        shiraz.mainloop()

# VODKA product page

def VODKA():
        vodka = Toplevel()
        vodka.geometry('1400x1400+0+0')
        vodka.title('Russian Drink')
        vodka.configure(bg='#2C1503')

        c5 = Canvas(vodka, height=50, width=1400, bg='maroon')
        c5.pack()




        Absolut = PhotoImage(file='Absolut.png')

        bAbsolut = Button(vodka, image=Absolut)
        bAbsolut.pack()
        bAbsolut.place(bordermode=OUTSIDE, height=210, width=210, x=65, y=100)



        smirnoff = PhotoImage(file='smirnoff.png')

        bsmirnoff = Button(vodka, image=smirnoff)
        bsmirnoff.pack()
        bsmirnoff.place(bordermode=OUTSIDE, height=210, width=210, x=65, y=360)


        ciroc = PhotoImage(file='ciroc.png')

        bciroc = Button(vodka, image=ciroc)
        bciroc.pack()
        bciroc.place(bordermode=OUTSIDE, height=210, width=210, x=325, y=100)


        greygoose = PhotoImage(file='greygoose.png')

        bgreygoose = Button(vodka, image=greygoose)
        bgreygoose.pack()
        bgreygoose.place(bordermode=OUTSIDE, height=210, width=210, x=325, y=360)


        eight = PhotoImage(file='8848.png')

        beight = Button(vodka,image=eight)
        beight.pack()
        beight.place(bordermode=OUTSIDE, height=210, width=210, x=585 , y=100)


        ruslan = PhotoImage(file='ruslan.png')

        bruslan = Button(vodka,image=ruslan)
        bruslan.pack()
        bruslan.place(bordermode=OUTSIDE, height=210, width=210, x=585 , y=360)


        # = PhotoImage(file='.png')

        # b = Button(vodka,image=)
        # b.pack()
        # b.place(bordermode=OUTSIDE, height=210, width=210, x=845 , y=100)


        # = PhotoImage(file='.png')

        # b = Button(vodka,image=)
        # b.pack()
        # b.place(bordermode=OUTSIDE, height=210, width=210, x=845 , y=360)



    
        photo1 = PhotoImage(file='vodka cali.png')

        c5.create_image(670,30, image=photo1, anchor=CENTER)
        c5.create_image.pack()

        vodka.mainloop()
      
# BEER product page

def BEER():
        beer = Toplevel()
        beer.geometry('1400x1400+0+0')
        beer.title('Russian Drink')
        beer.configure(bg='#2C1503')

        c5 = Canvas(beer, height=50, width=1400, bg='maroon')
        c5.pack()




        corona = PhotoImage(file='corona.png')

        bcorona = Button(beer, image=corona)
        bcorona.pack()
        bcorona.place(bordermode=OUTSIDE, height=210, width=210, x=65, y=100)



        hoegarden = PhotoImage(file='hoegarden.png')

        bhoegarden = Button(beer, image=hoegarden)
        bhoegarden.pack()
        bhoegarden.place(bordermode=OUTSIDE, height=210, width=210, x=65, y=360)


        budweiser = PhotoImage(file='budweiser.png')

        bbudweiser = Button(beer, image=budweiser)
        bbudweiser.pack()
        bbudweiser.place(bordermode=OUTSIDE, height=210, width=210, x=325, y=100)


        stella = PhotoImage(file='stella.png')

        bstella = Button(beer, image=stella)
        bstella.pack()
        bstella.place(bordermode=OUTSIDE, height=210, width=210, x=325, y=360)

        carlsberg= PhotoImage(file='carlsberg.png')

        bcarlsberg = Button(beer,image=carlsberg)
        bcarlsberg.pack()
        bcarlsberg.place(bordermode=OUTSIDE, height=210, width=210, x=585 , y=100)


        tuborg = PhotoImage(file='tuborg.png')

        btuborg = Button(beer,image=tuborg)
        btuborg.pack()
        btuborg.place(bordermode=OUTSIDE, height=210, width=210, x=585 , y=360)


        gorkha = PhotoImage(file='gorkha.png')

        bgorkha = Button(beer,image=gorkha)
        bgorkha.pack()
        bgorkha.place(bordermode=OUTSIDE, height=210, width=210, x=845 , y=100)


        nepalice = PhotoImage(file='nepalice.png')

        bnepalice = Button(beer,image=nepalice)
        bnepalice.pack()
        bnepalice.place(bordermode=OUTSIDE, height=210, width=210, x=845 , y=360)



    
        photo1 = PhotoImage(file='beer cali.png')

        c5.create_image(670,30, image=photo1, anchor=CENTER)
        c5.create_image.pack()

        beer.mainloop()
    
# TEQUILA product page

def TEQUILA():
        tequila = Toplevel()
        tequila.geometry('1400x1400+0+0')
        tequila.title('Mexican Drink')
        tequila.configure(bg='#2C1503')

        c6 = Canvas(tequila, height=50, width=1400, bg='maroon')
        c6.pack()




        olmeca = PhotoImage(file='olmeca.png')

        bolmeca = Button(tequila, image=olmeca)
        bolmeca.pack()
        bolmeca.place(bordermode=OUTSIDE, height=210, width=210, x=65, y=100)



        josecuervo = PhotoImage(file='josecuervo.png')

        bjosecuervo = Button(tequila, image=josecuervo)
        bjosecuervo.pack()
        bjosecuervo.place(bordermode=OUTSIDE, height=210, width=210, x=65, y=360)


        pepelopez = PhotoImage(file='pepelopez.png')

        bpepelopez = Button(tequila, image=pepelopez)
        bpepelopez.pack()
        bpepelopez.place(bordermode=OUTSIDE, height=210, width=210, x=325, y=100)


        #  = PhotoImage(file='.png')

        # b = Button(tequila, image=)
        # b.pack()
        # b.place(bordermode=OUTSIDE, height=210, width=210, x=325, y=360)


        # = PhotoImage(file='.png')

        # b = Button(tequila,image=)
        # b.pack()
        # b.place(bordermode=OUTSIDE, height=210, width=210, x=585 , y=100)


        # = PhotoImage(file='.png')

        # b = Button(tequila,image=)
        # b.pack()
        # b.place(bordermode=OUTSIDE, height=210, width=210, x=585 , y=360)


        # = PhotoImage(file='.png')

        # b = Button(tequila,image=)
        # b.pack()
        # b.place(bordermode=OUTSIDE, height=210, width=210, x=845 , y=100)


        # = PhotoImage(file='.png')

        # b = Button(tequila,image=)
        # b.pack()
        # b.place(bordermode=OUTSIDE, height=210, width=210, x=845 , y=360)


    
        photo1 = PhotoImage(file='beer cali.png')

        c6.create_image(670,30, image=photo1, anchor=CENTER)
        c6.create_image.pack()

        tequila.mainloop()


        #product detail page


app.mainloop()