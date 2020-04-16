from tkinter import *
root = Tk()
root.title("My Calci")

	


b1 = Entry(root, width =30, borderwidth = 5)
b1.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)


def button_click(number):
	current = b1.get()
	b1.delete(0, END)
	b1.insert(0, str(current) + str(number))
def button_clear():
	b1.delete(0, END)

def button_sum():
	global current1
	global math
	math = "add"
	current1 = float(b1.get())
	b1.delete(0, END) 

	 

def button_equal():
    if(math == "add"):
    	current2 = float(b1.get())
    	b1.delete(0, END)
    	e1 = current1 + current2
    	b1.insert(0, str(e1))
	    
	    
	     
    if(math == "sub"):
    	current2 = float(b1.get())
    	b1.delete(0, END)
    	e1 = current1 - current2
    	b1.insert(0, str(e1))
	    
	    
	    
    if(math == "mult"):
    	current2 = float(b1.get())
    	b1.delete(0, END)
    	e1 = current1 * current2
    	b1.insert(0, str(e1))
	    
	    
	    
    if(math == "div"):
    	current2 = float(b1.get())
    	b1.delete(0, END)
    	e1 = current1/current2
    	b1.insert(0, str(e1))
	    
	    
	    


def button_sub():
	global current1
	global math
	math = "sub"
	current1 = float(b1.get())
	b1.delete(0, END) 
def button_div():
	global current1
	global math
	math = "div"
	current1 = float(b1.get())
	b1.delete(0, END) 
def button_mult():
	global current1
	global math
	math = "mult"
	current1 = float(b1.get())
	b1.delete(0, END) 


a = Button(root, text = '9', width = 10, command = lambda: button_click(9))
a.grid(row = 1, column = 2)

b = Button(root, text = '8', width = 10, command = lambda: button_click(8))
b.grid(row = 1, column = 1)

c = Button(root, text = '7', width = 10, command = lambda: button_click(7))
c.grid(row = 1, column = 0)

d = Button(root, text = '6', width = 10, command = lambda: button_click(6))
d.grid(row = 2, column = 2)

e = Button(root, text = '5', width = 10, command = lambda: button_click(5))
e.grid(row = 2, column = 1)

f = Button(root, text = '4', width = 10, command = lambda: button_click(4))
f.grid(row = 2, column = 0)

g = Button(root, text = '3', width = 10, command = lambda: button_click(3))
g.grid(row = 3, column = 2)


h = Button(root, text = '2', width = 10, command = lambda: button_click(2))
h.grid(row = 3, column = 1)

i = Button(root, text = '1', width = 10, command = lambda: button_click(1))
i.grid(row = 3, column = 0)

j = Button(root, text = '0', width = 10, command = lambda: button_click(0))
j.grid(row = 4, column = 0)

k = Button(root, text = "Clear", width = 21, command = button_clear)
k.grid(row = 4, column = 1, columnspan = 2)

f1 = Button(root, text = "+", width = 3, height = 3, command = button_sum)
f1.grid(row = 1, column = 3, rowspan = 2)

f2 = Button(root, text = "=", width = 3, height = 4, command = button_equal)
f2.grid(row = 3, column = 3, rowspan = 3)

f3 = Button(root, text = '*', width = 10, command = button_mult)
f3.grid(row = 5, column = 1)

f4 = Button(root, text = '/', width = 10, command = button_div)
f4.grid(row = 5, column = 0)

f5 = Button(root, text = '-', width = 10, command = button_sub)
f5.grid(row = 5, column = 2)





root.mainloop()
