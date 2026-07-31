### Number system and representation for the notes of the Unit 5 - Digital Electronics in the subject of FUNDAMENTALS OF ELECTRONICS ENGINEERING

- A number system is a way of representing information using symbols or digits.
- The base or radix of a number system is the total number of symbols or digits used in the number system.
- The most common number systems in digital electronics are decimal, binary, octal, and hexadecimal.
- Decimal number system uses 10 symbols or digits: 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9. It is the standard system for human arithmetic and communication.
- Binary number system uses 2 symbols or digits: 0 and 1. It is the simplest and most fundamental system for digital electronics and computers. Each digit or bit can represent two states: on or off, true or false, high or low, etc.
- Octal number system uses 8 symbols or digits: 0, 1, 2, 3, 4, 5, 6, and 7. It is a convenient way of grouping binary bits into three-bit groups or octets. Each octal digit represents three binary digits.
- Hexadecimal number system uses 16 symbols or digits: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, and F. It is another convenient way of grouping binary bits into four-bit groups or nibbles. Each hexadecimal digit represents four binary digits.
- To convert a number from one base to another, we can use various methods such as division, multiplication, substitution, or table lookup.
- For example, to convert the decimal number 2843 to binary, we can use the division method as follows:

```
2843 / 2 = 1421 remainder 1
1421 / 2 = 710 remainder 1
710 / 2 = 355 remainder 0
355 / 2 = 177 remainder 1
177 / 2 = 88 remainder 1
88 / 2 = 44 remainder 0
44 / 2 = 22 remainder 0
22 / 2 = 11 remainder 0
11 / 2 = 5 remainder 1
5 / 2 = 2 remainder 1
2 / 2 = 1 remainder 0
1 / 2 = 0 remainder 1
```

- The binary number is obtained by reading the remainders from bottom to top: 101100100111
- To convert the binary number 101100100111 to octal, we can use the grouping method as follows:

```
101 100 100 111
  5   4   4   7
```

- The octal number is obtained by replacing each group of three binary digits with its corresponding octal digit: 5447
- To convert the binary number 101100100111 to hexadecimal, we can use the grouping method as follows:

```
10 1100 1001 11
 2    C    9   3
```

- The hexadecimal number is obtained by replacing each group of four binary digits with its corresponding hexadecimal digit: 2C93
- To convert the octal number 5447 to decimal, we can use the multiplication method as follows:

```
5447 = 7 x 8^0 + 4 x 8^1 + 4 x 8^2 + 5 x 8^3
5447 = 7 + 32 + 256 + 2560
5447 = 2855
```

- The decimal number is obtained by multiplying each octal digit with its corresponding power of 8 and adding them up: 2855
- To convert the hexadecimal number 2C93 to decimal, we can use the multiplication method as follows:

```
2C93 = 3 x 16^0 + 9 x 16^1 + C x 16^2 + 2 x 16^3
2C93 = 3 + 144 + 3072 + 8192
2C93 = 11411
```

- The decimal number is obtained by multiplying each hexadecimal digit with its corresponding power of 16 and adding them up: 11411
- In digital electronics, numbers can also be represented in different formats such as fixed point and floating point.