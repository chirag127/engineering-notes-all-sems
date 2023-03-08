 Here is the content in markdown format for the topic ### this pointer for the notes of Unit 8 - Polymorphism in Object Oriented System Design:

### this Pointer

- `this` is a pointer that points to the current object.
- It is passed as an implicit parameter to all non-static methods and is used to access the current object's properties and methods.
- `this` is particularly useful in constructors, when there are local variables with the same names as fields. We can use `this` to differentiate between them. For example:

```java
public class Person {
    private String name;

    public Person(String name) {
        this.name = name; // assigns to field
    }
}
```

- We can also use `this` to pass a reference to the current object to other methods. For example:

```java
public class Person {
    public void greet(Person p) {
        System.out.println("Hello " + p.getName());
    }

    public void selfGreet() {
        greet(this); // pass reference to current object
    }
}
```

- The type of `this` is the class type, e.g. `Person.this` for the `Person` class.
- You cannot explicitly change the value of `this`. It always points to the object that invokes the current method.
- `this` cannot be used in static methods because static methods are not passed a reference to the object.

**Advantages:**
- Differentiates between local variables and fields
- Passes current object reference
- Readable code (clear intent)

**Disadvantages:**
- Not useful in static methods

**Applications:** Commonly used to differentiate between local variables and fields, and to pass a reference to the current object.

How's this? I have written the content on this pointer in points in a formal tone with explanations, examples and advantages/disadvantages as you requested. Please let me know if you would like me to modify or add anything.