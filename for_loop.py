# Pre-questions
# Student List
students = ["Atharv", "Arshika", "Avyan", "Aahil", "Aadhya"]
for a in students:
  print(a)
print("\n")
# Main Questions
# 1. Print numbers 1 to 10 using a for loop.
for b in range(11):
  print(b)
print("\n")

# 2. Print even numbers from 1 to 20 using a for loop.
for c in range(1 , 21):
  if c % 2 == 0:
    print(c, "= Even")
  else:
    print(c, "= Odd")
print("\n")
# 3. Find the sum of numbers from 1 to 100 using a for loop.
count = 0
for d in range(1 , 101):
  total = count + d
print(total, "\n")
# 4. Print the multiplication table of 5 using a for loop.
for e in range(11):
  print(e*5)
print("\n")
# 5. Print each character of a string using a for loop.
for f in "Atharv":
  print(f)
print("\n")
# 6. Reverse a string using a for loop.


# 7. Count the number of vowels in a string using a for loop.
word = input("Enter Word: ")
start = 0
for h in word:
  if h == "a" or h == "A":
    start = start + 1
  elif h == "e" or h == "E":
    start = start + 1
  elif h == "i" or h == "I":
    start = start + 1
  elif h == "o" or h == "O":
    start = start + 1
  elif h == "u" or h == "U":
    start = start + 1
print("There are" ,start,"vowels")
# 8. Find the largest number in a list using a for loop.

# 9. Print all elements of a 2D list using nested for loops.
# 10. Check if a number is prime using a for loop.

# 11. Generate a Fibonacci sequence of n terms using a for loop.
# 12. Remove duplicates from a list using a for loop (without using set).
# 13. Count frequency of each element in a list using nested for loops.
# 14. Flatten a nested list (one level) using a for loop.
# 15. Loop over a dictionary and print key-value pairs using a for loop.