#### Methods & Classes in Core Java

A class in Java is a blueprint that defines the attributes and behaviors of an object. A class can contain both data and methods that operate on that data. The data or variables defined within a class are called instance variables and the code that operates on this data is known as methods .

A method in Java is a block of code that performs a specific task. A method can be declared within a class and can be called by other methods or objects of the same class. A method can also accept parameters, which are values passed to the method when it is invoked. A method can also return a value to the caller .

The following diagram illustrates the basic structure of a class and a method in Java:

```
+---------------------+
|       Class         |
+---------------------+
|                     |
| - instance variable |
| - instance variable |
|                     |
+---------------------+
|                     |
| + method(parameter) |
| + method(parameter) |
|                     |
+---------------------+
```

The class name should start with an uppercase letter and match the name of the Java file. The instance variables are declared with a minus sign (-) and the methods are declared with a plus sign (+). The parentheses after the method name indicate the parameters that the method accepts. The return type of the method is not shown in the diagram, but it can be specified before the method name in the code.

To create an object of a class, use the keyword new followed by the class name and parentheses. To access the instance variables and methods of an object, use the dot (.) operator followed by the variable or method name. For example:

```
// Create an object of the Main class
Main myObj = new Main();

// Access the instance variable x
System.out.println(myObj.x);

// Call the method myMethod
myObj.myMethod();
```