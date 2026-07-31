 Here is the formal content on the given topic:

####Using For and While Loops

I. For Loop

A. For loop is used to repeat a block of code for a specified number of times.

B. Syntax:
for (init counter; condition; increment)
{
    // code block to be executed
}

C. Working:
1. The init counter variable is used to initialize the counter variable. It is executed one time at the start.
2. The condition is checked. If it evaluates to true, the code block is executed.
3. After the code block finishes execution, the increment part is executed.
4. Again the condition is checked. If it evaluates to true, the code block is executed. This process repeats until the condition evaluates to false.

II. While Loop

A. While loop repeats a code block as long as the specified condition is true.

B. Syntax:
while (condition)
{
    // code block to be executed
}

C. The code block is executed repeatedly as long as the condition evaluates to true. Once the condition becomes false, the loop exits.

III. Printing Current Time 10 Times

A. We can use a for loop to print the current time 10 times.

B. Syntax:
for (int i = 0; i < 10; i++)
{
    // Print current time
}

C. On each iteration of the for loop, the current time will be printed. This will be done 10 times as specified by the loop condition.

IV. Handling Divide By Zero Exception

A. An exception occurs when there is an error in the execution of a program.

B. Divide By Zero is an exception which occurs when a number is divided by zero.

C. To handle this, we use a try-catch block. The code which can cause an exception is written in the try block. The catch block handles the exception if it occurs.

D. Syntax:
try
{
    // Code which may cause exception
}
catch (Exception e)
{
    // Handle the exception here
}