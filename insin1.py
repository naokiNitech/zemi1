from calendar import c
import numpy as np
import matplotlib.pyplot as plt
import csv 
import pandas as pd
with open('sinwave1.csv','r')as f:
    reader=csv.reader(f)
    L=[row for row in reader]
   

sinx=[S[0]for S in L]
siny=[S[1]for S in L]

Sinx=[float(t)for t in sinx]
Siny=[float(t_1)for t_1 in siny]


plt.figure()
plt.plot(Sinx,Siny)
plt.show()

with open('coswave1.csv','r')as f_1:
    reader_1=csv.reader(f_1)
    L_1=[low for low in reader_1]
   

cosx=[C[0]for C in L_1]
cosy=[C[1]for C in L_1]

Cosx=[float(c)for c in cosx]
Cosy=[float(c_1)for c_1 in cosy]


plt.figure()
plt.plot(Cosx,Cosy)
plt.show()


