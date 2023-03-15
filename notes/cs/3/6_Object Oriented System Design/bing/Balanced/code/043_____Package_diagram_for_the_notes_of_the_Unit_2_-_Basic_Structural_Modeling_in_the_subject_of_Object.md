### Package diagram for the notes of the Unit 2 - Basic Structural Modeling in the subject of Object Oriented System Design

- A package diagram is a structural diagram that shows the organization and arrangement of various model elements in the form of packages .
- A package is a grouping of related UML elements, such as diagrams, documents, classes, or even other packages .
- A package diagram can be used to simplify complex class diagrams, by grouping classes into packages based on some criteria, such as functionality, domain, layer, etc.
- A package diagram can also show the dependencies between packages, classes, components, and other named elements within a system.
- A dependency is a relationship that indicates that one element requires another element for its specification or implementation.
- There are different types of dependencies, such as import, access, merge, use, etc.
- A package diagram can be drawn using the following notation :
  - A package is represented by a tabbed folder, with the name of the package on the tab or below the folder.
  - A package can contain other packages or elements, which are shown inside the folder.
  - A dependency is represented by a dashed line with an arrowhead, pointing from the dependent element to the supplier element.
  - The type of dependency can be indicated by a stereotype, such as <<import>>, <<access>>, <<merge>>, <<use>>, etc.
  - A package can also have a visibility, such as public (+), protected (#), private (-), or package (~), which determines the accessibility of its contents by other elements.
  - A package can also have a URI, which is a unique identifier that can be used to locate the package or its contents on the web or in a repository.

- An example of a package diagram is shown below, which depicts the structure of a banking system:

![Package diagram example](https://www.visual-paradigm.com/servlet/editor-content/tutorials/what-is-package-diagram/package-diagram-example.png)

- In this example, the banking system is divided into four packages: Account, Customer, Transaction, and Report.
- The Account package contains the classes that represent the different types of accounts, such as CheckingAccount, SavingsAccount, etc.
- The Customer package contains the classes that represent the customers and their information, such as Customer, Address, Phone, etc.
- The Transaction package contains the classes that represent the transactions and their details, such as Transaction, Deposit, Withdrawal, etc.
- The Report package contains the classes that generate the reports for the banking system, such as Report, AccountStatement, TransactionHistory, etc.
- The dependencies between the packages are shown by the dashed lines with arrowheads and stereotypes.
- For example, the Report package imports the Account package, which means that the Report package uses the classes from the Account package in its specification or implementation.
- Similarly, the Account package accesses the Customer package, which means that the Account package can access the public or protected elements of the Customer package.
- The Transaction package merges the Account package, which means that the Transaction package extends or modifies the elements of the Account package.
- The Customer package uses the Transaction package, which means that the Customer package invokes the operations of the Transaction package.