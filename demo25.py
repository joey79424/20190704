day0fweek = ['Sunday', 'Monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
length = []
for i in day0fweek:
    length.append(len(i))
    pass
print length

print [len(day) for day in day0fweek]
print [day for day in day0fweek]
print [day for day in day0fweek if len(day) > 6]
sun, mon, tue, wed, thu, fri, sat = day0fweek
print sun, wed, fri
print tue, thu, sat
number_list = [3, 1, 4, 1, 5, 9, 26, 83, 47, 100, 29, 5, 7]
s1 = sorted(e for e in number_list if e > 10)
print s1
s2 = sorted(number_list)
print s2
s3 = sorted((e for e in number_list if e < 40), reverse=True)
print s3
