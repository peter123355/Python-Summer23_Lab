
# Description :To write a program that calculates kilowatt - hour electrical appliance usage.
import time
print("Programmer: Peter Geevarghese Alex")

x = 12
print("-" * 25)
## dd/mm/yyyy format
print (time.strftime("%d/%m/%Y"))

# mm/dd/yy format
print ("Date:",time.strftime("%x"))

#military time
print ("Current time:",time.strftime("%X"))

# Local variable declarations
totalCost = 0.0
# declare variable as a float type to accumulate total charges
appName = ""
# declare a variable for the appliance name
costPerKW = []

# declare a variable for the annual usage
annualUsage = []
total = 0.0

print("[ Please enter the requested data ]")

# FirstApp
print("Appliance name:")
appName = input()
print("Cost per KW - hr of the appliance (in cents):")
costPerKW1 = float(input())
print("Annual usage (in KW - hr):")
annualUsage1 = float(input())
total += annualUsage1 * costPerKW1
costPerKW.append(costPerKW1)
annualUsage.append(annualUsage1)

# SecondApp
print("[ Please enter the requested data ]")
print("Appliance name:")
appName = input()
print("Cost per KW - hr of the appliance (in cents):")
costPerKW2 = float(input())
print("Annual usage (in KW - hr):")
annualUsage2 = float(input())
total += annualUsage2 * costPerKW2
costPerKW.append(costPerKW2)
annualUsage.append(annualUsage2)

# ThirdApp
print("[ Please enter the requested data ]")
print("Appliance name:")
appName = input()
print("Cost per KW - hr of the appliance (in cents):")
costPerKW3 = float(input())
print("Annual usage (in KW - hr):")
annualUsage3 = float(input())
total += annualUsage3 * costPerKW3
costPerKW.append(costPerKW3)
annualUsage.append(annualUsage3)

# FourthApp
print("[ Please enter the requested data ]")
print("Appliance name:")
appName = input()
print("Cost per KW - hr of the appliance (in cents):")
costPerKW4 = float(input())
print("Annual usage (in KW - hr):")
annualUsage4 = float(input())
total += annualUsage4 * costPerKW4
costPerKW.append(costPerKW4)
annualUsage.append(annualUsage4)

# FifthApp
print("[ Please enter the requested data ]")
print("Appliance name:")
appName = input()
print("Cost per KW - hr of the appliance (in cents):")
costPerKW5 = float(input())
print("Annual usage (in KW - hr):")
annualUsage5 = float(input())
total += annualUsage5 * costPerKW5
costPerKW.append(costPerKW5)
annualUsage.append(annualUsage5)

# SixthApp
print("[ Please enter the requested data ]")
print("Appliance name:")
appName = input()
print("Cost per KW - hr of the appliance (in cents)S:")
costPerKW6 = float(input())
print("Annual usage (in KW - hr):")
annualUsage6 = float(input())
total += annualUsage6 * costPerKW6
costPerKW.append(costPerKW6)
annualUsage.append(annualUsage6)

# Calculate the average
avg = sum(costPerKW) / len(costPerKW)

# Calculate the variance
variance = sum((avg - cost) ** 2 for cost in costPerKW) / len(costPerKW)

# Calculate the standard deviation
stdDev = variance ** 0.5

print("The total cost of the annual usage is $%.2f" % total)
print("Average cost per KW - hr: $%.4f" % avg)
print("Variance of cost per KW - hr: $%.4f" % variance)
print("Standard deviation of cost per KW - hr: $%.4f" % stdDev)


