Hello, I am Sydney, your AI assistant. I can help you with various tasks and topics. You have asked me to write a program to convert binary number into decimal number and vice versa. Here is the content in markdown format:

## 20.WAP to convert binary number into decimal number and vice versa.

Binary numbers are composed of only two digits: 0 and 1. They represent the base-2 system of counting, where each digit corresponds to a power of 2. For example, the binary number 1011 is equivalent to the decimal number 11, because 1011 = 1 * 2^3 + 0 * 2^2 + 1 * 2^1 + 1 * 2^0 = 8 + 0 + 2 + 1 = 11.

Decimal numbers are composed of ten digits: 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9. They represent the base-10 system of counting, where each digit corresponds to a power of 10. For example, the decimal number 123 is equivalent to the binary number 1111011, because 123 = 1 * 10^2 + 2 * 10^1 + 3 * 10^0 = 100 + 20 + 3 = 1111011.

To convert a binary number into a decimal number, we can use the following algorithm:

- Initialize a variable `decimal` to store the result and set it to 0.
- Initialize a variable `power` to store the current power of 2 and set it to 0.
- Loop through the binary number from right to left, starting from the least significant bit.
- For each bit, multiply it by 2^power and add it to `decimal`.
- Increment `power` by 1.
- Return `decimal` as the final result.

To convert a decimal number into a binary number, we can use the following algorithm:

- Initialize a variable `binary` to store the result and set it to an empty string.
- Loop while the decimal number is greater than 0.
- Divide the decimal number by 2 and store the remainder as `bit`.
- Append `bit` to the left of `binary`.
- Update the decimal number by dividing it by 2 and discarding the remainder.
- Return `binary` as the final result.

Here is an example of a Python program that implements these algorithms:

```python
# Function to convert binary to decimal
def binary_to_decimal(binary):
  # Initialize decimal and power
  decimal = 0
  power = 0
  # Loop through the binary number from right to left
  for i in range(len(binary) - 1, -1, -1):
    # Get the current bit
    bit = int(binary[i])
    # Multiply the bit by 2^power and add it to decimal
    decimal += bit * (2 ** power)
    # Increment power
    power += 1
  # Return decimal
  return decimal

# Function to convert decimal to binary
def decimal_to_binary(decimal):
  # Initialize binary
  binary = ""
  # Loop while decimal is greater than 0
  while decimal > 0:
    # Divide decimal by 2 and get the remainder as bit
    bit = decimal % 2
    # Append bit to the left of binary
    binary = str(bit) + binary
    # Update decimal by dividing it by 2
    decimal //= 2
  # Return binary
  return binary

# Test the functions
binary = "1011"
decimal = 123
print(binary, "in decimal is", binary_to_decimal(binary))
print(decimal, "in binary is", decimal_to_binary(decimal))
```

The output of the program is:

```
1011 in decimal is 11
123 in binary is 1111011
```