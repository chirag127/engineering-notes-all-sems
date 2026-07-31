## 32. WAP to check whether a given word exists in a file or not. If yes then find the number of times it occurs.

In programming, it is often required to search for a specific word or pattern in a file. This is a common task when dealing with large data sets or logs. In this program, we will learn how to check whether a given word exists in a file or not, and if it does, we will find the number of times it occurs.

### Steps to check whether a given word exists in a file or not

1. Open the file in read mode using the `open()` function. 
2. Read the contents of the file using the `read()` function and store it in a variable.
3. Close the file using the `close()` function.
4. Convert the contents of the file to lowercase using the `lower()` function. This is done to ensure that the search is not case-sensitive.
5. Prompt the user to enter the word they want to search for and store it in a variable.
6. Use the `count()` function to count the number of occurrences of the word in the file. 
7. If the count is greater than zero, print the number of occurrences of the word in the file. Otherwise, print that the word does not exist in the file.

### Program Implementation

```
# Step 1: Open the file in read mode
file_name = input("Enter the file name: ")
try:
    file = open(file_name, "r")

    # Step 2: Read the contents of the file
    contents = file.read()

    # Step 3: Close the file
    file.close()

    # Step 4: Convert the contents to lowercase
    contents = contents.lower()

    # Step 5: Prompt the user to enter the word they want to search for
    word = input("Enter the word to search: ")

    # Step 6: Count the number of occurrences of the word
    count = contents.count(word)

    # Step 7: Print the number of occurrences of the word
    if count > 0:
        print("The word", word, "was found", count, "times in the file.")
    else:
        print("The word", word, "was not found in the file.")

except FileNotFoundError:
    print("File not found. Please check the file name and try again.")
```

### Conclusion

In this program, we have learned how to check whether a given word exists in a file or not, and if it does, we have found the number of times it occurs. This is a useful tool when dealing with large data sets and logs, as it allows us to quickly and easily search for specific information within the file.