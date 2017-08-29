a=int(input("Enter a : "))
b=int(input("Enter b : "))
if a<b:
	a,b=b,a
flag=0
temp=0
i=0
while flag==0:
	if a%b==0:
		flag=1
	else:
		temp=a
		a=b
		b=temp%b
	i+=1
print(b)