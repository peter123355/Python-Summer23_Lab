# Description :To write a program that will generate a person’s BMI result based on the persons weight and height.
import time

print("Programmer: Peter Geevarghese Alex")

x = 12
print("-" * 25)


# mm/dd/yy format
print ("Date:",time.strftime("%x"))

#military time
print ("Current time:",time.strftime("%X"))
# Menu 1
print("Unit System Menu:")
print("1. Customary English units")
print("2. Metric units")
choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    # Input weight and height in customary English units
    print("Prompt the User for the Person Weight (in pounds U.S.)")
    weight = float(input())
    print("Prompt the User for the Person Height (in inches U.S.)")
    height = float(input())
    unit_system = "english"
elif choice == 2:
    # Input weight and height in metric units
    print("Prompt the User for the Person Weight (in kilograms)")
    weight = float(input())
    print("Prompt the User for the Person Height (in meters)")
    height = float(input())
    unit_system = "metric"
else:
    print("Invalid choice.")
    exit()

#Compute the BMI
if unit_system == "english":
    # Compute the BMI using customary English units
    BMI = (weight * 703) / (height ** 2)
else:
    # Compute the BMI using metric units
    BMI = weight / (height ** 2)
print (BMI)
if BMI < 18.5 :
	print(" Person is Underweight")   
elif BMI >=18.5 and BMI <=24.9:
	print ("the Person is Normal")
elif BMI >=25.0 and BMI <=29.9:
	print("the Person is Overweight ") 
else:	 
    print("the Person is Obese")




