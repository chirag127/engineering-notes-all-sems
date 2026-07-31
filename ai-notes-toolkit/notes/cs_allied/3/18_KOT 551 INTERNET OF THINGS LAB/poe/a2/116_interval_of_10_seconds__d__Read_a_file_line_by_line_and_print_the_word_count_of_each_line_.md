 Here is the formal content in Markdown format without any emojis or external links:

# Read a file line by line and print the word count of each line

1. Open the file in read mode
2. Read the file line by line using a loop
3. Split each line into words using .split()
4. Count the number of words in each line using len()
5. Print the word count for each line

Example:

f = open("file.txt", "r")
for line in f:
    words = line.split()
    count = len(words)
    print("Line{}: {}".format(count, line.strip()))
f.close()

This program will read the file line by line and print the word count for each line. The output will be in the format "Line5: This is a line with 5 words".

Does this meet your requirements? Let me know if you would like me to modify or expand the content in any way.