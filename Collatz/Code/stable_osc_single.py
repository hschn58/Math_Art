import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import Normalize
import matplotlib.cm as cm
import pandas as pd

# Create some data
iter = 1000000000
x = np.linspace(0, iter, iter + 1)

daty = []

for dec in range(1):
    y = []
    ncur = 1.01

    for iteration in range(iter + 1):  # Ensure y has the same length as x
        y.append(ncur)

        if int(str(ncur)[-1]) % 2 == 0:
            ncur /= 2
        else:
            ncur = 3 * ncur

    daty.append(y)

y = np.array(daty[0])

data=np.column_stack((x,y))	
pd.DataFrame(data=data,columns=['x','y']).to_csv('ftdata.csv')

plt.axis('off')
plt.show()


