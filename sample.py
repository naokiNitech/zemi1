
import numpy as np
# import matplotlib.pyplot as plt

# f=5
# x=np.linspace(0,5,1000)
# y=np.sin(1*np.pi*x*f)

# plt.figure()
# plt.plot(x,y)
# plt.show()

import csv
freq=5
x=np.linspace(0,5,1000)
y=np.sin(1*np.pi*x*freq)

import numpy as np
#例としてsinカーブを作る


data = np.c_[x,y]

#csvファイルとして保存
np.savetxt('out.csv',data,delimiter=',')


# A=[]

# for i in x:
    # j=0
    # A[j][0]=x[i]
    # j=j=1

# for I in Y:
    # j=0
    # A[j][1]=x[I]
    # J=J+1
# print(A)
