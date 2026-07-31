# Reading a File Line by Line and Printing Word Count of Each Line

In this topic, we will learn how to read a file line by line and count the number of words in each line using Python. This can be useful for analyzing text data and extracting information from large datasets.

## Steps to Read a File Line by Line

1. Open the file using the `open()` function in Python. The file should be in the same directory as your Python script or you can provide the file path.

   ```
   file = open('filename.txt', 'r')
   ```

2. Use a `for` loop to read the file line by line.

   ```
   for line in file:
       print(line)
   ```

3. Close the file using the `close()` function.

   ```
   file.close()
   ```

## Steps to Count Words in Each Line

1. Use the `split()` function to split each line into a list of words.

   ```
   words = line.split()
   ```

2. Use the `len()` function to count the number of words in the list.

   ```
   word_count = len(words)
   ```

3. Print the word count for each line.

   ```
   print(word_count)
   ```

## Putting it All Together

Here's an example script that reads a file line by line and prints the word count for each line:

```
file = open('filename.txt', 'r')

for line in file:
    words = line.split()
    word_count = len(words)
    print(word_count)

file.close()
```

You can modify this script to suit your needs, such as writing the word count to a new file or adding additional analysis to the text data.

## Conclusion

Reading a file line by line and counting the number of words in each line is a useful skill for analyzing text data in Python. By following these steps, you can easily extract information and insights from large datasets.