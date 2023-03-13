 Here is the content in markdown format on the topic #### Data type in Core Java:

#### Data type in Core Java

The following are the primary data types in Core Java:

1. **byte**: stores whole numbers from -128 to 127. Mnemonic: *by eight bits*.
2. **short**: stores whole numbers from -32768 to 32767. Mnemonic: *short range*.
3. **int**: stores whole numbers from -2147483648 to 2147483647. Mnemonic: *integer, default type*.
4. **long**: stores whole numbers from -9223372036854775808 to 9223372036854775807. Mnemonic: *long range*.
5. **float**: stores decimal numbers from 3.4e−038 to 3.4e+038. Mnemonic: *single precision float*.
6. **double**: stores decimal numbers from 4.9e-324 to 1.8e+308. Mnemonic: *double precision float, default for decimal*.
7. **boolean**: stores true or false values. Mnemonic: *two choices*.
8. **char**: stores a single character/letter or ASCII values. Mnemonic: *character*.

Advantages:
- Appropriate data type can be chosen based on the size and range of values to be stored. This saves memory and increases efficiency.
- Clearly defines the type of data being used, avoiding type-related errors.

Disadvantages:
- The programmer has to consciously choose the correct data type and verify that the values being stored fit in its range. This can lead to errors if not done properly.

Examples:
```
byte b = 10;
short s = 20000;
int i = 200000;
long l = 2000000000L;
float f = 5.6f;
double d = 5.1234;
boolean bool = true;
char c = 'A';
```

Applications:
- Storing values in variables and arrays.
- Passing parameters to methods.
- Return types of methods.
- Almost everywhere data is manipulated in a Java program.

I hope this helps you learn and understand Data types in Core Java. Let me know if you would like me to explain anything in more detail.