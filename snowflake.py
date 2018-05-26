import turtle
import time

def tree(branchLen,t,level):
    if branchLen > 5:
        #print(level+"\n")
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t,"level 2")
        t.left(40)
        tree(branchLen-15,t,"level 3")
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(70)
    t.down()
    t.color("green")
    angle = 360
    while angle > 0:
        tree(75,t,"level 1")
        t.left(45)
        angle = angle - 45
    myWin.exitonclick()

main()
