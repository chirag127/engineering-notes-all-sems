 Here are the key points to cover for the given topic:

1. Take input from the user for the word to search in the file.
2. Open the file in read mode.
3. Use a loop to traverse through each line of the file.
4. Split each line into words and check if the user input word exists in the line.
5. If exists, increment a counter variable each time the word is found.
6. After traversing through the complete file, print the counter variable which will contain the total occurrences of the word in the file.
7. If the word is not found in the file at all, print a message stating the same.

The code can be written as follows:

word = input("Enter the word to search: ")
count = 0
with open("file.txt", "r") as f:
    for line in f:
        words = line.split()
        if word in words:
            count += 1
if count > 0:
    print(f"The word {word} occurs {count} times in the file.")
else:
    print(f"The word {word} does not exist in the file.")

The above code first takes input from the user for the word to search. It then opens the file in read mode and traverses through each line. For each line, the line is split into words and checked for the existence of the user input word. If found, a count variable is incremented. After completing the traversal, the count is printed if greater than 0, else a message is printed stating the word does not exist in the file.