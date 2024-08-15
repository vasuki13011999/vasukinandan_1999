# importing
from tkinter import *
from tkinter import ttk
from Views.AuthView import AuthView
from Controllers.AuthController import AuthController


class details:
    def __init__(self):

        # to revieve from the controller names, email , ....
        C = AuthController()
        self.cd = C.det()


    # to desplay details
    def details(self):
        print("details")
        self.window = Tk()
        self.window.title("Object Tracking")
        self.window.geometry("600x400")
        
        self.window.configure(background='#f2efe6')

        l1 = Label(self.window,text = "DETAILS",fg="blue" ,font = "Helvetica 20 italic")
        l1.place(relx =0.5, rely = 0.15, anchor = "n")


        # name
        l2 = Label(self.window,text = "NAME:", font = "Helvetica 14 italic")
        l2.place(relx =0.35, rely = 0.30, anchor = "n")

        nl = Label(self.window,text = self.cd[1], font = "Helvetica 14 italic")
        nl.place(relx =0.5, rely = 0.30, anchor = "n")

        # fullname 
        l3 = Label(self.window,text = "FULL NAME:", font = "Helvetica 14 italic")
        l3.place(relx =0.31, rely = 0.40, anchor = "n")

        fl = Label(self.window,text = self.cd[2], font = "Helvetica 14 italic")
        fl.place(relx =0.5, rely = 0.40, anchor = "n")

        # Email 
        l4 = Label(self.window,text = "EMAIL:", font = "Helvetica 14 italic")
        l4.place(relx =0.35, rely = 0.50, anchor = "n")

        el = Label(self.window,text = self.cd[4], font = "Helvetica 14 italic")
        el.place(relx =0.6, rely = 0.50, anchor = "n")

        # phone NO:
        l4 = Label(self.window,text = "PHONE NO:", font = "Helvetica 14 italic")
        l4.place(relx =0.31, rely = 0.60, anchor = "n")

        pl = Label(self.window,text = self.cd[5], font = "Helvetica 14 italic")
        pl.place(relx =0.5, rely = 0.60, anchor = "n")

        # button

        b1 = Button(self.window, text = "HOME",command=self.goto_home, fg="red", bg="white", width=6, height=2)
        b1.place(relx =0.5, rely = 0.7, anchor = "n")

        self.window.mainloop()
    

    # destroy the window
    def goto_home(self):
        self.window.destroy()

# a = details()
# a.details()