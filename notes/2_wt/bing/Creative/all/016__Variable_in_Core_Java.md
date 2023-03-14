#### Variable in Core Java

- A variable is a named memory location that can store a value of a specific data type in Java.
- A variable has three components: a name, a type, and a value.
- The name of a variable is an identifier that follows the Java naming rules and conventions. For example, `num`, `firstName`, and `MAX_VALUE` are valid variable names.
- The type of a variable determines the range of values that it can store and the operations that can be performed on it. For example, `int`, `String`, and `boolean` are some of the data types in Java.
- The value of a variable is the data that is stored in the memory location assigned to the variable. For example, `num = 10`, `firstName = "John"`, and `MAX_VALUE = 2147483647` are some of the variable assignments in Java.
- Variables can be classified into two categories based on their scope: local variables and global variables.
- Local variables are declared and used within a method, constructor, or block. They are created when the method, constructor, or block is entered and destroyed when it is exited. They are not accessible outside their scope. For example,

```java
public class Test {
    public static void main(String[] args) {
        int x = 10; // local variable
        System.out.println(x); // prints 10
    }
}
```

- Global variables are declared and used outside any method, constructor, or block. They are also known as class variables or instance variables. They are created when the class is loaded and destroyed when the class is unloaded. They are accessible throughout the class and can also be accessed by other classes depending on their access modifiers. For example,

```java
public class Test {
    static int y = 20; // class variable
    int z = 30; // instance variable

    public static void main(String[] args) {
        System.out.println(y); // prints 20
        Test obj = new Test();
        System.out.println(obj.z); // prints 30
    }
}
```

- Variables can also be classified into two categories based on their initialization: static variables and non-static variables.
- Static variables are initialized only once at the time of class loading. They are also known as class variables. They are declared with the keyword `static`. They can be accessed by using the class name or an object reference. For example,

```java
public class Test {
    static int a = 40; // static variable

    public static void main(String[] args) {
        System.out.println(Test.a); // prints 40
        Test obj = new Test();
        System.out.println(obj.a); // prints 40
    }
}
```

- Non-static variables are initialized every time an object of the class is created. They are also known as instance variables. They are declared without the keyword `static`. They can be accessed only by using an object reference. For example,

```java
public class Test {
    int b = 50; // non-static variable

    public static void main(String[] args) {
        Test obj1 = new Test();
        System.out.println(obj1.b); // prints 50
        Test obj2 = new Test();
        System.out.println(obj2.b); // prints 50
    }
}
```

- A mnemonic to remember the difference between static and non-static variables is: **S**tatic variables are **S**hared by all objects of the class, while **N**on-static variables are **N**ot shared by all objects of the class.