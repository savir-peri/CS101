#Task1
Task1List1 = [True, "hello", True, False, 46789, "Savir", 0.9]
BooleanList = [True, False]
for i in Task1List1:
  if i in BooleanList:
    print("List has a Boolean")
    break    

#Task2
Task2List1 = [1, 2, 3, 4, 5, 6, 7]
EvenList = []
for i in Task2List1:
  if i%2 == 0:
    EvenList.append(i)
print(Task2List1)
print(EvenList)

#Task3
DivBy7List = []
for i in range(1,1000,1):
  if i%7 == 0:
   DivBy7List.append(i)
print(DivBy7List)