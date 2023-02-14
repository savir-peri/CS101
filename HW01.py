#Task2
#Savir
def task2():
  pass

def test_task2():
  pass

#Task3
def task3():
  print("Hello world!")

#Task4
def task4(x, y):
  if x%2 == 0:
    if y%2 == 0 and y > x:
      print(y)
      return y
    else:
      print(x)
      return x
  elif y%2 == 0:
      print(y)
      return y
  else:
    print("Neither number is even")
    return ""

def test_task4():
  assert(task4(0, 2) == 2)
  assert(task4(0, 1) == 0)
  assert(task4(1, 0) == 0)
  assert(task4(1, 3) == "")
  assert(task4(2.5, 3.5) == "")
  assert(task4(10//5, 2) == 2)

#Task5
def find_largest_odd(ars):
    
    return max(ar for ar in ars if ar%2 != 0)
    print(ar)
ars = []
find_largest_odd(ars)
#Task6
def task6():
  h = 1
  bl = 2
  atri = (h*bl)/2
  print(atri)

def task7():
  #Task7
  sl = 2
  asqr = sl**2
  print(asqr)

#Task8
def task8():
  import math
  r = 2
  acirc = math.pi * r**2
  print(acirc)

#task2()
#task3()
test_task4()
#task5()
#task6()
#task7()
#task8()