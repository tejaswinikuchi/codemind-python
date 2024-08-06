m = int(input())
h = m//60
min = m%60
d = '{:.0f}'.format(h)
c = '{:.0f}'.format(min)
print(str(d) + ' Hour(s)' +" "+ str(c) + ' Minute(s)')