import numpy as np
import matplotlib.pyplot as mpl
import math

t = np.arange(-2, 2, 0.01)
y = t**2*np.sin(t)
g = math.e**t

mpl.xlabel("T")
mpl.ylabel("Y")
mpl.plot(t, y, label='wykres')
mpl.plot(t, g, label='wykres')


mpl.legend(["f(t)","g(t)"])
mpl.title("wykres do zadania 1")

mpl.savefig("plot_zad1.jpg")
mpl.show()
print("t                f(x)                        g(x)")
for i in range(-2,3):
    if(i==0):
        print(i, "           ", i ** 2 * np.sin(i), "                            ", math.e ** i)
    else:
        print(i,"           ",i**2*np.sin(i),"          ", math.e**i)
