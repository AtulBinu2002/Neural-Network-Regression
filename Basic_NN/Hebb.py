#Hebb Rule
import pandas as pd
import numpy as np
from google.colab import drive
drive.mount('drive')

table=pd.read_csv("/content/drive/MyDrive/Data/ANDR.csv")
print(table)
N=len(table.columns)-1

head=[]
for i in range(1,N+1):
  if(i!=N):
    head.append('x'+str(i))
  else:
    head.append('b')
head.append('y')
for i in range(1,N+1):
  if(i!=N):
    head.append('w'+str(i))
  else:
    head.append('b')
tab=[head]

L= table.to_numpy().tolist()
w=np.zeros(N)
yin=[]

for i in L:
  y=i[-1]
  t=np.array(i[:-1])        #[x1,x2,...xn]
  w=np.add(w,t*y)           #W=W+Xy
  i.extend(w)
  tab.append(i)

pd.DataFrame(tab)
