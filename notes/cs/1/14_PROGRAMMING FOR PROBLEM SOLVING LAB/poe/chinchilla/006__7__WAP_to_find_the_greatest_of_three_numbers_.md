## 7. WAP to find the greatest of three numbers.

In programming, it is often necessary to compare multiple values and determine the largest among them. The process of finding the greatest of three numbers can be achieved through the following steps:

1. Declare three variables to store the three numbers.

   ```
   int num1, num2, num3;
   ```

2. Prompt the user to enter the three numbers and store them in the respective variables.

   ```
   printf("Enter three numbers: ");
   scanf("%d %d %d", &num1, &num2, &num3);
   ```

3. Use conditional statements to compare the values and determine the largest among them. 

   ```
   if (num1 > num2 && num1 > num3) {
       printf("%d is the greatest.", num1);
   } else if (num2 > num1 && num2 > num3) {
       printf("%d is the greatest.", num2);
   } else {
       printf("%d is the greatest.", num3);
   }
   ```

   In the above code, the `if` statement checks if `num1` is greater than both `num2` and `num3`. If it is true, then `num1` is the greatest and it is printed. If it is false, then the `else if` statement checks if `num2` is greater than both `num1` and `num3`. If it is true, then `num2` is the greatest and it is printed. If both `if` and `else if` are false, then `num3` must be the greatest and it is printed.

4. Display the result to the user.

   ```
   printf("\n");
   ```

   The `printf("\n")` statement is used to add a new line after the result is printed, for better readability.

By following the above steps, the program can find the greatest of three numbers. It is important to note that this method can be extended to find the greatest of any number of values, not just three.