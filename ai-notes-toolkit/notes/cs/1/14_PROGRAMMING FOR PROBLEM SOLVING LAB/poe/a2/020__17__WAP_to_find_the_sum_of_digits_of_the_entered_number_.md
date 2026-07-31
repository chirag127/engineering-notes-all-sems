 Here is the content in formal markdown format without any emojis or external links:

## 17. WAP to find the sum of digits of the entered number.

1. Take input from the user for a number
2. Initialize a variable to store the sum and set it to 0
3. Use modulus operator to extract the last digit of the number
4. Add the last digit to the sum
5. Remove the last digit from the number by dividing it by 10
6. Repeat steps 3, 4 and 5 until the number becomes 0
7. Print the sum

To find the sum of digits of a number:

1. Take input from the user for a number n
2. sum = 0
3. While n > 0:
    - rem = n % 10
    - sum = sum + rem
    - n = n // 10
4. Print the sum

This is a formal program to find the sum of digits of an entered number. The logic utilizes repeating extraction of the last digit and accumulating the sum until the original number reduces to 0. The sum of all extracted digits is then printed.