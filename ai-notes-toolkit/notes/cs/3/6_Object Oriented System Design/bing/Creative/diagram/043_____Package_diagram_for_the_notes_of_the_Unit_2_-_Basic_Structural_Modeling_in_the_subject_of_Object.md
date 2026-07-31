### Package diagram

- A package diagram is a structural diagram that shows the organization and arrangement of various model elements in the form of packages.
- A package is a grouping of related UML elements, such as diagrams, documents, classes, or even other packages.
- The main goal of package diagrams is to simplify the complex class diagrams that can be used to group classes into packages.
- These groups help define the hierarchy and dependencies among the packages and their elements.
- A package diagram can also show the visibility and accessibility of the elements within the packages.

#### Basic notation of package diagram

- A package is represented by a tabbed folder with the package name on the top of the folder.
- A dependency is represented by a dashed arrow with the direction pointing from the dependent package to the independent package.
- A package import is a special kind of dependency that indicates that all the public elements of the imported package are available to the importing package.
- A package merge is another special kind of dependency that indicates that the contents of the merged package are combined with the contents of the receiving package.
- A package access is a relationship that specifies the accessibility of the elements of a package from another package.
- A package access can be public, private, protected, or package.

#### Example of package diagram

- Here is an example of a package diagram for a banking system.

![Package diagram for banking system](https://www.edrawmax.com/images/article/package-diagram-uml-1.png)

- The diagram shows four packages: Bank, Customer, Account, and Transaction.
- The Bank package depends on the Customer package, which means that the Bank package uses some elements from the Customer package.
- The Bank package also imports the Account package, which means that the Bank package can access all the public elements of the Account package.
- The Account package merges with the Transaction package, which means that the Account package includes the contents of the Transaction package.
- The Account package has a public access to the Customer package, which means that the Account package can access all the elements of the Customer package.
- The Transaction package has a private access to the Account package, which means that the Transaction package can only access the elements of the Account package that are declared as private.