file_read = open("iris.data.txt", "r");
contents = [];

for line in file_read:
	print(str(line));
file_read.close()
