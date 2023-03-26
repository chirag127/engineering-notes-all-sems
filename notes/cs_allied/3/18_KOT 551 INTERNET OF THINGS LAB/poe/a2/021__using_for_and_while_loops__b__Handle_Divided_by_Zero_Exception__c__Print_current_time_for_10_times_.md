 Here is the formal content on the given topic:

####Using For and While Loops

I. For Loop

1. For loop is used to repeat a set of statements for a given number of times.
2. The for loop consists of 3 parts:

- Initialization: Run once at the beginning. Usually to declare and initialize a counter variable.
- Condition: Checked before every loop iteration. The loop continues until this evaluates to false.
- Increment: Run after each loop iteration. Usually increments the counter variable.

3. Syntax:
for (initialize; condition; increment) {
    // statements to be executed
}

II. While Loop

1. While loop repeats a set of statements as long as a specified condition is true.
2. Syntax:
while (condition) {
    // statements to be executed
}

3. The condition is checked before each iteration. If it evaluates to true, the statements inside the loop are executed. This repeats until the condition becomes false.

III. Handling Divided By Zero Exception

1. Dividing a number by zero results in an error called Divide By Zero exception.
2. To handle this, we use a try-catch block.
3. Syntax:
try {
    // code that may generate the exception
} catch (ExceptionType e) {
    // handle the exception here
}

4. In the catch block, we can print an appropriate error message or perform some other action to handle the exception.

IV. Printing Current Time

1. We can use the Date object to print the current time.
2. Create a Date object and use its methods like getHours(), getMinutes(), getSeconds() to extract the current time values.
3. Print the values to display the time.
4. To print the time 10 times, we can use a for loop with count ranging from 1 to 10.