m=[]
n=[]
m.append(int(input("Enter m : ")))
n.append(int(input("Enter n : ")))
sum=0
i=0
while m[i]>1:
	m.append(m[i]//2)
	n.append(n[i]*2)
	i+=1
for x in range(len(n)):
	if m[x]%2==0:
		n[x]=0
	sum+=n[x]
print (sum)