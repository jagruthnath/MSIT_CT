n=int(input("Enter Number : "))
f=[]
print("Enter ",n,"numbers : ")
for x in range(n):
	f.append(int(input()))
s=int(input("Enter search element : "))
try:
    k=f.index(s)
    print("Element found at position",k)
except ValueError:
	print("Element not found")