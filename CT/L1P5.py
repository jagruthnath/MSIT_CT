n=int(input("Enter n : "))
sum=0
while(n>0):
	i=n%10
	sum+=i
	n=n//10
print(sum)