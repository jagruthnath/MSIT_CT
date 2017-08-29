n=int(input("Enter n : "))
i=2
j=1
f=[]
f.append(1)
print("Factors of ",n," are")
while i<=n/2:
	if n%i==0:
		f.append(i)
	i+=1
f.append(n)
print (f)