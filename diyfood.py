from tkinter import*
import tkinter.messagebox
import time
import random

operator = ""

#Defining Main Window
root = Tk()
root.geometry("1600x800+0+0")
root.state('zoomed')
root.title("Restaurant Bill Calculator")
root.configure(bg='LemonChiffon2')


top = Frame(root, width = 1600, height = 50,bg='LemonChiffon2', relief = SUNKEN)
top.pack(side = TOP)

left = Frame(root, width = 800, height = 700,bg='LemonChiffon2', relief = SUNKEN)
left.pack(side = LEFT)

right = Frame(root, width = 300, height = 700, bg='LemonChiffon2',relief = SUNKEN)
right.pack(side = RIGHT)

#Title Name
label_info = Label(top, font = ('arial',50,'bold'), text ="Restaurant Bill Calculator", fg = "steel blue",bg='LemonChiffon2', bd = 10, anchor = 'w')
label_info.grid(row = 0, column = 0)

#Syntax For Time
local_time = time.asctime(time.localtime(time.time()))

label_info = Label(top, font = ('arial',20,'bold'), text = local_time, fg = "steel blue",bg='LemonChiffon2', bd = 10, anchor = 'w')
label_info.grid(row = 1, column = 0)

#Single Variable to be used in the code on which functions are defined
txt_inp = StringVar()

#Adding A Calculator For Extra Aid

#Defining operations for operator buttons

def btn_click(number):
	global operator
	operator = operator+ str(number)
	txt_inp.set(operator)

def fun_clear():
	global operator
	operator = ""
	txt_inp.set(operator)

def calculate():
	global operator
	try:
		sumup = str(eval(operator))
	except Exception as e:
		tkinter.messagebox.showinfo('Error','Incorrect Input')
		sumup = 0
		fun_clear()
	txt_inp.set(sumup)
	operator = ""



#Display box for calculator
txt = Entry(right, font = ('arial',20,'bold'), textvariable = txt_inp, bd = 30, insertwidth = 4, bg = "powderblue", justify = 'right')
txt.grid(columnspan = 4)


#Defining Buttons on the calculator
btn7 = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="7", bg="steel blue", command=lambda: btn_click(7))
btn7.grid(row= 2, column= 0)

btn8 = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="8", bg="steel blue", command=lambda: btn_click(8))
btn8.grid(row= 2, column= 1)

btn9 = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="9", bg="steel blue", command=lambda: btn_click(9))
btn9.grid(row= 2, column= 2)

plus = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="+", bg="steel blue", command=lambda: btn_click("+"))
plus.grid(row= 2, column= 3)



btn4 = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="4", bg="steel blue", command=lambda: btn_click(4))
btn4.grid(row= 3, column= 0)

btn5 = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="5", bg="steel blue", command=lambda: btn_click(5))
btn5.grid(row= 3, column= 1)

btn6 = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="6", bg="steel blue", command=lambda: btn_click(6))
btn6.grid(row= 3, column= 2)

minus = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="-", bg="steel blue", command=lambda: btn_click("-"))
minus.grid(row= 3, column= 3)




btn1 = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="1", bg="steel blue", command=lambda: btn_click(1))
btn1.grid(row= 4, column= 0)

btn2 = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="2", bg="steel blue", command=lambda: btn_click(2))
btn2.grid(row= 4, column= 1)

btn3 = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="3", bg="steel blue", command=lambda: btn_click(3))
btn3.grid(row= 4, column= 2)

multiply = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="*", bg="steel blue", command=lambda: btn_click("*"))
multiply.grid(row= 4, column= 3)



btn0 = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="0", bg="steel blue", command=lambda: btn_click(0))
btn0.grid(row= 5, column= 0)

btn_clear = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="C", bg="steel blue",command=fun_clear)
btn_clear.grid(row= 5, column= 1)

btn_equal = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="=", bg="steel blue",command= calculate)
btn_equal.grid(row= 5, column= 2)

division = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="/", bg="steel blue", command=lambda: btn_click("/"))
division.grid(row= 5, column= 3) 


#Giving different value to the single variable as selected by user
rand = StringVar()
SHAKE_inp = StringVar()
BAR_inp = StringVar()
SALAD_inp = StringVar()
GRILL_inp = StringVar()
total_inp = StringVar()
subtotal_inp = StringVar()
services_inp = StringVar()
tax_inp = StringVar()
cost_inp = StringVar()
PASTA_inp = StringVar() 
STEW_inp = StringVar()

#Main function for taking orders
def ref():
	
	#Defining prices
	SHAKE_p = 200
	BAR_p = 100
	SALAD_p = 100
	GRILL_p = 50
	PASTA_p = 250
	STEW_p = 200
	
                #Generating Random Ref. ID
	x = random.randint(23133,33344)
	random_ref = str(x)
	rand.set(random_ref)

	#Defining to Input Quantity of Shake required
	try:
		if SHAKE_inp.get() == "":
			CoF = 0
		else:
			CoF = float(SHAKE_inp.get())*SHAKE_p
	#Defining Error Message within tkinter window itself
	except Exception as e:
		tkinter.messagebox.showinfo('Error','Incorrect Input')
		SHAKE_inp.set("")

                #Defining inputs for every item
		
	try:	
		if BAR_inp.get() == "":
			CoS = 0
		else:
			CoS = float(BAR_inp.get())*BAR_p
	except Exception as e:
		tkinter.messagebox.showinfo('Error','Incorrect Input')
		BAR_inp.set("")
	
	try:
		if SALAD_inp.get() == "":
			CoB = 0
		else:
			CoB = float(SALAD_inp.get())*SALAD_p
	except Exception as e:
		tkinter.messagebox.showinfo('Error','Incorrect Input')
		SALAD_inp.set("")

	try:
		if GRILL_inp.get() == "":
			CoD = 0
		else:
			CoD = float(GRILL_inp.get())*GRILL_p
	except Exception as e:
		tkinter.messagebox.showinfo('Error','Incorrect Input')
		GRILL_inp.set("")

	try:
		if PASTA_inp.get() == "":
			CoP = 0
		else:
			CoP = float(PASTA_inp.get())*PASTA_p
	except Exception as e:
		tkinter.messagebox.showinfo('Error','Incorrect Input')
		PASTA_inp.set("")

	try:
		if STEW_inp.get() == "":
			CoC = 0
		else:
			CoC = float(STEW_inp.get())*STEW_p
	except Exception as e:	
		tkinter.messagebox.showinfo('Error','Incorrect Input')
		STEW_inp.set("")

	#Total Cost,Tax,Charges,etc using values given by user

	CostOfMeal = (CoF+CoS+CoB+CoD+CoP+CoC)
	
	PayTax = (CostOfMeal)*0.09
	ServiceCharge = (CostOfMeal)*0.09 	
	totalTax = PayTax + ServiceCharge
	totalCost = (CostOfMeal + PayTax + ServiceCharge)

                #Setting results till 2 decimal places
	services_inp.set(str('%.2f' % (ServiceCharge)))
	tax_inp.set(str('%.2f' % (PayTax)))
	subtotal_inp.set(str('%.2f' % (CostOfMeal)))
	total_inp.set(str('%.2f' % (totalCost)))
	cost_inp.set(str('%.2f' % (totalTax)))
	 		

#Defining function to quit Cafe window
def bck():
	root.destroy()
	import menu


#Defining function to quit the program
def qexit():
	root.destroy()

#For new order
def reset():
	rand.set("")
	SHAKE_inp.set("")
	BAR_inp.set("")
	SALAD_inp.set("")
	GRILL_inp.set("")
	total_inp.set("")
	subtotal_inp.set("")
	services_inp.set("")
	tax_inp.set("")
	cost_inp.set("")
	PASTA_inp.set("")
	STEW_inp.set("")

#New Window for displaying prices of items
def price():
    roo = Tk()
    roo.geometry("450x300")
    roo.title("Price List")
        
    #Labels for each item and its price
    
    lblinfo = Label(roo, font=('arial', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('arial', 15,'bold'), text="_____________", fg="white", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('arial', 15, 'bold'), text="PRICE", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('arial', 15, 'bold'), text="SHAKE", fg="red", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('arial', 15, 'bold'), text="200", fg="red", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('arial', 15, 'bold'), text="BAR ", fg="red", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('arial', 15, 'bold'), text="100", fg="red", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('arial', 15, 'bold'), text="SALAD", fg="red", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('arial', 15, 'bold'), text="100", fg="red", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('arial', 15, 'bold'), text="GRILL", fg="red", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('arial', 15, 'bold'), text="50", fg="red", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('arial', 15, 'bold'), text="PASTA", fg="red", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('arial', 15, 'bold'), text="250", fg="red", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('arial', 15, 'bold'), text="STEW", fg="red", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('arial', 15, 'bold'), text="200", fg="red", anchor=W)
    lblinfo.grid(row=6, column=3)
    roo.mainloop()


#Defining Label+Input for each item
customer_number = Label(left, font=('arial',16,'bold'),text = "Reference Id", bd = 16, anchor = 'w',bg='LemonChiffon2',fg='steel blue')
customer_number.grid(row=0,column=0,sticky = E)
txt_customer = Entry(left,font=('arial',16,'bold'), textvariable=rand, bd=10, insertwidth =4,bg = "gray65", justify ='right', state=DISABLED)
txt_customer.grid(row=0,column=1)

SHAKE = Label(left, font=('arial',16,'bold'),text = "SHAKE", bd = 16, anchor = 'w' ,bg='LemonChiffon2',fg='steel blue')
SHAKE.grid(row=1,column=0,sticky = E)
txt_SHAKE = Entry(left,font=('arial',16,'bold'), textvariable=SHAKE_inp, bd=10, insertwidth =4,bg = "steel blue", justify ='right')
txt_SHAKE.grid(row=1,column=1)

BAR = Label(left, font=('arial',16,'bold'),text = "BAR", bd = 16, anchor = 'w' ,bg='LemonChiffon2',fg='steel blue')
BAR.grid(row=2,column=0,sticky = E)
txt_BAR = Entry(left,font=('arial',16,'bold'), textvariable=BAR_inp, bd=10, insertwidth =4,bg = "steel blue", justify ='right')
txt_BAR.grid(row=2,column=1)


SALAD = Label(left, font=('arial',16,'bold'),text = "SALAD", bd = 16, anchor = 'w' ,bg='LemonChiffon2',fg='steel blue')
SALAD.grid(row=3,column=0,sticky = E)
txt_SALAD = Entry(left,font=('arial',16,'bold'), textvariable=SALAD_inp, bd=10, insertwidth =4,bg = "steel blue", justify ='right')
txt_SALAD.grid(row=3,column=1)

GRILL = Label(left, font=('arial',16,'bold'),text = "GRILL", bd = 16, anchor = 'w',bg='LemonChiffon2',fg='steel blue' )
GRILL.grid(row=4,column=0,sticky = E)
txt_GRILL = Entry(left,font=('arial',16,'bold'), textvariable=GRILL_inp, bd=10, insertwidth =4,bg = "steel blue", justify ='right')
txt_GRILL.grid(row=4,column=1)

PASTA = Label(left, font=('arial',16,'bold'),text = "PASTA", bd = 16, anchor = 'w',bg='LemonChiffon2',fg='steel blue' )
PASTA.grid(row=5,column=0,sticky = E)
txt_PASTA = Entry(left,font=('arial',16,'bold'), textvariable=PASTA_inp, bd=10, insertwidth =4,bg = "steel blue", justify ='right')
txt_PASTA.grid(row=5,column=1)

STEW = Label(left, font=('arial',16,'bold'),text = "STEW", bd = 16, anchor = 'w' ,bg='LemonChiffon2',fg='steel blue')
STEW.grid(row=0,column=2,sticky = E)
txt_STEW = Entry(left,font=('arial',16,'bold'), textvariable=STEW_inp, bd=10, insertwidth =4,bg = "steel blue", justify ='right')
txt_STEW.grid(row=0,column=3)

subtotal = Label(left, font=('arial',16,'bold'),text = "Cost of Meal", bd = 16, anchor = 'w' ,bg='LemonChiffon2',fg='steel blue')
subtotal.grid(row=1,column=2,sticky = E)
txt_subtotal = Entry(left,font=('arial',16,'bold'), textvariable=subtotal_inp, bd=10, insertwidth =4,bg = "gray65", justify ='right', state=DISABLED)
txt_subtotal.grid(row=1,column=3)

services = Label(left, font=('arial',16,'bold'),text = "Service Charge", bd = 16, anchor = 'w',bg='LemonChiffon2',fg='steel blue' )
services.grid(row=2,column=2,sticky = E)
txt_services = Entry(left,font=('arial',16,'bold'), textvariable=services_inp, bd=10, insertwidth =4,bg = "gray65", justify ='right', state=DISABLED)
txt_services.grid(row=2,column=3)

tax = Label(left, font=('arial',16,'bold'),text = "GST", bd = 16, anchor = 'w' ,bg='LemonChiffon2',fg='steel blue')
tax.grid(row=3,column=2,sticky = E)
txt_tax = Entry(left,font=('arial',16,'bold'), textvariable=tax_inp, bd=10, insertwidth =4,bg = "gray65", justify ='right', state=DISABLED)
txt_tax.grid(row=3,column=3)

cost = Label(left, font=('arial',16,'bold'),text = "Total Tax", bd = 16, anchor = 'w' ,bg='LemonChiffon2',fg='steel blue')
cost.grid(row=4,column=2,sticky = E)
txt_cost = Entry(left,font=('arial',16,'bold'), textvariable=cost_inp, bd=10, insertwidth =4,bg = "gray65", justify ='right', state=DISABLED)
txt_cost.grid(row=4,column=3)

total = Label(left, font=('arial',16,'bold'),text = "Total Cost", bd = 16, anchor = 'w',bg='LemonChiffon2',fg='steel blue' )
total.grid(row=5,column=2,sticky = E)
txt_total = Entry(left,font=('arial',16,'bold'), textvariable=total_inp, bd=10, insertwidth =4,bg = "gray65", justify ='right', state=DISABLED)
txt_total.grid(row=5,column=3) 



#Defining Buttons for each specific funtion
btn_total = Button(left, padx= 16, pady= 8, bd= 16, fg= "black", font=('arial',16,'bold'), width=10, text= "Total", bg= "steel blue",command = ref)
btn_total.grid(row=7, column= 1)

btn_reset = Button(left, padx= 16, pady= 8, bd= 16, fg= "black", font=('arial',16,'bold'), width=10, text= "Reset", bg= "steel blue",command = reset)
btn_reset.grid(row=7, column= 2)

btn_exit = Button(left, padx= 16, pady= 8, bd= 16, fg= "black", font=('arial',16,'bold'), width=10, text= "Exit", bg= "steel blue",command = qexit)
btn_exit.grid(row=8, column= 3)

btn_bck = Button(left, padx= 16, pady= 8, bd= 16, fg= "black", font=('arial',16,'bold'), width=10, text= "Back", bg= "steel blue",command = bck)
btn_bck.grid(row=8, column= 2)

btn_price = Button(left, padx= 16, pady= 8, bd= 16, fg= "black", font=('arial',16,'bold'), width=10, text= "Price", bg= "steel blue",command = price)
btn_price.grid(row=7, column= 3)


root.mainloop()

