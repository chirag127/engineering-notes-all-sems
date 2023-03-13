According to the search results, Scala has only a handful of built-in control structures, which are if, while, for, try, match, and function calls . The reason Scala has so few is that it has included function literals since its inception . A function literal is a function that is not defined by a name, but by its parameters and body, such as `(a:Int, b:Int) => a + b`.

The following diagram illustrates the basic architecture of a built-in control structure in Scala:

#### Built-in control structures in Scala

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    if/else      |     |     while       |     |      for        |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Condition      |     |  Condition      |     |  Generator      |
|                 |     |                 |     |                 |
|  Then block     |     |  Loop block     |     |  Filter         |
|                 |     |                 |     |                 |
|  Else block     |     |                 |     |  Body           |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
          |                     |                     |
          |                     |                     |
          |                     |                     |
          |                     |                     |
          |                     |                     |
          |                     |                     |
          |                     |                     |
          |                     |                     |
          |                     |                     |
          |                     |                     |
          |                     |                     |
          |                     |                     |
          v                     v                     v
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|      try        |     |     match       |     |  function call  |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Try block      |     |  Expression     |     |  Function name  |
|                 |     |                 |     |                 |
|  Catch block    |     |  Case clauses   |     |  Arguments      |
|                 |     |                 |     |                 |
|  Finally block  |     |                 |     |                 |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```