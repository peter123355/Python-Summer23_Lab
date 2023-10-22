# Name : Peter Geevarghese Alex
# Lab 4

# Description :
import time
print("Programmer: Peter Geevarghese Alex")

x = 12
print("-" * 25)
## dd/mm/yyyy format
print (time.strftime("%d/%m/%Y"))



#military time
print ("Current time:",time.strftime("%X"))

# If the card number is valid, this function returns True
def isValid(number):
    total = sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)
    return total % 10 == 0

# Obtain the result from Step 2
def sumOfDoubleEvenPlace(number):
    total = 0
    num = str(number)
    for i in range(len(num)-2, -1, -2):
        total += getDigit(int(num[i]) * 2)
    return total

# If the variable number is a single digit, then return the number
# Otherwise, return the number as the sum of the two digits
def getDigit(number):
    if number < 10:
        return number
    else:
        return (number % 10) + (number // 10)

# This function returns the sum of odd place digits in variable number
def sumOfOddPlace(number):
    total = 0
    num = str(number)
    for i in range(len(num)-1, -1, -2):
        total += int(num[i])
    return total

# If the digit d is a prefix for variable number, then return True
def prefixMatched(number, d):
    return getPrefix(number, len(str(d))) == d

# This function returns the number of digits in variable d
def getSize(d):
    return len(str(d))

# Returns the first k number of digits from variable number, but if the
# number of digits in variable number is less than k, return number
def getPrefix(number, k):
    num = str(number)
    if len(num) < k:
        return number
    else:
        return int(num[:k])

# Prompt the user to enter a credit card number
credit_card_number = int(input("Enter a credit card number: "))

# Check if the credit card number is valid and display the result
if isValid(credit_card_number):
    print("Valid credit card number")
else:
    print("Invalid credit card number")
