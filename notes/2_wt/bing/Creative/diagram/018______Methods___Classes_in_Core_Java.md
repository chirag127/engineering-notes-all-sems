A class in Java is a blueprint that defines the attributes and behaviors of an object. A class can contain both data and methods that operate on that data. A method in Java is a block of code that performs a specific task and can be called by other parts of the program. A method can also accept parameters and return values.

Here is a possible ASCII diagram for methods and classes in core Java:

#### Methods & Classes in Core Java

```
+---------------------+
|       Class         |
+---------------------+
| - instance variables|
| + static variables  |
+---------------------+
| + constructor(s)    |
| - instance methods  |
| + static methods    |
+---------------------+
         | ^
         | | method call
         v |
+---------------------+
|       Object        |
+---------------------+
| - state (values of  |
|   instance variables)|
+---------------------+
| - behavior (actions |
|   of instance methods)|
+---------------------+
```