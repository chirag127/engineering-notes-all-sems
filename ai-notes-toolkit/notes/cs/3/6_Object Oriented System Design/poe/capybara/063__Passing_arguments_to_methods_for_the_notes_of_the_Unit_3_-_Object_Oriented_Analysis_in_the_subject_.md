### Passing arguments to methods

When we create methods in Object Oriented Programming, we often need to pass arguments to these methods. Arguments are values that we pass to a method so that it can perform some operation on them. In this section, we will discuss passing arguments to methods in more detail.

#### Types of arguments

There are two types of arguments that we can pass to a method:

1. Value arguments: A value argument is a copy of the actual value that is passed to the method. This means that if we change the value of a value argument inside the method, it will not affect the original value.

2. Reference arguments: A reference argument is a reference to the actual value that is passed to the method. This means that if we change the value of a reference argument inside the method, it will also change the original value.

#### Syntax for passing arguments

When we call a method and pass arguments to it, we need to specify the argument values inside the parentheses. The syntax for passing arguments is as follows:

```java
methodName(argument1, argument2, argument3, ...);
```

#### Example

Let's take an example to understand passing arguments to methods in Java:

```java
public class MyClass {
  public static void main(String[] args) {
    int num1 = 5;
    int num2 = 10;
    int result = sum(num1, num2);
    System.out.println(result);
  }

  public static int sum(int a, int b) {
    int c = a + b;
    return c;
  }
}
```

In the above example, we have created a method named `sum` that takes two integer arguments `a` and `b` and returns their sum. We have also called this method from the main method and passed two integer values `num1` and `num2` as arguments.

#### Conclusion

Passing arguments to methods is an important concept in Object Oriented Programming. Understanding how to pass arguments correctly can help us write more efficient and effective code. Remember that when we pass value arguments, the original value is not affected, but when we pass reference arguments, the original value can be changed inside the method.