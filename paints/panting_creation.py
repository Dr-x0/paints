import turtle as t 
from tkinter import *
from tkinter import ttk
def turtul():         
    t.speed("fastest")
    color=["#FF00FF","blue","green","yellow","red","#16F529","white","gray","brown"]
    t.begin_fill()
    for i in range(65):
        for j in range(4):
            t.pencolor(color[i % 9])
            t.fd(2*i*j)
            t.lt(55)
    t.hideturtle()
    t.end_fill()
    t.done()
def turtul_1():    
    t.speed("fastest")
    color=["#FF00FF","blue","green","yellow","red","#16F529","white","gray"]
    t.begin_fill()
    for i in range(65):
        for j in range(4):
            t.pencolor(color[i % 8])
            t.fd(2*i*j)
            t.lt(50)
    t.hideturtle()
    t.end_fill()
    t.done()
def turtul_2():    
    t.speed("fastest")
    color=["#FF00FF","blue","green","yellow","red","#16F529","white","gray"]
    t.begin_fill()
    for i in range(65):
        for j in range(4):
            t.pencolor(color[i % 8])
            t.fd(2*i*j)
            t.lt(60)
    t.hideturtle()
    t.end_fill()
    t.done()
def turtul_3():    
    t.speed("fastest")
    color=["#FF00FF","blue","green","yellow","red","#16F529","white","gray"]
    t.begin_fill()
    for i in range(50):
        for j in range(4):
            t.pencolor(color[i % 8])
            t.fd(2*i*j)
            t.lt(30)
    t.hideturtle()
    t.end_fill()
    t.done()    
def turtul_4():    
    t.speed("fastest")
    color=["#FF00FF","blue","green","yellow","red","#16F529","white","gray"]
    t.begin_fill()
    for i in range(70):
        for j in range(4):
            t.pencolor(color[i % 8])
            t.fd(2*i*j)
            t.lt(40)
    t.hideturtle()
    t.end_fill()
    t.done()    
def turtul_5():    
    t.speed("fastest")
    color=["#FF00FF","blue","green","yellow","red","#16F529","white","gray"]
    t.begin_fill()
    for i in range(90):
        for j in range(4):
            t.pencolor(color[i % 8])
            t.fd(2*i*j)
            t.lt(30)
    t.hideturtle()
    t.end_fill()
    t.done()    
root=Tk()
root.geometry("300x300")
root.title("paint")
root.resizable(False,False)
Button(root,height=10,width=10,activebackground="#FF00FF",bg="black",command=turtul).place(x=0,y=0)
Button(root,height=10,width=10,activebackground="yellow",bg="red",command=turtul_1).place(x=81,y=0)
Button(root,height=10,width=10,activebackground="yellow",bg="red",command=turtul_2).place(x=155,y=0)
Button(root,height=10,width=10,activebackground="#FF00FF",bg="black",command=turtul_3).place(x=220,y=0)
Button(root,width=21,height=9,activebackground="white",bg="black",command=turtul_4).place(x=0,y=160)
Button(root,width=21,height=9,activebackground="white",bg="black",command=turtul_5).place(x=155,y=160) 
root.mainloop()
