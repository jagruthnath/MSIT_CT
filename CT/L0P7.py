n=int(input("Enter n "))
f=[]
sum=0
print("Enter ",n," elements")
for x in range(n):
	f.append(int(input()))
	sum+=f[x]
print("Mean is ",sum/n)