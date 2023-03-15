#### Methods & Classes in Core Java

- A class is a blueprint or template for creating objects in Java. An object is an instance of a class that has its own state and behavior.
- A class is declared using the `class` keyword, followed by the name of the class and a pair of curly braces `{}` that enclose the class body. For example:

```java
class Car {
  // class body
}
```

- A class can contain both data and methods that operate on that data. The data or variables defined within a class are called instance variables or fields, and the code that operates on this data is known as methods or functions.
- An instance variable is declared inside a class, but outside a method. It can be accessed by all the methods of the class. For example:

```java
class Car {
  // instance variable
  String color;
  int speed;
}
```

- A method is a block of code that performs a specific task. It can be called by other methods or objects to execute the task. A method is declared using a method header and a method body. The method header consists of the method name, a pair of parentheses `()` that may contain some parameters, and a return type. The method body consists of a pair of curly braces `{}` that enclose the statements of the method. For example:

```java
class Car {
  // method header
  void drive(int distance) {
    // method body
    System.out.println("Driving " + distance + " kilometers.");
  }
}
```

- To create an object of a class, use the `new` keyword, followed by the name of the class and a pair of parentheses `()`. For example:

```java
Car myCar = new Car(); // create an object of the Car class
```

- To access the instance variables and methods of an object, use the dot operator `.` followed by the name of the variable or method. For example:

```java
myCar.color = "red"; // assign a value to the color variable of myCar object
myCar.drive(100); // call the drive method of myCar object
```

- A class can have multiple objects, each with its own state and behavior. For example:

```java
Car yourCar = new Car(); // create another object of the Car class
yourCar.color = "blue"; // assign a different value to the color variable of yourCar object
yourCar.drive(50); // call the drive method of yourCar object
```

- A class can also use other classes by creating objects of them or by inheriting from them. For example:

```java
class Truck extends Car { // Truck class inherits from Car class
  // Truck class can access the instance variables and methods of Car class
  int load; // Truck class can also have its own instance variables and methods
  void haul(int weight) {
    System.out.println("Hauling " + weight + " kilograms.");
  }
}

Truck myTruck = new Truck(); // create an object of the Truck class
myTruck.color = "black"; // assign a value to the color variable of myTruck object
myTruck.speed = 80; // assign a value to the speed variable of myTruck object
myTruck.load = 1000; // assign a value to the load variable of myTruck object
myTruck.drive(200); // call the drive method of myTruck object
myTruck.haul(500); // call the haul method of myTruck object
```

- A mnemonic to remember the syntax of declaring a class is: **C**lass **N**ame **B**ody, or **CNB**.
- A mnemonic to remember the syntax of declaring a method is: **R**eturn **T**ype **M**ethod **N**ame **P**arameters **B**ody, or **RTMNPB**.
- A mnemonic to remember the syntax of creating an object is: **C**lass **N**ame **O**bject **N**ame **N**ew **C**lass **N**ame, or **CNONNCN**.