st = input("Enter year : ")
d=int(st[6:len(st)])
if d%4==0:
	if d%100==0:
		if d%400==0:
			print (d," is a leap year")
		else:
			print(d," is not a leap year")
	else:
		print (d," is a leap year")
else:
	print(d," is not a leap year")