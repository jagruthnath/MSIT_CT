def prime(i,m):
	flag=0
	while i<=m//2 and flag==0:
		if m%i==0:
			flag=1
		i+=1
	return flag
def rev(m):
	i=2
	j=0
	while m!=0:
		j=(j*10)+(m%10)
		m=m//10
	return j
n=int(input("Enter n : "))
m=11
c=0
j=0
while c!=n:
	flag=0
	i=2
	flag=prime(i,m)
	q=m
	if flag==0:
		j=rev(m)
		flag=prime(i,j)
		if flag==0:
			c+=1
	m+=1
print(q)