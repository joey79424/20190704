class course:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def __str__(self):
        return '[course](name=%s)(duration=%d)' % (self.name, self.duration)

    def __repr__(self):
        return '[curse]{name=%s\n, duration=%s\n}' % (self.name, self.duration)


c1 = course('BDPY', 35)
c2 = course('BDR', 35)
print 'c1=%s,c2=%s' % (c1, c2)
print c1
print [c1]
print '%s,%r' % (c1, c2)
print '{0!s},{0!r}'.format(c1)
