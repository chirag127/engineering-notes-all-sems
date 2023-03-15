# Entity Relationship Diagrams

- Entity Relationship Diagrams (ERDs) are a data modeling method used in software engineering to produce a conceptual data model of an information system.
- ERDs help to identify different system elements and their relationships with each other.
- ERDs are often used as the basis for data flow diagrams or DFDs.
- ERDs contain different symbols and connectors that visualize two important information: the major entities within the system scope, and the inter-relationships among these entities.
- An entity is a real-world object or concept that exists independently and can be identified uniquely .
- A relationship is a logical association or connection between two or more entities .
- An attribute is a property or characteristic of an entity or a relationship .
- A cardinality is a constraint that specifies the number of instances of one entity that can be associated with each instance of another entity .
- A primary key is an attribute or a set of attributes that uniquely identifies each instance of an entity .
- A foreign key is an attribute or a set of attributes that refers to the primary key of another entity or the same entity .

## Example of an ERD

- Consider a simple information system for a library that keeps track of books, authors, and borrowers.
- The following ERD shows the entities, attributes, relationships, and cardinalities of this system.

![ERD example](https://www.conceptdraw.com/How-To-Guide/picture/erd-entity-relationship-diagram-software-engineering/Entity-Relationship-Diagram-Software-Engineering.png)

- The entity Book has four attributes: ISBN, Title, Year, and Pages. ISBN is the primary key of Book.
- The entity Author has three attributes: ID, Name, and Country. ID is the primary key of Author.
- The entity Borrower has three attributes: CardNo, Name, and Phone. CardNo is the primary key of Borrower.
- The relationship Written_by connects Book and Author. It has a cardinality of many-to-many, meaning that a book can have multiple authors and an author can write multiple books.
- The relationship Borrowed_by connects Book and Borrower. It has a cardinality of one-to-many, meaning that a book can be borrowed by only one borrower at a time and a borrower can borrow multiple books.
- The attribute DueDate is attached to the relationship Borrowed_by to indicate the date when the book should be returned.
- The attribute ID of Author is a foreign key in Book, meaning that it refers to the primary key of Author.
- The attribute CardNo of Borrower is a foreign key in Borrowed_by, meaning that it refers to the primary key of Borrower.

## Benefits of ERDs

- ERDs help to communicate the requirements and design of an information system to various stakeholders, such as developers, users, and managers .
- ERDs help to ensure the consistency and accuracy of the data in an information system by enforcing the rules and constraints of the entities and relationships .
- ERDs help to facilitate the implementation and maintenance of an information system by providing a clear and logical structure of the data and their interdependencies .
- ERDs help to reduce the complexity and ambiguity of an information system by using standardized symbols and notation to represent the data and their relationships .