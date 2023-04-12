# Number system and representation for the notes of the Unit 5 - Digital Electronics in the subject of FUNDAMENTALS OF ELECTRONICS ENGINEERING

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

- The binary equivalent of 2843 is the remainders in reverse order: 101100100011
- To convert the binary number 101100100011 to octal, we can group the bits into three-bit groups from right to left and use a table to find the corresponding octal digit:

```
101 100 100 011
 5   4   4   3
```

- The octal equivalent of 101100100011 is 5443
- To convert the binary number 101100100011 to hexadecimal, we can group the bits into four-bit groups from right to left and use a table to find the corresponding hexadecimal digit:

```
1011 0010 0011
  B   2   3
```

- The hexadecimal equivalent of 101100100011 is B23
- To convert a number from octal or hexadecimal to decimal, we can use the multiplication method as follows:

```
5443 (octal) = 5 x 8^3 + 4 x 8^2 + 4 x 8^1 + 3 x 8^0
             = 5 x 512 + 4 x 64 + 4 x 8 + 3 x 1
             = 2560 + 256 + 32 + 3
             = 2843 (decimal)

B23 (hexadecimal) = B x 16^2 + 2 x 16^1 + 3 x 16^0
                  = 11 x 256 + 2 x 16 + 3 x 1
                  = 2816 + 32 + 3
                  = 2843 (decimal)
```

- To convert a number from octal or hexadecimal to binary, we can use the substitution method as follows:

```
5443 (octal) = 5 4 4 3
             = 101 100 100 011 (binary)

B23 (hex

```
