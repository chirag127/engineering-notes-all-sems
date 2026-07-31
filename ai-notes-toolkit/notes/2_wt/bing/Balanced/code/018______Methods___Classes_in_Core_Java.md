#### Methods & Classes in Core Java

A class is a blueprint or template for creating objects in Java. An object is an instance of a class that has its own state and behavior. A class can contain both data and methods that operate on that data. The data or variables defined within a class are called instance variables and the code that operates on this data is known as methods.

To declare a class in Java, the `class` keyword is used, followed by the name of the class and a pair of curly braces that enclose the class body. For example:

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
    System.out.println("I am " + age + " years old");
  }
}
```

To create an object of a class, the `new` keyword is used, followed by the name of the class and a pair of parentheses. The object can be assigned to a variable of the same type as the class. For example:

```java
// Creating an object of the Person class
Person p1 = new Person();

// Assigning values to the instance variables
p1.name = "Alice";
p1.age = 20;

// Calling the methods on the object
p1.greet();
p1.birthday();
```

The output of the above code would be:

```
Hello, my name is Alice
I am 21 years old
```

A class can have multiple objects, each with its own state and behavior. For example:

```java
// Creating another object of the Person class
Person p2 = new Person();

// Assigning values to the instance variables
p2.name = "Bob";
p2.age = 25;

// Calling the methods on the object
p2.greet();
p2.birthday();
```

The output of the above code would be:

```
Hello, my name is Bob
I am 26 years old
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
    p3.greet();
    p3.birthday();
  }
}
```

The output of the above code would be:

```
Hello, my name is Charlie
I am 31 years old
```

A method is a block of code that performs a specific task. A method can be called by using its name followed by a set of parentheses. A method can also accept data, known as parameters, and return data, known as the return value. A method can be defined inside a class by using the following syntax:

```java
modifier returnType methodName(parameterList) {
  // Method body
}
```

The modifier specifies the access level of the method, such as `public`, `private`, or `protected`. The returnType specifies the type of data that the method returns, such as `int`, `String`, or `void`. The methodName is the name of the method, which should follow the naming conventions of Java. The parameterList is a comma-separated list of parameters that the method accepts, each with a type and a name. The method body is a block of code that contains the logic of the method.

For example, the following method takes two `int` parameters and returns their sum as an `int` value:

```java
// A method that returns the sum of two integers
public int add(int a, int b) {
  int sum = a + b;
  return sum;
}
```

To call a method, the method name is followed by a set of parentheses that contain the arguments that match the parameters of the method. The arguments are the actual values that are passed to the method. For example, the following code calls the `add` method with the arguments `10` and `20` and assigns the return value to a variable `result`:

```java
// Calling the add method
int result = add(10, 20);
System.out.println("The sum is " + result);
```

The output of the above code would be: