 Here is the formal content written in Markdown format using for and while loops without any emojis or external links:

# Using Loops

## For Loop

For loops are used to repeat a block of code a specified number of times.

For example:

```
for (int i = 0; i < 5; i++)
{
    Print(i);
}
```

This will print the numbers 0 to 4.

The loop has three parts:

1. Initialization (int i = 0) - This is executed one time at the beginning.
2. Condition (i < 5) - This is checked before every loop iteration. The loop continues iterating while this evaluates to true.
3. Update (i++) - This is executed at the end of every loop iteration. Generally, this is used to update the variable used in the condition.

## While Loop

While loops repeat a block of code while a specified condition is true.

For example:

```
int i = 0;
while (i < 5)
{
    Print(i);
    i++;
}
```

This will also print the numbers 0 to 4.

The loop evaluates the condition before each iteration and continues iterating while it evaluates to true.

## Handling Divide By Zero Exception

Attempting to divide a number by zero causes a divide by zero exception. This can be avoided using an if check:

```
int x = 5;
int y = 0;

if (y != 0)
{
    int result = x / y;
}
```

Here, the code in the if block will not run if y is zero, and so the exception will be avoided.

## Printing Current Time

The current time can be printed using the DateTime module:

```
for (int i = 0; i < 10; i++)
{
    Console.WriteLine(DateTime.Now);
}
```

This will print the current time 10 times.