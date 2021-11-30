# my_names={}
# names=["Eleanora","Seun","Babatunde","Ayo","Dorcas","Oluwaseun","Eleanora","Ayo","Babatunde","Eleanora","Seun","Dorcas","Eleanora","Seun","Oluwaseun","Ayo","Eleanora"]
# first=names.count("Eleanora")
# second=names.count("Seun")
# third=names.count("Babatunde")
# fourth=names.count("Ayo")
# fifth=names.count("Dorcas")
# sixth=names.count("Oluwaseun")

# name1=names[0]
# name2=names[1]
# name3=names[2]
# name4=names[3]
# name5=names[4]
# name6=names[5]


# my_names={name1:first,
# name2:second,
# name3:third, 
# name4:fourth,
# name5:fifth, 
# name6:sixth}
# print(my_names)



# or

states=['lagos', 'Abuja', 'Osun', 'imo', 'ABUJA', 'OSUN', 'LaGos', 'IMO', 'osun']

counts={}

# for i in states:
#     if i.lower() in counts.keys():
#         counts[i.lower()]+=1
#     else:
#         counts[i.lower()] = 1

# print(counts)



# or

# for i in states:
#     counts[i.lower()] = counts.get(i.lower(), 0) + 1

# print(counts)

# or


for i in states:
    key = i.lower().strip()
    counts[key] = counts.get(key, 0) + 1

print(counts)