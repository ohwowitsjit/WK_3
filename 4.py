num = int(input("Enter a positive integer to check if it is a prime:"));
found = False;
file = open("primes1000000.txt", "r");

if num >= 999983*999983:
	print("Your number is too big to calculate, please retry with a smaller number. Sorry whoops :D")
elif num < 1000000:
	for line in file:
		if (num == int(line)):
			found = True;
			break;
		
	file.close();
	print(str(found));
elif num > 1000000:
	found = True;
	for line in file:
		if (num%int(line)==0):
			found = False;
			break;
	
	file.close();
	print(str(found));
