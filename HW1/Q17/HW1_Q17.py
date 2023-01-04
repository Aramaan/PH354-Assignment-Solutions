"""
Abhinav Sinha
SR. No. - 18750
"""

import matplotlib.pyplot as plt
import numpy as np

prs = 0.01

x = np.arange(-2,2,prs)
y = np.arange(-2,2,prs)
xx, yy = np.meshgrid(x,y)


def d(a,b):
    c = np.array([a,b])
    z = np.array([0.,0.])
    i = 0
    while np.linalg.norm(z) < 2 and i<100:
        z = np.array([z[0]**2-z[1]**2,2*z[0]*z[1]]) + c
        i = i+1
    return i-1


rr = np.zeros((len(x),len(y)))


def doit(rr,x,y):
    for i in  range(len(x)):
        for j in range(len(y)):
            rr[i][j] = d(x[i],y[j])



doit(rr,x,y)

# black and white plot
black = (rr != 99)
'''fp = np.zeros(rr.shape)
fp[black] = 1'''
fig, ax = plt.subplots()
ax.scatter(xx, yy, c=black, s=100, cmap='gray')
plt.title("The Mandelbrot set")
plt.savefig('HW1_Q17_bw.png')
plt.show()

# colorful plot
fig2, ax = plt.subplots()
ax.scatter(xx, yy, c=rr, s=100)
plt.title("The Mandelbrot set")
plt.savefig('HW1_Q17_color.png')
plt.show()

# logarithmic colorful plot
fig3, ax = plt.subplots()
ax.scatter(xx, yy, c=np.log(rr+1), s=100)
plt.title("The Mandelbrot set")
plt.savefig('HW1_Q17_logcolor.png')
plt.show()
