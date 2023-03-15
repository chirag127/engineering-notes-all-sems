### Number system and representation for the notes of the Unit 5 - Digital Electronics in the subject of FUNDAMENTALS OF ELECTRONICS ENGINEERING

- A number system is a way of representing information using symbols or digits. Different number systems have different bases or radices, which are the total number of symbols or digits used in the system.
- The most common number systems in digital electronics are decimal, binary, octal, and hexadecimal . These number systems are used to represent data, instructions, and addresses in digital circuits and computers.
- The decimal number system has a base of 10 and uses 10 symbols: 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9. It is the most familiar and widely used number system in everyday life.
- The binary number system has a base of 2 and uses 2 symbols: 0 and 1. It is the simplest and most fundamental number system in digital electronics, as it can represent any information using only two states: on or off, high or low, true or false, etc. Each symbol or digit in binary is also called a bit, which is the basic unit of information in digital systems .
- The octal number system has a base of 8 and uses 8 symbols: 0, 1, 2, 3, 4, 5, 6, and 7. It is a convenient way of representing binary numbers in a shorter form, as one octal digit can represent three binary digits. For example, the binary number 101101 can be written as 55 in octal.
- The hexadecimal number system has a base of 16 and uses 16 symbols: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, and F. It is another way of representing binary numbers in a shorter form, as one hexadecimal digit can represent four binary digits. For example, the binary number 101101 can be written as 2D in hexadecimal.
- To convert a number from one base to another, there are different methods depending on the bases involved. Some common methods are:
  - To convert a decimal number to binary, divide the number by 2 repeatedly and write the remainders from bottom to top. For example, to convert 13 to binary, we have:

    ```
    13 / 2 = 6 remainder 1
    6 / 2 = 3 remainder 0
    3 / 2 = 1 remainder 1
    1 / 2 = 0 remainder 1
    ```

    So, 13 in binary is 1101.
  - To convert a binary number to decimal, multiply each bit by its corresponding power of 2 and add the results. For example, to convert 1101 to decimal, we have:

    ```
    1101 = 1 x 2^3 + 1 x 2^2 + 0 x 2^1 + 1 x 2^0
         = 8 + 4 + 0 + 1
         = 13
    ```

    So, 1101 in decimal is 13.
  - To convert a binary number to octal, group the bits from right to left into groups of three and replace each group with its equivalent octal digit. For example, to convert 110101 to octal, we have:

    ```
    110 101 = 6 5
    ```

    So, 110101 in octal is 65.
  - To convert an octal number to binary, replace each octal digit with its equivalent three-bit binary group. For example, to convert 65 to binary, we have:

    ```
    6 5 = 110 101
    ```

    So, 65 in binary is 110101.
  - To convert a binary number to hexadecimal, group the bits from right to left into groups of four and replace each group with its equivalent hexadecimal digit. For example, to convert 110101 to hexadecimal, we have:

    ```
    0011 0101 = 3 5
    ```

    So, 110101 in hexadecimal is 35.
  - To convert a hexadecimal number to