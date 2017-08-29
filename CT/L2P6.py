def prime(m):
	i=2
	flag=0
	if(m==1):
		return flag+1
	while i<=m//2 and flag==0:
		if m%i==0:
			flag=1
		i+=1
	return flag
#n=int(input("Enter n : "))
n=99999999
i=2
j=1
f=[]
f.append(1)
while i<=n/2:
	if n%i==0:
		f.append(i)
	i+=1
f.append(n)
for x in range(len(f)-1):
	flag=prime(f[x])
	if flag==0:
		k=f[x]	
print(k)