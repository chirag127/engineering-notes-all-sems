### Number system and representation for the notes of the Unit 5 - Digital Electronics in the subject of FUNDAMENTALS OF ELECTRONICS ENGINEERING

- A number system is a way of representing information using symbols called digits.
- The base or radix of a number system is the total number of digits used in the number system.
- The most common number systems in digital electronics are decimal, binary, octal, and hexadecimal.
- Decimal number system uses 10 digits: 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9. It is the standard system for human arithmetic and communication.
- Binary number system uses 2 digits: 0 and 1. It is the simplest and most fundamental system for digital electronics and computers. Each digit is also called a bit.
- Octal number system uses 8 digits: 0, 1, 2, 3, 4, 5, 6, and 7. It is a convenient way of representing binary numbers in groups of three bits.
- Hexadecimal number system uses 16 digits: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, and F. It is a convenient way of representing binary numbers in groups of four bits. The digits A to F represent the values 10 to 15 respectively.
- To convert a number from one base to another, we can use various methods such as division, multiplication, substitution, or table lookup.
- For example, to convert the decimal number 25 to binary, we can use the division method as follows:

```
25 / 2 = 12 remainder 1
12 / 2 = 6 remainder 0
6 / 2 = 3 remainder 0
3 / 2 = 1 remainder 1
1 / 2 = 0 remainder 1
```

- The binary equivalent of 25 is the remainders in reverse order: 11001.
- To convert the binary number 11001 to octal, we can group the bits in groups of three from right to left and replace each group with its octal equivalent:

```
11001 = 011 001
011 = 3
001 = 1
```

- The octal equivalent of 11001 is 31.
- To convert the binary number 11001 to hexadecimal, we can group the bits in groups of four from right to left and replace each group with its hexadecimal equivalent:

```
11001 = 0001 1001
0001 = 1
1001 = 9
```

- The hexadecimal equivalent of 11001 is 19.
- To convert a number from octal or hexadecimal to decimal, we can use the multiplication method as follows:

```
31 (octal) = 3 x 8^1 + 1 x 8^0
           = 24 + 1
           = 25 (decimal)

19 (hexadecimal) = 1 x 16^1 + 9 x 16^0
                 = 16 + 9
                 = 25 (decimal)
```

- To convert a number from octal or hexadecimal to binary, we can use the substitution method as follows:

```
31 (octal) = 011 (binary) 001 (binary)
           = 11001 (binary)

19 (hexadecimal) = 0001 (binary) 1001 (binary)
                 = 11001 (binary)
```

- To convert a number from binary to decimal, we can use the multiplication method as follows:

```
11001 (binary) = 1 x 2^4 + 1 x 2^3 + 0 x 2^2 + 0 x 2^1 + 1 x 2^0
               = 16 + 8 + 0 + 0 + 1
               = 25 (decimal)
```

- In digital electronics, we also need to represent fractional numbers, negative numbers, and alphanumeric characters using binary bits.
- To represent fractional numbers, we can use fixed-point or floating-point formats.
- Fixed-point format uses a fixed number of bits to represent the integer part and the fractional part of a number. For example, using 8 bits, we can represent the decimal number 12.75 as 00001100.11000000 in binary fixed-point format.
- Floating-point