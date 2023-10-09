from tkinter import *
import math,random,os
from tkinter import messagebox

root=Tk()
root.title("Billing Software")
root.geometry("1350x700+0+0")
bg_color="#074463"
title=Label(root,pady=2,text="Shree Mart",bd=12,bg=bg_color,fg="white",font=("times new roman", 30 ,"bold"),relief=GROOVE).pack(fill=X)


#================Variables=========================
soap = IntVar()
face_cream = IntVar()
face_wash = IntVar()
spray = IntVar()
gell = IntVar()
lotion = IntVar()

rice = IntVar()
food_oil = IntVar()
daal = IntVar()
wheat = IntVar()
sugar = IntVar()
tea = IntVar()

maza = IntVar()
coke = IntVar()
frooti = IntVar()
thumbsup = IntVar()
limca = IntVar()
sprite = IntVar()

cosmetic_price = StringVar()
grocery_price = StringVar()
cold_drink_price = StringVar()

cosmetic_tax = StringVar()
grocery_tax = StringVar()
cold_drink_tax = StringVar()

total_other = StringVar()
tax_cos = StringVar()
tax_groc = StringVar()
tax_other = StringVar()

c_name = StringVar()
c_phon = StringVar()
bill_no = StringVar()
x=random.randint(1000,9999)
bill_no.set(str(x))
search_bill = StringVar()

#================Functions=========================
def total():
    total_cosmetic_price=float((soap.get()*40)+(face_cream.get()*120)+(face_wash.get()*60)+(spray.get()*180)+(gell.get()*140)+(lotion.get()*180))
    cosmetic_price.set("Rs. "+str(total_cosmetic_price))
    c_tax=round((total_cosmetic_price*0.05),2)
    cosmetic_tax.set("Rs. "+str(c_tax))

    total_grocery_price=float((rice.get()*80)+(food_oil.get()*180)+(daal.get()*60)+(wheat.get()*240)+(sugar.get()*45)+(tea.get()*150))
    grocery_price.set("Rs. "+str(total_grocery_price))
    g_tax=round((total_grocery_price*0.1),2)
    grocery_tax.set("Rs. "+str(g_tax))

    total_drinks_price=float((maza.get()*60)+(coke.get()*60)+(frooti.get()*50)+(thumbsup.get()*45)+(limca.get()*40)+(sprite.get()*60))
    cold_drink_price.set("Rs. "+str(total_drinks_price))
    d_tax=round((total_drinks_price*0.05),2)
    cold_drink_tax.set("Rs. "+str(d_tax))

    Total_bill=float(total_cosmetic_price+total_grocery_price+total_drinks_price+c_tax+g_tax+d_tax)
    return Total_bill


def welcome_bill():
    txtarea.delete('1.0',END)
    txtarea.insert(END,"\tWelcome to Shree Mart")
    txtarea.insert(END,f"\n\n Bill Number : {bill_no.get()}")
    txtarea.insert(END,f"\n Customer Name : {c_name.get()}")
    txtarea.insert(END,f"\n Phone Number : {c_phon.get()}")
    txtarea.insert(END,f"\n======================================")
    txtarea.insert(END,f"\n Products\t\tQTY\t\tPrice")
    txtarea.insert(END,f"\n======================================")


def bill_area():
        if c_name.get()=="" or c_phon.get()=="":
            messagebox.showerror("Error","Customer details are must")
        elif cosmetic_price.get()=="Rs. 0.0" and grocery_price.get()=="Rs. 0.0" and cold_drink_price.get()=="Rs. 0.0":
            messagebox.showerror("Error","No Product Purchased")
        else:
            welcome_bill()
        
            if soap.get() != 0:
                txtarea.insert(END,f"\n Bath Soap\t\t{soap.get()}\t\t{soap.get()*40}")
            if face_cream.get() != 0:
                txtarea.insert(END,f"\n Face Cream\t\t{face_cream.get()}\t\t{face_cream.get()*120}")
            if face_wash.get() != 0:
                txtarea.insert(END,f"\n Face Wash\t\t{face_wash.get()}\t\t{face_wash.get()*60}")
            if spray.get() != 0:
                txtarea.insert(END,f"\n Hair Spray\t\t{spray.get()}\t\t{spray.get()*180}")
            if gell.get() != 0 :
                txtarea.insert(END,f"\n Hair Gell\t\t{gell.get()}\t\t{gell.get()*180}")
            if lotion.get() != 0 :
                txtarea.insert(END,f"\n Body Lotion\t\t{lotion.get()}\t\t{lotion.get()*180}")
            
            if rice.get() != 0:
                txtarea.insert(END,f"\n Rice\t\t{rice.get()}\t\t{rice.get()*40}")
            if food_oil.get() != 0:
                txtarea.insert(END,f"\n Food Oil\t\t{food_oil.get()}\t\t{food_oil.get()*120}")
            if daal.get() != 0:
                txtarea.insert(END,f"\n Daal\t\t{daal.get()}\t\t{daal.get()*60}")
            if wheat.get() != 0:
                txtarea.insert(END,f"\n Wheat\t\t{wheat.get()}\t\t{wheat.get()*180}")
            if sugar.get() != 0:
                txtarea.insert(END,f"\n Sugar\t\t{sugar.get()}\t\t{sugar.get()*140}")
            if tea.get() != 0:
                txtarea.insert(END,f"\n Tea\t\t{tea.get()}\t\t{tea.get()*180}")
            
            if maza.get() != 0:
                txtarea.insert(END,f"\n Maza\t\t{maza.get()}\t\t{maza.get()*60}")
            if coke.get() != 0:
                txtarea.insert(END,f"\n Coke\t\t{coke.get()}\t\t{coke.get()*60}")
            if frooti.get() != 0:
                txtarea.insert(END,f"\n Frooti\t\t{frooti.get()}\t\t{frooti.get()*50}")
            if thumbsup.get() != 0:
                txtarea.insert(END,f"\n Thumbs Up\t\t{thumbsup.get()}\t\t{thumbsup.get()*45}")
            if limca.get() != 0:
                txtarea.insert(END,f"\n Limca\t\t{limca.get()}\t\t{limca.get()*40}")
            if sprite.get() != 0:
                txtarea.insert(END,f"\n Sprite\t\t{sprite.get()}\t\t{sprite.get()*60}")
            
            txtarea.insert(END,f"\n======================================")
            if cosmetic_tax != "Rs. 0.0":
                txtarea.insert(END,f"\n Cosmetic Tax\t\t\t  {cosmetic_tax.get()}")
            if grocery_tax != "Rs. 0.0":
                txtarea.insert(END,f"\n Grocery Tax\t\t\t  {grocery_tax.get()}")
            if cold_drink_tax != "Rs. 0.0":
                txtarea.insert(END,f"\n Cold Drinks Tax\t\t\t  {cold_drink_tax.get()}")

            txtarea.insert(END,f"\n======================================")
            txtarea.insert(END,f"\n\t    Total Bill :  Rs. {total()}")
            txtarea.insert(END,f"\n======================================")
            save_bill()
            

def save_bill():
    op = messagebox.askyesno("Save Bill","Do you want to save the Bill?")
    if op > 0:
        bill_data = txtarea.get('1.0',END)
        f1 = open("Bills/"+str(bill_no.get())+".txt","w")
        f1.write(bill_data)
        f1.close()
        messagebox.showinfo("Saved",f"Bill no. : {bill_no.get()} saved successfully")
    else:
        return
    

def find_bill():
    present="no"
    for i in os.listdir("Bills/"):
        if i.split('.')[0]==search_bill.get():
            f1=open(f"Bills/{i}","r")
            txtarea.delete('1.0',END)
            for d in f1:
                txtarea.insert(END,d)
            f1.close()
            present="yes"

    if present == "no":
        messagebox.showinfo("Error","Invalid Bill No.")


def clear_data():
    op = messagebox.askyesno("Clear","Do you really want to clear data?")
    if op > 0:
        soap.set(0)
        face_cream.set(0)
        face_wash.set(0)
        spray.set(0)
        gell.set(0)
        lotion.set(0)

        rice.set(0)
        food_oil.set(0)
        daal.set(0)
        wheat.set(0)
        sugar.set(0)
        tea.set(0)

        maza.set(0)
        coke.set(0)
        frooti.set(0)
        thumbsup.set(0)
        limca.set(0)
        sprite.set(0)

        cosmetic_price.set("")
        grocery_price.set("")
        cold_drink_price.set("")

        cosmetic_tax.set("")
        grocery_tax.set("")
        cold_drink_tax.set("")

        c_name.set("")
        c_phon.set("")
        bill_no.set("")
        x=random.randint(1000,9999)
        bill_no.set(str(x))
        search_bill.set("")
        welcome_bill()


def Exit_app():
    op = messagebox.askyesno("Exit","Do you really want to exit?")
    if op > 0:
        root.destroy()
    






#================Customer Detail Frame=========================
F1=LabelFrame(root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
F1.place(x=0,y=80,relwidth=1)

cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman", 15 ,"bold")).grid(row=0,column=0,padx=20,pady=5)
cname_txt=Entry(F1,width=15,textvariable=c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

cphn_lbl=Label(F1,text="Phone No.",bg=bg_color,fg="white",font=("times new roman", 15 ,"bold")).grid(row=0,column=2,padx=20,pady=5)
cphn_txt=Entry(F1,width=15,textvariable=c_phon,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

c_bill_lbl=Label(F1,text="Bill Number",bg=bg_color,fg="white",font=("times new roman", 15 ,"bold")).grid(row=0,column=4,padx=20,pady=5)
c_bill_txt=Entry(F1,width=15,textvariable=search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

bill_btn=Button(F1,text="Search",command=find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,pady=10,padx=10)

#================Cosmetics Frame=========================
F2=LabelFrame(root,bd=10,relief=GROOVE,text="Cosmetics",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
F2.place(x=5,y=180,width=325,height=380)

bath_lbl=Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
bath_txt=Entry(F2,width=10,textvariable=soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

Face_cream_lbl=Label(F2,text="Face Cream",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
Face_cream_txt=Entry(F2,width=10,textvariable=face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

Face_w_lbl=Label(F2,text="Face Wash",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
Face_w_txt=Entry(F2,width=10,textvariable=face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

Hair_s_lbl=Label(F2,text="Hair Spray",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
Hair_s_txt=Entry(F2,width=10,textvariable=spray,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

Hair_g_lbl=Label(F2,text="Hair Gell",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
Hair_g_txt=Entry(F2,width=10,textvariable=gell,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

Body_lbl=Label(F2,text="Body Lotion",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
Body_txt=Entry(F2,width=10,textvariable=lotion,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

#================Grocery Frame=========================
F3=LabelFrame(root,bd=10,relief=GROOVE,text="Grocery",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
F3.place(x=340,y=180,width=325,height=380)

g1_lbl=Label(F3,text="Rice",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
g1_txt=Entry(F3,width=10,textvariable=rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

g2_lbl=Label(F3,text="Food Oil",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
g2_txt=Entry(F3,width=10,textvariable=food_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

g3_lbl=Label(F3,text="Daal",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
g3_txt=Entry(F3,width=10,textvariable=daal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

g4_lbl=Label(F3,text="Wheat",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
g4_txt=Entry(F3,width=10,textvariable=wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

g5_lbl=Label(F3,text="Sugar",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
g5_txt=Entry(F3,width=10,textvariable=sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

g6_lbl=Label(F3,text="Tea",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
g6_txt=Entry(F3,width=10,textvariable=tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

#================Cold Drink Frame=========================
F4=LabelFrame(root,bd=10,relief=GROOVE,text="Cold Drink",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
F4.place(x=670,y=180,width=325,height=380)

c1_lbl=Label(F4,text="Maza",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
c1_txt=Entry(F4,width=10,textvariable=maza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

c2_lbl=Label(F4,text="Coke",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
c2_txt=Entry(F4,width=10,textvariable=coke,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

c3_lbl=Label(F4,text="Frooti",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
c3_txt=Entry(F4,width=10,textvariable=frooti,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

c4_lbl=Label(F4,text="Thumbs Up",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
c4_txt=Entry(F4,width=10,textvariable=thumbsup,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

c5_lbl=Label(F4,text="Limca",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
c5_txt=Entry(F4,width=10,textvariable=limca,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

c6_lbl=Label(F4,text="Sprite",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
c6_txt=Entry(F4,width=10,textvariable=sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

#================Bill Area=========================
F5=LabelFrame(root,bd=10,relief=GROOVE)
F5.place(x=1010,y=180,width=350,height=380)
bill_title=Label(F5,text='Bill Area',font='arial 15 bold',bd=7,relief=GROOVE).pack(fill=X)
scrol_y=Scrollbar(F5,orient=VERTICAL)
scrol_y.pack(side=RIGHT,fill=Y)
txtarea=Text(F5,yscrollcommand=scrol_y.set)
txtarea.pack(fill=BOTH,expand=1)
scrol_y.config(command=txtarea.yview)

#================Button Frame=========================
F6=LabelFrame(root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),bg=bg_color,fg="gold")
F6.place(x=0,y=560,relwidth=1,height=140)

m1=Label(F6,text="Total Cosmetic Price",font=("times new roman",14,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=20,pady=1,sticky="w")
m1_txt=Entry(F6,width=18,textvariable=cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

m2=Label(F6,text="Total Grocery Price",font=("times new roman",14,"bold"),bg=bg_color,fg="white").grid(row=1,column=0,padx=20,pady=1,sticky="w")
m2_txt=Entry(F6,width=18,textvariable=grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

m3=Label(F6,text="Total Cold Drinks Price",font=("times new roman",14,"bold"),bg=bg_color,fg="white").grid(row=2,column=0,padx=20,pady=1,sticky="w")
m3_txt=Entry(F6,width=18,textvariable=cold_drink_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

c1=Label(F6,text="Cosmetic Tax",font=("times new roman",14,"bold"),bg=bg_color,fg="white").grid(row=0,column=2,padx=20,pady=1,sticky="w")
c1_txt=Entry(F6,width=18,textvariable=cosmetic_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

c2=Label(F6,text="Grocery Tax",font=("times new roman",14,"bold"),bg=bg_color,fg="white").grid(row=1,column=2,padx=20,pady=1,sticky="w")
c2_txt=Entry(F6,width=18,textvariable=grocery_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

c3=Label(F6,text="Cold Drinks Tax",font=("times new roman",14,"bold"),bg=bg_color,fg="white").grid(row=2,column=2,padx=20,pady=1,sticky="w")
c3_txt=Entry(F6,width=18,textvariable=cold_drink_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

btn_F=Frame(F6,bd=7,relief=GROOVE)
btn_F.place(x=750,width=585,height=105)

total_btn=Button(btn_F,text="Total",command=total,bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
GBill_btn=Button(btn_F,text="Generate Bill",command=bill_area,bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5)
Clear_btn=Button(btn_F,text="Clear",command=clear_data,bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5)
Exit_btn=Button(btn_F,text="Exit",command=Exit_app,bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)


root.mainloop()