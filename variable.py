# Python Variable-Based Problem-Solving Questions (Basic to Advanced)
# 1. Simple Interest: SI = (P * R * T) / 100
p = int(input("Enter Principle Amount: "))
r = 10
t = 365
SI = (p * r * t)/100
print("Answer 1:" ,SI)
# 2. Area of Rectangle: A = length * breadth
l = int(input("Enter Length in cm: "))
b = int(input("Enter Breadth in cm: "))
area = l*b
print("Answer 2: Area of rectangle: " ,area)
# 3. Perimeter of Rectangle: 2 * (length + breadth)
l = int(input("Enter Length in cm: "))
b = int(input("Enter Breadth in cm: "))
perimeter = 2*(l+b)
print("Answer 2: Perimeter of rectangle: " ,perimeter)
# 4. Swap Two Variables using a third variable
v1 = "v1"
v2 = "v2"
temp = v1
v1 = v2
v2 = temp
print("Answer 4:" ,v1 ,v2)
# 5. Convert Celsius to Fahrenheit: F = (C * 9/5) + 32
cel = int(input("Enter you number in celsius: "))
fah = (cel * 9/5) + 32
print(cel, "celsius in Fahrenheit is:" , fah)
# 6. Calculate Square and Cube of a Number
num = int(input("Enter number: "))
squ = num ** 2
cube = num ** 3
print("Answer 5: The square of the number is:" ,squ, "and the cube is:" ,cube)
# 7. Calculate Total and Average of 3 Marks
mathm = int(input("Enter number of marks recieved in Math: "))
scim = int(input("Enter number of marks recieved in Science: "))
csm = int(input("Enter number of marks recieved in Coumpter Science: "))
ave = (mathm + scim + csm) / 2
tot = mathm + scim + csm
print("The average is:" ,ave, "and the total is:" ,tot)
# 8. Convert Minutes to Seconds
mins = int(input("Enter minutes: "))
secs = mins * 60
print(mins, "minutes in seconds is:" ,secs)
# 9. Calculate GST Amount: price + 18%
price = int(input("Enter price: "))
gst = price * 0.18
print("The GST amount of" ,price, "is" ,gst)
# 10. Area of Circle: π * r * r
r = int(input("Enter raduis of circle: "))
pi = 3.14159265359
area = pi * r * r
print("The area of the circle is:" ,area)

#11. Compound Interest: A = P (1 + r/100)^t
#12. BMI Calculator: weight / (height * height)
#13. Total Salary = Basic + HRA(20%) + DA(40%)
#14. Calculate Discount on a Product
#15. Fahrenheit to Celsius: C = (F − 32) * 5/9
#16. Electricity Bill Calculator (slab wise)
#17. Calculate Speed = distance / time
#18. Grading System based on average marks
#19. Convert Days to Years, Months, Days
#20. SI with different rates for each year

#21. EMI Calculator
#22. Profit & Loss % Calculator
#23. Distance Between Two Points
#24. Loan Eligibility Checker
#25. Percentage Calculator for 5 Subjects
#26. Volume of Cylinder: π * r2 * h
#27. Currency Converter (INR to USD/EUR)
#28. GST Split: CGST + SGST
#29. CAGR: (End/Start)^(1/n) - 1
#30. Working Hours Salary with Overtime