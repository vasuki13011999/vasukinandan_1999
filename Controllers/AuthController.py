# importing
from models.AuthModel import AuthModel

# class
class AuthController:

    # login recieved login entry from view sending to db
    def login(self,un,pa):

        # checking field is empty or not
        if len(un) ==0:
            mes ="No user Name"
            return mes

        if len(pa) ==0:
            mes ="No password"
            return mes

        am = AuthModel()

        # sending db
        r=am.show(un,pa)

        # printing all
        print(r)

        # for home and details
        global dn
        dn = r

        # if r has value is true
        if r:

            # user found
            mes = 1
            # pop up
            return mes

        else:

            # user not found
            mes = "user not found"
            # pop up
            return mes

    # login recieved register entry from view sending to db
    def register(self,un,na,pa,em,ph):

        # checking the filed is empty or not
        if len(un) == 0 or len(na) == 0 or len(pa) == 0 or len(em) == 0 or len(ph) == 0 :
            mes = "some thing is null"
            return mes


        am = AuthModel()
        # sending to db
        r = am.ad(un,na,pa,em,ph)
        print(r)
        mes = 'Registered'

        # pop up
        return mes

    # sending to details_view
    def det(self):
        return dn

#A = AuthController()
#A.login("sarath","123")
#A.register("","","","","")