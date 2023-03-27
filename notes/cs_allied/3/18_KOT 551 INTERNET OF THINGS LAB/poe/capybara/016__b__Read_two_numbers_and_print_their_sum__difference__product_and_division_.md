#### b) Read two numbers and print their sum, difference, product and division.

When working with programming languages such as Python, it is essential to know how to perform basic arithmetic operations. In this case, we will explore how to read two numbers and print their sum, difference, product, and division.

Here are the steps to perform these operations:

1. First, we need to read the two numbers from the user. We can use the input() function in Python to read the numbers. 

2. We will store the two numbers in two separate variables. Let us assume that the first number is stored in a variable called "num1" and the second number is stored in a variable called "num2".

3. To print the sum of the two numbers, we can use the following code:

```
sum = num1 + num2
print("The sum of", num1, "and", num2, "is", sum)
```

4. To print the difference of the two numbers, we can use the following code:

```
diff = num1 - num2
print("The difference between", num1, "and", num2, "is", diff)
```

5. To print the product of the two numbers, we can use the following code:

```
prod = num1 * num2
print("The product of", num1, "and", num2, "is", prod)
```

6. To print the division of the two numbers, we can use the following code:

```
div = num1 / num2
print("The division of", num1, "and", num2, "is", div)
```

7. However, we need to be cautious when performing division as we may run into a division by zero error. To avoid this, we can add a simple conditional statement that checks if the second number is not zero before we perform the division.

Here is the complete code to read two numbers and print their sum, difference, product, and division:

```
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

sum = num1 + num2
print("The sum of", num1, "and", num2, "is", sum)

diff = num1 - num2
print("The difference between", num1, "and", num2, "is", diff)

prod = num1 * num2
print("The product of", num1, "and", num2, "is", prod)

if num2 != 0:
    div = num1 / num2
    print("The division of", num1, "and", num2, "is", div)
else:
    print("Cannot perform division as the second number is zero.")
``` 

By following these steps, we can read two numbers and perform basic arithmetic operations to find their sum, difference, product, and division.