bdate =0

print("1 3 5 7\n9 11 13 15\n17 19 21 23\n25 27 29 31\nIs your bdate is in this set(y/n)?")
if('y'==input()):
  bdate+=1

print("2 3 6 7\n10 11 14 15\n 18 19 22 23\n26 27 30 31\nIs your bdate is in this set(y/n)?")
if('y'==input()):
  bdate+=2

print("4 5 6 7\n12 13 14 15\n20 21 22 23\n28 29 30 31\nIs your bdate is in this set(y/n)?")
if('y'==input()):
  bdate+=4

print("8 9 10 11\n12 13 14 15\n24 25 26 27\n28 29 30 31\nIs your bdate is in this set(y/n)?")
if('y'==input()):
  bdate+=8

print("16 17 18 19\n20 21 22 23\n24 25 26 27\n28 29 30 31\nIs your bdate is in this set(y/n)?")
if('y'==input()):
  bdate+=16

print("Your bdate is: ",bdate)
