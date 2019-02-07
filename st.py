a = raw_input("enter a string")

l=[]

for i in a:
	if i != "=" and i != ";":
		l.append(i)

print l

t=[]

for i in range(len(l)):
	if i>0 and i%2==1:
		t.append(((l[i-1]),(l[i])))

print t
