#Task1
string = '123456789'
string = string[5:]
print(string)
#Task2
def countvowels(string):
  string = "Hello"
  num_vowels = 0
  for char in string:
      if char in "aeiouAEIOU":
         num_vowels = num_vowels+1
  return num_vowels
#Task3
string = "Hello, my name is Savir"
num_words = 1
for char in string:
  if char == " ":
    num_words = num_words+1
print(num_words)
#Task4
text = "Hello!"[::-1]
print(text)
#Task5
string = "Hello, my name is Savir"
if string == string[::-1]:
  print("It is a palindrome")
else:
  print("It is not a palindrome")
#Task6
text = "Hello, my name is Savir"
text_capitalized = text.title()
print(text_capitalized)
