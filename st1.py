def input():
        a = raw_input("enter a string")
        m=st(a)
	return m

def st(a):
        l=[]
        for i in a:
                if i != "=" and i != ";":
                        l.append(i)

        t=[]
        for i in range(len(l)):
                if i>0 and i%2==1:
                        t.append(((l[i-1]),(l[i])))
	return t

h=input()
print h
