f = open("task2_data.dat", "r")
def parse_line(line):
    return [i.strip() for i in line.split(' '*2) if i]

with open('task2_data.dat', 'r') as file:
    kok = [line.strip().expandtabs() for line in f.readlines()]
    kok = [parse_line(line) for line in kok if line]
    kuk = list(kok)
#print(kok)

import pandas as pd
df = pd.DataFrame(kok)
kok = df.drop(labels=None, axis=0, index=0)
#print(kok)
df_1 = df.iloc[:,0]
df_1 = df_1.drop(labels=None, axis=0, index=0)
#print(df_1)
Stars = list(df_1)
#print(Stars)
df_2 = df.iloc[:,2]
df_2 = df_2.drop(labels=None, axis=0, index=0)
#print(df_2)
Filters = list(df_2)
#print(Filters)

Newstars1 = []
Newstars2 = []
for i in Stars:
    if "o" in i:
        Newstars1.append(i)
for j in range(0, len(Newstars1)):
    Newstars1[j] = Newstars1[0]
#print(Newstars1)
for i in Stars:
    if "y" in i:
        Newstars2.append(i)
for j in range(0, len(Newstars2)):
    Newstars2[j] = Newstars2[0]
#print(Newstars2)
SU_Hor = Newstars1
RZ_Lyr = Newstars2
object = SU_Hor + RZ_Lyr
#print(Object)

df_3 = df.iloc[:,1]
df_3 = df_3.drop(labels=None, axis=0, index=0)
#print(df_3)
HJD = list(df_3)
#print(HJD)
df_4 = df.iloc[:,3]
df_4 = df_4.drop(labels=None, axis=0, index=0)
#print(df_4)
Magnitude = list(df_4)
#print(Magnitude)
#Часы:
#делаем таблицу для фильтра B
B1 = []
B2 = []
B3 = []
B4 = []
for i in range(0,len(SU_Hor)):
    if Filters[i] == 'B' or Filters[i] =='b':
        B1.append(object[i])
        B2.append(Filters[i])
        B3.append(HJD[i])
        B4.append(Magnitude[i])
#print(B1)
#print(B2)
#print(B3)
#print(B4)
Table1 = [B1] + [B2] + [B3] + [B4]
#print(Table1)
Data1 = pd.DataFrame(Table1)
Data1 = Data1.rename(index = {0:'Object' , 1:'Filter' , 2:'HJD' , 3:'Magnitude'})
Data1 = Data1.T
print(Data1)

#для фильтра V аналогично
V1 = []
V2 = []
V3 = []
V4 = []
for i in range(0,len(SU_Hor)):
    if Filters[i] == 'V' or Filters[i] == 'v':
        V1.append(object[i])
        V2.append(Filters[i])
        V3.append(HJD[i])
        V4.append(Magnitude[i])
#print(V1)
#print(V2)
#print(V3)
#print(V4)
Table2 = [V1] + [V2] + [V3] + [V4]
#print(Table2)
Data2 = pd.DataFrame(Table2)
Data2 = Data2.rename(index = {0:'Object' , 1:'Filter' , 2:'HJD' , 3:'Magnitude'})
Data2 = Data2.T
print(Data2)

#Ic...
Ic1 = []
Ic2 = []
Ic3 = []
Ic4 = []
for i in range(0,len(SU_Hor)):
    if Filters[i] == 'Ic':
        Ic1.append(object[i])
        Ic2.append(Filters[i])
        Ic3.append(HJD[i])
        Ic4.append(Magnitude[i])
Table3 = [Ic1] + [Ic2] + [Ic3] + [Ic4]
#print(Table3)
Data3 = pd.DataFrame(Table3)
Data3 = Data3.rename(index = {0:'Object' , 1:'Filter' , 2:'HJD' , 3:'Magnitude'})
Data3 = Data3.T
print(Data3)

#Лира:
B1 = []
B2 = []
B3 = []
B4 = []
for i in range(len(SU_Hor),len(object)):
    if Filters[i] == 'B' or Filters[i] =='b':
        B1.append(object[i])
        B2.append(Filters[i])
        B3.append(HJD[i])
        B4.append(Magnitude[i])
#print(B1)
#print(B2)
#print(B3)
#print(B4)
Table1 = [B1] + [B2] + [B3] + [B4]
#print(Table1)
Data1R = pd.DataFrame(Table1)
Data1R = Data1R.rename(index = {0:'Object' , 1:'Filter' , 2:'HJD' , 3:'Magnitude'})
Data1R = Data1R.T
print(Data1R)

#для фильтра V аналогично:
V1 = []
V2 = []
V3 = []
V4 = []
for i in range(len(SU_Hor),len(object)):
    if Filters[i] == 'V' or Filters[i] == 'v':
        V1.append(object[i])
        V2.append(Filters[i])
        V3.append(HJD[i])
        V4.append(Magnitude[i])
#print(V1)
#print(V2)
#print(V3)
#print(V4)
Table2 = [V1] + [V2] + [V3] + [V4]
#print(Table2)
Data2R = pd.DataFrame(Table2)
Data2R = Data2R.rename(index = {0:'Object' , 1:'Filter' , 2:'HJD' , 3:'Magnitude'})
Data2R = Data2R.T
print(Data2R)
#Ic...
Ic1 = []
Ic2 = []
Ic3 = []
Ic4 = []
for i in range(len(SU_Hor),len(object)):
    if Filters[i] == 'Ic':
        Ic1.append(object[i])
        Ic2.append(Filters[i])
        Ic3.append(HJD[i])
        Ic4.append(Magnitude[i])
Table3 = [Ic1] + [Ic2] + [Ic3] + [Ic4]
#print(Table3)
Data3R = pd.DataFrame(Table3)
Data3R = Data3R.rename(index = {0:'Object' , 1:'Filter' , 2:'HJD' , 3:'Magnitude'})
Data3R = Data3R.T
print(Data3R)

Data1.to_excel('SU_Hor_B.excel', header=None, index=False, sep='    ')
Data2.to_excel('SU_Hor_V.excel', header=None, index=False, sep='    ')
Data3.to_excel('SU_Hor_Ic.excel', header=None, index=False, sep='    ')
Data1R.to_excel('RZ_Lyr_B.excel', header=None, index=False, sep='    ')
Data2R.to_excel('RZ_Lyr_V.excel', header=None, index=False, sep='    ')
Data3R.to_excel('RZ_Lyr_Ic.excel', header=None, index=False, sep='    ')

print("кайфарик")