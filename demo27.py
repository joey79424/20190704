l1 = ['sunday', 'monday', 'tuesday']
t1 = ('sunday', 'monday', 'tuesday')
print type(l1), type(t1), len(l1), len(t1)
print [len(e) for e in l1]
print [len(e) for e in t1]
# l1 += 'wedwsday'
print "before add list:", hex(id(l1))
l1.append('wedesday')
print l1
print "before add list:", hex(id(l1))
print "\n"
print "before add tuple:", hex(id(l1))
t1 += ('wedesday',)
print t1
print "before add tuple:", hex(id(l1))
s2 = ('thursday')
t2 = ('thursday',)
print type(s2), type(t2)
print s2 * 5
print t2 * 5


print len(t1), t1[0],t1[2],t1[3],t1[1]
print 'day' in s2
print 'day' in t2 , 'thursday' in t2


day0fweek = ['Sunday', 'Monday', 'tuesday', 'wednesday', 'thursday', 'friday']

def split_head(x):
    return seq[s2],seq[t2]
head,remaining = split_head(day0fweek)
print type(remaining),len(remaining),remaining