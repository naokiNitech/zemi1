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
y=np.cos(1*np.pi*x*freq)

data = np.c_[x,y]
    
# X=x.T
# Y=y.T
     


# with open('sample.csv', 'w') as f:
 
#    writer =csv.writer(f)
#    writer.writerows(data)

#  f.close

np.savetxt('coswave1.csv',data,delimiter=',')