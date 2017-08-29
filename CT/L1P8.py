n=int(input("Enter n : "))
f=[]
print("Enter ",n," elements")
for x in range(n):
	f.append(int(input()))
f.sort()
if n%2!=0:
	print("Median is ",f[n//2])
else:
	print("Median is ",((f[(n//2)]+f[(n//2)-1])/2))