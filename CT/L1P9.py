n=int(input("Enter n : "))
f=[]
c=[]
print("Enter ",n," elements")
for x in range(n):
	f.append(int(input()))
for x in range(n):
	c.append(f.count(x))
big=c.index(max(c))
print("Mode is ",f[big])