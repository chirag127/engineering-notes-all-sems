#### Using for and while loops
- A for loop is a repetition control structure that allows you to efficiently write a loop that needs to execute a specific number of times.
- A while loop is a repetition control structure that allows you to write a loop that will repeat as long as a condition is true.
- The syntax of a for loop is:

```
for (initialization; condition; update) {
  // statements
}
```

- The syntax of a while loop is:

```
while (condition) {
  // statements
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
- A divided by zero exception is an error that occurs when you try to divide a number by zero, which is not allowed in mathematics.
- To handle a divided by zero exception, you can use a try-catch block, which is a way of dealing with errors in Java.
- A try-catch block consists of two parts: a try block and a catch block. The try block contains the code that may cause an error, and the catch block contains the code that will execute if an error occurs.
- The syntax of a try-catch block is:

```
try {
  // code that may cause an error
}
catch (ExceptionType e) {
  // code that will execute if an error occurs
}
```

- For example, to handle a divided by zero exception, you can write:

```
try {
  int a = 10;
  int b = 0;
  int c = a / b; // this will cause a divided by zero exception
  System.out.println(c);
}
catch (ArithmeticException e) {
  // this will execute if a divided by zero exception occurs
  System.out.println("Cannot divide by zero");
}
```

#### Print current time for 10 times with an interval of 1 second
- To print the current time, you can use the System.currentTimeMillis() method, which returns the current time in milliseconds since January 1, 1970.
- To format the time in a human-readable way, you can use the SimpleDateFormat class, which allows you to specify a pattern for the date and time.
- To create a delay of 1 second, you can use the Thread.sleep() method, which pauses the execution of the current thread for a specified number of milliseconds.
- To print the current time for 10 times with an interval of 1 second, you can write:

```
// create a SimpleDateFormat object with the desired pattern
SimpleDateFormat sdf = new SimpleDateFormat("HH:mm:ss");

// create a for loop to repeat 10 times
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
  }
  catch (InterruptedException e) {
    // handle the interruption
    e.printStackTrace();
  }
}
```