from Views.AuthView import AuthView
from Views.Home import Home
class App:
    # Starting
    def run(self):
        Auth = AuthView()
        Auth.transfer_control = self.ho    
        Auth.run()
    
    # signout to goback run
    def ho(self):
        home = Home()
        home.tab_so = self.run
        home.hme()

# calling 
app = App()
app.run()