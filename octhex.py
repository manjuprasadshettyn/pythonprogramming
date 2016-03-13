#The following program demonstrates conversion of a decimal value into
#octal and hexa and vice versa.

a=0o25
b=0x0f
print ('Value of a in decimal is', a)
print ('Value of b in decimal is', b)
c=19
print ('19 in octal is %o and in hex is %x' %(c,c))
d=oct(c)
e=hex(c)
print ('19 in octal is', d, 'and in hexa is', e)
