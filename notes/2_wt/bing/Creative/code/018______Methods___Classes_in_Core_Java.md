#### Methods & Classes in Core Java

A class is a blueprint or template for creating objects in Java. An object is an instance of a class that has its own state and behavior. A class can contain both data and methods that operate on that data. The data or variables defined within a class are called instance variables and the code that operates on this data is known as methods.

To declare a class in Java, the class keyword is used followed by the name of the class. The class name should start with a capital letter and follow the camel case convention. For example:

```java
// A simple class declaration
class Person {
  // Instance variables
  String name;
  int age;
  
  // Methods
  void greet() {
    System.out.println("Hello, my name is " + name);
  }
  
  void birthday() {
    age++;
    System.out.println("I am " + age + " years old now");
  }
}
```

To create an object of a class, the new keyword is used followed by the class name and a pair of parentheses. The object can be assigned to a variable of the same type as the class. For example:

```java
// Creating an object of the Person class
Person p1 = new Person();

// Assigning values to the instance variables
p1.name = "Alice";
p1.age = 20;

// Calling the methods on the object
p1.greet(); // Prints "Hello, my name is Alice"
p1.birthday(); // Prints "I am 21 years old now"
```

A class can have multiple objects, each with its own state and behavior. For example:

```java
// Creating another object of the Person class
Person p2 = new Person();

// Assigning values to the instance variables
p2.name = "Bob";
p2.age = 25;

// Calling the methods on the object
p2.greet(); // Prints "Hello, my name is Bob"
p2.birthday(); // Prints "I am 26 years old now"
```

A class can also be used in another class by creating an object of that class and accessing its members. For example:

```java
// A class that uses the Person class
class Main {
  public static void main(String[] args) {
    // Creating an object of the Person class
    Person p3 = new Person();
    
    // Assigning values to the instance variables
    p3.name = "Charlie";
    p3.age = 30;
    
    // Calling the methods on the object
    p3.greet(); // Prints "Hello, my name is Charlie"
    p3.birthday(); // Prints "I am 31 years old now"
  }
}
```

A method is a block of code that performs a specific task and can be called by other parts of the program. A method can have parameters, which are variables that are passed to the method when it is called. A method can also return a value, which is the result of the method execution. A method can be defined inside a class using the following syntax:

```java
modifier returnType methodName(parameterList) {
  // Method body
  return value;
}
```

The modifier specifies the access level of the method, such as public, private, protected, etc. The returnType specifies the type of the value that the method returns, such as int, double, String, etc. If the method does not return any value, the returnType is void. The methodName is the name of the method, which should follow the camel case convention. The parameterList is a comma-separated list of parameters, each with a type and a name. The method body is the code that performs the task of the method. The return statement is used to return a value from the method. If the method is void, the return statement is optional.

For example, the following method takes two int parameters and returns their sum as an int value:

```java
// A method that returns the sum of two integers
public int add(int a, int b) {
  // Declare a variable to store the result
  int result;
  
  // Calculate the result
  result = a + b;
  
  // Return the result
  return result;
}
```

To call a method in Java, write the method name followed by a set of parentheses, followed by a semicolon. If the method has parameters, pass the values of the arguments inside the parentheses. If the method returns a value, assign it to a variable of the same type as the return type. For example:

```java

```
