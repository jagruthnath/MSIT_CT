n=input("Enter credit card number : ")
#n="0234567812345678"
if len(n)==16:
	if n[0:1]!='0':
		print("Valid")
	else:
		print("Invalid")