# Chinese Zodiac sign is based on 12 year cycle and each year is represented by an animal.

year= eval(input("Enter your birth year "))

sign=year%12

print("your Chinese Zodiac Sign is ")

if sign==0 :
 print("Sheep")
elif sign == 1 :
 print("Monkey")
elif sign == 2 :
 print("Roaster")
elif sign == 3 :
 print("Dog")
elif sign == 4 :
 print("Pig")
elif sign == 5 :
 print("Rat")
elif sign == 6 :
 print("Ox")
elif sign == 7 :
 print("Tiger")
elif sign == 8 :
 print("Rabit")
elif sign == 9 :
 print("Dragon")
elif sign == 10 :
 print("Snake") 
elif sign == 11 :
 print("Horse")
else :
 print("Invalid Input")

