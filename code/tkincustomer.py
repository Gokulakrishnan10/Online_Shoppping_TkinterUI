from tkinter import *
from datetime import date,timedelta
from tkinter import messagebox
from time import strftime

class Customer:

    def __init__(self,cursor,mydb,root):
        self.cursor=cursor
        self.mydb=mydb
        self.root=root

    def customer_signup(self,lfc):

        lfc.destroy()
        lfcsu=Frame(self.root,height=80,width=160,bg='#04042e')
        lfcsu.pack()

        Label(lfcsu,text='CUSTOMER',font=('bold',35),fg='#67e9f0',bg='#04042e').grid()
        Label(lfcsu,text='SIGNUP PAGE',font=('bold',25),fg='#67e9f0',bg='#04042e').grid()
        Label(lfcsu,text='Enter your id:',font=('bold',18),fg='#67e9f0',bg='#04042e').grid(row=2,column=0)
        Label(lfcsu,text='Enter your name:',font=('bold',18),fg='#67e9f0',bg='#04042e').grid(row=3,column=0)
        Label(lfcsu,text='Enter your phone number:',font=('bold',18),fg='#67e9f0',bg='#04042e').grid(row=4,column=0)
        Label(lfcsu,text='Enter the password',font=('bold',18),fg='#67e9f0',bg='#04042e').grid(row=5,column=0)
        Label(lfcsu,text='Enter your address:',font=('bold',18),fg='#67e9f0',bg='#04042e').grid(row=6,column=0)


        cust_id=Entry(lfcsu,bg='#02021c',fg='#67e9f0')
        name=Entry(lfcsu,bg='#02021c',fg='#67e9f0')
        phone_no=Entry(lfcsu,bg='#02021c',fg='#67e9f0')
        password=Entry(lfcsu,bg='#02021c',fg='#67e9f0')
        address=Entry(lfcsu,bg='#02021c',fg='#67e9f0')
        cust_id.grid(row=2,column=1)
        name.grid(row=3,column=1)
        phone_no.grid(row=4,column=1)
        password.grid(row=5,column=1)
        address.grid(row=6,column=1)
        
        def submit():
            query="INSERT INTO customer(cust_id,name,phone_no,password,address) VALUES( %s, %s, %s,%s,%s)"
            self.cursor.execute(query,(cust_id.get(),name.get(),phone_no.get(),password.get(),address.get()))
            self.mydb.commit()
            self.customerhome(cust_id,address,lfcsu)
        Button(lfcsu,text='Submit',command=submit,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).grid(row=6,column=0)


    

    def customer_signin(self,lfc):
        lfc.destroy()
        lfcsi=Frame(self.root,height=80,width=160,bg='#04042e')
        lfcsi.pack()
        Label(lfcsi,text='SIGNIN PAGE',font=('bold',25),fg='#67e9f0',bg='#04042e').grid()
        Label(lfcsi,text='Enter your name:',font=('bold',18),fg='#67e9f0',bg='#04042e').grid(row=1,column=0)
        Label(lfcsi,text='Enter the password',font=('bold',18),fg='#67e9f0',bg='#04042e').grid(row=2,column=0)
        name=Entry(lfcsi,bg='#02021c',fg='#67e9f0')
        password=Entry(lfcsi,bg='#02021c',fg='#67e9f0')
        name.grid(row=1,column=1)
        password.grid(row=2,column=1)
        def submit():
            query="SELECT name,password FROM customer WHERE name=%s and password=%s"
            self.cursor.execute(query,(name.get(),password.get()))
            val=self.cursor.fetchone()

            query="SELECT cust_id FROM customer WHERE name=%s and password=%s"
            self.cursor.execute(query,(name.get(),password.get()))
            cus=self.cursor.fetchone()
            cust_id=cus[0]

            query="SELECT address FROM customer WHERE name=%s and password=%s"
            self.cursor.execute(query,(name.get(),password.get()))
            addd=self.cursor.fetchone()
            address=addd[0]

            if(val==None):
                print("Wrong password")
            else:
                self.customerhome(cust_id,address,lfcsi)

        
        Button(lfcsi,text='Submit',command=submit,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).grid(row=6,column=0)
        
       
    def customerhome(self,cust_id,address,prev):
        prev.destroy()
        lfch=Frame(self.root,height=80,width=160,bg='#04042e')
        lfch.pack()
       
        def search_item():
            lfch.destroy()
         
            
            lfcst=Frame(self.root,height=80,width=160,bg='#04042e')
            lfcst.pack()
            l1=Label(lfcst,text="Enter the item:",font=('bold',18),fg='#67e9f0',bg='#04042e')
            l1.grid(row=0,column=0)

            item=Entry(lfcst,bg='#02021c',fg='#67e9f0')
            item.grid(row=0,column=1)
            def search(item):
                lfcst.destroy()
                lfcsts=Frame(self.root,height=80,width=160,bg='#04042e')
                lfcsts.pack()
                #global lfcsts
                query="SELECT itemid,itemname,price,spec,quantity FROM item WHERE itemname=%s and itemname=%s"
                self.cursor.execute(query,(item,item))
                i=self.cursor.fetchone()
                itemid,itemname,price,spec,quantity=i
                i2=Label(lfcsts,text='{}-{}-{}-{}-{}'.format(itemid,itemname,price,spec,quantity),font=('bold',12),fg='#67e9f0',bg='#04042e')
                i2.pack()
        
                def buy():
                    lfcsts.destroy()
                    lfcstsb=Frame(self.root,height=80,width=160,bg='#04042e')
                    lfcstsb.pack()
                    Label(lfcstsb,text="Available quantity::{}".format(quantity),font=('bold',18),fg='#67e9f0',bg='#04042e').grid(row=0,column=0)
                    self.customer_buy(itemid,cust_id,address,lfcstsb)
                def addtocart():
                    lfcsts.destroy()
                    lfcstsc=Frame(self.root,height=80,width=160,bg='#04042e')
                    lfcstsc.pack()
                    self.customer_add_to_cart(itemid,cust_id,address,lfcstsc)
                def back():
                    self.customerhome(cust_id,address,lfcsts)

                b2=Button(lfcsts,text='Buy',command=buy,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10))
                b2.pack()
                b3=Button(lfcsts,text='Add to cart',command=addtocart,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10))
                b3.pack()
                b4=Button(lfcsts,text='Back',command=back,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10))
                b4.pack()
            def back():
                    self.customerhome(cust_id,address,lfcst)



            b1=Button(lfcst,text='Search',command=lambda:search(item.get()),bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10))
            b1.grid()
            b10=Button(lfcst,text='Back',command=back,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10))
            b10.grid()


            
        def display_item():
            lfch.destroy()
            lfcdt=Frame(self.root,height=80,width=160,bg='#04042e')
            lfcdt.pack()
            Label(lfcdt,text='search item',font=('bold',18),fg='#67e9f0',bg='#04042e').pack()
            lib1=Listbox(lfcdt)
            lib1.pack(pady=20,padx=30)
            query="SELECT itemid,itemname,price FROM item"
            self.cursor.execute(query)
            lst1=self.cursor.fetchall()   
            for item in lst1:
                a,b,c=item
                lib1.insert(END,'>{} - Rs.{} - {}'.format(b,c,a)) 
            def select(lib1,lfcdt):
                lfcdt.destroy()
                lfcdtd=Frame(self.root,height=80,width=160,bg='#04042e')
                lfcdtd.pack()
                lii1=lib1
                lii=lii1.split('-')
                i_id=lii[2].strip()
                query="SELECT itemname,spec,quantity FROM item WHERE itemid=%s and itemid=%s"
                self.cursor.execute(query,(i_id,i_id))
                lst2=self.cursor.fetchone()
                a,b,quantity=lst2
                Label(lfcdtd,text="Product name:{}".format(a),font=('bold',18),fg='#67e9f0',bg='#04042e').pack()
                Label(lfcdtd,text="Specification:{}".format(b),font=('bold',18),fg='#67e9f0',bg='#04042e').pack()
                def buy():
                    lfcdtd.destroy()
                    lfcdtdb=Frame(self.root,height=80,width=160,bg='#04042e')
                    lfcdtdb.pack()
                    Label(lfcdtdb,text="Available quantity::{}".format(quantity),font=('bold',18),fg='#67e9f0',bg='#04042e').grid(row=0,column=0)
                    self.customer_buy(i_id,cust_id,address,lfcdtdb)
                def addtocart():
                    lfcdtd.destroy()
                    lfcdtdc=Frame(self.root,height=80,width=160,bg='#04042e')
                    lfcdtdc.pack()
                    self.customer_add_to_cart(i_id,cust_id,address,lfcdtdc)
                def back():
                    self.customerhome(cust_id,address,lfcdtd)

                b2=Button(lfcdtd,text='Buy',command=buy,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10))
                b2.pack()
                b3=Button(lfcdtd,text='Add to cart',command=addtocart,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10))
                b3.pack()
                b4=Button(lfcdtd,text='Back',command=back,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10))
                b4.pack()
            def back():
                    self.customerhome(cust_id,address,lfcdt)


            Button(lfcdt,text='Select',command=lambda:select(lib1.get(ANCHOR),lfcdt),bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()
            Button(lfcdt,text='Back',command=back,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()
            
            
            
            
           

        def cart():
            lfch.destroy()
            lfch_c=Frame(self.root,bg='#04042e')
            lfch_c.pack()
            Label(lfch_c,text="CART ITEM",font=('bold',25),fg='#67e9f0',bg='#04042e').pack()
            lib2=Listbox(lfch_c)
            lib2.pack()
        
            
            query1="SELECT itemid FROM cart WHERE cust_id=%s and cust_id=%s"
            self.cursor.execute(query1,(cust_id,cust_id))
            lst=self.cursor.fetchall()

            query2="SELECT itemid,itemname,price FROM item WHERE itemid=%s and itemid=%s"
            for i in lst:
                self.cursor.execute(query2,(i[0],i[0]))
                l=self.cursor.fetchone()
            
                a,name,price=l
               
                lib2.insert(END,'>{} - Rs.{} - {}'.format(name,price,a))


            def select(lib2,lfch_c):
                lfch_c.destroy()
                lfch_cs=Frame(self.root,height=80,width=160,bg='#04042e')
                lfch_cs.pack()
                lii1=lib2
                lii=lii1.split('-')
                i_id=lii[2].strip()
                query="SELECT itemname,spec,quantity FROM item WHERE itemid=%s and itemid=%s"
                self.cursor.execute(query,(i_id,i_id))
                lst2=self.cursor.fetchone()
                a,b,quantity=lst2
                Label(lfch_cs,text="Product name:{}".format(a),font=('bold',18),fg='#67e9f0',bg='#04042e').pack()
                Label(lfch_cs,text="Specification:{}".format(b),font=('bold',18),fg='#67e9f0',bg='#04042e').pack()
                def buy():
                    lfch_cs.destroy()
                    lfch_csb=Frame(self.root,height=80,width=160,bg='#04042e')
                    lfch_csb.pack()
                    Label(lfch_csb,text="Available quantity::{}".format(quantity),font=('bold',18),fg='#67e9f0',bg='#04042e').grid(row=0,column=0)
                    self.customer_buy(i_id,cust_id,address,lfch_csb)

                
                    
                
                
                b2=Button(lfch_cs,text='Confirm',command=buy,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10))
                b2.pack()
                
                

            def remove(lib2,liib2):
                lii1=liib2
                lii=lii1.split('-')
                i_id=lii[2].strip()
                lib2.delete(ANCHOR)
                self.customer_remove_from_cart(i_id,cust_id,address,lfch_c)
            def back():
                self.customerhome(cust_id,address,lfch_c)


            Button(lfch_c,text='Buy',command=lambda:select(lib2.get(ANCHOR),lfch_c),bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()
            Button(lfch_c,text='Remove from cart',command=lambda:remove(lib2,lib2.get(ANCHOR)),bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()
            Button(lfch_c,text='Back',command=back,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()

            
        def buyed_product():
            lfch.destroy()
            lfch_bp=Frame(self.root,height=80,width=160,bg='#04042e')
            lfch_bp.pack()
            Label(lfch_bp,text="BUYED PRODUCT",font=('bold',25),fg='#67e9f0',bg='#04042e').pack()
            def back():
                self.customerhome(cust_id,address,lfch_bp)
            Button(lfch_bp,text='back',command=back,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()
            lib3=Listbox(lfch_bp,width=50)
            lib3.pack()
            query1="SELECT itemid,quantity,status FROM buyed_product WHERE cust_id=%s and cust_id=%s"
            self.cursor.execute(query1,(cust_id,cust_id))
            lst1=self.cursor.fetchall()

            for i in lst1:
                itemid,quantity,status=i
                self.customer_status(cust_id,itemid)
                query2="SELECT itemname,price,spec FROM item WHERE itemid=%s and itemid=%s"
                self.cursor.execute(query2,(itemid,itemid))
                lst2=self.cursor.fetchone()
                itemname,price,spec=lst2
                lib3.insert(END,">{} - Rs.{} - ({})".format(itemname,price*quantity,status))
            
            
        def logout():
            self.customer_signin(lfch)
        
        
        Label(lfch,text='HOME PAGE',font=('bold',25),fg='#67e9f0',bg='#04042e').pack()
 
        Button(lfch,text='Search item',command=search_item,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()
        Button(lfch,text='display item',command=display_item,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()
        Button(lfch,text='Cart',command=cart,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()
        Button(lfch,text='Buyed product',command=buyed_product,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()
        Button(lfch,text='Logout',command=logout,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()

        








        
    def customer_buy(self,itemid,cust_id,address,prev):
        def buy(quant):
            prev.destroy()
            prev1=Frame(self.root,height=80,width=160,bg='#04042e')
            prev1.pack()
            delivery_date=date.today()+timedelta(7)
            ordered_date=date.today()
            quantity=int(quant)
            query1="INSERT INTO buyed_product(cust_id,itemid,quantity,address,ordered_date,delivery_Date) VALUES(%s,%s,%s,%s,%s,%s)"
            self.cursor.execute(query1,(cust_id,itemid,quantity,address,ordered_date,delivery_date))
            self.mydb.commit()

            query4="update buyed_product SET status='Not Delivered' where itemid=%s and cust_id=%s"
            self.cursor.execute(query4,(itemid,cust_id))
            self.mydb.commit()
        
            query2="UPDATE item SET quantity=quantity-%s WHERE itemid=%s"
            self.cursor.execute(query2,(quantity,itemid))
            self.mydb.commit()

            query3="SELECT itemname,price FROM item WHERE itemid=%s and itemid=%s"
            self.cursor.execute(query3,(itemid,itemid))
            lst=self.cursor.fetchone()
            itemname,price=lst
            
            lb1=Label(prev1,text="item name:{}".format(itemname),font=('bold',18),fg='#67e9f0',bg='#04042e')
            lb1.pack()
            lb2=Label(prev1,text="total price:{}".format(quantity*price),font=('bold',18),fg='#67e9f0',bg='#04042e')
            lb2.pack()
            lb3=Label(prev1,text="Delivery date:{}".format(delivery_date),font=('bold',18),fg='#67e9f0',bg='#04042e')
            lb3.pack()
            def backtohome1():
                self.customerhome(cust_id,address,prev1)
            Button(prev1,text="Back to Home",command=backtohome1,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()
        
        Label(prev,text="Enter the quantity you want::",font=('bold',18),fg='#67e9f0',bg='#04042e').grid(row=1,column=0)
        quantity=Entry(prev,bg='#02021c',fg='#67e9f0')
        quantity.grid(row=1,column=1)
        b9=Button(prev,text='Submit',command=lambda:buy(quantity.get()),bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10))
        b9.grid()
    

    

    def customer_add_to_cart(self,itemid,cust_id,address,cur_fr):
        query="INSERT INTO cart(itemid,cust_id) VALUES(%s,%s)"
        self.cursor.execute(query,(itemid,cust_id))
        self.mydb.commit()
        Label(cur_fr,text="item added to the cart....",font=('bold',18),fg='#67e9f0',bg='#04042e').pack()
        def backtohome():
            self.customerhome(cust_id,address,cur_fr)
        Button(cur_fr,text='Bact to Home',command=backtohome,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()

    
    def customer_remove_from_cart(self,itemid,cust_id,address,lfch_c):
        query="DELETE FROM cart WHERE itemid=%s and cust_id=%s"
        self.cursor.execute(query,(itemid,cust_id))
        self.mydb.commit()
        Label(lfch_c,text="Item removed from the cart",font=('bold',15),fg='#67e9f0',bg='#04042e').pack()

    def customer_status(self,itemid,cust_id):
        query1="select Delivery_date,ordered_date from buyed_product where itemid=%s and cust_id=%s"
        self.cursor.execute(query1,(itemid,cust_id))
        lst1=self.cursor.fetchone()
        Delivery_date,Ordered_date=lst1
        today=date.today()+timedelta(7)

        if(Delivery_date==today):
            query2="update buyed_product SET status='Delivered' where itemid=%s and cust_id=%s"
            self.cursor.execute(query2,(itemid,cust_id))
            self.mydb.commit()
            

        elif(today>Delivery_date):
            query3="update buyed_product SET status='Delivered' where itemid=%s and cust_id=%s"
            self.cursor.execute(query3,(itemid,cust_id))
            self.mydb.commit()
            

        else:
            query4="update buyed_product SET status='Not Delivered' where itemid=%s and cust_id=%s"
            self.cursor.execute(query4,(itemid,cust_id))
            self.mydb.commit()
        
    
