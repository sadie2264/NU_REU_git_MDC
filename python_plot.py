#here is some code to rune in python that will run cos x form 0 to 2Pi

#here is some code to rune in python that will run cos x form 0 to 2Pi

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi,1000)
y = np.exp(x)

f,ax = plt.subplots(figsize = (8,5))
ax.plot(x,y, c = '#99badd')
ax.set_xlabel('x')
ax.set_ylabel('y')






