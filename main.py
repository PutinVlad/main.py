print("Здраааавствуйте")
Dat = open("chisla.txt", "r")
chisla_1 = Dat.readlines()
for line in chisla_1:
    keks = line.split("b")
print(keks)
int_keks = map(int, keks)
print(int_keks)
list_1 = list(int_keks)
list_2 = list_1
for i in range(0, len(list_1)):
    for k in range(0, i):
        if list_1[k] <= list_1[i]:
            list_2[k] = list_1[k]
        elif list_1[k] > list_1[i]:
            # c = list_2[k]
            list_2[k], list_1[i] = list_1[i], list_2[k]
            # list_1[i] = c
print(list_2)
