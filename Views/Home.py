# importing
from tkinter import *
from tkinter import ttk
from Controllers.AuthController import AuthController
from Views.AuthView import AuthView
from Views.Details_View import details
from lib.ColorDetect import ColorDetect
class Home:

    def __init__(self):
        A = AuthView()
        self.k = A.nam()

        
    # home page
    def hme(self):
        print("this is Home")

        # tkinter
        self.window = Tk()
        self.window.title("Object Tracking")
        self.window.geometry("600x400")
        
        self.window.configure(background='#f2efe6')

        # welcome name
        l1 = Label(self.window,text = "welcome "+self.k+".", font = "Helvetica 16 italic")
        l1.place(relx = 0.0,rely = 0.0)

        # obj detect

        l2 = Label(self.window,text = "Click any color to Object track", font = "Helvetica 10 italic")
        l2.place(relx =0.35, rely = 0.25)

        # blue
        l3 = Button(self.window,text = "Blue",command =lambda: self.ot(0), fg='blue',bg="white",width=7, height=2)
        l3.place(relx = 0.5,rely = 0.38,anchor = 'center') 

        # red
        l4 = Button(self.window,text = "Red", fg='red',bg="white",command = lambda: self.ot(1) , width=7, height=2)
        l4.place(relx = 0.4,rely = 0.38,anchor = 'center')

        # yellow
        l5 = Button(self.window,text = "yellow", fg="#9b870c",command =lambda: self.ot(2) ,bg="white", width=7, height=2)
        l5.place(relx = 0.6,rely = 0.38,anchor = 'center')          

        # escape
        ex = Label(self.window, text = "*Press <ESC> to exit the Camera", font = "Helvetica 10 bold")
        ex.place(relx = 0.5, rely = 0.5, anchor = 's') 


        # user details
        l6 = Label(self.window, text = "Click here for User Details", font = "Helvetica 10 italic")
        l6.place(relx = 0.5, rely = 0.6, anchor = 's') 

        l7 = Button(self.window,text = "User details", command = self.detail ,fg="black",bg="white", width=11, height=2)
        l7.place(relx = 0.5, rely = 0.75,anchor = 's')

        # sign out
        l8 = Button(self.window,text="Sign out", command = self.fp, fg="black", bg="white", width=6, height=2)
        l8.place(relx = 0.9, rely = 0.95, anchor='sw')


        self.window.mainloop()

    # sign out
    def fp(self):
        print("Sign Out")
        self.window.destroy()
        self.tab_so()

    # to go details view
    def detail(self):
        print(self.k)
        self.A = details()
        self.A.details()


    # button selection to send

    def ot(self,c):
        global d
        d = c
        cd = ColorDetect()
        cd.otd(d)
