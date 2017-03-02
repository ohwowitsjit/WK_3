num = int(input("Enter the number: "));
square = 0;
file=open("perfect_squares.txt", "w")
for i in range(1, num):
	square=i*i;
	if (square<num):
		file.write(str(square)+ "\n");
	elif (square >= num):
		break;
file.close();