# generate two integers for number1 and number2
# if n1 is less than n2 swap the two numbers
# prompt the student to ansner the question " What is n1-n2 ?"
# check whether the students answer is correct

import random

n1 = random.randint(0,100)
n2 = random.randint(0,100)

if n1 < n2 :
 n1,n2 = n2,n1

diff1 = n1 - n2

print("what is ", n1 , "-", n2,"?")
result = eval(input("result = "))

if result == diff1 :
 print("Bingo! correct answer")
else :
 print("OOPs! Wrong answer")
