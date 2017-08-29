n=int(input("Enter n : "))
f=[]
print("Enter n elements : ")
for x in range(n):
	f.append(int(input()))
s=set(f)
print(s)