#n=int(input("Enter Number : "))
n=111
a=0
j=0
while n!=0:
	i=n%10
	n=n//10
	a=a+i*(2**j)
	j+=1
print(a)