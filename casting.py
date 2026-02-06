# Question 1: Convert a string "123" into an integer and add 10. What is the result?
""" string = 123
adding = 10
integer = 0
newinteger = string + adding + integer
newstring = string - 123
print("Answer 1:" ,newinteger)
 """
value = "123"
ans = int(value) + 10
print("Answer 1:" ,ans)

 # Question 2: Write a Python program to convert a floating-point number 45.67 into an integer.
""" float = 45.67
float == int
print("Answer 2:" ,int) """
value2 = 45.67
ans2 = int(value2)
print("Answer 2:" ,ans2)

# Question 3: Convert the string "56.78" into a float and multiply it by 2.
value3 = "56.78"
ans3 = float(value3) * 2
print("Answer 3:" ,ans3)
# Question 4: Given a list of string numbers ["1", "2", "3", "4"], convert all elements into integers.
numbers = ["1", "2", "3", "4"]
for i in numbers:
  newnumbers = i
  ans4 = int(newnumbers)
  print("Answer 4 Part:" ,ans4)
# Question 5: Convert an integer 100 into a string and print its type.
prevalue5 = 100
intvalue = int(prevalue5)
strvalue = str(intvalue)
print("Answer 5:" ,strvalue)
# Question 6: Convert a boolean value True into an integer. What output will you get?
boolean = True
intboolean = int(boolean)
print("Answer 6:" ,intboolean)
# Question 7: What happens when you try to convert the string "abc" into an integer using int("abc")?
"""abcstring = "abc"
intabc = int(abcstring)"""
print("Answer 7: It will show an error")
# Question 8: Write a Python program to convert a tuple of numbers (10, 20, 30) into a list of strings.
numberstruple = (10, 20 , 30)
numberlist = list(numberstruple)
stringlist = []
for i in numberlist:
  stringlist2 = str(i)
  stringlist.append(stringlist2)
print("Answer 8:" ,stringlist)
# Question 9: Convert the integer 255 into its binary, octal, and hexadecimal string formats.
numberinterger = 255
binarystring = str(bin(numberinterger))
octalstring = str(oct(numberinterger))
hexadecimalstring = str(hex(numberinterger))
print("Answer 9: Binary:" ,binarystring, "Octal:" ,octalstring, "Hexadecimal:" ,hexadecimalstring)
# Question 10: Write a Python program to take user input (as a string) and convert it to float, then display the result.
userinput = input("Enter a number:")
inputfloat = float(userinput)
print("Answer 10:" ,inputfloat)