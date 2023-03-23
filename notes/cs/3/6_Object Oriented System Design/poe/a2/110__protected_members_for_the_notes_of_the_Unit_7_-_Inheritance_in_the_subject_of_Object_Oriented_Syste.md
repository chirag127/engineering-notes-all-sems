 Here are the notes on protected members for Unit 7 - Inheritance in Object Oriented System Design:

### Protected Members

- Protected members are accessible within the class and its subclasses.
- They are more restrictive than public members but less restrictive than private members.
- Protected access modifier is used when we want to hide members within the class hierarchy but allow subclasses to access them.
- This is useful in case of inheritance where we want to share members among subclasses but don't want external classes to access them.
- For example:

```
class Parent {
  protected int x = 5;
}

class Child extends Parent {
  void printX() {
    System.out.println(x); // can access protected member
  }
}

class NotChild {
  void printX() {
    System.out.println(new Parent().x); // error, cannot access protected member
  }
}
```

- Protected constructors and methods can also be accessed only within the class and its subclasses.
- Protected members allow related classes to access each other's implementation details which can aid in code reuse through inheritance. However, it also exposes the class's implementation which can potentially break encapsulation. Thus, protected access should be used judiciously based on the requirements.

The content is written in a formal tone with points and without emojis or external links as requested. Let me know if you would like me to modify or expand the notes in any way.