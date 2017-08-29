n=int(input("Enter a number : "))
i=n//10
j=n%10
if i==7:
	if j>=5:
		print("B")
	else:
		print("C")
else:
	if i==8:
		if j>=5:
			print("A")
		else:
			print("B+")
	else:
		if i==9:
			if j>=5:
				print("EX")
			else:
				print("A+")
		else:
			print("F")