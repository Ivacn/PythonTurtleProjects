from turtle import*
colors=("red4","blue3","pink")
bgcolor("antiquewhite")

width(4)
delay(0)
speed(0)
ht()

for i in range(100):
    color(colors[i%len(colors)])
    lt(150)
    fd(i)
    
done()
