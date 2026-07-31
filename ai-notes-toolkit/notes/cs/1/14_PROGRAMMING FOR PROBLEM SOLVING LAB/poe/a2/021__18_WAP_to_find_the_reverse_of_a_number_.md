 Here is the content in the requested format:

## 18.WAP to find the reverse of a number.

1. Take the input number from the user.
2. Initialize a variable to store the reverse of the number. Initialize it to 0.
3. Loop while the input number is greater than 0.
4. Within the loop, find the last digit of the number using modulus operator.
5. Append the last digit to the variable storing the reverse of the number.
6. Remove the last digit from the input number by dividing it by 10 using integer division.
7. Print the reverse of the number after the loop ends.

The logic is to iteratively extract the last digit of the number and append it to the reverse number. This is done in a loop till all the digits of the number are processed. In this way, the reverse of the number is obtained.

The code can be written as:

num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    reverse = reverse * 10 + num % 10
    num = num // 10

print("Reverse of the number is: ", reverse)

This is a standard logic to find the reverse of a number. The time complexity is O(n) where n is the number of digits in the input number.