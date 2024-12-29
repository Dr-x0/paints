import turtle as t 
t.speed("fastest")
color=["#FF00FF","blue","green","#16F529"]
t.begin_fill()
for i in range(65):
    for j in range(4):
        t.pencolor(color[i % 4])
        t.fd(2*i*j)
        t.lt(50)
t.hideturtle()
t.end_fill()
t.done()





