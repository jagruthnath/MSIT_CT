n=int(input("Enter n : "))
m=n
f=[]
while n!=0:
	f.append(n%10)
	n=n//10
big=f[0]*f[1]*f[2]
for x in range(3,len(f)-2):
	val=f[x]*f[x+1]*f[x+2]
	if big<val:
		big=val
print(big)