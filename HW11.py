#Task1
#1, 2, 3, 4, 5, 

#Task2
list = [59, 432, 7, 4, 600, 2]
list.sort()
print(list[0])

#Task3
list1 = [59, 432, 7, 4, 600, 2]
if 0 in list1:
  print("This list contains 0")
else:
  print("This list does not contain 0")

#Task4
list2 = [59, -432, 7, -4, 600, -2]
poslist = []
for num in list2:
  if num > 0:
    poslist.append(num)
print(list2)
print(poslist)