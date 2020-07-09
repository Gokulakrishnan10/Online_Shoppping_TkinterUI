from datetime import date,timedelta
from tkinter import * 
from tkinter import messagebox
class Admin:
    def __init__(self,cursor,mydb,root):
        self.cursor=cursor
        self.mydb=mydb
        self.root=root

    def admin_signin(self,lfa):
        lfa.destroy()
        lfas=Frame(self.root,height=80,width=160,bg='#04042e')
        lfas.pack()
        Label(lfas,text='ADMIN',font=('bold',35),fg='#67e9f0',bg='#04042e').grid()
        Label(lfas,text='SIGNIN PAGE',font=('bold',25),fg='#67e9f0',bg='#04042e').grid()
        Label(lfas,text='Enter your name:',font=('bold',18),fg='#67e9f0',bg='#04042e').grid(row=2,column=0)
        Label(lfas,text='Enter the password',font=('bold',18),fg='#67e9f0',bg='#04042e').grid(row=3,column=0)
        name=Entry(lfas,bg='#02021c',fg='#67e9f0')
        password=Entry(lfas,bg='#02021c',fg='#67e9f0')
        name.grid(row=2,column=1)
        password.grid(row=3,column=1)
        def submit():
            query="SELECT name,password FROM admin WHERE name=%s and password=%s"
            self.cursor.execute(query,(name.get(),password.get()))
            val=self.cursor.fetchone()

    
            if(val==None):
                messagebox.showinfo('Unsuccessful signin','please Enter valid username and password')
                
            else:
                self.admin_home(lfas)
        Button(lfas,text='Submit',command=submit,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).grid(row=6,column=0)


    def admin_home(self,prev):
        prev.destroy()
        lfah=Frame(self.root,height=80,width=160,bg='#04042e')
        lfah.pack()

        def change_product():
            lfah.destroy()
            lfacp=Frame(self.root,height=80,width=160,bg='#04042e')
            lfacp.pack()
            self.admin_product(lfacp)
            

        def change_quantity():
            lfah.destroy()
            lfacq=Frame(self.root,height=80,width=160,bg='#04042e')
            lfacq.pack()
            self.admin_quantity(lfacq)
        def view_product():
            lfah.destroy()
            lfavp=Frame(self.root,height=80,width=160,bg='#04042e')
            lfavp.pack()
            self.admin_view_product(lfavp)
            
        def view_customer():
            lfah.destroy()
            lfavc=Frame(self.root,height=80,width=160,bg='#04042e')
            lfavc.pack()
            self.admin_view_customer(lfavc)
            
        def logout():
            self.admin_signin(lfah)

        Label(lfah,text='HOME PAGE',font=('bold',25),fg='#67e9f0',bg='#04042e').pack()
 
        Button(lfah,text='Changing product',command=change_product,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()
        Button(lfah,text='Changing quantity',command=change_quantity,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()
        Button(lfah,text='View product',command=view_product,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()
        Button(lfah,text='View customer',command=view_customer,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()
        Button(lfah,text='Logout',command=logout,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()

        
        
       



        
    
    def admin_product(self,cur):
        lib1=Listbox(cur)
        lib1.pack()

        query="SELECT itemid,itemname,quantity,price FROM item"
        self.cursor.execute(query)
        lst=self.cursor.fetchall()   
        for item in lst:
            a,b,c,d=item
            lib1.insert(END,'+{} - {} - {} - Rs{}'.format(a,b,c,d))

        def add_product():
            cur.destroy()
            lfa_ap=Frame(self.root,height=80,width=160,bg='#04042e')
            lfa_ap.pack()
            Label(lfa_ap,text='Enter the item ID:',font=('bold',18),fg='#67e9f0',bg='#04042e').grid(row=1,column=0)
            Label(lfa_ap,text='Enter the item name:',font=('bold',18),fg='#67e9f0',bg='#04042e').grid(row=2,column=0)
            Label(lfa_ap,text='Enter price of the item:',font=('bold',18),fg='#67e9f0',bg='#04042e').grid(row=3,column=0)
            Label(lfa_ap,text='Enter item specificaiton:',font=('bold',18),fg='#67e9f0',bg='#04042e').grid(row=4,column=0)
            Label(lfa_ap,text='Enter the quantity:',font=('bold',18),fg='#67e9f0',bg='#04042e').grid(row=5,column=0)

            itemid=Entry(lfa_ap,bg='#02021c',fg='#67e9f0')
            itemid.grid(row=1,column=1) 
            itemname=Entry(lfa_ap,bg='#02021c',fg='#67e9f0')
            itemname.grid(row=2,column=1)
            price=Entry(lfa_ap,bg='#02021c',fg='#67e9f0')
            price.grid(row=3,column=1)
            spec=Entry(lfa_ap,bg='#02021c',fg='#67e9f0')
            spec.grid(row=4,column=1)
            quantity=Entry(lfa_ap,bg='#02021c',fg='#67e9f0')
            quantity.grid(row=5,column=1)
            def submit():
                #lfa_ap.destroy()
                #lfa_ap=Frame(self.root,height=80,width=160,bg='#04042e')
                #lfa_ap.pack()
               # price=int(price.get())
                #quantity=int(quantity.get())
                query="INSERT INTO item(itemid,itemname,price,spec,quantity) VALUES(%s,%s,%s,%s,%s)"
                self.cursor.execute(query,(itemid.get(),itemname.get(),int(price.get()),spec.get(),int(quantity.get())))
                self.mydb.commit()
                def back():
                    self.admin_home(lfa_ap)

                Label(lfa_ap,text="added succesfully",font=('bold',15),fg='#67e9f0',bg='#04042e').grid()
                Button(lfa_ap,text="Back to Home",command=back,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).grid()
                


            Button(lfa_ap,text='submit',command=submit,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).grid()
            
        def remove_product():
            cur.destroy()
            lfa_rp=Frame(self.root,height=80,width=160,bg='#04042e')
            lfa_rp.pack()
            lib2=Listbox(lfa_rp)
            lib2.pack()
            query="SELECT itemid,itemname,quantity,price FROM item"
            self.cursor.execute(query)
            lst=self.cursor.fetchall()   
            for item in lst:
                a,b,c,d=item
                lib2.insert(END,'+{} - {} - Rs{} - {}'.format(b,c,d,a))

            def remove(lib2,liib2):
                lii1=liib2
                lii=lii1.split('-')
                itemid=lii[3].strip()
                lib2.delete(ANCHOR)
                query="DELETE FROM item WHERE itemid=%s and itemid=%s"
                self.cursor.execute(query,(itemid,itemid))
                self.mydb.commit()
                Label(lfa_rp,text="Removed successfully",font=('bold',15),fg='#67e9f0',bg='#04042e').pack()
                
            def backtohome():
                self.admin_home(lfa_rp)


            Button(lfa_rp,text='Remove',command=lambda:remove(lib2,lib2.get(ANCHOR)),bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()
            Button(lfa_rp,text='Back to Home',command=backtohome,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()

        def back():
            self.admin_home(cur)


        Button(cur,text='Add product',command=add_product,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()
        Button(cur,text='Remove product',command=remove_product,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()
        Button(cur,text='Back',command=back,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()
       










    def admin_quantity(self,cur):
        lib3=Listbox(cur)
        lib3.pack()
        query="SELECT itemid,itemname,quantity FROM item"
        self.cursor.execute(query)
        lst=self.cursor.fetchall()   
        for item in lst:
            a,b,c=item
            lib3.insert(END,'>{} - {} - {}'.format(c,b,a))

        def add_quantity():
            cur.destroy()
            lfa_aq=Frame(self.root,height=80,width=160,bg='#04042e')
            lfa_aq.pack()
            lib4=Listbox(lfa_aq)
            lib4.pack()
            query="SELECT itemid,itemname,quantity FROM item"
            self.cursor.execute(query)
            lst=self.cursor.fetchall()   
            for item in lst:
                a,b,c=item
                lib4.insert(END,'>{} - {} - {}'.format(c,b,a))
            def select(lii):
                lii1=lii.split('-')
                itemid=lii1[2].strip()
                Label(lfa_aq,text="Enter the number of quantity:",font=('bold',18),fg='#67e9f0',bg='#04042e').pack()
                aq=Entry(lfa_aq,bg='#02021c',fg='#67e9f0')
                aq.pack()
                def add():
                    query="UPDATE item SET quantity=quantity+%s WHERE itemid=%s"
                    self.cursor.execute(query,(aq.get(),itemid))
                    self.mydb.commit()
                    Label(lfa_aq,text=aq.get()+" item added successfully",font=('bold',15),fg='#67e9f0',bg='#04042e').pack()
                    def refresh():
                        self.admin_home(lfa_aq)
                    Button(lfa_aq,text='Back',command=refresh,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()
                    

                Button(lfa_aq,text='add',command=add,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()   
              
            def back():
                self.admin_home(lfa_aq)


            Button(lfa_aq,text='select',command=lambda:select(lib4.get(ANCHOR)),bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()
            Button(lfa_aq,text='Back',command=back,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()
            

        def remove_quantity():
            cur.destroy()
            lfa_rq=Frame(self.root,height=80,width=160,bg='#04042e')
            lfa_rq.pack()
            lib5=Listbox(lfa_rq)
            lib5.pack()
            query="SELECT itemid,itemname,quantity FROM item"
            self.cursor.execute(query)
            lst=self.cursor.fetchall()   
            for item in lst:
                a,b,c=item
                lib5.insert(END,'>{} - {} - {}'.format(c,b,a))
            
            def select(lii):
                lii1=lii.split('-')
                itemid=lii1[2].strip()
                Label(lfa_rq,text="Enter the number of quantity:",font=('bold',18),fg='#67e9f0',bg='#04042e').pack()
                rq=Entry(lfa_rq,bg='#02021c',fg='#67e9f0')
                rq.pack()
                def remove():
                    query="UPDATE item SET quantity=quantity-%s WHERE itemid=%s"
                    self.cursor.execute(query,(rq.get(),itemid))
                    self.mydb.commit()
                    Label(lfa_rq,text=rq.get()+" item removed successfully",font=('bold',15),fg='#67e9f0',bg='#04042e').pack()
                    def refresh():
                        self.admin_home(lfa_rq)
                    Button(lfa_rq,text='Back',command=refresh,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()

                Button(lfa_rq,text='remove',command=remove,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()
           #q="SELECT item_name FROM product WHERE item_id=%s and item_id=%s"
           #self.cursor.execute(q,(item_id,item_id))
           #i=self.cursor.fetchone()
           #prod_name=i[0]
           #choice=input('sure this ({}) product [yes/no]? '.format(prod_name))
           #if(choice=='yes' or choice=='y'):
            #elif(choice=='no' or choice=='n'):
           #    self.admin_quantity()
            Button(lfa_rq,text='select',command=lambda:select(lib5.get(ANCHOR)),bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()
            Button(lfa_rq,text='Back',command=back,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()



        def back():
            self.admin_home(cur)

        Button(cur,text='Add quantity',command=add_quantity,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()
        Button(cur,text='Remove quantity',command=remove_quantity,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()
        Button(cur,text='back',command=back,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()





    def admin_view_product(self,cur):
        lib6=Listbox(cur)
        lib6.pack()
        query="SELECT itemid,itemname,quantity FROM item"
        self.cursor.execute(query)
        lst=self.cursor.fetchall()   
        for item in lst:
            a,b,c=item
            lib6.insert(END,'>{} - {} - {}'.format(a,b,c))
        def back():
            self.admin_home(cur)

        Button(cur,text='Back',command=back,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()

    def admin_view_customer(self,cur):
        lib6=Listbox(cur)
        lib6.pack()
        query1="SELECT cust_id,name FROM customer"
        self.cursor.execute(query1)
        lst1=self.cursor.fetchall()
        for i in lst1:
            id,name=i
            lib6.insert(END,">{} - {}".format(name,id))

        def select(liii):
            cur.destroy()
            lfa_vc=Frame(self.root,height=80,width=160,bg='#04042e')
            lfa_vc.pack()
            liii1=liii.split('-')
            cust_id=liii1[1].strip()
            def backtohome():
                self.admin_home(lfa_vc)
            query2="SELECT name,phone_no,address FROM customer WHERE cust_id=%s and cust_id=%s"
            self.cursor.execute(query2,(cust_id,cust_id))
            lst2=self.cursor.fetchone()
            name,phone_no,address=lst2
            Label(lfa_vc,text="Name:{}".format(name),font=('bold',18),fg='#67e9f0',bg='#04042e').pack()
            Label(lfa_vc,text="Phone Number:{}".format(phone_no),font=('bold',18),fg='#67e9f0',bg='#04042e').pack()
            Label(lfa_vc,text="Address:{}".format(address),font=('bold',18),fg='#67e9f0',bg='#04042e').pack()
            Button(lfa_vc,text='Back to Home',command=backtohome,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()
            lib7=Listbox(lfa_vc,width=60)
            lib7.pack()
            query3="SELECT itemid,quantity,delivery_date FROM buyed_product WHERE cust_id=%s and cust_id=%s"
            self.cursor.execute(query3,(cust_id,cust_id))
            lst3=self.cursor.fetchall()
            for i in lst3:
                itemid,quantity,delivery_date=i
                query4='SELECT itemname,price FROM item WHERE itemid=%s and itemid=%s'
                self.cursor.execute(query4,(itemid,itemid))
                lst4=self.cursor.fetchone()
                itemname,price=lst4
                lib7.insert(END,'Item:{}-Qn:{}-Tot.Rs:{}'.format(itemname,quantity,quantity*price))
            
            
            
                
            
        def back():
            self.admin_home(cur)

            
        
        Button(cur,text='Select',command=lambda:select(lib6.get(ANCHOR)),bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()
        Button(cur,text='Back',command=back,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()
       
        
        
