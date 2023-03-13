## Unit 1 - Introduction to Software Engineering

One of the diagrams that can be used to introduce software engineering is the class diagram. A class diagram is a type of static structure diagram that describes the structure of a system by showing the system's classes, their attributes, operations (or methods), and the relationships among objects. A class diagram can be used to model the logical design of a software system, as well as the physical design of a database or a component.

A class diagram consists of the following elements:

- Classes: A class is a blueprint for an object. It defines the properties and behaviors of a group of objects that share the same characteristics. A class is represented by a rectangle with the class name at the top, followed by the attributes and operations in separate compartments.
- Attributes: An attribute is a property or characteristic of a class. It defines the state or data of an object. An attribute is represented by a name and a type, optionally followed by a visibility indicator and an initial value.
- Operations: An operation is a function or method that defines the behavior or action of a class. It specifies what an object can do or how it can interact with other objects. An operation is represented by a name and a parameter list, optionally followed by a visibility indicator and a return type.
- Relationships: A relationship is a connection or association between two or more classes. It defines how the classes interact or depend on each other. There are different types of relationships, such as inheritance, association, aggregation, composition, and dependency. A relationship is represented by a line or an arrow between the classes, optionally labeled with a name, a multiplicity, and a role.

The following diagram illustrates the basic structure of a class diagram using an example of a bank system:

```
+----------------+       +----------------+       +----------------+
|    Customer    |       |    Account     |       |    BankCard    |
+----------------+       +----------------+       +----------------+
| -name: String  |       | -number: String|       | -number: String|
| -address: String|      | -balance: double|      | -pin: int      |
+----------------+       +----------------+       +----------------+
| +deposit(amount:|      | +deposit(amount:|      | +withdraw(amount:|
|  double): void |<>-----|  double): void |<>-----|  double): void |
| +withdraw(amount:|     | +withdraw(amount:|     | +checkBalance():|
|  double): void |       |  double): void |       |  double        |
| +transfer(amount:|     | +transfer(amount:|     +----------------+
|  double, to: Account):|  double, to: Account):|
|  void           |       |  void           |
+----------------+       +----------------+
       ^                        ^
       |                        |
       |                        |
       |                        |
+----------------+       +----------------+
|    Employee    |       |    Manager     |
+----------------+       +----------------+
| -id: String    |       | -id: String    |
| -name: String  |       | -name: String  |
| -salary: double|       | -salary: double|
+----------------+       +----------------+
| +login(): void |       | +login(): void |
| +logout(): void|       | +logout(): void|
| +checkCustomer(|       | +checkCustomer(|
|  id: String): Customer|  id: String): Customer|
| +createAccount(|       | +createAccount(|
|  customer: Customer): |  customer: Customer): |
|  Account       |       |  Account       |
+----------------+       +----------------+
```

The diagram shows that:

- A Customer class has attributes name and address, and operations deposit, withdraw, and transfer. A Customer class has an aggregation relationship with an Account class, meaning that a customer can have one or more accounts, but the accounts can exist independently of the customer.
- An Account class has attributes number and balance, and operations deposit, withdraw, and transfer. An Account class has a composition relationship with a BankCard class, meaning that an account has one or more bank cards, and the bank cards cannot exist without the account.
- A BankCard class has attributes number and pin, and operations withdraw and checkBalance.
- An Employee class has attributes id, name, and salary, and operations login, logout, and checkCustomer. An Employee class has an inheritance relationship with a Manager class, meaning that a manager is a special type of employee