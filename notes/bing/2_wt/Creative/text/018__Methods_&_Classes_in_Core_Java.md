#### Methods & Classes in Core Java

- A method is a block of code that performs a specific task. A method can have parameters, which are values that are passed to the method when it is invoked. A method can also return a value to the caller, or perform some action without returning anything.
- A class is a blueprint for creating objects. A class defines the properties and behaviors of the objects of that type. A class can have fields, which are variables that store data for each object, and methods, which are functions that operate on the object's fields or provide other services.
- To define a method in a class, use the following syntax:

```java
modifier returnType methodName(parameterList) {
  // method body
}
```

- The modifier specifies the access level of the method, such as public, private, protected, or default. The returnType specifies the type of value that the method returns, or void if it does not return anything. The methodName is the name of the method, which must follow the Java naming conventions. The parameterList is a comma-separated list of parameters, each with a type and a name. The method body is a block of code that implements the logic of the method.
- To invoke a method in a class, use the following syntax:

```java
objectName.methodName(argumentList);
```

- The objectName is the name of the object that the method belongs to, or the class name if the method is static. The methodName is the name of the method to be invoked. The argumentList is a comma-separated list of values that are passed to the method as parameters.
- To define a class in Java, use the following syntax:

```java
modifier class ClassName {
  // class body
}
```

- The modifier specifies the access level of the class, such as public, private, protected, or default. The ClassName is the name of the class, which must follow the Java naming conventions. The class body is a block of code that contains the fields and methods of the class.
- To create an object of a class in Java, use the following syntax:

```java
ClassName objectName = new ClassName(argumentList);
```

- The ClassName is the name of the class that the object belongs to. The objectName is the name of the object, which must follow the Java naming conventions. The argumentList is a comma-separated list of values that are passed to the constructor of the class, which is a special method that initializes the object's fields. The new keyword creates a new instance of the class and assigns it to the objectName.