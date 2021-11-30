number 1

list1=[10,20,30,40]
list2=[100,200,300,400]
list2.reverse()
for i in range(len(list1)):
    print(list1[i]," ",list2[i])

  
number 2

alist=["Mike","","Emma","Kelly","","Brad"]
for i in alist:
    if i == "":
        alist.remove("")

print(alist)


number 3

aList=[10,20,[300,400,[5000,6000],500],30,40]
aList[2][2].append(7000)
print(aList)




number 4
myList=["a", "b",["c",["d","e",["f","g"],"k"],"l"],"m","n"]
subList=["h","i","j"]
myList[2][1][2].extend(subList)
print(myList)


number 5
theList=[5,10,15,20,25,50,20]
newList=theList.index(20)
theList[newList]=200
print(theList)

