t=input("Enter time in HH:MM:SS : ")
f=0
for x in range(len(t)):
	if x!=':':
		f=(f*10)+(ord(x)-48)	
h=f//100000
f=f%100000
m=f/100
s=f%100
print((h*3600)+(m*60)+s)