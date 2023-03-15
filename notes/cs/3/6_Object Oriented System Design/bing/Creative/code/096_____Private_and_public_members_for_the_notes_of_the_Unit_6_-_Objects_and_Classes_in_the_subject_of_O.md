### Private and public members

- In object-oriented system design, classes are the basic units of abstraction that contain properties and methods.
- Properties are also called attributes or data members, and they represent the state or characteristics of a class.
- Methods are also called operations or functions, and they represent the behavior or functionality of a class.
- Private and public are two types of access modifiers that specify the visibility or accessibility of the properties and methods of a class from other classes or components of the system.
- A public member is visible from anywhere in the system, and it can be accessed by any other class or component that has a reference to the class object. A public member is prefixed by the symbol `+` in a class diagram .
- A private member is visible only from within the class, and it cannot be accessed by any other class or component outside the class. A private member is prefixed by the symbol `-` in a class diagram .
- The purpose of using private and public members is to implement the principle of data hiding or encapsulation, which is one of the important features of object-oriented programming. Data hiding allows preventing the functions of a program to access directly the internal representation of a class type, and to enforce the separation of concerns between the interface and the implementation of a class .
- Some examples of private and public members are:

```java
// A class named Person with private and public members
public class Person {
  // A private attribute named name
  private String name;
  // A public attribute named age
  public int age;
  // A private method named getName
  private String getName() {
    return name;
  }
  // A public method named setName
  public void setName(String newName) {
    name = newName;
  }
}
```

```c++
// A class named Rectangle with private and public members
class Rectangle {
  // A private attribute named length
  private:
    double length;
  // A private attribute named width
    double width;
  // A public method named getArea
  public:
    double getArea() {
      return length * width;
    }
  // A public method named setLength
    void setLength(double newLength) {
      length = newLength;
    }
  // A public method named setWidth
    void setWidth(double newWidth) {
      width = newWidth;
    }
};
```