n=int(input("Enter a number : "))
j=0
k=1
p=1
print("0 ",end="")
for x in range(n):
	print(p," ",end="")
	p=j+k
	j=k
	k=p