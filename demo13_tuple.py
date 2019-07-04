a = 5
b = 7
print "a=%d, b=%d" % (a, b)
temp = a
a = b
b = temp
print "a=%d , b=%d" % (a, b)
c = 6
d = 8
print "c=%d, b=%d" % (c, d)

c, d = c ,c
print "c=%d , d=%d" %(c,d)
e='hello word'
f=3.14
print "e=%s, f=%.3f" % (e,f)
e,f =f,e
print "e={},f={}" .format(e,f)
l1='A'
l2='K'
l3='Q'
l4='J'
l5='10'
print l1,l2,l3,l4,l5
