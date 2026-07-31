
#### Interval of 10 Seconds
1. To read a file line by line and print the word count of each line, we can use the `readlines()` method. This method reads the entire file into memory, then splits it into separate lines.
2. To get the word count of each line, we can use the `len()` function. This function takes a string as an argument and returns the length of that string.
3. We can then loop through the lines in the file and print the word count for each line. For example, the following code will print the word count of each line in the file:
```python
file = open("myfile.txt")
lines = file.readlines()
for line in lines:
    print("Line Word Count:", len(line))
```
4. Finally, we can use the `time.sleep()` function to pause the program for a given interval of time. This function takes a single argument, which is the number of seconds to pause the program for. For example, the following code will pause the program for 10 seconds:
```python
import time
time.sleep(10)
```