a=int(input("Enter a : "))
b=int(input("Enter b : "))
if a>b:
	big=a
else:
	big=b
flag=0
while flag==0:
	if big%a==0 and big%b==0:
		flag=1
	else:
		big+=1
print(big)