#Program to find the given nuber is positive or negative or 0
num = float(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


#Program to find the year entered s leap year or non leap year
year = int(input("Enter a year you want"))
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))
elif (year % 4 == 0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))


#program to display the calender
import calendar

yy = int(input("Enter an year"))
mm = int(input("Enter a month"))

print(calendar.month(yy, mm))


#Python program to convert decimal into other number systems
dec = int(input("Enter a number"))

print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")

