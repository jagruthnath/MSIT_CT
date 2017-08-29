for x in range(100):
	flag=0
	if x%3==0:
		flag+=3
	if x%5==0:
		flag+=5
	if flag==3:
		print("Hello")
	elif flag==5:
		print("World")
	elif flag==8:
		print("Hello World")
	else:
		print(x)