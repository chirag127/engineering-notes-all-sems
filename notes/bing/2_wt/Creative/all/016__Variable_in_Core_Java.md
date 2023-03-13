#### Variable in Core Java

- A variable is a named memory location that can store a value of a specific data type in Java.
- A variable has three components: a name, a type, and a value.
- The name of a variable is an identifier that follows the Java naming rules and conventions. For example, `num`, `firstName`, `MAX_VALUE` are valid variable names.
- The type of a variable determines the range of values that it can store and the operations that can be performed on it. For example, `int`, `String`, `boolean` are some of the data types in Java.
- The value of a variable is the data that is stored in the memory location assigned to the variable. For example, `num = 10`, `firstName = "Sydney"`, `MAX_VALUE = 2147483647` are some of the variable assignments in Java.
- Variables can be classified into two categories based on their scope: local variables and global variables.
- Local variables are declared and used within a method, constructor, or block. They are created when the method, constructor, or block is executed and destroyed when it ends. They are not accessible outside their scope. For example,

```java
public class Test {
  public static void main(String[] args) {
    int x = 5; // local variable
    System.out.println(x); // prints 5
  }
}
```

- Global variables are declared outside any method, constructor, or block, usually at the class level. They are also called fields or attributes. They are created when the class is loaded and destroyed when the class is unloaded. They are accessible throughout the class and can be modified by any method. For example,

```java
public class Test {
  static int y = 10; // global variable
  public static void main(String[] args) {
    System.out.println(y); // prints 10
    change(); // calls the change method
    System.out.println(y); // prints 20
  }
  public static void change() {
    y = 20; // modifies the global variable
  }
}
```

- Variables can also be classified into three categories based on their modifiers: final variables, static variables, and instance variables.
- Final variables are variables that are declared with the `final` keyword. They can be assigned only once and cannot be changed later. They are also called constants. For example,

```java
public class Test {
  final int Z = 100; // final variable
  public static void main(String[] args) {
    Z = 200; // error: cannot assign a value to final variable Z
  }
}
```

- Static variables are variables that are declared with the `static` keyword. They belong to the class and not to any specific object. They are shared by all the objects of the class. They are also called class variables. For example,

```java
public class Test {
  static int count = 0; // static variable
  public Test() {
    count++; // increments the static variable
  }
  public static void main(String[] args) {
    Test t1 = new Test(); // creates an object of Test
    Test t2 = new Test(); // creates another object of Test
    System.out.println(count); // prints 2
  }
}
```

- Instance variables are variables that are declared without any modifier. They belong to the object and not to the class. They are unique for each object of the class. They are also called object variables. For example,

```java
public class Test {
  int age; // instance variable
  public Test(int a) {
    age = a; // assigns the parameter value to the instance variable
  }
  public static void main(String[] args) {
    Test t1 = new Test(20); // creates an object of Test with age 20
    Test t2 = new Test(30); // creates another object of Test with age 30
    System.out.println(t1.age); // prints 20
    System.out.println(t2.age); // prints 30
  }
}
```

- A mnemonic to remember the difference between static and instance variables is: **S**tatic variables are **S**hared by all objects, **I**nstance variables are **I**ndividual for each object.