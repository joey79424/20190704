#encoding =UTF-8
print '%10s' % '1234567890'
print '%10s' % '1234567890'[:5]
print '%10s' % '1234567890' * 2
print '%10s' % '555'
print '%10s' % '中文'
print '%10s' % u'中文'
print '{:10s}==='.format('01234')
print '{:>10s}==='.format('01234')
print '{:>10s}==='.format('中文')
print u'{:>10s}==='.format(u'中文')