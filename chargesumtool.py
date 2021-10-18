from itertools import islice
import linecache
import sys
import csv
def picklines(thefile, line):
    return linecache.getline(thefile, line)


temp1=picklines("POSCAR",6)
temp2= picklines("POSCAR",7)

list1 = temp1.split()
list2 = temp2.split()
l= len(list2)
list2 = list(map(float,list2[0:l]))
print(type(list2))

print(list1)
print(list2)

with open("ACF.txt") as fin:
    for line in islice(fin, 1, 89):
        result=(fin.read().split()[4::7])
    len= len(result)
    final=list(map(float,result[0:len-1]))

list3= []
add = 0
start=0
for each in list2:
    #print("============each:"+str(each)+"==============")
    # print("============end:" + str(start+each) + "==============")
    # list3.append(sum(final[int(start):int(start+each)-1],int(start)))
    for i in range(int(each)):
        add= final[int(i+start)]+add
        if(i==each):
            break
    list3.append(add)
    start = start + each
    add =0

    #print("start=========="+str(start))
#print(final)
print("==========================Charge Sum list===============================")
print(list3)
print("==========================Charge Sum===============================")
print(sum(list3))



