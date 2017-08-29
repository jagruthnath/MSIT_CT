n=int(input("Enter n : "))
m=n
k=0
while n!=0:
	j=n%10
	k=k+(j**3)
	n=n//10
if k==m:
	print(m,"is armstrong")
else:
	print(m,"is not armstrong")