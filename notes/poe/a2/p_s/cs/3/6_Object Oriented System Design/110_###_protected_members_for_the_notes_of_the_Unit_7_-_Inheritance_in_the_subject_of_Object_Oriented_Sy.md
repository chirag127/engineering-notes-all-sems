 Here is the content in markdown format for the topic ### protected members for the notes of the Unit 7 - Inheritance in the subject of Object Oriented System Design:

### Protected Members

- Protected members are similar to private members in that they can only be accessed by members of the class in which they are declared.
- However, protected members can also be accessed by inherited subclasses. This is useful when you want to allow subclasses to access the internals of the superclass, but not external code.
- For example:
```java
class Superclass {
    protected int protMember;

    public Superclass() {
        protMember = 1;
    }
}

class Subclass extends Superclass {
    public void accessProtectedMember() {
        System.out.println(protMember); // OK
    }
}

class Unrelated {
    public void cannotAccess() {
        Superclass sup = new Superclass();
        System.out.println(sup.protMember); // Compile-time error
    }
}
```
- Here, the Subclass can access the protected member of Superclass via inheritance, but the Unrelated class cannot access it.
- Protected access can be useful for defining "internal interfaces" for subclasses - the subclass can access the protected members to use the superclass in specific ways, but external code cannot interfere with this.
- However, you should be careful with protected access - it can lead to tight coupling between superclasses and subclasses, and it can make superclass internals leaked more widely than necessary (to all subclasses, not just closely-related ones). Often, private with well-designed public accessors is a better approach.

- Advantages: Allows related subclasses access, encourages code reuse.
- Disadvantages: Can lead to tight coupling, protected details leaked more widely than necessary.
- Applications: Defining internal interfaces for subclasses to use superclass features.

[Detailed ascii diagrams, examples, etc. can be added here if helpful for learning]