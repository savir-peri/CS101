#Task3
n=100
i=1
while i<n:
  i=i+1
  print(i)
#Task4
for n in range(1, 101):
  print(n)
#Task5
if input("Please enter the password (3 chances remaining): ") == "hello":
  print("Correct")
else:
  if input("Incorrect, please reenter the password (2 chances remaining): ") == "hello":
    print("Correct")
  else:
    if input("Incorrect, please enter the password (1 chance remaining): ") == "hello":
      print("Correct")
    else:
      print("You shall not pass")
#Task6
total = 0
for number in range(0, 101):
    if(number % 2 == 0):
        total = total + number

print("The Sum of Even Numbers from 1 to {0} = {1}".format(number, total))