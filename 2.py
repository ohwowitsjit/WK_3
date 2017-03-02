start_num = int(input("Enter the number n:"));
end_num = int(input("Enter the number n:"));

file = open("perfect_squares.txt", "a")

file.write("\n\n");
for i in range(1, end_num+1):
	file.write(str(i+start_num) + "\n")
	
file.close();