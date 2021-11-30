
# str1="Eleanora"
# str2="Dorcas"
# middle=len(str1)//2
# half=len(str2)//2
# new_name=(str1[0]+str2[0]+str1[middle]+str2[half]+str1[-1]+str2[-1])
# print(new_name)





message="Emma is a data scientist who knows python. Emma works at google."
p=message.split()

# print(p)
# # print(len(p))
# print(p.index("Emma"))
print(message.rindex("Emma"))


# a=0
# count = 0
# value=100
# while a <=value:
#     count+=a
#     a+=1
# print(count)



a=0
count=50
while a<=50:
    counter=count-a
    a+=1
    print(counter)


initial=5
product=1
while initial>0 and initial<=5:
    product*=initial
    initial-=1
print(product)
print(initial)
