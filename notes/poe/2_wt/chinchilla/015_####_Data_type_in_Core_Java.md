#### Data type in Core Java

In Java, a data type is a classification of data that specifies the type of data that a variable can hold. Java provides eight primitive data types, which are further divided into two categories: numeric and non-numeric.

##### Numeric Data Types

1. **byte**: A byte is an 8-bit signed two's complement integer, with a minimum value of -128 and a maximum value of 127. It is used to save memory in large arrays or in situations where memory is a concern.

2. **short**: A short is a 16-bit signed two's complement integer, with a minimum value of -32,768 and a maximum value of 32,767. It is used when memory is a concern, but more precision is needed than a byte can provide.

3. **int**: An int is a 32-bit signed two's complement integer, with a minimum value of -2^31 and a maximum value of 2^31-1. It is the most commonly used data type for integer values.

4. **long**: A long is a 64-bit signed two's complement integer, with a minimum value of -2^63 and a maximum value of 2^63-1. It is used when an int is not large enough to hold the required value.

5. **float**: A float is a single-precision 32-bit floating-point number. It is used when fractional values are needed but precision is not critical.

6. **double**: A double is a double-precision 64-bit floating-point number. It is used when higher precision is needed for fractional values.

##### Non-numeric Data Types

7. **char**: A char is a 16-bit Unicode character. It can hold any character from the Unicode character set, including letters, digits, and symbols. It is used to represent characters and strings.

8. **boolean**: A boolean data type represents only two possible values: true or false. It is used for logical expressions and conditions.

##### Mnemonics and Learning Tricks

- To remember the order of numeric data types by size, use the mnemonic: "Be Sober, I Rarely Feel Like Punching Somebody Daily." This stands for byte, short, int, long, float, double.

- To remember the size of a char data type, think of it as being twice the size of a byte (8 bits), so 2 x 8 = 16 bits.

##### Advantages and Disadvantages

- Primitive data types are faster to manipulate and require less memory than objects.

- However, primitive data types cannot be used to store complex data structures or to call methods.

##### Examples

- int age = 25;
- double price = 9.99;
- char grade = 'A';
- boolean isTrue = true;

##### Applications

- Numeric data types are used for calculations, counting, and indexing.

- Non-numeric data types are used for representing strings, characters, and logical values.