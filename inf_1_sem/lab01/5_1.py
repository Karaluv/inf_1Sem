
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import csv
import math
# save numpy array as csv file


results = []

result_d = []

with open('C:/Users/karaluv/Pictures/Samsung Flow/Table1 (1).csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='|') 
    for row in reader: # each row is a list
        results.append(row)


for i in range(len(results[0])):
    for j in range(i+1, len(results[0])):
        result_d.append(int(int(results[0][i])+int(results[0][j])))


#savetxt('C:/Users/karaluv/Pictures/Samsung Flow/result_d.csv', result_d, fmt='%i', newline="\n", delimiter=';')
s=0
for i in range(len(result_d)):
    s = s+result_d[i]

sr = s / len(result_d)

sum = 0


x_pos = np.arange(len(result_d))

y_pos = np.arange(0,len(result_d),1)

x = np.arange(0,np.max(result_d)+1,1)



for i in range(len(result_d)):
   # print(i)
    x[result_d[i]]=x[result_d[i]]+1


print(x)

y = list(range(0,len(x)))

for i in range(len(result_d)):
    sum= sum+(result_d[i] - sr)*(result_d[i] - sr)

sum = math.sqrt(sum / (len(result_d)-1))

x = np.array(x)
y = np.array(y)

x,y=y,x

df = pd.DataFrame({'x':x,'y':y})
sns.lmplot(x='x',y='y', data=df, order=20)

plt.show()

#plt.errorbar(y, x, xerr=0, yerr=7.3)
#plt.grid()
#plt.show()


