According to the search results, Scala has only a handful of built-in control structures. The only control structures are if, while, for, try, match, and function calls. The reason Scala has so few is that it has included function literals since its inception.

The following diagram illustrates the basic architecture of a function literal in Scala:

```
+----------------+      +-----------------+      +----------------+
| Function name  | ---> | Parameter list  | ---> | Function body  |
+----------------+      +-----------------+      +----------------+
| val add        |      | (a:Int, b:Int)  |      | a + b          |
+----------------+      +-----------------+      +----------------+
```

The following diagram illustrates the basic syntax of an if expression in Scala:

```
+----------------+      +-----------------+      +----------------+
| If keyword     | ---> | Condition       | ---> | Then branch    |
+----------------+      +-----------------+      +----------------+
| if             |      | x < 0           |      | println("neg") |
+----------------+      +-----------------+      +----------------+
                         |
                         |                  +----------------+
                         +----------------> | Else branch    |
                                            +----------------+
                                            | println("pos") |
                                            +----------------+
```

The following diagram illustrates the basic syntax of a while loop in Scala:

```
+----------------+      +-----------------+      +----------------+
| While keyword  | ---> | Condition       | ---> | Loop body      |
+----------------+      +-----------------+      +----------------+
| while          |      | x > 0           |      | x = x - 1      |
+----------------+      +-----------------+      +----------------+
```

The following diagram illustrates the basic syntax of a for loop in Scala:

```
+----------------+      +-----------------+      +----------------+
| For keyword    | ---> | Generator       | ---> | Loop body      |
+----------------+      +-----------------+      +----------------+
| for            |      | i <- 1 to 10    |      | println(i)     |
+----------------+      +-----------------+      +----------------+
```

The following diagram illustrates the basic syntax of a for expression in Scala:

```
+----------------+      +-----------------+      +----------------+
| For keyword    | ---> | Generator       | ---> | Yield keyword  |
+----------------+      +-----------------+      +----------------+
| for            |      | i <- 1 to 10    |      | yield          |
+----------------+      +-----------------+      +----------------+
                                            |
                                            |      +----------------+
                                            +----> | Expression     |
                                                   +----------------+
                                                   | i * 2          |
                                                   +----------------+
```

The following diagram illustrates the basic syntax of a try expression in Scala:

```
+----------------+      +-----------------+      +----------------+
| Try keyword    | ---> | Try block       | ---> | Catch keyword  |
+----------------+      +-----------------+      +----------------+
| try            |      | x / y           |      | catch          |
+----------------+      +-----------------+      +----------------+
                                            |
                                            |      +----------------+
                                            +----> | Catch block    |
                                                   +----------------+
                                                   | case e: ...    |
                                                   +----------------+
```

The following diagram illustrates the basic syntax of a match expression in Scala:

```
+----------------+      +-----------------+      +----------------+
| Expression     | ---> | Match keyword   | ---> | Case keyword   |
+----------------+      +-----------------+      +----------------+
| x              |      | match           |      | case           |
+----------------+      +-----------------+      +----------------+
                                            |
                                            |      +----------------+
                                            +----> | Pattern        |
                                                   +----------------+
                                                   | 0              |
                                                   +----------------+
                                                   |
                                                   |      +----------------+
                                                   +----> | Expression     |
                                                          +----------------+
                                                          | "zero"         |
                                                          +----------------+
```