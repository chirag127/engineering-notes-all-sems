# Private and public members

- In object-oriented programming, a class is a blueprint that defines the attributes and behaviors of a type of objects.
- An object is an instance of a class that has specific values for the attributes and can perform the behaviors defined by the class.
- A class can have members, which are variables or methods that belong to the class or its objects.
- Members can have different access modifiers, which determine the visibility and accessibility of the members from other classes or objects.
- The two most common access modifiers are private and public.
- Private members are only accessible within the same class or by the objects of the same class. They are hidden from other classes or objects.
- Public members are accessible by any class or object. They are exposed to other classes or objects.
- The purpose of using private and public members is to achieve encapsulation, which is one of the principles of object-oriented design.
- Encapsulation means hiding the implementation details of a class from the outside world and providing a public interface to interact with the class.
- Encapsulation helps to maintain the integrity and security of the class, as well as to reduce the complexity and dependencies of the code.
- To declare a private member, use the keyword `private` before the member name. To declare a public member, use the keyword `public` before the member name.
- For example, consider the following class that represents a bank account:

```java
class BankAccount {
  // private members
  private String owner;
  private double balance;

  // public members
  public BankAccount(String owner, double balance) {
    // constructor
    this.owner = owner;
    this.balance = balance;
  }

  public String getOwner() {
    // getter method
    return owner;
  }

  public double getBalance() {
    // getter method
    return balance;
  }

  public void deposit(double amount) {
    // public method
    balance += amount;
  }

  public void withdraw(double amount) {
    // public method
    if (amount <= balance) {
      balance -= amount;
    }
  }
}
```

- In this class, the owner and balance are private members, which means they can only be accessed or modified by the methods of the same class or by the objects of the same class.
- The constructor, the getter methods, and the deposit and withdraw methods are public members, which means they can be accessed or invoked by any class or object that has a reference to a BankAccount object.
- The public members provide a public interface to interact with the BankAccount class, while the private members hide the implementation details of the class.