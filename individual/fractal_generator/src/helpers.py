
import turtle

#create function triangle, get length
def triangle(t,length):
    #create triangle side lengths length
    for i in range(3):
        t.forward(length)
        t.rt(120)

#create function square, get length
def square(t,length):
    #create square side lengths length
    for i in range(4):
        t.forward(length)
        t.lt(90)