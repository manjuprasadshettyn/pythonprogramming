# PRIME NUMBER IN RANGE OF 1 AND 50

for i in range(2,50):
      x=1
      for j in range(2, i):
            n=i%j
            if n==0:
               x=0
               break
      if x==1:
        print (i)
