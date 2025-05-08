for i in range(3):
	for j in range(5):
		if i+j==2 or i==2 or i-j==-2 or i-j==4:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print("\n")