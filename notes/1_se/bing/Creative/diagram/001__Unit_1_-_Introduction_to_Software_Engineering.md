## Unit 1 - Introduction to Software Engineering

Software engineering is a set of engineering methods used in the software development of system applications. It defines principles for specification, design, development, testing, evaluation, and maintenance.

A software engineering diagram is a visual representation that maps out the physical implementation for components of a software system. It shows the general structure of the software system and the associations, limitations, and boundaries between each element.

There are different types of software engineering diagrams, such as class diagrams, use case diagrams, sequence diagrams, activity diagrams, component diagrams, deployment diagrams, etc. Each type serves a different purpose and has a different notation.

One of the most common types of software engineering diagrams is the class diagram. A class diagram in the Unified Modeling Language (UML) is a type of static structure diagram that describes the structure of a system by showing the system's classes, their attributes, operations (or methods), and the relationships among objects.

The following diagram illustrates the basic notation of a class diagram:

```
+---------------------+
|       Class         |
+---------------------+
| - attribute : type  |
| + operation()       |
+---------------------+
        |  |  |
        |  |  |
        |  |  |
+---------------------+
|       Subclass      |
+---------------------+
| - attribute : type  |
| + operation()       |
+---------------------+
```

The class name is shown in the top compartment of the rectangle. The class attributes are shown in the middle compartment, with a visibility symbol (- for private, + for public, # for protected) and a type. The class operations are shown in the bottom compartment, with a visibility symbol and parentheses. The subclass inherits from the class and can override or add attributes and operations. The inheritance relationship is shown by a solid line with a hollow triangle pointing to the superclass.

The following diagram shows an example of a class diagram for a banking system:

```
+---------------------+
|      Account        |
+---------------------+
| - number : int      |
| - balance : double  |
| + deposit(amount)   |
| + withdraw(amount)  |
| + getBalance()      |
+---------------------+
        |  |  |
        |  |  |
        |  |  |
+---------------------+    +---------------------+
|     SavingsAccount  |    |    CheckingAccount  |
+---------------------+    +---------------------+
| - interestRate : double | - overdraftLimit : double |
| + addInterest()         | + withdraw(amount)        |
+---------------------+    +---------------------+
```

The SavingsAccount and CheckingAccount are subclasses of Account. They inherit the attributes and operations of Account and add their own specific ones. The SavingsAccount has an interestRate attribute and an addInterest operation. The CheckingAccount has an overdraftLimit attribute and overrides the withdraw operation to allow overdrawing up to the limit.