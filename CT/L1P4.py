n = int(input("Enter a number : "))
flag=0
if n==1:
	print(n,"is neither prime nor composite")
elif n<1:
	print(n,"is negative")
else:
	if n!=2:
		for i in range(2,(n//2)+1):
			if n%i==0:
				flag=1
			else:
				i+=1		
	if flag==0:
		print(n,"is prime")
	else:
		print(n,"is not prime")