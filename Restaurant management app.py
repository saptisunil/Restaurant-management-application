from tkinter import*
import random
import time

root = Tk()
root.geometry("1600x700+0+0")
root.title("Restaurant Management System")

Tops = Frame(root,bg="white",width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width = 900,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root ,width = 400,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)

localtime=time.asctime(time.localtime(time.time()))

lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="RESTAURANT MANAGEMENT SYSTEM",fg="Indian Red",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)
lblinfo = Label(Tops, font=( 'aria' ,20, ),text=localtime,fg="Indian Red",anchor=W)
lblinfo.grid(row=1,column=0)

text_Input=StringVar()
operator =""

txtdisplay = Entry(f2,font=('ariel' ,20,'bold'), textvariable=text_Input , bd=5 ,insertwidth=7 ,bg="white",justify='right')
txtdisplay.grid(columnspan=4)

def  btnclick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def clrdisplay():
    global operator
    operator=""
    text_Input.set("")

def eqals():
    global operator
    sumup=str(eval(operator))

    text_Input.set(sumup)
    operator = ""

def Ref():
    x=random.randint(12980, 50876)
    randomRef = str(x)
    rand.set(randomRef)

    cof =float(chickenbiriyani.get())
    colfries= float(thaimeal.get())
    cob= float(friedrice.get())
    cofi= float(gingerchicken.get())
    cochee= float(chillichicken.get())
    codr= float(Drinks.get())

    costoffries = cof*25
    costoflargefries = colfries*40
    costofburger = cob*35
    costoffilet = cofi*50
    costofcheeseburger = cochee*50
    costofdrinks = codr*35

    costofmeal = "Rs.",str('%.2f'% (costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks))
    PayTax=((costoffries +  costoflargefries + costofburger + costoffilet +  costofcheeseburger + costofdrinks)*0.33)
    Totalcost=(costoffries +  costoflargefries + costofburger + costoffilet  + costofcheeseburger + costofdrinks)
    Ser_Charge=((costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks)/99)
    Service="Rs.",str('%.2f'% Ser_Charge)
    OverAllCost="Rs.",str( PayTax + Totalcost + Ser_Charge)
    PaidTax="Rs.",str('%.2f'% PayTax)

    Service_Charge.set(Service)
    cost.set(costofmeal)
    Tax.set(PaidTax)
    Subtotal.set(costofmeal)
    Total.set(OverAllCost)


def qexit():
    root.destroy()

def reset():
    rand.set("")
    chickenbiriyani.set("")
    thaimeal.set("")
    friedrice.set("")
    gingerchicken.set("")
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    cost.set("")
    chillichicken.set("")


btn7=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="7",bg="light coral", command=lambda: btnclick(7) )
btn7.grid(row=2,column=0)

btn8=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="8",bg="light coral", command=lambda: btnclick(8) )
btn8.grid(row=2,column=1)

btn9=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="9",bg="light coral", command=lambda: btnclick(9) )
btn9.grid(row=2,column=2)

Addition=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="+",bg="light coral", command=lambda: btnclick("+") )
Addition.grid(row=2,column=3)

btn4=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="4",bg="light coral", command=lambda: btnclick(4) )
btn4.grid(row=3,column=0)

btn5=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="5",bg="light coral", command=lambda: btnclick(5) )
btn5.grid(row=3,column=1)

btn6=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="6",bg="light coral", command=lambda: btnclick(6) )
btn6.grid(row=3,column=2)

Substraction=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="-",bg="light coral", command=lambda: btnclick("-") )
Substraction.grid(row=3,column=3)

btn1=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="1",bg="light coral", command=lambda: btnclick(1) )
btn1.grid(row=4,column=0)

btn2=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="2",bg="light coral", command=lambda: btnclick(2) )
btn2.grid(row=4,column=1)

btn3=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="3",bg="light coral", command=lambda: btnclick(3) )
btn3.grid(row=4,column=2)

multiply=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="*",bg="light coral", command=lambda: btnclick("*") )
multiply.grid(row=4,column=3)

btn0=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="0",bg="light coral", command=lambda: btnclick(0) )
btn0.grid(row=5,column=0)

btnc=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="c",bg="light coral", command=clrdisplay)
btnc.grid(row=5,column=1)

btnequal=Button(f2,padx=16,pady=16,bd=4,width = 16, fg="white", font=('ariel', 20 ,'bold'),text="=",bg="light coral",command=eqals)
btnequal.grid(columnspan=4)

Decimal=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text=".",bg="light coral", command=lambda: btnclick(".") )
Decimal.grid(row=5,column=2)

Division=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="/",bg="light coral", command=lambda: btnclick("/") )
Division.grid(row=5,column=3)
status = Label(f2,fg="white",font=('aria', 15, 'bold'),width = 16, text="-By Sapti Sunil",bg="light coral",bd=2,relief=SUNKEN)
status.grid(row=7,columnspan=3)

rand = StringVar()
chickenbiriyani = StringVar()
thaimeal = StringVar()
friedrice = StringVar()
gingerchicken = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
cost = StringVar()
chillichicken = StringVar()


lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="Order No.",fg="Indian Red",bd=10,anchor='w')
lblreference.grid(row=0,column=0)
txtreference = Entry(f1,font=('ariel' ,16,'bold'), textvariable=rand , bd=6,insertwidth=4,bg="light coral" ,justify='right')
txtreference.grid(row=0,column=1)

lblfries = Label(f1, font=( 'aria' ,16, 'bold' ),text="Chicken Biriyani",fg="Indian Red",bd=10,anchor='w')
lblfries.grid(row=1,column=0)
txtfries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=chickenbiriyani , bd=6,insertwidth=4,bg="light coral" ,justify='right')
txtfries.grid(row=1,column=1)

lblLargefries = Label(f1, font=( 'aria' ,16, 'bold' ),text="Thai Meal",fg="Indian Red",bd=10,anchor='w')
lblLargefries.grid(row=2,column=0)
txtLargefries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=thaimeal , bd=6,insertwidth=4,bg="light coral" ,justify='right')
txtLargefries.grid(row=2,column=1)


lblburger = Label(f1, font=( 'aria' ,16, 'bold' ),text="Fried Rice",fg="Indian Red",bd=10,anchor='w')
lblburger.grid(row=3,column=0)
txtburger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=friedrice , bd=6,insertwidth=4,bg="light coral" ,justify='right')
txtburger.grid(row=3,column=1)

lblFilet = Label(f1, font=( 'aria' ,16, 'bold' ),text="Ginger Chicken",fg="Indian Red",bd=10,anchor='w')
lblFilet.grid(row=4,column=0)
txtFilet = Entry(f1,font=('ariel' ,16,'bold'), textvariable=gingerchicken , bd=6,insertwidth=4,bg="light coral" ,justify='right')
txtFilet.grid(row=4,column=1)

lblCheese_burger = Label(f1, font=( 'aria' ,16, 'bold' ),text="Chilli Chicken",fg="Indian Red",bd=10,anchor='w')
lblCheese_burger.grid(row=5,column=0)
txtCheese_burger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=chillichicken , bd=6,insertwidth=4,bg="light coral" ,justify='right')
txtCheese_burger.grid(row=5,column=1)


lblDrinks = Label(f1, font=( 'aria' ,16, 'bold' ),text="Drinks",fg="Indian Red",bd=10,anchor='w')
lblDrinks.grid(row=0,column=2)
txtDrinks = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Drinks , bd=6,insertwidth=4,bg="light coral" ,justify='right')
txtDrinks.grid(row=0,column=3)

lblcost = Label(f1, font=( 'aria' ,16, 'bold' ),text="Cost",fg="Indian Red",bd=10,anchor='w')
lblcost.grid(row=1,column=2)
txtcost = Entry(f1,font=('ariel' ,16,'bold'), textvariable=cost , bd=6,insertwidth=4,bg="light coral" ,justify='right')
txtcost.grid(row=1,column=3)

lblService_Charge = Label(f1, font=( 'aria' ,16, 'bold' ),text="Service Charge",fg="Indian Red",bd=10,anchor='w')
lblService_Charge.grid(row=2,column=2)
txtService_Charge = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Service_Charge , bd=6,insertwidth=4,bg="light coral" ,justify='right')
txtService_Charge.grid(row=2,column=3)

lblTax = Label(f1, font=( 'aria' ,16, 'bold' ),text="Tax",fg="Indian Red",bd=10,anchor='w')
lblTax.grid(row=3,column=2)
txtTax = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Tax , bd=6,insertwidth=4,bg="light coral" ,justify='right')
txtTax.grid(row=3,column=3)

lblSubtotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Subtotal",fg="Indian Red",bd=10,anchor='w')
lblSubtotal.grid(row=4,column=2)
txtSubtotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Subtotal , bd=6,insertwidth=4,bg="light coral" ,justify='right')
txtSubtotal.grid(row=4,column=3)

lblTotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Total",fg="Indian Red",bd=10,anchor='w')
lblTotal.grid(row=5,column=2)
txtTotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Total , bd=6,insertwidth=4,bg="light coral" ,justify='right')
txtTotal.grid(row=5,column=3)

lblTotal = Label(f1,text="---------------------",fg="white")
lblTotal.grid(row=6,columnspan=3)

btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="light coral",command=Ref)
btnTotal.grid(row=7, column=1)

btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="light coral",command=reset)
btnreset.grid(row=7, column=2)

btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="light coral",command=qexit)
btnexit.grid(row=7, column=3)

def price():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Price List")
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15,'bold'), text="_____________", fg="white", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Chicken Biriyani", fg="salmon", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="100", fg="salmon", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Thai Meal", fg="salmon", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="160", fg="salmon", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Fried Rice", fg="salmon", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="90", fg="salmon", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Ginger Chicken", fg="salmon", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="60", fg="salmon", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Chilli Chicken", fg="salmon", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="60", fg="salmon", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Drinks", fg="salmon", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="salmon", anchor=W)
    lblinfo.grid(row=6, column=3)

    roo.mainloop()

btnprice=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="MENU", bg="light coral",command=price)
btnprice.grid(row=7, column=0)

root.mainloop()
