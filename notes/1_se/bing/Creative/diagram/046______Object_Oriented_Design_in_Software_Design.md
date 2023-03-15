Object-oriented design (OOD) is the process of planning a system of interacting objects for the purpose of solving a software problem. It is one approach to software design. An object contains encapsulated data and procedures grouped together to represent an entity. Object-oriented design follows some principles, such as abstraction, encapsulation, inheritance, polymorphism, modularity, and reusability. One of the popular ways to apply object-oriented design is to follow the SOLID principles, which stand for Single-responsibility, Open-closed, Liskov substitution, Interface segregation, and Dependency inversion. These principles help to create software that is easy to maintain, extend, and reuse.

A common way to represent object-oriented design is to use a Unified Modeling Language (UML) diagram, which is a graphical notation that shows the relationships between classes, objects, interfaces, and other components of a system. A UML diagram can have different types, such as class diagram, use case diagram, sequence diagram, etc. depending on the purpose and level of abstraction. Here is an example of a class diagram that shows the object-oriented design of a simple bank system:

#### Object Oriented Design in Software Design

```
+-----------------+       +-----------------+       +-----------------+
|     Account     |       |    Customer     |       |    BankCard     |
+-----------------+       +-----------------+       +-----------------+
| -balance: double|       | -name: String   |       | -number: String |
| -interest: double|      | -address: String|       | -expiry: String |
+-----------------+       +-----------------+       +-----------------+
| +deposit(amount)|       | +addAccount(a)  |       | +validate()     |
| +withdraw(amount)|      | +removeAccount(a)|      | +withdraw(amount)|
| +transfer(amount, a)|   | +getAccounts()  |       |                 |
| +calculateInterest()|   |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
         ^                       ^    ^                     ^
         |                       |    |                     |
         |                       |    |                     |
         |                       |    +---------------------+
         |                       |                |
         |                       |                |
         |                       |                |
+-----------------+       +-----------------+    |
|   SavingsAccount|       |  CheckingAccount|    |
+-----------------+       +-----------------+    |
| -limit: double  |       | -fee: double    |    |
+-----------------+       +-----------------+    |
| +withdraw(amount)|      | +withdraw(amount)|   |
+-----------------+       +-----------------+   |
         ^                       ^               |
         |                       |               |
         |                       |               |
         +-----------------------+---------------+
                         |
                         |
                         |
                  +-----------------+
                  |    BankSystem   |
                  +-----------------+
                  | -customers: List|
                  | -accounts: List |
                  | -cards: List    |
                  +-----------------+
                  | +addCustomer(c) |
                  | +removeCustomer(c)|
                  | +createAccount(c, type)|
                  | +closeAccount(a)|
                  | +issueCard(a)   |
                  | +cancelCard(c)  |
                  +-----------------+
```

: Object-oriented design - Wikipedia
: Object Oriented Design in Software Engineering
: SOLID: The First 5 Principles of Object Oriented Design
: A Short Overview of Object Oriented Software Design - freeCodeCamp.org