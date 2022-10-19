# Program to graph the function and the piecewise linear function from problems 10 and 11
import numpy as np
import matplotlib.pyplot as plt
import math

# Problem 2.4.10
plt.figure(figsize=(7,8))
x=np.linspace(1/4,1,100)
y=np.array([math.sqrt(xval) for xval in x])

x2=np.linspace(1/4,9/16,100)
y2=np.array([0.8*xval+0.3 for xval in x2])
plt.scatter(x2[0],y2[0])
plt.scatter(x2[-1],y2[-1])

x3=np.linspace(9/16,1,100)
y3=np.array([(4/7)*xval+(3/7) for xval in x3])
plt.scatter(x3[0],y3[0])
plt.scatter(x3[-1],y3[-1])


plt.plot(x,y,label="f(x)=x^1/2")
plt.plot(x2,y2,label="0.8x+0.3 1/4<=x<=9/16")
plt.plot(x3,y3,label="(4/7)x+3/7 9/16<=x<=1")
plt.legend()

# Problem 2.4.11
plt.figure(figsize=(7,8))
x=np.linspace(1/8,1,100)
y=np.array([xval**(1/3) for xval in x])

x2=np.linspace(1/8,27/64,100)
y2=np.array([(16/19)*xval+(15/38) for xval in x2])
plt.scatter(x2[0],y2[0])
plt.scatter(x2[-1],y2[-1])

x3=np.linspace(27/64,1,100)
y3=np.array([(16/37)*xval+(21/37) for xval in x3])
plt.scatter(x3[0],y3[0])
plt.scatter(x3[-1],y3[-1])


plt.plot(x,y,label="f(x)=x^1/3")
plt.plot(x2,y2,label="(16/19)x+(15/38) 1/8<=x<=27/64")
plt.plot(x3,y3,label="(16/37)x+(21/37) 27/64<=x<=1")
plt.legend()
plt.show()