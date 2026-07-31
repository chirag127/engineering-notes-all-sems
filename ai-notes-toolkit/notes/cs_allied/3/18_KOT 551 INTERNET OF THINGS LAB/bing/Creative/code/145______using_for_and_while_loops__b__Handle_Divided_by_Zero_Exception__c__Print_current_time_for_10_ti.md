Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic you requested:

#### Using for and while loops
- A for loop is a repetition control structure that allows you to efficiently write a loop that needs to execute a specific number of times.
- A while loop is a repetition control structure that allows you to write a loop that will repeat as long as a condition is true.
- The syntax of a for loop is:

```
for (initialization; condition; update) {
  // statements to be executed
}
```

- The syntax of a while loop is:

```
while (condition) {
  // statements to be executed
}
```

- For example, to print the numbers from 1 to 10 using a for loop, you can write:

```
for (int i = 1; i <= 10; i++) {
  System.out.println(i);
}
```

- To print the numbers from 1 to 10 using a while loop, you can write:

```
int i = 1;
while (i <= 10) {
  System.out.println(i);
  i++;
}
```

#### Handle Divided by Zero Exception
- An exception is an event that occurs during the execution of a program that disrupts the normal flow of instructions.
- A divided by zero exception is a type of arithmetic exception that occurs when an integer is divided by zero.
- To handle an exception, you can use a try-catch block, which consists of two parts: a try block and a catch block.
- The try block contains the code that may cause an exception, and the catch block contains the code that handles the exception if it occurs.
- The syntax of a try-catch block is:

```
try {
  // code that may cause an exception
} catch (ExceptionType e) {
  // code that handles the exception
}
```

- For example, to handle a divided by zero exception, you can write:

```
try {
  int a = 10;
  int b = 0;
  int c = a / b; // this may cause a divided by zero exception
  System.out.println(c);
} catch (ArithmeticException e) {
  // this block will execute if a divided by zero exception occurs
  System.out.println("Cannot divide by zero");
}
```

#### Print current time for 10 times with an interval of 1 second
- To print the current time, you can use the System.currentTimeMillis() method, which returns the current time in milliseconds since the epoch (January 1, 1970, 00:00:00 GMT).
- To format the time in a human-readable way, you can use the SimpleDateFormat class, which allows you to specify a pattern for the date and time.
- To create a delay of 1 second, you can use the Thread.sleep() method, which pauses the current thread for the specified number of milliseconds.
- To repeat the task for 10 times, you can use a for loop or a while loop.
- For example, to print the current time for 10 times with an interval of 1 second using a for loop, you can write:

```
// create a SimpleDateFormat object with the desired pattern
SimpleDateFormat sdf = new SimpleDateFormat("hh:mm:ss a");

// use a for loop to repeat the task 10 times
for (int i = 0; i < 10; i++) {
  // get the current time in milliseconds
  long time = System.currentTimeMillis();
  // format the time using the SimpleDateFormat object
  String formattedTime = sdf.format(time);
  // print the formatted time
  System.out.println(formattedTime);
  // create a delay of 1 second
  try {
    Thread.sleep(1000);
  } catch (InterruptedException e) {
    e.printStackTrace();
  }
}
```