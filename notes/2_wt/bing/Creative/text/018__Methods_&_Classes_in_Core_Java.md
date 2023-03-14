#### Methods & Classes in Core Java

- A **method** is a block of code that performs a specific task. A method can be called by other methods or by the main program. A method can also take some input data (parameters) and return some output data (return value).
- A **class** is a blueprint for creating objects. A class defines the attributes (variables) and behaviors (methods) of the objects of that type. A class can also have constructors, which are special methods that are invoked when an object is created.
- To declare a class in Java, use the keyword `class` followed by the class name. The class name should start with an uppercase letter and follow the camel case convention. For example:

```java
class Person {
  // attributes and methods
}
```

- To create an object of a class, use the keyword `new` followed by the class name and parentheses. For example:

```java
Person p = new Person(); // creates a new Person object and assigns it to p
```

- To access the attributes and methods of an object, use the dot operator (`.`) followed by the attribute or method name. For example:

```java
p.name = "John"; // assigns the value "John" to the name attribute of p
p.sayHello(); // calls the sayHello method of p
```

- To declare a method in Java, use the following syntax:

```java
modifier returnType methodName(parameters) {
  // method body
}
```

- The `modifier` specifies the access level of the method, such as `public`, `private`, `protected`, or `default`. The `returnType` specifies the type of data that the method returns, such as `int`, `String`, `void`, etc. The `methodName` is the name of the method, which should start with a lowercase letter and follow the camel case convention. The `parameters` are the input data that the method takes, which are enclosed in parentheses and separated by commas. The `method body` is the block of code that performs the task of the method, which is enclosed in curly braces.
- To call a method in Java, use the method name followed by parentheses and optionally pass some arguments that match the parameters of the method. For example:

```java
int sum = add(10, 20); // calls the add method with arguments 10 and 20 and assigns the return value to sum
```

- To return a value from a method, use the keyword `return` followed by the value or expression to be returned. For example:

```java
int add(int a, int b) {
  return a + b; // returns the sum of a and b
}
```

- If a method does not return any value, use the keyword `void` as the return type. For example:

```java
void sayHello() {
  System.out.println("Hello"); // prints "Hello" to the standard output
}
```