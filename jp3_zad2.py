import numpy as np
import matplotlib.pyplot as mpl
import math
import random

x=[range(1000)]
y=[range(1000)]

x[0]=0
y[0]=0
for i in range(0,1000):
    r = random.uniform(0, 1)
    if (r <= 0.25):
        #print("1")
        x.append(x[i])
        y.append(y[i]+1)

    if (0.25 <= r < 0.50):
        #print("2")
        x.append(x[i]+1)
        y.append(y[i])

    if (0.50 <= r < 0.75):
        #print("3")
        x.append(x[i])
        y.append(y[i]-1)

    if (0.75 <= r < 1):
        #print("4")
        x.append(x[i]-1)
        y.append(y[i])

    #print(i,".",x[i],y[i])

figure, axis = mpl.subplots(1,1)
axis.plot(x,y)
axis.scatter(0,0,marker="o",c="blue",zorder=-1)
axis.scatter(x[-1],y[-1],marker="*",c="blue",zorder=-1)
axis.legend(["Droga","Start","Koniec"])




mpl.xlabel("X")
mpl.ylabel("Y")
#mpl.title("zadanie 2")

#mpl.savefig("plot_zad2.jpg")
mpl.show()