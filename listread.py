# read 10 numbers and store in list
list1=[]
for i in range (0,10) :
 num=eval(input("enter number"+str(i+1)+":" ))
 list1.append(num)

print("the entered list is ",list1)
