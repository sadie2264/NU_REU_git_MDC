import numpy as np
import matplotlib.pyplot as plt

x=np.linespace(0,10,1000)
y=x

fig, ax=plt.subplots()
ax.plot(x,y)
ax.set_xlabel('x')
ax.set_ylabel('y')
fig.tight_layout()

