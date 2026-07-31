# Package Diagram

- A package diagram is a type of structural diagram in UML that shows the arrangement and organization of model elements in middle to large scale projects .
- A package is a namespace that contains other model elements, such as classes, components, use cases, or other packages .
- A package diagram can be used to simplify complex class diagrams, group related elements, and define dependencies and visibility among elements .
- A package diagram can also show the logical structure of the system, the subsystems, the modules, and the relationships between them.

## Elements of a Package Diagram

- A package is represented by a tabbed folder with the name of the package on the tab .
- A package can contain other packages or model elements, which are shown inside the folder .
- A dependency is a relationship that indicates that one element requires another element for its specification or implementation .
- A dependency is represented by a dashed arrow with the name of the dependency on the arrow or near it .
- A dependency can have different types, such as import, access, use, call, or instantiate .
- An import dependency indicates that one package imports the public contents of another package .
- An access dependency indicates that one element accesses the contents of another element .
- A use dependency indicates that one element uses the functionality of another element .
- A call dependency indicates that one element invokes the behavior of another element .
- An instantiate dependency indicates that one element creates an instance of another element .
- A visibility is a property that defines the scope of access to an element .
- A visibility can be public, protected, private, or package .
- A public visibility means that the element is visible to any other element .
- A protected visibility means that the element is visible to elements in the same package or subclasses .
- A private visibility means that the element is visible only to elements in the same package .
- A package visibility means that the element is visible only to elements in the same package or nested packages .
- A visibility is represented by a symbol on the dependency arrow or near the element .
- A public visibility is represented by a plus sign (+) .
- A protected visibility is represented by a hash sign (#) .
- A private visibility is represented by a minus sign (-) .
- A package visibility is represented by a tilde sign (~) .

## Example of a Package Diagram

- The following diagram shows an example of a package diagram for a banking system .
- The diagram contains four packages: Bank, Customer, Account, and Transaction .
- The Bank package imports the public contents of the Customer and Account packages .
- The Customer package accesses the Account package with a protected visibility .
- The Account package uses the Transaction package with a public visibility .
- The Transaction package calls the Account package with a private visibility .

```
+-----------------+    +-----------------+    +-----------------+
|     Bank        |    |    Customer     |    |     Account     |
|-----------------|    |-----------------|    |-----------------|
|+BankController  |    |+Customer        |    |+Account         |
|+BankService     |    |+CustomerService |    |+AccountService  |
|+BankRepository  |    |+CustomerDAO     |    |+AccountDAO      |
+-----------------+    +-----------------+    +-----------------+
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |

```
