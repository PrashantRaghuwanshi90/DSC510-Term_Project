count = 0;

# Opens a file in read mode
file = open('C:/Users/dell/Desktop/MS_DataScience/sourcefile/gettysburg.txt', 'r')

# Gets each line till end of file is reached
for line in file:
    # Splits each line into words
    words = line.split(" ");
    # Counts each word
    print(words)
    print(count)
    count = count + len(words);

print("Number of words present in given file: " + str(count));
file.close();