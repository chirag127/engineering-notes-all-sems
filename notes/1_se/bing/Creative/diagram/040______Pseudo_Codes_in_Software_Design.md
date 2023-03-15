Pseudo codes are a way of describing the steps of an algorithm in a simple and clear language that is independent of any programming language. Pseudo codes help the programmer to design the solution to the problem and communicate it to others. Pseudo codes also make it easier to translate the algorithm into different programming languages.

To draw a detailed ASCII diagram for pseudo codes in software design, we can use the following symbols and conventions:

- Use `//` to write comments that explain the purpose of each step or block of pseudo code.
- Use `START` and `END` to mark the beginning and end of the pseudo code.
- Use `INPUT` and `OUTPUT` to indicate the data that is received and produced by the algorithm.
- Use `IF`, `ELSE`, `ELSE IF`, `WHILE`, `FOR`, `DO WHILE`, `SWITCH`, `CASE`, `BREAK`, `CONTINUE` to represent the control structures of the algorithm.
- Use `=` to assign values to variables and `==` to compare values for equality.
- Use `+`, `-`, `*`, `/`, `%`, `^` to represent the arithmetic operators and `&&`, `||`, `!` to represent the logical operators.
- Use `(` and `)` to group expressions and `[` and `]` to access array elements.
- Use indentation and line breaks to make the pseudo code more readable and structured.
- Use `->` to indicate the flow of the algorithm from one step to another.

Here is an example of a pseudo code that calculates the factorial of a given number n:

```
// This pseudo code calculates the factorial of a given number n
START
  INPUT n
  IF n < 0 THEN
    OUTPUT "Invalid input"
    END
  ELSE
    SET factorial = 1
    FOR i = 1 TO n DO
      factorial = factorial * i
    END FOR
    OUTPUT factorial
  END IF
END
```

Here is the ASCII diagram for the pseudo code:

```
+-----------------+
|     START       |
+-----------------+
        |
        v
+-----------------+
|    INPUT n      |
+-----------------+
        |
        v
+-----------------+
|  IF n < 0 THEN  |
+-----------------+
        |
        |
   +----+----+
   |         |
   v         v
+-----------------+     +-----------------+
| OUTPUT "Invalid |     | SET factorial=1 |
| input"          |     +-----------------+
+-----------------+             |
        |                       v
        v                  +-----------------+
+-----------------+        | FOR i=1 TO n DO |
|      END        |        +-----------------+
+-----------------+             |
                                |
                           +----+----+
                           |         |
                           v         v
                      +-----------------+     +-----------------+
                      | factorial=factor|     | OUTPUT factorial|
                      | ial * i         |     +-----------------+
                      +-----------------+             |
                           |                       v
                           v                  +-----------------+
                      +-----------------+     |      END        |
                      | END FOR         |     +-----------------+
                      +-----------------+
                           |
                           v
                      +-----------------+
                      | END IF          |
                      +-----------------+
                           |
                           v
                      +-----------------+
                      |      END        |
                      +-----------------+
```