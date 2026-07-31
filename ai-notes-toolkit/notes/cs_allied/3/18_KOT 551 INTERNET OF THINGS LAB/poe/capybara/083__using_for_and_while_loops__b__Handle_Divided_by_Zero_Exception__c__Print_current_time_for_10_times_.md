#### Using For and While Loops

- Loops are programming constructs that allow the repetition of a set of instructions until a certain condition is met.
- Python has two main types of loops: for loops and while loops.
- For loops are used to iterate over a sequence of elements, such as a list or a string.
- While loops are used to repeat a block of code as long as a specified condition is true.

#### Handling Divided by Zero Exception

- Dividing by zero is a mathematical error and can cause a program to crash.
- To handle this error in Python, we can use a try-except block.
- The try block contains the code that might cause the error, and the except block contains the code to handle the error.
- In the case of a divide by zero error, we can print an error message and exit the program gracefully.

#### Printing Current Time for 10 Times with an

- To print the current time in Python, we can use the datetime module.
- We can create a datetime object that represents the current time using the `datetime.now()` function.
- To print the current time multiple times, we can use a for loop that iterates 10 times.
- We can use the `time.sleep()` function to add a delay between each print statement, which can make the output easier to read.
- To add the word "an" before each printed time, we can use an f-string and format the time object using the `strftime()` function.