### Type Conversion

- Type conversion is the process of changing the data type of a value or an expression to another data type.
- There are two types of type conversion: implicit and explicit.
- Implicit type conversion is done automatically by the compiler or the interpreter when the operands of an expression have different data types or when a value is assigned to a variable of a different data type.
- Explicit type conversion is done by the programmer using type casting operators or methods to explicitly convert a value or an expression to a desired data type.
- Type conversion can be done between primitive data types (such as int, float, char, etc.) or between reference data types (such as objects, arrays, strings, etc.).
- Type conversion can also be done between user-defined data types (such as classes, interfaces, enums, etc.) using constructors, methods, or inheritance.
- Some examples of type conversion are:

```java
// implicit type conversion
int x = 10;
double y = x; // x is converted to double and assigned to y
System.out.println(y); // prints 10.0

// explicit type conversion
double z = 3.14;
int w = (int) z; // z is casted to int and assigned to w
System.out.println(w); // prints 3

// type conversion between reference data types
String s = "Hello";
Object o = s; // s is converted to Object and assigned to o
System.out.println(o); // prints Hello

// type conversion between user-defined data types
class A {
  int a;
  A(int a) {
    this.a = a;
  }
}

class B extends A {
  int b;
  B(int a, int b) {
    super(a);
    this.b = b;
  }
}

A obj1 = new A(10);
B obj2 = new B(20, 30);
obj1 = obj2; // obj2 is converted to A and assigned to obj1
System.out.println(obj1.a); // prints 20
System.out.println(obj1.b); // error: b is not a member of A
obj2 = (B) obj1; // obj1 is casted to B and assigned to obj2
System.out.println(obj2.a); // prints 20
System.out.println(obj2.b); // prints 30
```