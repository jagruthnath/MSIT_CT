c=0
for i in range(100):
	if i%10==7:
		c+=1
	if i//10==7:
		c+=1
print(c)