#### Variable in Core Java

- A variable in Core Java is a data container that stores the data values during the execution of a Java program  .
- A variable is a name given to a memory location that can hold different types of values.
- A variable is the basic unit of storage in a program.
- Every variable has a data type that specifies the type and size of the value it can hold  .
- Variables in Java can be defined anywhere in the code (inside a class, inside a method, or as a method argument) and can have different modifiers.
- Depending on these conditions, variables in Java can be divided into four categories:
  - Instance Variable: A variable that is declared inside a class but outside a method. It is also called a non-static field or an object variable. It belongs to an instance of a class and each object has its own copy of the instance variable  .
  - Static Variable: A variable that is declared inside a class but outside a method with the static keyword. It is also called a class variable. It belongs to the class and is shared by all the objects of the class  .
  - Local Variable: A variable that is declared inside a method or a block of code. It is also called a method variable. It is only visible within the scope of the method or the block and is destroyed when the method or the block exits  .
  - Parameter Variable: A variable that is declared as an argument of a method. It is also called a formal parameter or a method parameter. It is used to pass values to the method from the caller  .
- Variables in Java follow some naming rules and conventions :
  - A variable name can start with a letter, a dollar sign ($), or an underscore (_), but not with a digit .
  - A variable name can contain any number of letters, digits, dollar signs, or underscores, but not any other characters or spaces .
  - A variable name is case-sensitive, which means that uppercase and lowercase letters are treated as different .
  - A variable name should not be a reserved word or a keyword in Java, such as int, class, public, etc .
  - A variable name should be descriptive and meaningful, and follow the camelCase convention for multiple words, such as firstName, lastName, etc .
- Variables in Java can be initialized with a value at the time of declaration, or assigned a value later in the code  .
- Variables in Java can be used in expressions, statements, and method calls, as long as they are in the same scope and have compatible data types  .

- Here is an example of declaring and using different types of variables in Core Java:

```java
public class VariableExample {
  // static variable
  static int x = 10; // belongs to the class and shared by all objects
  
  // instance variable
  int y = 20; // belongs to an object and each object has its own copy
  
  // method with parameter variable
  public void add(int z) { // z is a parameter variable that receives a value from the caller
    // local variable
    int result = x + y + z; // result is a local variable that is only visible in this method
    System.out.println("The result is " + result);
  }
  
  public static void main(String[] args) {
    // create an object of the class
    VariableExample obj = new VariableExample();
    
    // call the method with an argument
    obj.add(30); // 30 is an argument that is passed to the parameter variable z
    
    // print the values of the variables
    System.out.println("The value of x is " + x); // x is a static variable that can be accessed by the class name
    System.out.println("The value of y is " + obj.y); // y is

```
