from tkinter import  *


def bclick(number):
	global operator
	operator= operator+ str(number)
	t.set(operator)

def bclear():
	global operator
	operator=""
	t.set("")

def answer():
	global operator
	sumup=str(eval(operator))
	t.set(sumup)
	operator=""

root=  Tk()
root.title("Billing")
operator=""
t= StringVar()
txt= Entry(root, font=('arial',20, 'bold'), textvariable= t, bd= 30, insertwidth= 4, bg='powder blue', justify='right').grid(columnspan= 4)


b7= Button(root, padx= 16, pady=16, bd= 2, fg='blue',  font=('arial',20, 'bold'), text='7', bg='powder blue', command=lambda:bclick(7)).grid(row=1, column=0)
b8= Button(root, padx= 16, pady=16, bd= 2, fg='blue',  font=('arial',20, 'bold'), text='8', bg='powder blue', command=lambda:bclick(8)).grid(row=1, column=1)
b9= Button(root, padx= 16, pady=16, bd= 2, fg='blue',  font=('arial',20, 'bold'), text='9', bg='powder blue', command=lambda:bclick(9)).grid(row=1, column=2)
bplus= Button(root, padx= 16, pady=16, bd= 2, fg='blue',  font=('arial',20, 'bold'), text='+', bg='powder blue', command=lambda:bclick('+')).grid(row=1, column=3)


b4= Button(root, padx= 16, pady=16, bd= 2, fg='blue',  font=('arial',20, 'bold'), text='4', bg='powder blue', command=lambda:bclick(4)).grid(row=2, column=0)
b5= Button(root, padx= 16, pady=16, bd= 2, fg='blue',  font=('arial',20, 'bold'), text='5', bg='powder blue', command=lambda:bclick(5)).grid(row=2, column=1)
b6= Button(root, padx= 16, pady=16, bd= 2, fg='blue',  font=('arial',20, 'bold'), text='6', bg='powder blue', command=lambda:bclick(6)).grid(row=2, column=2)
bminus= Button(root, padx= 16, pady=16, bd= 2, fg='blue',  font=('arial',20, 'bold'), text='-', width=2, bg='powder blue', command=lambda:bclick('-')).grid(row=2, column=3)


b1= Button(root, padx= 16, pady=16, bd= 2, fg='blue',  font=('arial',20, 'bold'), text='1', bg='powder blue', command=lambda:bclick(1)).grid(row=3, column=0)
b2= Button(root, padx= 16, pady=16, bd= 2, fg='blue',  font=('arial',20, 'bold'), text='2', bg='powder blue', command=lambda:bclick(2)).grid(row=3, column=1)
b3= Button(root, padx= 16, pady=16, bd= 2, fg='blue',  font=('arial',20, 'bold'), text='3', bg='powder blue', command=lambda:bclick(3)).grid(row=3, column=2)
bemul= Button(root, padx= 16, pady=16, bd= 2, fg='blue',  font=('arial',20, 'bold'), text='x', bg='powder blue', command=lambda:bclick('*')).grid(row=3, column=3)


b0= Button(root, padx= 16, pady=16, bd= 2, fg='blue',  font=('arial',20, 'bold'), text='0', bg='powder blue', command=lambda:bclick(0)).grid(row=4, column=0)
bclear= Button(root, padx= 16, pady=16, bd= 2, fg='blue', width=2,  font=('arial',20, 'bold'), text='C', bg='powder blue', command=bclear).grid(row=4, column=1)
bequal= Button(root, padx= 16, pady=16, bd= 2, fg='blue',  font=('arial',20, 'bold'), text='=', bg='powder blue', command=answer).grid(row=4, column=3)
bediv= Button(root, padx= 16, pady=16, bd= 2, fg='blue',  font=('arial',20, 'bold'), text='/ ', bg='powder blue', command=lambda:bclick('/')).grid(row=4, column=2)



root.mainloop()