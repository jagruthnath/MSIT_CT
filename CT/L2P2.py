st=input("Enter a string : ")
flag=0
i=0
j=len(st)-1
while i<=j and flag==0:
	if st[i]!=st[j]:
		flag=1
	i+=1
	j-=1
if flag==0:
	print("Palindrome")
else:
	print("Not palindrome")