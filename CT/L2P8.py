n=int(input("Enter n : "))
a=[]
i=0
if n>0:
	i=n
	flag=0
	while i!=0 and flag==0:
		x=i
		while x!=0:
			a.append(x%10)
			x=x//10
		p=len(a)-1
		flag2=0
		while p!=0 and flag2==0:
			if a[p-1]<a[p]:
				flag2=1
			p-=1
		if flag2==0:
			flag=1
		i-=1
	print(i+1)