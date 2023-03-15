## 20. WAP to convert binary number into decimal number and vice versa.

Converting a binary number into a decimal number involves taking the sum of the products of each binary digit by its corresponding power of 2. For example, the binary number 1011 can be converted into a decimal number as follows:

1. Start with the rightmost digit (in this case, 1). Multiply it by 2^0 (which is 1) to get 1.
2. Move to the next digit to the left (in this case, 1). Multiply it by 2^1 (which is 2) to get 2.
3. Move to the next digit to the left (in this case, 0). Multiply it by 2^2 (which is 4) to get 0.
4. Move to the next digit to the left (in this case, 1). Multiply it by 2^3 (which is 8) to get 8.
5. Add all the products together to get the decimal equivalent of the binary number: 1 + 2 + 0 + 8 = 11.

Converting a decimal number into a binary number involves repeatedly dividing the decimal number by 2 and recording the remainder until the decimal number becomes 0. For example, the decimal number 11 can be converted into a binary number as follows:

1. Divide 11 by 2 to get a quotient of 5 and a remainder of 1. Record the remainder (1).
2. Divide 5 by 2 to get a quotient of 2 and a remainder of 1. Record the remainder (1).
3. Divide 2 by 2 to get a quotient of 1 and a remainder of 0. Record the remainder (0).
4. Divide 1 by 2 to get a quotient of 0 and a remainder of 1. Record the remainder (1).
5. Since the quotient is now 0, stop the process. The binary equivalent of the decimal number is obtained by reading the remainders in reverse order: 1011.

Here is an example of a program in Python that converts a binary number into a decimal number and vice versa:

```python
def binary_to_decimal(binary):
    decimal = 0
    for i in range(len(binary)):
        decimal += int(binary[i]) * (2 ** (len(binary) - 1 - i))
    return decimal

def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        binary += str(decimal % 2)
        decimal = decimal // 2
    return binary[::-1]

binary = input("Enter a binary number: ")
decimal = binary_to_decimal(binary)
print(f"The decimal equivalent of {binary} is {decimal}.")

decimal = int(input("Enter a decimal number: "))
binary = decimal_to_binary(decimal)
print(f"The binary equivalent of {decimal} is {binary}.")
```