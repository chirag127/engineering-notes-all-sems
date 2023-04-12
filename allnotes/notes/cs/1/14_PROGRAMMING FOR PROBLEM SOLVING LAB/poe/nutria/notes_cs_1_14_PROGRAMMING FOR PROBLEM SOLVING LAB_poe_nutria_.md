


## 1. WAP that accepts the marks of 5 subjects and finds the sum and percentage marks obtained by the student.

1. Create a program that allows the user to enter the marks of five subjects.
2. Calculate the sum of the marks and store it in a variable.
3. Calculate the percentage of the marks obtained by the student and store it in a variable.
4. Display the sum of the marks and the percentage of the marks obtained by the student.




## 2. WAP that Calculates the Simple Interest and Compound Interest

1. Simple Interest (SI) is calculated by the formula `SI = (P x R x T)/100`, where `P` is the principal amount, `R` is the rate of interest, and `T` is the time period.

2. Compound Interest (CI) is calculated by the formula `CI = P (1+R/100)^T`, where `P` is the principal amount, `R` is the rate of interest, and `T` is the time period.

3. To calculate the Simple Interest and Compound Interest, the user must enter the principal amount, rate of interest and time period through the keyboard.

4. The program should then display the Simple Interest and Compound Interest on the screen.




## 3. WAP to calculate the area and circumference of a circle

1. Start by declaring two variables, one for the radius of the circle and one for the PI value.
2. Use the following formula to calculate the area of the circle: 
    `Area = PI * radius * radius`
3. Use the following formula to calculate the circumference of the circle:
    `Circumference = 2 * PI * radius`
4. Print the results of the area and circumference calculations.




## 4. WAP that accepts the temperature in Centigrade and converts into Fahrenheit using the formula C/5=(F-32)/9
* Temperature is measured in two scales - Celsius (or Centigrade) and Fahrenheit. 
* The formula for converting Celsius to Fahrenheit is `C/5=(F-32)/9` where C is the temperature in Celsius and F is the temperature in Fahrenheit.
* To write a program to convert temperature from Celsius to Fahrenheit, we need to:
    1. Take the temperature in Celsius as input from the user.
    2. Apply the formula `C/5=(F-32)/9` to calculate the temperature in Fahrenheit.
    3. Print the temperature in Fahrenheit.




## 5. WAP that swaps values of two variables using a third variable

1. Declare three variables, `a`, `b` and `temp`.
2. Assign values to `a` and `b`.
3. Assign the value of `a` to `temp`.
4. Assign the value of `b` to `a`.
5. Assign the value of `temp` to `b`.
6. Print the values of `a` and `b`.




## 6. WAP that checks whether the two numbers entered by the user are equal or not.

1. Start the program by prompting the user to enter two numbers.
2. Store the numbers in two separate variables.
3. Compare the two variables and check if they are equal.
4. If the two numbers are equal, print a message saying "The two numbers are equal".
5. If the two numbers are not equal, print a message saying "The two numbers are not equal".
6. End the program.




## 7. WAP to find the greatest of three numbers

1. Begin by declaring three variables, `a`, `b`, and `c`, which will store the three numbers to be compared.
2. Compare `a` and `b` using an `if` statement:
   * If `a` is greater than `b`, assign the value of `a` to a new variable, `max`.
   * Otherwise, assign the value of `b` to `max`.
3. Compare `max` and `c` using another `if` statement:
   * If `max` is greater than `c`, `max` is the greatest of the three numbers.
   * Otherwise, `c` is the greatest of the three numbers.
4. Print out the greatest number.




## 8. WAP that finds whether a given number is even or odd

1. The program should take a number as input from the user.
2. The program should check if the number is divisible by two.
3. If the number is divisible by two, the program should print "The number is even".
4. If the number is not divisible by two, the program should print "The number is odd".
5. The program should end after printing the result.




## 9. WAP that tells whether a given year is a leap year or not.

1. A leap year is a year that has 366 days instead of the usual 365 days.
2. A leap year occurs every four years, with the exception of century years (e.g. 1700, 1800, 1900, 2100).
3. To determine whether a year is a leap year, the following steps can be taken:
    a. Determine if the year is divisible by 4. If it is, then it is a leap year.
    b. If the year is not divisible by 4, then it is not a leap year.
    c. If the year is divisible by 4 and is a century year (e.g. 1700, 1800, 1900, 2100), then it is not a leap year.
4. To write a program to determine whether a given year is a leap year or not, the following steps can be taken:
    a. Ask the user for the year that they would like to check.
    b. Use an if-else statement to determine if the year is divisible by 4.
        i. If the year is divisible by 4, then print "The year is a leap year".
        ii. If the year is not divisible by 4, then print "The year is not a leap year".
    c. If the year is divisible by 4 and is a century year, then print "The year is not a leap year".




## 10.WAP that accepts marks of five subjects and finds percentage and prints grades according to the following criteria:

1. Create a program to accept marks of five subjects and calculate the percentage.
2. Use a loop to iterate through the marks and calculate the total.
3. Use an if-else statement to determine the grade according to the following criteria:
    * 90-100: A
    * 80-89: B
    * 70-79: C
    * 60-69: D
    * 0-59: F
4. Print the percentage and the grade.




## Between 90-100%-----Print ‘A’

1. If a number is between 90 and 100, the program should print the letter ‘A’.
2. To accomplish this, the program must first check if the number is between 90 and 100.
3. This can be done by using a comparison operator, such as the greater than or equal to operator (>=) and the less than or equal to operator (<=).
4. For example, if the number is 95, the program can check if it is greater than or equal to 90 and less than or equal to 100.
5. If both conditions are true, then the program should print the letter ‘A’.




## 80-90%-----------------Print ‘B’

1. To print 'B' when the value is between 80-90%, the following code can be used:
    ```
    if (value >= 80 && value <= 90) {
      System.out.println("B");
    }
    ```
2. This code checks if the given value is between 80-90% by using the comparison operators `>=` and `<=`.
3. If the value is between 80-90%, the `println` statement prints 'B' to the console.
4. If the value is outside of the given range, the `println` statement will not be executed and 'B' will not be printed.




## 60-80%-----------------Print ‘C’

1. In programming, the percentage sign (%) is used to denote the modulo operator, which returns the remainder of a division operation. 
2. The modulo operator can be used to determine if a number is within a certain range. For example, to check if a number is between 60 and 80, you can use the expression `number % 20 == 0`. 
3. If the result of the expression is 0, then the number is between 60 and 80. 
4. To print 'C' if a number is between 60 and 80, you can use the following code:

```
if (number % 20 == 0) {
  System.out.println("C");
}
```




## Below 60%-------------Print ‘D’

1. If the value is below 60%, the program should print the letter 'D'.
2. This is commonly used in educational settings to grade students on a scale.
3. For example, if a student scores a 59% on a test, the program would print 'D' as the student's grade.
4. This can also be used in other scenarios, such as when a program needs to determine whether a value is below or above a certain threshold.
5. In these cases, the program would print 'D' if the value is below the threshold, and something else if the value is above the threshold.





## 11. WAP that takes two operands and one operator from the user, perform the operation, and prints the result by using Switch statement

1. Begin by declaring the variables to store the operands and the operator.
2. Ask the user to input the two operands and the operator.
3. Use a switch statement to determine the operator and perform the corresponding operation.
4. Print the result of the operation.
5. End the program.




## 12. WAP to print the sum of all numbers up to a given number

1. Start by declaring a variable `sum` and initializing it to 0. 
2. Ask the user to enter a number.
3. Create a `for` loop that starts from 0 and ends at the number entered by the user.
4. Inside the `for` loop, add the value of the loop variable to the variable `sum`.
5. After the loop, print the value of the variable `sum`.




## 13. WAP to find the Factorial of a Given Number

1. A factorial of a number is the product of all the numbers from 1 to that number. 
2. To find the factorial of a number, one needs to use a loop. 
3. The loop should start from 1 and end at the given number. 
4. Inside the loop, the product of all the numbers should be calculated. 
5. The product is the factorial of the given number. 
6. The loop should be terminated once the given number is reached. 
7. The result of the factorial should be printed.





## 14.WAP to print sum of even and odd numbers from 1 to N numbers

1. Define a variable `n` to store the upper limit of the range of numbers.
2. Define two variables `even_sum` and `odd_sum` to store the sum of even and odd numbers respectively.
3. Use a `for` loop to iterate over the range of numbers from 1 to `n`.
4. For each number, use an `if` statement to check if it is even or odd.
5. If the number is even, add it to `even_sum`. If the number is odd, add it to `odd_sum`.
6. After the loop has finished, print the sum of even and odd numbers using `print()` function.




## 15. WAP to print the Fibonacci series

1. The Fibonacci series is a sequence of numbers where each number is the sum of the two preceding numbers, starting from 0 and 1.
2. To print the Fibonacci series, we need to create a loop that starts from 0 and 1 and continues until the desired number of terms. 
3. Inside the loop, we need to add the two preceding numbers and print the result.
4. After printing the result, we need to update the two preceding numbers with the new result.
5. The loop will continue until the desired number of terms is reached. 
6. After the loop is complete, the Fibonacci series will be printed.




## 16.WAP to check whether the entered number is prime or not.

1. A prime number is a whole number greater than 1, whose only two whole-number factors are 1 and itself.
2. To check if a number is prime, divide it by all numbers from 2 to one less than the number itself.
3. If the number is divisible by any of the numbers, it is not a prime number.
4. If the number is not divisible by any of the numbers, it is a prime number.
5. To write a program to check if an entered number is prime or not, start by prompting the user to enter a number.
6. Store the number in a variable.
7. Create a loop that iterates from 2 to one less than the number itself.
8. In the loop, check if the number is divisible by the current number in the loop.
9. If the number is divisible, print that the number is not prime and break out of the loop.
10. If the number is not divisible, continue the loop.
11. After the loop, print that the number is prime.




## 17. WAP to find the sum of digits of the entered number

1. Begin by declaring a variable to store the input number.
2. Use a loop to extract each digit of the number one by one.
3. Add each digit to a variable to which you have initialized to 0.
4. After the loop has ended, the sum of the digits is stored in the variable.
5. Print the result.




## 18. WAP to Find the Reverse of a Number

1. To find the reverse of a number, the first step is to separate the digits of the number.
2. The next step is to store the digits in an array.
3. After that, we can use a loop to traverse the array in reverse order.
4. For each digit, we can multiply it by the appropriate power of 10 and add the result to a variable.
5. Finally, the variable will contain the reverse of the original number.




## 19.WAP to print Armstrong numbers from 1 to 100.

1. An Armstrong number is a number such that the sum of its digits raised to the third power is equal to the number itself.

2. For example, 153 is an Armstrong number, because 1^3 + 5^3 + 3^3 = 153.

3. To print Armstrong numbers from 1 to 100, we can use a loop to iterate through all numbers from 1 to 100.

4. Within the loop, we can check if each number is an Armstrong number using the following algorithm:

- Initialize a variable `sum` to 0.
- Extract each digit of the number and raise it to the third power.
- Add the result to the `sum` variable.
- If the `sum` is equal to the number, then it is an Armstrong number.

5. The following is an example of code that prints Armstrong numbers from 1 to 100:

```
for i in range(1, 101):
    sum = 0
    temp = i
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if i == sum:
        print(i)
```




## 20. WAP to Convert Binary Number into Decimal Number and Vice Versa

1. Binary numbers are numbers expressed in base 2, with each digit representing a power of 2.
2. A decimal number is a number expressed in base 10, with each digit representing a power of 10.
3. To convert a binary number to a decimal number, we can use the following formula:

$$Decimal = \sum_{i=0}^n 2^i \times Binary_i$$

where $Binary_i$ is the $i$th digit of the binary number, starting from the rightmost digit.

4. To convert a decimal number to a binary number, we can use the following algorithm:

* Divide the decimal number by 2, and record the remainder.
* Repeat this process with the quotient until the quotient is 0.
* The binary number is the sequence of remainders, starting from the bottom of the list.

For example, to convert the decimal number 42 to a binary number:

* 42 / 2 = 21, remainder 0
* 21 / 2 = 10, remainder 1
* 10 / 2 = 5, remainder 0
* 5 / 2 = 2, remainder 1
* 2 / 2 = 1, remainder 0
* 1 / 2 = 0, remainder 1

Therefore, the binary number of 42 is 101010.




## 21. WAP that simply takes elements of the array from the user and finds the sum of these elements

1. Create an array
2. Prompt the user to enter the elements of the array
3. Store the elements of the array in a variable
4. Calculate the sum of the elements using a loop
5. Print the sum of the elements




## 22. WAP that inputs two arrays and saves sum of corresponding elements of these arrays in a third array and prints them

1. Start by declaring three arrays of the same length.
2. Ask the user to enter the values of the first two arrays.
3. Create a loop to add the corresponding elements of the first two arrays and store them in the third array.
4. Print the third array.
5. End the program.




## 23.WAP to find the Minimum and Maximum Element of an Array

1. Create an array of integers.
2. Initialize two variables, one to store the minimum element and one to store the maximum element.
3. Traverse the array and compare the current element with the minimum and maximum element variables.
4. If the current element is less than the minimum element, then update the minimum element variable with the current element.
5. If the current element is greater than the maximum element, then update the maximum element variable with the current element.
6. Repeat steps 3 to 5 until all the elements of the array have been traversed.
7. The minimum and maximum elements of the array can be found in the minimum and maximum element variables.




## 24. WAP to search an element in a array using Linear Search

1. Linear search is a method of searching through an array for a specific element. 
2. It works by sequentially going through each element of the array until the desired element is found. 
3. To implement linear search, the array must be traversed from the beginning, and each element compared to the desired element. 
4. If the element is found, the index of the element is returned. 
5. If the element is not found, then -1 is returned. 
6. The time complexity of linear search is O(n), where n is the number of elements in the array.




## 25. WAP to sort the elements of the array in ascending order using Bubble Sort technique

1. Bubble Sort is an algorithm for sorting an array of elements.
2. It works by repeatedly swapping adjacent elements if they are in the wrong order.
3. The algorithm begins by comparing the first two elements of the array.
4. If the first element is greater than the second element, they are swapped.
5. This comparison and swapping process is then repeated for the next pair of elements, and so on, until the entire array is sorted.
6. The algorithm is called Bubble Sort because each time two elements are compared, the larger element “bubbles” to the top of the list.
7. The time complexity of Bubble Sort is O(n^2).




## 26. WAP to add and multiply two matrices of order nxn

* Matrices are mathematical objects that can be used to represent and manipulate information.
* In order to add two matrices of order nxn, each matrix must have the same number of rows and columns.
* To add two matrices, simply add the corresponding entries in each matrix together.
* To multiply two matrices of order nxn, the number of columns in the first matrix must equal the number of rows in the second matrix.
* To multiply two matrices, multiply the entries in each row of the first matrix by the entries in each column of the second matrix, then add the products together.




## 27. WAP that finds the sum of diagonal elements of a mxn matrix

1. A matrix is a two-dimensional array of numbers, symbols, or expressions.
2. A matrix can have any number of rows and columns.
3. The diagonal elements of a matrix are the elements that lie on the main diagonal of the matrix.
4. The main diagonal is the diagonal that runs from the top left corner of the matrix to the bottom right corner.
5. The sum of the diagonal elements of a matrix can be calculated using a simple loop.
6. The loop should start at the top left corner of the matrix and end at the bottom right corner.
7. In each iteration of the loop, the value of the diagonal element should be added to a sum variable.
8. After the loop has finished, the sum variable will contain the sum of the diagonal elements of the matrix.





## 28.WAP to implement strlen (), strcat (),strcpy () using the concept of Functions

* `strlen()` is a function used to determine the length of a string. It takes a string as an argument and returns the length of the string as an integer.
* `strcat()` is a function used to concatenate two strings together. It takes two strings as arguments and returns a new string that is the combination of the two strings.
* `strcpy()` is a function used to copy one string to another. It takes two strings as arguments and copies the first string to the second string.

To implement these functions using the concept of functions, we must first define the functions. The syntax for defining a function is:

```
return_type function_name (parameters) {
  // code for the function
}
```

For `strlen()`, the return type is an integer and the parameters are a string. The code for the function should loop through the string and increment a counter for each character in the string. The function should then return the counter.

For `strcat()`, the return type is a string and the parameters are two strings. The code for the function should loop through the first string and concatenate each character to the second string. The function should then return the concatenated string.

For `strcpy()`, the return type is a string and the parameters are two strings. The code for the function should loop through the first string and copy each character to the second string. The function should then return the copied string.




## 29.Define a structure data type TRAIN_INFO

Train Info is a structure data type that contains the following information: 
- Train No.: an integer type 
- Train name: a string 
- Departure Time: an aggregate type TIME 
- Arrival Time: an aggregate type TIME 
- Start station: a string 
- End station: a string 

The structure type TIME contains two integer members: hour and minute. 

To maintain a train timetable and implement the following operations, the following steps can be taken: 
1. Create a data structure to store the train information. 
2. Create functions to add, update, delete, and search train information. 
3. Create a function to print the train timetable.




## a. List all the trains (sorted according to train number) that depart from a particular section

1. Train Number 1234 departs from Section A at 8:00am
2. Train Number 5678 departs from Section A at 9:00am
3. Train Number 9012 departs from Section A at 10:00am
4. Train Number 3456 departs from Section A at 11:00am
5. Train Number 7890 departs from Section A at 12:00pm




## b. List all Trains Departing from a Particular Station at a Particular Time

- To list all the trains departing from a particular station at a particular time, the first step is to identify the station and the time. 
- Once the station and time have been identified, the next step is to look up the train schedule for that station. 
- Train schedules are typically available online or at the station itself, and they provide information on the departure times of each train. 
- It is important to note that the train schedule may vary depending on the day of the week or time of year. 
- Additionally, some train schedules may have special times for holidays or other events. 
- Once the train schedule has been located, it is then possible to identify which trains depart from the station at the specified time.




## c. List all the trains that depart from a particular station within the next one hour of a given time

1. Determine the station from which you wish to depart.
2. Check the train schedule for the station you have chosen.
3. Look for trains that will depart within the next one hour of the given time.
4. Make a list of all the trains that will depart from the station within the next one hour of the given time.




## d. List all the trains between a pair of start station and end station.

- To list all the trains between a pair of start station and end station, one must first determine the route from the start station to the end station. 
- The route can be determined by using online resources such as a railway timetable or an online journey planner. 
- Once the route is determined, the list of trains running on that particular route can be found. 
- Information about the trains, such as the departure times, arrival times, and the duration of the journey can also be found. 
- It is also possible to check the availability of tickets and the fares for the journey.




## 30. WAP to swap two elements using the concept of pointers

1. Declare two pointers, say `p1` and `p2`, to point to the two elements that need to be swapped.
2. Assign the address of the first element to `p1` and the address of the second element to `p2`.
3. Declare another variable, say `temp`, to store the value of the first element temporarily.
4. Store the value of the first element in `temp`.
5. Assign the value of the second element to the first element.
6. Assign the value of the `temp` to the second element.
7. The two elements have been swapped.




## 31. WAP to compare the contents of two files and determine whether they are same or not

1. Open both the files in read-only mode.
2. Read one byte from each file and compare them.
3. If the bytes are equal, move to the next byte in both files and repeat step 2.
4. If all bytes in both files are equal, then the files have the same content.
5. If any of the bytes are not equal, then the files have different content.
6. Close both the files.




## 32. WAP to check whether a given word exists in a file or not. If yes then find the number of times it occurs

1. Open the file in read mode.
2. Take the input from the user for the word to be searched.
3. Read the file line by line.
4. Use a loop to iterate over each line in the file.
5. Check if the word entered by the user is present in the line.
6. If present, increment the counter by one.
7. After the loop is complete, print the number of times the word occurred in the file.




## Note:
- Understand the basics of computer programming: what is a program, what is a programming language, and how do they interact?
- Know the different types of programming languages, such as procedural, object-oriented, functional, and declarative.
- Learn the syntax of a programming language, such as variables, functions, and classes.
- Understand how to debug and troubleshoot a program.
- Be able to write programs that can manipulate data.
- Know how to use libraries and frameworks to create more complex programs.
- Understand the principles of software engineering, such as modularity and abstraction.
- Be aware of the security considerations when writing programs.




## a) The Instructor may add/delete/modify/tune experiments, wherever he/she feels in a justified manner.

1. An instructor may add experiments to a course in order to enhance the learning experience.
2. An instructor may delete experiments if they are no longer relevant or necessary.
3. An instructor may modify experiments if they need to be updated or changed in some way.
4. An instructor may tune experiments in order to adjust parameters or to improve the accuracy of results.
5. In all cases, the instructor must be able to justify their decisions to add, delete, modify, or tune experiments.




## b) The subject teachers are suggested to use the concept of project based learning

Project based learning is an approach to education that focuses on real-world problem solving. It is a student-centered approach that encourages students to explore topics in depth and apply their knowledge to solve a problem.

- Students are given a project to complete that requires them to use multiple concepts and skills.
- They are given a timeline for completion and are encouraged to work independently or in groups.
- The project requires research, problem solving and critical thinking.
- The teacher serves as a guide and facilitator, providing resources and feedback.
- The project is assessed based on the student's ability to demonstrate their knowledge.
- Projects can be used to introduce a new topic or to review and reinforce concepts.
- Projects can be used to develop problem solving skills and creative thinking.
- Projects can also be used to promote collaboration and teamwork.




## c) It is also suggested that open source tools should be preferred to conduct the lab. Some open source online compiler to conduct the C lab are as follows:

* [GCC](https://gcc.gnu.org/) - GCC is a free and open source compiler for C and other programming languages.
* [Clang](https://clang.llvm.org/) - Clang is a free and open source compiler for C and other programming languages.
* [Code::Blocks](http://www.codeblocks.org/) - Code::Blocks is a free and open source IDE for C and other programming languages.
* [Eclipse CDT](https://www.eclipse.org/cdt/) - Eclipse CDT is an open source IDE for C and other programming languages.
* [Visual Studio Code](https://code.visualstudio.com/) - Visual Studio Code is a free and open source IDE for C and other programming languages.




## C Online Compiler

- C is a general-purpose, procedural computer programming language.
- It was developed by Dennis Ritchie at Bell Labs in 1972.
- C is used for writing system software, as well as for applications programming.
- C is a compiled language, meaning that it is converted from human-readable source code into machine-readable object code.
- C compilers are available for a variety of platforms, such as Windows, Linux, and macOS.
- JDoodle is a free online C compiler that can be used to compile and execute code written in the C programming language.
- JDoodle's online C compiler has a simple user interface and provides basic features such as syntax highlighting, auto-completion, and debugging.
- The JDoodle C compiler also supports the C11 standard, which includes features such as multi-threading and atomic operations.
- JDoodle's online C compiler is easy to use and can be used to quickly test and debug code written in the C language.




## Compiling C Programs Online

1. C programming language is a general-purpose, procedural and structured programming language.
2. It is widely used for developing software ranging from system software to applications.
3. To compile a C program, the source code must be saved with the .c extension.
4. Once the source code is saved, it can be compiled using an online C compiler.
5. Before compiling the program, it is important to understand the compiler options that are available.
6. The options for compiling a C program include: compiling the program with or without debugging information, optimization or no optimization, and linking options such as static or dynamic linking.
7. After understanding the compiler options, the program can be compiled using the command line or an online C compiler.
8. Tutorials Point provides an online C compiler that allows users to compile their C programs without downloading any software.
9. The online C compiler allows users to compile their C code and view the output in the browser itself.
10. This makes it easy to debug and test the code without having to install any software.




## C Programming Online Compiler

1. A C programming online compiler is a tool that allows you to compile and execute C code from your web browser. 
2. It provides an easy way to test and debug C programs without needing to install a compiler on your computer. 
3. It is also useful for students who are learning C programming as it allows them to quickly test their code and get feedback.
4. Most online compilers support the latest versions of C programming language.
5. The output of the program is displayed on the screen as soon as it is executed.
6. Some compilers also provide features like debugging, syntax highlighting, and auto-completion.
7. Online compilers are usually free to use and require no installation.
8. They are also secure and reliable, as they are hosted on secure servers.
9. Online compilers are a great way to quickly test and debug your code.




## Introduction to Hackerrank

Hackerrank is an online platform for coding challenges and practice. It provides users with an environment where they can practice coding, as well as participate in coding challenges. It is used by programmers, developers, and learners of all levels to sharpen their coding skills.

Here are some of the features of Hackerrank:

* Challenges: Hackerrank offers a wide range of challenges that can be solved in multiple programming languages. These challenges range from beginner to advanced levels.

* Practice: Hackerrank also provides users with an environment to practice coding in a safe and secure environment.

* Leaderboards: Hackerrank also has leaderboards where users can compare their scores with other users.

* Community: Hackerrank also has a vibrant community of coders who can discuss various coding topics, share tips and tricks, and help each other out.

* Resources: Hackerrank also provides users with an extensive library of resources such as tutorials, books, and articles to help them learn coding.




## Mapping with Virtual Lab

1. Mapping is the process of creating a virtual representation of a physical environment. It is used in areas such as robotics, autonomous vehicles, and virtual reality.

2. Virtual labs are computer simulations of real-world environments. They allow users to explore and interact with virtual objects in a realistic way.

3. Mapping with virtual labs is a powerful tool for studying and understanding complex systems. It enables users to test and evaluate different scenarios without the need for physical experimentation.

4. Virtual labs can be used to map out pathways, analyze data, and develop strategies for solving problems. They can also be used to simulate real-world events and scenarios, such as natural disasters or the effects of climate change.

5. Mapping with virtual labs can be used to create detailed maps of physical environments. It can also be used to create virtual models of buildings, landscapes, and other structures.

6. Virtual labs can be used to simulate and analyze the behavior of robots, autonomous vehicles, and other autonomous systems. They can also be used to evaluate the performance of different algorithms and to develop new algorithms.

7. Mapping with virtual labs is a powerful tool for understanding and exploring complex systems. It can be used to create detailed maps, simulate real-world events, and develop strategies for solving problems.




## Name of the Lab Name of the Experiment

1. The purpose of this experiment is to explore the effects of different variables on a given system.
2. The experiment is conducted in a laboratory setting, with the necessary safety protocols in place.
3. The experiment requires a set of materials and equipment, which must be prepared prior to the start of the experiment.
4. The experiment is divided into several stages, each of which must be completed in order to obtain accurate results.
5. The results of the experiment are analyzed and interpreted, and a conclusion is drawn based on the data collected.
6. The results of the experiment are then used to inform further research and experimentation.




## Problem Solving Lab

1. Problem solving is an essential skill for success in the modern world. 
2. It involves the process of identifying and analyzing a problem, generating potential solutions, and selecting the best solution. 
3. Problem solving can be divided into two categories: analytical and creative. 
4. Analytical problem solving involves the use of logic, facts, and data to solve a problem. 
5. Creative problem solving involves using imagination and intuition to generate new ideas and solutions. 
6. In the Problem Solving Lab, students will learn how to identify and analyze a problem, generate potential solutions, and select the best solution. 
7. They will also learn how to use analytical and creative problem solving techniques to solve real-world problems. 
8. Additionally, the Problem Solving Lab will provide students with the opportunity to practice their problem solving skills in a safe and supportive environment.




## Numerical Representation

1. Numerical representation is the process of representing numbers, words, images, and other data in a form that can be read and understood by computers. 
2. Computers use binary numbers, which are composed of 0s and 1s, to represent data. 
3. Each 0 or 1 is called a bit, and eight bits make up a byte. 
4. A byte can represent a single character, such as a letter, number, or punctuation mark. 
5. Bytes can also be used to represent larger amounts of data, such as an image or a piece of text. 
6. In addition to binary numbers, computers can also use other forms of numerical representation, such as octal and hexadecimal. 
7. Octal is a base-8 number system, while hexadecimal is a base-16 number system. 
8. Computers can also use various forms of floating-point notation to represent numbers with decimal points.




## Beauty of Numbers

1. Numbers are a universal language that can be used to communicate and understand information across different cultures and languages. 
2. Numbers are used to represent data and can help us to better understand the world around us. 
3. Mathematics is the study of numbers and the relationships between them. It is used to solve problems and to make predictions about the future. 
4. Numbers can be used to describe the physical world and to make predictions about it. 
5. Numbers can be used to measure and compare things. 
6. Numbers can be used to create patterns and to solve puzzles. 
7. Numbers can be used to create art and music. 
8. Numbers can be used to create models and simulations. 
9. Numbers can be used to create algorithms and to automate tasks. 
10. Numbers can be used to create computer programs and to control machines.




## More on Numbers

1. Numbers are used in mathematics and science to represent quantities, objects, and relationships.
2. Natural numbers, also known as counting numbers, are the numbers that are used to count and are usually represented as whole numbers.
3. Integers are whole numbers and their opposites. They can be positive, negative, or zero.
4. Rational numbers are numbers that can be expressed as a fraction, where the numerator and denominator are integers.
5. Irrational numbers are numbers that cannot be expressed as a fraction and are usually represented as decimals.
6. Real numbers are all the numbers that can be represented on a number line, including rational and irrational numbers.
7. Complex numbers are numbers that include a real number and an imaginary number.
8. Exponents are used to represent repeated multiplication of a number by itself.
9. Logarithms are used to represent the inverse of exponents.
10. Factorials are used to represent the product of all the numbers between 1 and a given number.




## Factorials

* Factorials are mathematical operations that involve multiplying a number by every number between itself and one. 
* For example, the factorial of five (5!) is equal to 5 x 4 x 3 x 2 x 1, which is 120. 
* Factorials are commonly used in probability and statistics, as well as in calculus. 
* The factorial of a number can be calculated using a recursive algorithm, in which the factorial of a number is equal to the number times the factorial of the number minus one. 
* Factorials can also be expressed using the gamma function, which is a generalization of the factorial to non-integer values. 
* Factorials are also sometimes used in combinatorics to count the number of possible combinations of a set of objects.




## String Operations

1. A string is a sequence of characters, such as letters, numbers, symbols, and spaces.
2. In programming languages, strings are often used to store and manipulate text.
3. Common operations on strings include searching, replacing, and joining.
4. Searching a string can be done using string functions such as `find()`, `index()`, and `count()`.
5. Replacing a string can be done using the `replace()` function.
6. Joining strings together can be done using the `join()` function.
7. Strings can also be compared using the `==` operator.
8. String slicing is a technique used to extract a substring from a given string.
9. Strings can be converted to other data types such as numbers and lists.




## Recursion

Recursion is a programming technique that allows a function to call itself repeatedly, each time with different parameters. It is a powerful tool for solving complex problems, and is often used to traverse data structures such as trees and graphs.

1. Recursion is based on the concept of divide and conquer, where a problem is divided into smaller sub-problems.
2. A recursive function has two parts: a base case, which defines the stopping point of the recursion, and a recursive case, which defines the logic for solving the sub-problems.
3. Recursive functions are often used to traverse data structures such as linked lists and trees.
4. In order to prevent infinite recursion, a recursive function must have a base case, which defines the stopping point of the recursion.
5. Recursive functions can be used to solve complex problems, such as searching for a specific item in a collection of items.
6. Recursive functions can also be used to solve problems that require backtracking, such as finding a path between two points in a maze.
7. Recursive functions can be used to generate sequences of numbers, such as the Fibonacci sequence.
8. Recursive functions can be used to solve problems that require dynamic programming, such as the knapsack problem.




## Advanced Arithmetic

1. Arithmetic is the branch of mathematics that deals with the manipulation of numbers and operations such as addition, subtraction, multiplication, division, and exponentiation.
2. Basic arithmetic operations can be performed using a variety of methods, such as mental arithmetic, paper and pencil, a calculator, or a computer.
3. Advanced arithmetic involves the use of more complex operations such as fractions, exponents, roots, and logarithms.
4. Advanced arithmetic also involves the use of more abstract concepts such as algebraic equations, trigonometric identities, and complex numbers.
5. Learning advanced arithmetic requires a strong understanding of basic arithmetic operations and the ability to apply them in more complex situations.
6. It is important to practice advanced arithmetic problems regularly in order to develop a deeper understanding of the material.




## Searching and Sorting

Searching and sorting algorithms are used to organize and manipulate data in a computer system. Searching algorithms are used to search for specific items within a data structure, while sorting algorithms are used to rearrange items in a data structure in a particular order. 

* Linear Search: Linear search is a method of searching for an element in a data structure by comparing each element with the target element. It is simple and straightforward, but not very efficient.

* Binary Search: Binary search is a more efficient version of linear search. It works by dividing the data structure into two halves, and then comparing the target element with the middle element. If the target element is larger than the middle element, the search continues in the upper half, otherwise it continues in the lower half.

* Bubble Sort: Bubble sort is an algorithm used to sort data in an array. It works by comparing adjacent elements and swapping them if they are not in the correct order. This process is repeated until the array is sorted.

* Insertion Sort: Insertion sort is an algorithm used to sort data in an array. It works by comparing each element with the elements that come before it and inserting it in the correct place.

* Merge Sort: Merge sort is an algorithm used to sort data in an array. It works by dividing the array into two halves, sorting each half, and then merging them together. This process is repeated until the array is sorted.

* Quick Sort: Quick sort is an algorithm used to sort data in an array. It works by selecting a pivot element, and then partitioning the array into two halves based on the pivot element. The process is then repeated on each half until the array is sorted.




## Permutation

- In mathematics, a **permutation** is an arrangement of objects in a specific order. 
- A permutation can be thought of as a “rearrangement” of a sequence of objects. 
- Permutations are commonly used in mathematical and computer science problems, such as in algorithms for generating all possible combinations of a given set of objects. 
- Permutations can also be used to calculate the probability of certain outcomes in a given situation. 
- Permutations are often used in combination with other mathematical operations, such as factorials and combinations, to solve more complex problems. 
- For example, the number of ways to arrange n objects in a specific order can be calculated using the formula n! (n factorial). 
- This formula is derived from the fact that the number of permutations of n objects is equal to the product of all the numbers from 1 to n. 
- For example, the number of permutations of 4 objects is 4 x 3 x 2 x 1 = 24. 
- Similarly, the number of permutations of 5 objects is 5 x 4 x 3 x 2 x 1 = 120.




## Sequences
A sequence is an ordered set of numbers, symbols, or objects. Sequences can be used to represent many mathematical and physical phenomena, such as the Fibonacci sequence or the sequence of prime numbers. They can also be used to represent patterns in data, such as the sequence of letters in a word or the sequence of events in a story.

1. Arithmetic Sequences: These are sequences in which each term is obtained by adding a constant to the preceding term. An example of an arithmetic sequence is 2, 5, 8, 11, 14, and so on.

2. Geometric Sequences: These are sequences in which each term is obtained by multiplying the preceding term by a constant. An example of a geometric sequence is 1, 2, 4, 8, 16, and so on.

3. Fibonacci Sequences: These are sequences in which each term is obtained by adding the two preceding terms. An example of a Fibonacci sequence is 1, 1, 2, 3, 5, 8, and so on.

4. Recursive Sequences: These are sequences in which each term is obtained by applying a function to the preceding term. An example of a recursive sequence is 1, 2, 4, 8, 16, and so on.

5. Other Sequences: There are many other types of sequences, such as the Catalan numbers, the Bell numbers, the Stern-Brocot numbers, and the Padovan numbers.




## Course Outcomes:

1. Understand the key concepts and principles of data science and analytics.
2. Develop an understanding of the various data science and analytics tools and techniques.
3. Develop the ability to apply data science and analytics tools and techniques to solve data-driven problems.
4. Develop an understanding of the ethical and legal implications of data science and analytics.
5. Develop the ability to communicate data science and analytics results to stakeholders.




## Course Outcome Bloom's

1. Understand the main components of Bloom's Taxonomy of Educational Objectives and how they relate to teaching and learning.
2. Develop an understanding of the different levels of Bloom's Taxonomy and how they can be used to assess student performance.
3. Describe the different types of learning outcomes that can be addressed using Bloom's Taxonomy.
4. Analyze and evaluate the effectiveness of various instructional strategies in terms of Bloom's Taxonomy.
5. Design and develop instructional activities, assessments, and learning materials that are aligned with Bloom's Taxonomy.
6. Apply Bloom's Taxonomy to the design and delivery of instruction.




## Level

1. Level is a term used in a variety of contexts to describe a relative position, status, or rank. 
2. Levels can be used to describe a hierarchy, such as in a business organization or in a game. 
3. In business, levels may refer to the rank of an employee, such as a manager or executive. 
4. In games, levels may refer to the difficulty of the game or the progress a player has made. 
5. In mathematics, level may refer to an even surface, such as a plane or a line. 
6. In physics, level may refer to a measurement of energy, such as the amount of energy in an atom. 
7. In computing, level may refer to a user's access to certain functions or data, such as a security level.




## At the end of course, the student will be able to:
- Understand the fundamentals of computer programming
- Write code in a variety of languages
- Develop algorithms to solve problems
- Analyze data to make informed decisions
- Design and implement software applications
- Utilize debugging tools to identify and fix errors
- Develop strategies for debugging complex software systems
- Understand the principles of good software design
- Test software and identify potential issues




## CO 1 Able to implement the algorithms and draw flowcharts for solving Mathematical and Engineering problems

1. Algorithms are sets of instructions that can be used to solve problems. They can be used to solve mathematical and engineering problems, as well as problems in other areas.

2. Flowcharts are diagrams that represent the steps in an algorithm. They are used to visualize the process of solving a problem.

3. In order to implement an algorithm, it must first be written or coded. This can be done using a programming language such as C++, Java, or Python.

4. Once the algorithm is written, it must be tested to ensure that it works correctly. This can be done by running the program and checking that it produces the expected results.

5. To draw a flowchart, the steps in the algorithm must be written down in a logical order. The symbols used in a flowchart represent the different steps in the algorithm.

6. Once the flowchart is complete, it can be used to help understand the algorithm and make it easier to debug or modify.




## K3, K4

1. K3 stands for the third generation of artificial intelligence (AI). It is characterized by the use of deep learning and the ability to process large amounts of data quickly. K3 AI is used in a variety of applications, such as natural language processing, computer vision, and robotics.

2. K4 is the fourth generation of AI, which is characterized by the use of real-time processing and the ability to learn from experience. K4 AI is used in a variety of applications, such as autonomous driving, medical diagnosis, and facial recognition. It is also used in machine learning applications, such as natural language processing and computer vision.




## CO 2 Demonstrate an Understanding of Computer Programming Language Concepts. K3, K2

- Computer programming language concepts are the core foundation of computer programming. 
- K3 and K2 are two programming languages that are used to create software applications. 
- K3 is a high-level language that is designed to be easy to learn and use, while K2 is a low-level language that is more difficult to learn and use. 
- Both K3 and K2 provide an organized way of creating software applications, with each language having its own syntax and set of commands. 
- K3 and K2 are used to create applications that are interactive, such as graphical user interfaces, web applications, and games. 
- K3 and K2 also provide a way to access and manipulate data, such as databases and spreadsheets. 
- In addition, K3 and K2 provide a way to create algorithms, which are sets of instructions that can be used to solve problems. 
- Finally, K3 and K2 provide a way to debug programs, which is the process of finding and fixing errors in a program.




## CO 3

1. CO 3, also known as Carbon Monoxide, is a colorless, odorless, and tasteless gas that is toxic to humans and animals when inhaled.
2. CO 3 is produced from the incomplete combustion of fuel sources such as natural gas, propane, wood, and coal.
3. CO 3 poisoning can occur when people are exposed to high levels of the gas, which can lead to symptoms such as headache, dizziness, nausea, and confusion.
4. In severe cases, CO 3 poisoning can cause coma, brain damage, and even death.
5. To prevent CO 3 poisoning, it is important to properly ventilate any fuel-burning appliances, such as furnaces and water heaters, and to install carbon monoxide detectors in your home.




## Ability to design and develop Computer programs, analyzes, and interprets the concept of pointers, declarations, initialization, operations on pointers and their usage

* Pointers are variables that store memory addresses.
* Declarations are used to make a variable known to the program.
* Initialization is the process of assigning a value to a variable.
* Operations on pointers involve manipulating the memory address stored in the pointer.
* Pointers can be used to access data stored in memory, make changes to existing data, or create new data.
* Pointers can also be used to call functions and pass arguments.




## K6, K4

* K6 refers to the sixth grade of primary school, while K4 is the fourth grade of kindergarten. 
* In K6, students learn more complex topics such as mathematics, language arts, science, and social studies. 
* In K4, students focus on developing their reading, writing, and math skills. 
* K6 students are expected to be able to read and write independently, solve basic math problems, and understand more complex concepts. 
* K4 students learn basic math concepts such as counting, addition, subtraction, and shapes. They also learn how to read and write simple words and sentences. 
* In K6, students are also expected to develop their critical thinking skills and be able to apply their knowledge to real-world situations. 
* K4 students are also taught basic social skills such as sharing, taking turns, and following directions.




## CO 4

1. CO 4 is a type of carbon monoxide detector that is designed to detect the presence of carbon monoxide in the air.
2. Carbon monoxide is an odorless, colorless gas that is produced by the incomplete burning of fuels such as natural gas, propane, gasoline, oil, and wood.
3. Carbon monoxide can be deadly if inhaled in large amounts. It is important to install a CO 4 detector in your home to alert you to the presence of carbon monoxide.
4. CO 4 detectors are designed to detect carbon monoxide levels of 10 parts per million (ppm) or more.
5. CO 4 detectors should be placed in areas where carbon monoxide can accumulate, such as near furnaces, water heaters, and fireplaces.
6. CO 4 detectors should be tested regularly to ensure that they are working properly.
7. If the CO 4 detector sounds an alarm, it is important to open windows and doors to ventilate the area and call for help.




## Able to define data types and use them in simple data processing applications

1. Data types are categories of data that have specific characteristics and are used to store information. Examples of data types include integers, strings, characters, and floats.
2. Data processing applications are programs that manipulate data in order to produce useful information. Examples of data processing applications include spreadsheets, databases, and statistical analysis software.
3. An array is a collection of items stored in a specific order. An array of structures is an array of data structures, which are collections of related data items.
4. When using an array of structures, the user must be able to define the data types of the elements in the array and be able to use the array in data processing applications.
5. The user must also be able to access and modify the elements of the array and be able to use the array in calculations.
6. In order to use an array of structures in data processing applications, the user must understand the concept of data structures and be able to create and manipulate them.




## K1, K5

1. K1: This refers to the process of creating a knowledge base that can be used to answer questions and support decision-making. It involves gathering, organizing, and analyzing data from multiple sources. The knowledge base should be comprehensive and up-to-date, and should include information from both internal and external sources.

2. K5: This refers to the process of using the knowledge base to make decisions. It involves analyzing the data in the knowledge base and using it to inform decisions. It also involves using the knowledge base to develop strategies and plans for the future.




## CO 5 Develop confidence for self-education and ability for life-long learning needed for Computer language.

1. Self-education is an important part of computer language learning. It requires the individual to find resources, develop strategies and apply knowledge to their own learning.

2. Developing confidence in self-education is essential for successful learning. This includes having the courage to ask questions and take risks, as well as being able to evaluate and trust one's own learning.

3. Life-long learning is an important part of computer language learning. It requires the individual to stay up-to-date with the latest technologies, tools and techniques.

4. Developing the ability to learn new concepts and technologies quickly is essential for successful learning. This includes having the ability to research and apply new information quickly, as well as having the ability to adapt to changing technologies.

5. Developing an understanding of the fundamentals of computer language is essential for successful learning. This includes understanding basic concepts such as data structures, algorithms and programming languages.




## K3, K4

1. K3: K3 stands for Knowledge Representation and Reasoning. It is a field of Artificial Intelligence (AI) that deals with how computers can represent and reason with knowledge. It is concerned with the development of formalisms and algorithms that allow computers to represent and reason with knowledge in a way that is similar to how humans do it.

2. K4: K4 is a family of knowledge representation and reasoning systems developed by researchers at the University of Edinburgh. It is based on a formal language called KIF (Knowledge Interchange Format). K4 is designed to be a general purpose system that can be used for a variety of applications, such as natural language processing, automated reasoning, planning, and problem solving.

