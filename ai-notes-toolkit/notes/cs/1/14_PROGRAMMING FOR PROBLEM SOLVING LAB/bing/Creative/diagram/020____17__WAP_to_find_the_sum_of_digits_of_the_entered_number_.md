Hello, I am Sydney, your AI assistant. I can help you with any topic you want to discuss. You have asked me to write a program to find the sum of digits of the entered number. Here is the content in markdown format:

## 17. WAP to find the sum of digits of the entered number.

- A program to find the sum of digits of the entered number is a common problem in programming that can be solved using a loop and some arithmetic operations.
- The basic idea is to extract each digit of the number by using the modulo operator (%) and then add it to a variable that stores the sum. The number is then divided by 10 to remove the last digit and the process is repeated until the number becomes zero.
- Here is an example of how the program works for the number 123:

  - Initialize a variable sum to 0 and a variable num to 123.
  - Extract the last digit of num by using num % 10, which gives 3. Add 3 to sum, which becomes 3.
  - Divide num by 10, which gives 12. Update num to 12.
  - Repeat the above steps until num becomes 0.
  - The final value of sum is 6, which is the sum of digits of 123.

- Here is the pseudocode of the program:

  - Start
  - Declare an integer variable sum and initialize it to 0
  - Declare an integer variable num and read its value from the user
  - While num is not equal to 0, do the following:
    - Declare an integer variable digit and assign it the value of num % 10
    - Add digit to sum and assign the result to sum
    - Divide num by 10 and assign the result to num
  - End while
  - Print the value of sum
  - Stop

- Here is the code of the program in Python:

  ```python
  # Python program to find the sum of digits of the entered number

  # Initialize sum to 0
  sum = 0

  # Read num from the user
  num = int(input("Enter a number: "))

  # Loop until num becomes 0
  while num != 0:
    # Extract the last digit of num
    digit = num % 10
    # Add digit to sum
    sum = sum + digit
    # Remove the last digit of num
    num = num // 10

  # Print the sum of digits
  print("The sum of digits is", sum)
  ```