st=input("Enter a string : ")
v=[]
c=[]
for x in st:
	if(x=='a' or x=='A' or x=='e' or x=='E' or x=='i' or x=='I'  or x=='o' or x=='O' or x=='u' or x=='U'):
		v.append(x)
	else:
		c.append(x)
print("Vowels are :",v)
print("Consonants are :",c)