Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of COMPUTER SYSTEM SECURITY. Here are some notes on the topic of format string vulnerabilities for the Unit 1 - Computer System Security Introduction.

### More Control Hijacking attacks format string vulnerabilities

- Format string vulnerabilities are a class of bug that take advantage of an easily avoidable programmer error.
- If the programmer passes an attacker-controlled buffer as an argument to a printf (or any of the related functions, including sprintf, fprintf, etc), the attacker can perform writes to arbitrary memory addresses.
- This can lead to information disclosure, code execution, or denial of service.
- The root cause of format string vulnerabilities is the misuse of the format string parameter in the printf family of functions.
- The format string parameter is supposed to contain a string with placeholders for the values of the other arguments, such as "%s" for a string, "%d" for an integer, "%x" for a hexadecimal number, etc.
- However, if the format string parameter is not a constant string, but a variable that can be influenced by the attacker, the attacker can insert arbitrary format specifiers that can cause the printf function to read or write from memory locations that are not intended by the programmer.
- For example, consider the following C code snippet:

```c
char buffer[100];
gets(buffer); // read user input into buffer
printf(buffer); // print buffer to standard output
```

- This code is vulnerable to a format string attack, because the buffer variable can contain any string that the attacker types in, including format specifiers.
- If the attacker types in "%x %x %x %x", the printf function will interpret the buffer as a format string and print the values of four memory locations from the stack.
- If the attacker types in "%n", the printf function will interpret the buffer as a format string and write the number of bytes printed so far to the memory location pointed by the next argument on the stack, which can be an arbitrary address chosen by the attacker.
- To prevent format string vulnerabilities, the programmer should always use a constant string as the format string parameter, or use a function that does not interpret the format string, such as puts or write .
- Alternatively, the programmer can use a format string sanitizer, such as FORTIFY_SOURCE, that can detect and abort format string attacks at runtime.
- The programmer should also avoid using unsafe functions, such as gets, that can cause buffer overflows, and use secure alternatives, such as fgets or getline .