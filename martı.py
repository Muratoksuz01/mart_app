import sqlite3 as sql
import time

class sing_in():
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.con=sql.connect("martı.db")
        
        self.imlec=self.con.cursor()
    def chack(self):
        self.imlec.execute("SELECT * from martı WHERE usernames='{}'and passwords='{}'".format(self.username,self.password))
        liste=self.imlec.fetchall()
        if len(liste)!=0:
            liste=list(liste[0])
            
        return len(liste)
    
    
    def menu(self):
        while True:
            print("""
            1-)start driving
            2-)user information
            3-)log out
            """)
            choose=int(input("choose:"))
            if choose==1:
                self.start_driving()
            if choose==2:
                self.user_information()
            if choose==3:
                break






    def start_driving(self):
        start=time.time()
        print("started your driving")
        times=(input("press anything key:"))
        finish=time.time()
        price=finish-start
        price=price/60
        total=price*1.8
        print("{} DK".format(price))
        print("price={}$".format(total))
        print("thank you for  you used  the martı app")
    
    
    def user_information(self):
        self.imlec.execute("SELECT * from martı WHERE usernames='{}'".format(self.username))
        list=self.imlec.fetchall()
        print("""
        name:{}
        surname:{}
        username:{}
        password:{}
        card_number:{}""".format(list[0][0],list[0][1],list[0][2],list[0][3],list[0][4]))
        self.menu()
        

class sing_up():
    def __init__(self,name,surname,username,password,card_num):
        self.name=name
        self.surname=surname
        self.username=username
        self.password=password
        self.card_num=card_num
        self.con=sql.connect("martı.db")
        self.imlec=self.con.cursor()
        self.imlec.execute("CREATE TABLE IF NOT EXISTS martı(names TEXT,surnames text,usernames text,passwords text,card_nm int)")
        self.con.commit()
        
    def chack(self):
        self.imlec.execute("SELECT * from martı WHERE usernames='{}'".format(self.username))
        list=self.imlec.fetchall()
        return len(list)
    def record(self):
        sql.connect("martı.db")
        self.imlec.execute("INSERT INTO martı VALUES('{}','{}','{}','{}','{}')".format(self.name,self.surname,self.username,self.password,self.card_num))
        self.con.commit()
        self.con.close()
        print("successfully registered")
        


while True:
    print("WELCOME TO MARTI APP:)")
    try:
        mom_choose=int(input("1-)SİNG İN \n2-)SİNG UP\n3-)EXIT\n VOTE ="))
        while mom_choose<0 and mom_choose>3:
            mom_choose=int(input("1-)SİNG İN \n2-)SİNG UP\n VOTE ="))       
    except ValueError:
        print("gecersiz giriş")
    if mom_choose==1:
        username=input("enter to username:")
        password=input("enter to password:")
        sing_in1=sing_in(username,password)
        piece=sing_in1.chack()
        if piece!=0:
            sing_in1.menu()  
        else:
            print("girdiğiniiz bilgilerle bir kişi yok!!!")
            continue
        
    if mom_choose==2:#kayıt olmak 
        name=input("enter to name:")
        surname=input("enter to surname:")
        username=input("enter to username:")
        password=input("enter to password:")
        card_number=input("enter to card number:")
        while len(card_number)!=16:
            print("invalid card number")
            card_number=input("enter to card number:")
        sing_up1=sing_up(name,surname,username,password,card_number)
        piece=sing_up1.chack()
        if piece!=0:
            print("böyle bir kullanıcı mevcut")
            continue
        else:
            sing_up1.record()
    

    if mom_choose==3:
        print("We hope you come again:):)")
        break