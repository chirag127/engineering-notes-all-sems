### Private and public members

- In object-oriented programming, a class is a blueprint that defines the attributes and behaviors of a set of objects.
- An attribute is a variable that stores some data associated with an object, such as its name, color, size, etc.
- A behavior is a method that performs some action on or with an object, such as moving it, changing its color, printing its data, etc.
- A class can have two types of members: private and public.
- A private member is an attribute or a method that can only be accessed by the object itself or by other members of the same class.
- A public member is an attribute or a method that can be accessed by any other object or class.
- The purpose of using private and public members is to enforce the principle of encapsulation, which means hiding the internal details of an object from the outside world and exposing only the essential features that are relevant for its use.
- Encapsulation helps to achieve modularity, security, and maintainability of the code, as it prevents unauthorized or unintended access or modification of the object's data and behavior.
- To declare a private member in a class, we use the keyword `private` before its name, such as `private int age;` or `private void printAge();`.
- To declare a public member in a class, we use the keyword `public` before its name, such as `public String name;` or `public void printName();`.
- By default, all members of a class are private, unless specified otherwise.
- To access a private member of an object, we use the dot operator (`.`) followed by the member name, such as `obj.age` or `obj.printAge();`, but only within the same class or the object itself.
- To access a public member of an object, we use the dot operator (`.`) followed by the member name, such as `obj.name` or `obj.printName();`, from anywhere in the code.
- An example of a class with private and public members is:

```java
// A class that represents a person
class Person {
  // Private attributes
  private String name; // The name of the person
  private int age; // The age of the person

  // Public constructor
  public Person(String name, int age) {
    // Assign the parameters to the attributes
    this.name = name;
    this.age = age;
  }

  // Public method to print the name of the person
  public void printName() {
    System.out.println("The name of the person is " + name);
  }

  // Private method to print the age of the person
  private void printAge() {
    System.out.println("The age of the person is " + age);
  }

  // Public method to call the private method printAge()
  public void showAge() {
    // Call the private method printAge()
    printAge();
  }
}

// A class that tests the Person class
class TestPerson {
  public static void main(String[] args) {
    // Create a Person object with name "Alice" and age 25
    Person p1 = new Person("Alice", 25);

    // Access and print the public attribute name
    System.out.println("The name attribute is " + p1.name);

    // Access and print the private attribute age
    // This will cause a compile-time error, as age is private
    // System.out.println("The age attribute is " + p1.age);

    // Call the public method printName()
    p1.printName();

    // Call the private method printAge()
    // This will also cause a compile-time error, as printAge() is private
    // p1.printAge();

    // Call the public method showAge(), which calls the private method printAge()
    p1.showAge();
  }
}
```

- The output of the TestPerson class is:

```
The name attribute is Alice
The name of the person is Alice
The age of the person is 25
```