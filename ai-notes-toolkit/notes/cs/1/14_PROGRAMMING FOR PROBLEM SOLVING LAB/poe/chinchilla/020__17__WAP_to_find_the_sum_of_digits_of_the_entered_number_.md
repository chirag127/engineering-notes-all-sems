## 17. WAP to find the sum of digits of the entered number.

In this program, we will write a code to find the sum of digits of the entered number. The following steps need to be followed to achieve the desired result:

1. Firstly, we will take an input from the user for the number whose digit sum needs to be calculated.
2. We will initialize a variable sum to 0, which will be used to store the sum of digits.
3. Next, we will use a while loop to extract each digit from the number one by one.
4. Inside the while loop, we will use the modulus operator to extract the last digit of the number and add it to the variable sum.
5. We will then divide the number by 10 to remove the last digit from it.
6. We will repeat step 4 and 5 for all the digits of the entered number until there are no digits left.
7. Finally, we will print the sum of digits calculated in step 2.

Below is the code for the program:

```python
# Taking input from user
num = int(input("Enter a number: "))

# Initializing variable sum
sum = 0

# Calculating sum of digits
while(num > 0):
    digit = num % 10    # Extracting last digit
    sum = sum + digit   # Adding digit to sum
    num = num // 10     # Removing last digit

# Printing the sum of digits
print("Sum of digits:", sum)
```

Note: The above code will only work for positive integers. If the entered number is negative or a decimal number, the program will not work correctly.