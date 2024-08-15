from lib.db import *
class AuthModel:

    def __init__(self):
        # commectong the Database
        self.con =connect("db/app.db")
    
    
    # adding the database
    def ad(self,un,na,pa,em,ph):
        query = f'INSERT INTO log (un,na,pa,em,ph) VALUES("{un}","{na}","{pa}","{em}",{ph});'
        se = insert(self.con,query)
        return se
       
    # checking user name and password
    def show(self,un,pa):
        query = f'SELECT * FROM log WHERE un= "{un}" and pa= "{pa}";'
        se = fetchone(self.con,query)
        return se

#am =AuthModel()
#am.show("sarath",123)
#am.ad("admin","administrator","admin","admin@",143)