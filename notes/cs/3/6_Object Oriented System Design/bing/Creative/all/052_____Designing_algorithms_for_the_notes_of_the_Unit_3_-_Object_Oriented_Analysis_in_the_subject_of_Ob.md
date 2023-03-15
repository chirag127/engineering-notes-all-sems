# Designing algorithms for object oriented analysis

Object oriented analysis (OOA) is the process of identifying and modeling the problem domain in terms of objects, classes, attributes, methods, and relationships. OOA aims to capture the functional requirements of the software system while remaining independent of the implementation details. OOA is usually performed before object oriented design (OOD), which transforms the analysis model into a design model that specifies how the system will be built using concrete technologies.

Designing algorithms for OOA involves the following steps:

- Identify the objects and classes in the problem domain. Objects are entities that have state and behavior, and classes are abstractions that define the common properties and methods of a group of objects. Objects and classes can be identified by using techniques such as noun-verb analysis, use case analysis, CRC cards, and class diagrams.
- Define the attributes and methods of each class. Attributes are data fields that store the state of an object, and methods are operations that define the behavior of an object. Attributes and methods can be defined by using techniques such as state diagrams, sequence diagrams, and collaboration diagrams.
- Establish the relationships and associations among the classes. Relationships are connections that show how classes interact with each other, and associations are specific instances of relationships that link objects. Relationships and associations can be defined by using techniques such as association rules, multiplicity, aggregation, composition, inheritance, and polymorphism.
- Specify the constraints and rules that govern the system. Constraints are restrictions that limit the values or actions of the objects and classes, and rules are statements that define the logic or functionality of the system. Constraints and rules can be defined by using techniques such as preconditions, postconditions, invariants, and contracts.
- Design the algorithms for each method. Algorithms are step-by-step procedures that solve the problem laid down in a method. Algorithms focus on how the method is to be implemented, and can be expressed in pseudocode, flowcharts, or programming languages.

The following is an example of designing an algorithm for a method in OOA:

- Problem domain: A library system that allows users to borrow and return books.
- Method: borrowBook(bookID, userID)
- Algorithm:

```
// pseudocode for borrowBook method
// input: bookID, userID
// output: none
// preconditions: bookID and userID are valid, book is available, user has not exceeded borrowing limit
// postconditions: book is borrowed by user, book status is updated, user record is updated

// check preconditions
if bookID is not valid or userID is not valid then
  display "Invalid input"
  exit
end if
if book is not available then
  display "Book is not available"
  exit
end if
if user has exceeded borrowing limit then
  display "User has exceeded borrowing limit"
  exit
end if

// borrow book
set book.borrower to userID
set book.status to "borrowed"
set book.dueDate to current date + 14 days
add book to user.borrowedBooks
display "Book is borrowed successfully"

// update book status and user record
save book to database
save user to database
```