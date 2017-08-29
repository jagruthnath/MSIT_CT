n=3
m=2
c=0
while c!=n:
	flag=0
	i=2
	while i<=m//2 and flag==0:
		if m%i==0:
			flag=1
		else:
			i+=1
	if flag==0:
		c+=1
	m+=1
print(m-1)