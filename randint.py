# generate two  integers for number1 and number2
# prompt the student to ansner the question " What is n1+n2 ?"
#check whether the students answer is correct

import random

n1 = random.randint(0,100)
n2 = random.randint(0,100)

sum1 = n1 + n2

print("what is ", n1 , "+ ", n2,"?")
result = eval(input("result = "))

if result == sum1 :
 print("Bingo! correct answer")
else :
 print("OOPs! Wrong answer")
