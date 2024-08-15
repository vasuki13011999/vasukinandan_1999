from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Controllers.AuthController import AuthController
class AuthView:

    def run(self):
        # creating tk window
        self.window = Tk()

        # Renaming the Title
        self.window.title("Object Tracking")

        # geomentry
        #self.window.geometry("250x150")
        
        # Notebook
        tab_control = ttk.Notebook(self.window)

        # Adding frames
        Login_frame = Frame(tab_control, padx = "200", pady = "100")
        Register_frame = Frame(tab_control, padx = "200", pady = "100")

        # connect Frames
        tab_control.add(Login_frame, text = "Login")
        tab_control.add(Register_frame, text = "Register")

        # presting Frames

        tab_control.grid()

        # calling Login
        self.Login(Login_frame)
        
        # calling Register
        self.Register(Register_frame)
        self.na ='temp'


        self.window.mainloop()

        # creating the Login view
    def Login(self, Login_frame):
        print("This is Login")
        
        # creating username
        un = Label(Login_frame, text="User Name: ")
        un.grid(row=0, column=0)

        ue = Entry(Login_frame, width="20")
        ue.grid(row=0,column=1)

        # creating password
        pn = Label(Login_frame, text="Password: ")
        pn.grid(row=1, column=0)

        pe = Entry(Login_frame, show ="*", width="20")
        pe.grid(row=1, column=1)

        # login button
        lb = Button(Login_frame, text="Login",command=lambda: self.logincontroller( ue.get(), pe.get() ), fg='blue', width=7, height=1)
        lb.grid(row=2, column=1, pady="5")
        self.na = ue.get()

        # sending the login entry to controller
    def logincontroller(self,un1,pa1):
        A = AuthController()
        mes = A.login(un1,pa1)
        global na
        na = un1

        # pop up
        if mes == 1:
            self.window.destroy()
            #print(self.na)
            self.transfer_control()
        else:
            messagebox.showinfo('message: ', mes)

    def nam(self):
        cra = na
        return cra
    

    # creating Register
    def Register(self, Register_frame):
        print("This is Register")


        #creating user name
        run = Label(Register_frame, text="User Name: ")
        run.grid(row=0, column=0)

        rue = Entry(Register_frame, width="22")
        rue.grid(row=0,column=1)

        #full name
        rfn = Label(Register_frame, text="Full Name: ")
        rfn.grid(row=1, column=0)

        rfe = Entry(Register_frame, width="22")
        rfe.grid(row=1,column=1)


        #Email
        ren = Label(Register_frame, text="Email: ")
        ren.grid(row=2, column=0)

        ree = Entry(Register_frame, width="22")
        ree.grid(row=2,column=1)

        #phone no
        rpn = Label(Register_frame, text="Phone No: ")
        rpn.grid(row=3, column=0)

        rpe = Entry(Register_frame, width="22")
        rpe.grid(row=3,column=1)

        #password
        rpan = Label(Register_frame, text="Password: ")
        rpan.grid(row=4, column=0)

        rpae = Entry(Register_frame, show="*", width="22")
        rpae.grid(row=4,column=1)

        #retype
        rrpn = Label(Register_frame, text="Re-Password: ")
        rrpn.grid(row=5, column=0)

        rrpe = Entry(Register_frame, show="*", width="22")
        rrpe.grid(row=5, column=1)

        #button
        rb = Button(Register_frame, text="Register", fg='blue',command=lambda: self.registercontroller( rue.get(), rfe.get(), ree.get(), rpe.get(), rrpe.get(), rpae.get()) ,width=7, height=1)
        rb.grid(row=6, column=1, pady="5")

    # sending the Register entry to controller
    def registercontroller(self,rue,rfe,ree,rpe,rrpe,rpae):

        # checking the password and re-type password
        if rrpe != rpae:
            messagebox.showwarning(title="password", message="Password Incorrect")

        else:
            A = AuthController()
            mes = A.register(rue,rfe,rrpe,ree,rpe)

            # pop up
            messagebox.showinfo('message: ', mes)

            # destroy window
            self.window.destroy()
            self.run()


        
if __name__ == "__main__":
    A = AuthView()