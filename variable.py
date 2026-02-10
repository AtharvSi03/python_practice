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
cir = int(input("Enter raduis of circle: "))
pi = 3.14159265359
area = pi * cir * cir
print("The area of the circle is:" ,area)

#11. Compound Interest: A = P (1 + r/100)^t
p = int(input("Enter Principal amount: "))
t = int(input("Enter time amount in years (e.g. 2): "))
cr = int(8.5)
a = p*(1 + cr/100)**t
print(p, "with an intrest of 20 percentage for" ,t, "years becomes:" ,a)
# BMI Calculator using height in cm
weight = float(input("Enter Weight (in kg): "))
height_cm = float(input("Enter Height (in cm): "))
age = int(input("Enter Age (in years): "))
height_m = height_cm / 100
bmi = weight / (height_m ** 2)
bmi = round(bmi, 2)

print("\nYour BMI is:", bmi)
if age >= 18:
  if bmi < 18.5:
    print("Because you are 18 or above, you are currently underweight")
  elif 18.5 <= bmi < 25:
    print("Because you are 18 or above, you are currently normal weight")
  elif 25 <= bmi < 30:
    print("Because you are 18 or above, you are currently overweight")
  else:
    print("Because you are 18 or above, you are currently obese")
else:
  if bmi < 14:
    print("Because you are under 18, you are currently underweight")
  elif 14 <= bmi < 20:
    print("Because you are under 18, you are currently normal weight")
  elif 20 <= bmi < 25:
    print("Because you are under 18, you are currently overweight")
  else:
    print("Because you are under 18, you are currently obese")

print("\nNote: For kids & teens, real BMI uses age-percentile charts.")
#13. Total Salary = Basic + HRA(20%) + DA(40%)
b = int(input("\nEnter Basic Amount (in ₹): "))
hra = 0.2
da = 0.4
hrda = (hra + da)*b
salary = b + hrda
print("Your salary is:" ,salary, "\n")
#14. Calculate Discount on a Product
discount_per = int(input("Enter Discount (in %): "))
price = int(input("Enter orignal price: "))
discount_amo = (discount_per / 100) * price
newprice = price - discount_amo
print("The discount amount is:" ,discount_amo, "and the new price is: ₹" ,newprice, "\n")
#15. Fahrenheit to Celsius: C = (F − 32) * 5/9
fh = int(input("Enter Fahrenheit: "))
cl = (fh - 32) * (5 / 9)
print(fh,"F in celsius is" ,cl,"C")
#16. Electricity Bill Calculator (slab wise)
#17. Calculate Speed = distance / time
distance = int(input("Enter Distance: "))
time = int(input("Enter Time taken: "))
speed = distance / time
print("If the distance is" ,distance, "and the time taken is" ,time, "then the speed is" ,speed, "\n")
#18. Grading System based on average marks
mathmar = int(input("Enter number of marks in Math: "))
sciencemar = int(input("Enter number of marks in Science: "))
comuptermar = int(input("Enter number of marks in Computer: "))
biomar = int(input("Enter number of marks in Biology: "))
avermar = (mathmar + sciencemar + comuptermar + biomar) / 2
print("Your average marks are" ,avermar)
if (avermar >= 90):
  print("You got grade A!")
elif (avermar >= 70):
  print("You got grade B!")
elif (avermar >= 50):
  print("You got grade C")
elif (avermar < 50):
  print("You got grade D")
elif (avermar < 30):
  print("You got grade F")
#19. Convert Days to Years, Months, Days
days = int(input("Enter number of days"))
leap = input("Is it leap year? Answer in Yes or No: ")
if (leap == "Yes"):
  years = days / 366
  months = days / 31
  print("The number of years would be:" ,years, " and it would be:" ,months,"months")
elif (leap == "No"):
  years = days / 365
  months = days / 31
  print("The number of years would be:" ,years, " and it would be:" ,months,"months")
else:
  print("You have to either type 'Yes' or 'No not" ,leap)
#20. SI with different rates for each year
sip = float(input("Enter Principal: ₹"))
years = int(input("Enter number of years: "))
total_rate = 0

for i in range(years):
    rate = float(input(f"Enter rate for year {i+1}: "))
    total_rate += rate

total_si = (sip * total_rate) / 100
total_amount = sip + total_si

print("Total Interest: ₹", total_si)
print("Total Amount to pay: ₹", total_amount)

#21. EMI Calculator
emip = 100000
emiyr = 10
emitm = 12

monthly_rate = emiyr / (12 * 100)
emi = (emip * monthly_rate * (1 + monthly_rate)**emitm) / ((1 + monthly_rate)**emitm - 1)
print(round(emi, 2))
#22. Profit & Loss % Calculator
cp = int(input("Enter Cost Price: "))
sp = int(input("Enter Sell Price: "))
if (sp > cp):
  p = sp - cp
  print("There is a profit of ", p)
elif (cp > sp):
  l = cp - sp
  print("There is a loss of ", l)
#23. Distance Between Two Points
v1x = int(input("Enter Point 1 X: "))
v1y = int(input("Enter Point 1 Y: "))
v2x = int(input("Enter Point 2 X: "))
v2y = int(input("Enter Point 2 Y: "))
ys = (v2y - v1y)*2
xs = (v2x - v1x)*2
d = (ys + xs)**2
print("The distance is:" ,d)
#24. Loan Eligibility Checker
#25. Percentage Calculator for 5 Subjects
amaths = int(input("Enter marks in Maths: "))
ascience = int(input("Enter marks in Science: "))
asst = int(input("Enter marks in SST: "))
aenglish = int(input("Enter marks in English: "))
acomputer = int(input("Enter marks in Computer: "))
total_amount_per = amaths + ascience + asst + aenglish + acomputer
pmaths = (amaths/total_amount_per) * 100
pscience = (ascience/total_amount_per) * 100
psst = (asst/total_amount_per) * 100
penglish = (aenglish/total_amount_per) * 100
pcomputer = (acomputer/total_amount_per) * 100
print("The percantage of Maths is:" ,pmaths, "% and in Science:" ,pscience, "% and in SST:" ,psst, "% and in English:" ,penglish, "% and in Computer:" ,pcomputer)
#26. Volume of Cylinder: π * r2 * h
cyraduis = int(input("Enter Raduis: "))
cyheight = int(input("Enter Height: "))
cyvolume = pi * (cyraduis * 2) * cyheight
print("The volume of the cylinder is" ,cyvolume)
#27. Currency Converter (INR to USD/EUR)
inr = int(input("Enter amount of money in INR: ₹"))
usdreur = input("USD (USA dollar), EUR (Euro) or both?: ")
if (usdreur == "USD"):
  usd = inr * 0.011
  print("In USD (USA dollar)" ,inr, "rupees would be $" ,usd)
elif (usdreur == "EUR"):
  eur = inr * 0.0093
  print("In EUR (Euro)" ,inr, "rupees would be €" ,eur)
elif (usdreur == "Both" or usdreur == "both"):
  usd = inr * 0.011
  eur = inr * 0.0093
  print("In USD (USA dollar)" ,inr, "rupees would be $" ,usd, "and in EUR (Euro) it would be €" ,eur)
#28. GST Split: CGST + SGST
#29. CAGR: (End/Start)^(1/n) - 1
start_val = 100000
end_val = 150000
years = 3
cagr = (end_val / start_val)**(1 / years) - 1
finalcagr =  {round(cagr * 100, 2)}%
print("CAGR is:" ,finalcagr)
#30. Working Hours Salary with Overtime
base_salary = 40000
standard_hours = 160
totalhrsw = 175
ot_multiplier = 2

hourly_rate = base_salary / standard_hours
overtime_hours = max(0, totalhrsw - standard_hours)

regular_pay = standard_hours * hourly_rate
overtime_pay = overtime_hours * (hourly_rate * ot_multiplier)
total_salary = regular_pay + overtime_pay

print("The total salary is:" ,total_salary)