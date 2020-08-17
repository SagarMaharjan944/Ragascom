from tkinter import *
from tkinter import ttk


app = Tk()
app.iconbitmap('favicon.ico')
app.title('Liquor Detailer')
app.configure(background='#7d161a')
app.geometry('1400x1400+0+0')

c = Canvas(app, height=500, width=700, bg='#7d161a')

c.pack()



photoverify = PhotoImage(file='verify.png')

c.create_image(230,435, image=photoverify, anchor=NW)

photoone = PhotoImage(file='one.png')
c.create_image(350,50, image=photoone, anchor=CENTER)

photobg = PhotoImage(file='Bar BG.gif')
c.create_image(350, 250, image=photobg, anchor=CENTER)


class Beginning:

   def __init__(self, root):
      myFrame = Frame(root)
      myFrame.pack()

      self.b1 = Button(app, text="ABOVE 21", font=('Exceptional Experience', 12), bg='green', bd=10, relief=GROOVE, padx=53, pady=5, command=self.Register)
      self.b2 = Button(app, text="BELLOW 21", font=('Exceptional Experience', 12), bg='red', bd=10, relief=GROOVE, padx=50, pady=5,  command=self.myClick)

      self.b1.pack()
      self.b2.pack()
   

   def Register_User(self):
           Username_info = Username.get()
           Password_info = Password.get()

           file=open(Username_info+".txt", "w")
           file.write(Username_info+"\n")
           file.write(Password_info)
           file.close()

           Username_entry.delete(0, END)
           Password_entry.delete(0, END)   

           Label(register, text="*Registration successful*", fg='white', bg='maroon', font = ("calibri", 12)).pack()

   def Register(self):
           global register 
           register = Toplevel()        
           register.title("Register")
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
           myLabel = Label(app, text="You are not eligible to access this Application", font='LARGE_FONT')
           myLabel.pack(padx=25, pady=3)

           button_quit = Button(app, text="Exit Program", command=app.quit)
           button_quit.pack()

 # firstpage of products

  

   def Welcome(self):
           top = Toplevel()
           top.geometry('1400x1400')
           top.title('Know your price')

    


           c1 = Canvas(top, height=50, width=1400, bg='maroon')
           c1.pack()




           #WHISKY  

           whisky = PhotoImage(file='whisky time.png')

           bwhisky = Button( top, image=whisky, command=self.WHISKY)
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
    

b = Beginning(app)

class Catagories:

        def __init__(self, products):
                myFrame = Frame(products)
                myFrame.pack()

        def WHISKY(self):
                scotch = Toplevel()
                scotch.geometry('1400x1400')
                scotch.title('Gentleman drink')

                c2 = Canvas(scotch, height=50, width=1400, bg='maroon')
                c2.pack()
        

                imported = PhotoImage(file='imported product .png')

                bimported = Button( scotch, image=imported)
                bimported.pack()
                bimported.place(bordermode=OUTSIDE, height=150, width=130, x=450, y=260)

                lblimported = Label(scotch, text="IMPORTED PRODUCT")
                lblimported.pack()
                lblimported.place(bordermode=OUTSIDE, height=50, width=130, x=450, y=425)

        

                nepaliproduct = PhotoImage(file='Nepal.png')


                bnepaliproduct = Button(scotch, image=nepaliproduct )
                bnepaliproduct.pack()
                bnepaliproduct.place(bordermode=OUTSIDE, height=150, width=130, x=720, y=260)

                lblnepaliproduct = Label(scotch, text="NEPALI PRODUCT")
                lblnepaliproduct.pack()
                lblnepaliproduct.place(bordermode=OUTSIDE, height=50, width=130, x=720, y=425)

    
                photo1 = PhotoImage(file='WHISKY.png')

                c2.create_image(670,30, image=photo1, anchor=CENTER)
                c2.pack()
        

                scotch.mainloop()

        def Imported(self):
                imported=Toplevel()
                imported.geometry('1400x1400+0+0')
                imported.title('Gentleman Drink')

                c7 = Canvas(imported, height=50, width=1400, bg='maroon')
                c7.pack()

                johnniewalker = PhotoImage()


                bnepaliproduct = Button(scotch, image=nepaliproduct )
                bnepaliproduct.pack()
                bnepaliproduct.place(bordermode=OUTSIDE, height=150, width=130, x=720, y=260)

                lblnepaliproduct = Label(scotch, text="NEPALI PRODUCT")
                lblnepaliproduct.pack()
                lblnepaliproduct.place(bordermode=OUTSIDE, height=50, width=130, x=720, y=425)

    
                photo1 = PhotoImage(file='WHISKY.png')

                c7.create_image(670,30, image=photo1, anchor=CENTER)
                c7.pack()
   
        def RUM(self):
                rum = Toplevel()
                rum.geometry('1400x1400')
                rum.title('Rum')

                c3 = Canvas(rum, height=50, width=1400, bg='maroon')
                c3.pack()
 

                imported = PhotoImage(file='imported product .png')

                bimported = Button(rum, image=imported)
                bimported.pack()
                bimported.place(bordermode=OUTSIDE, height=150, width=130, x=450, y=260)

                lblimported = Label(rum, text="IMPORTED PRODUCT")
                lblimported.pack()
                lblimported.place(bordermode=OUTSIDE, height=50, width=130, x=450, y=425)

        

                nepaliproduct = PhotoImage(file='Nepal.png')


                bnepaliproduct = Button(rum, image=nepaliproduct )
                bnepaliproduct.pack()
                bnepaliproduct.place(bordermode=OUTSIDE, height=150, width=130, x=720, y=260)

                lblnepaliproduct = Label(rum, text="NEPALI PRODUCT")
                lblnepaliproduct.pack()
                lblnepaliproduct.place(bordermode=OUTSIDE, height=50, width=130, x=720, y=425)


    
                photo1 = PhotoImage(file='rum cali.png')

                c3.create_image(670,30, image=photo1, anchor=CENTER)
                c3.create_image.pack()

                rum.mainloop()

                # RUM product page

        def GIN(self):
                gin = Toplevel()
                gin.geometry('1400x1400')
                gin.title('Rum')

                c4 = Canvas(gin, height=50, width=1400, bg='maroon')
                c4.pack()


   

                imported = PhotoImage(file='imported product .png')

                bimported = Button(gin, image=imported)
                bimported.pack()
                bimported.place(bordermode=OUTSIDE, height=150, width=130, x=450, y=260)

                lblimported = Label(gin, text="IMPORTED PRODUCT")
                lblimported.pack()
                lblimported.place(bordermode=OUTSIDE, height=50, width=130, x=450, y=425)

        

                nepaliproduct = PhotoImage(file='Nepal.png')


                bnepaliproduct = Button(gin, image=nepaliproduct)
                bnepaliproduct.pack()
                bnepaliproduct.place(bordermode=OUTSIDE, height=150, width=130, x=720, y=260)

                lblnepaliproduct = Label(gin, text="NEPALI PRODUCT")
                lblnepaliproduct.pack()
                lblnepaliproduct.place(bordermode=OUTSIDE, height=50, width=130, x=720, y=425)


    
                photo1 = PhotoImage(file='gin cali.png')

                c4.create_image(670,30, image=photo1, anchor=CENTER)
                c4.create_image.pack()

                gin.mainloop()

        
                # WINE product page

        def WINE(self):
                shiraz = Toplevel()
                shiraz.geometry('1400x1400')
                shiraz.title('Wine drink')

                c3 = Canvas(shiraz, height=50, width=1400, bg='maroon')
                c3.pack()

                imported = PhotoImage(file='imported product .png')

                bimported = Button( shiraz, image=imported)
                bimported.pack()
                bimported.place(bordermode=OUTSIDE, height=150, width=130, x=450, y=260)

                lblimported = Label(shiraz, text="IMPORTED PRODUCT")
                lblimported.pack()
                lblimported.place(bordermode=OUTSIDE, height=50, width=130, x=450, y=425)

        

                nepaliproduct = PhotoImage(file='Nepal.png')


                bnepaliproduct = Button(shiraz, image=nepaliproduct )
                bnepaliproduct.pack()
                bnepaliproduct.place(bordermode=OUTSIDE, height=150, width=130, x=720, y=260)

                lblnepaliproduct = Label(shiraz, text="NEPALI PRODUCT")
                lblnepaliproduct.pack()
                lblnepaliproduct.place(bordermode=OUTSIDE, height=50, width=130, x=720, y=425)


    
                photo1 = PhotoImage(file='wine cali.png')

                c3.create_image(670,30, image=photo1, anchor=CENTER)
                c3.create_image.pack()
                shiraz.mainloop()

                # VODKA product page

        def VODKA(self):
                vodka = Toplevel()
                vodka.geometry('1400x1400')
                vodka.title('Russian Drink')

                c5 = Canvas(vodka, height=50, width=1400, bg='maroon')
                c5.pack()




                imported = PhotoImage(file='imported product .png')

                bimported = Button(vodka, image=imported)
                bimported.pack()
                bimported.place(bordermode=OUTSIDE, height=150, width=130, x=450, y=260)

                lblimported = Label(vodka, text="IMPORTED PRODUCT")
                lblimported.pack()
                lblimported.place(bordermode=OUTSIDE, height=50, width=130, x=450, y=425)

        

                nepaliproduct = PhotoImage(file='Nepal.png')


                bnepaliproduct = Button(vodka, image=nepaliproduct)
                bnepaliproduct.pack()
                bnepaliproduct.place(bordermode=OUTSIDE, height=150, width=130, x=720, y=260)

                lblnepaliproduct = Label(vodka, text="NEPALI PRODUCT")
                lblnepaliproduct.pack()
                lblnepaliproduct.place(bordermode=OUTSIDE, height=50, width=130, x=720, y=425)


    
                photo1 = PhotoImage(file='vodka cali.png')

                c5.create_image(670,30, image=photo1, anchor=CENTER)
                c5.create_image.pack()

                vodka.mainloop()

                # BEER product page

        def BEER(self):
                beer = Toplevel()
                beer.geometry('1400x1400')
                beer.title('Russian Drink')

                c5 = Canvas(beer, height=50, width=1400, bg='maroon')
                c5.pack()




                imported = PhotoImage(file='imported product .png')

                bimported = Button(beer, image=imported)
                bimported.pack()
                bimported.place(bordermode=OUTSIDE, height=150, width=130, x=450, y=260)

                lblimported = Label(beer, text="IMPORTED PRODUCT")
                lblimported.pack()
                lblimported.place(bordermode=OUTSIDE, height=50, width=130, x=450, y=425)

        

                nepaliproduct = PhotoImage(file='Nepal.png')


                bnepaliproduct = Button(beer, image=nepaliproduct)
                bnepaliproduct.pack()
                bnepaliproduct.place(bordermode=OUTSIDE, height=150, width=130, x=720, y=260)

                lblnepaliproduct = Label(beer, text="NEPALI PRODUCT")
                lblnepaliproduct.pack()
                lblnepaliproduct.place(bordermode=OUTSIDE, height=50, width=130, x=720, y=425)


    
                photo1 = PhotoImage(file='beer cali.png')

                c5.create_image(670,30, image=photo1, anchor=CENTER)
                c5.create_image.pack()

                beer.mainloop()

                # TEQUILA product page

        def TEQUILA(self):
                tequila = Toplevel()
                tequila.geometry('1400x1400')
                tequila.title('Mexican Drink')

                c6 = Canvas(tequila, height=50, width=1400, bg='maroon')
                c6.pack()




                imported = PhotoImage(file='imported product .png')

                bimported = Button(tequila, image=imported)
                bimported.pack()
                bimported.place(bordermode=OUTSIDE, height=150, width=130, x=450, y=260)

                lblimported = Label(tequila, text="IMPORTED PRODUCT")
                lblimported.pack()
                lblimported.place(bordermode=OUTSIDE, height=50, width=130, x=450, y=425)

        

                nepaliproduct = PhotoImage(file='Nepal.png')


                bnepaliproduct = Button(tequila, image=nepaliproduct )
                bnepaliproduct.pack()
                bnepaliproduct.place(bordermode=OUTSIDE, height=150, width=130, x=720, y=260)

                lblnepaliproduct = Label(tequila, text="NEPALI PRODUCT")
                lblnepaliproduct.pack()
                lblnepaliproduct.place(bordermode=OUTSIDE, height=50, width=130, x=720, y=425)


    
                photo1 = PhotoImage(file='beer cali.png')

                c6.create_image(670,30, image=photo1, anchor=CENTER)
                c6.create_image.pack()

                tequila.mainloop()

c = Catagories(app)                



app.mainloop()