import sys
# sys.stdin=open('input.txt','r')
# sys.stdout=open('output.txt','w')

name=input("What is Your Name? ")
print("Hello "+name)
number=int(input("Give an integer Number: "))
print(type(number))
print(f"Your input number is: {number}")

floatVal=float(input("Enter a float Value: "))
print(f"Type: {type(floatVal)}, Entered float value is: {floatVal}")

birth_Year=input("Enter Your Birth Year: ")
age=2025-int(birth_Year)
print(f"Your age is: {age}")

number2=int(input("Input one Number: "))
print(f"The Square of this Number is: {number2**2}")