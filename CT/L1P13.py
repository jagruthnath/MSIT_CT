#n=int(input("Enter n : "))
n=4
m=1
k=1
for x in range(n):
	for y in range(x+1):
		print(m," ", end="")
		m+=1
	print(" ")
	m=k+1
	k=k+1