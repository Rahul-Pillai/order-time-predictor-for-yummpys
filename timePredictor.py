from tkinter import *
import pandas as pd
import numpy as np
import math
import random
from sklearn.utils import shuffle

root=Tk()

msg=''
dayVal=StringVar()
timeVal=StringVar()
itemsVal=StringVar()
ansLabel=Label(root,text="")
ansLabel.grid(row=4,columnspan=2)

def Func():
    ansLabel.configure(text=msg)

dayV = Label(root,text="Day:")
timeV=Label(root,text="time:")
itemsV = Label(root,text="items ordered:")
entry_1 = Entry(root,textvariable= dayVal)
entry_2 = Entry(root,textvariable=timeVal)
entry_3 = Entry(root,textvariable=itemsVal)
dayV.grid(row=0,sticky=E)
timeV.grid(row=1,sticky=E)
itemsV.grid(row=2,sticky=E)
button=Button(root,text='Submit',command=lambda : Func())
button.grid(row=3,columnspan=2)

day=entry_1
data = pd.read_csv("Monday.csv")
if day=='monday':
    data = pd.read_csv("Monday.csv")
if day=='tuesday':
    data = pd.read_csv("Tuesday.csv")
if day=='wednesday':
    data = pd.read_csv("Wednesday.csv")
if day=='thursday':
    data = pd.read_csv("Thursday.csv")
if day=='friday':
    data = pd.read_csv("Friday.csv")
if day=='saturday':
    data = pd.read_csv("Saturday.csv")
if day=='sunday':
    data = pd.read_csv("Sunday.csv")     
#data = shuffle(data)

#print(data['classic maggi'][0])

classifiers = {}
conditions = {}
name_to_num = {}
l = 0
for col in data.columns:
    #print(col)
    name_to_num[l] = col
    conditions[col] = l
    l += 1

classifier_cnt = 0
classifier_cnt_1 = []
print(len(data[name_to_num[0]]))

row_num = int(input("Enter row num:"))
for i in range(0,62):
    if data.iloc[row_num][i] == 1:
       print(name_to_num[i])
x = []
for x in entry_3.split(","):
    x.append(x)
print(x)
#f=list(map(int,input("Food items:").split()))
t=entry_2

for i in range(56,62):
    cnt = 0
    for j in range(0,len(data[name_to_num[0]])-int((0.2*len(data[name_to_num[0]])))):
        if data[name_to_num[i]][j] == 1:
            cnt += 1
    classifiers[classifier_cnt] = cnt/(len(data[name_to_num[0]])-int((0.2*len(data[name_to_num[0]]))))
    classifier_cnt_1.append(cnt)
    classifier_cnt += 1

for key,value in classifiers.items():
    print(key," ",value)

priori_probability = np.zeros(shape=(56, 6))
for i in range(0,56):
    for j in range(56,62):
        cnt = 0
        for k in range(0,len(data[name_to_num[0]])):
            if data[name_to_num[i]][k] == 1 and data[name_to_num[j]][k] == 1:
                cnt += 1
        priori_probability[i][j-56] = cnt/classifier_cnt_1[j-56]

print(priori_probability)

ptotal=0
prod = []

for i in range(0,6):
    pprod=1
    for j in range(0,len(x)):
        pprod*=priori_probability[conditions[x[j]]][i]
    pprod *= priori_probability[conditions[t]][i]
    pprod *= classifiers[i]
    prod.append(pprod)
    ptotal += pprod

wtime=0
sum=0

for i in range(0,6):
    #wtime+=priori_probability[conditions[f]][i]*priori_probability[conditions[t]][i]/ptotal*(10*i+5)
    sum+=prod[i]
for i in range(0,6):
    wtime+=prod[i]*((10*i)+5)/sum
msg="time: ",int(wtime)," mins"
print(msg)
root.mainloop()

