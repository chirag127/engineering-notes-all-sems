## Unit 6 - Use case 1

- A use case is a description of how a system interacts with one or more external entities, called actors, to achieve a specific goal.
- A use case diagram is a graphical representation of the use cases and actors involved in a system.
- A use case diagram consists of the following elements:
  - Actors: represent the external entities that interact with the system. They are drawn as stick figures with a name.
  - Use cases: represent the goals or functions that the system provides to the actors. They are drawn as ovals with a name.
  - Associations: represent the communication or interaction between an actor and a use case. They are drawn as solid lines with optional arrows to indicate the direction of the interaction.
  - System boundary: represents the scope or boundary of the system under consideration. It is drawn as a rectangle that encloses the use cases and actors that are part of the system.
  - Packages: represent a grouping of related use cases or actors. They are drawn as rectangles with a name and a dashed line around the grouped elements.
  - Generalization: represent a relationship of inheritance or specialization between two actors or two use cases. They are drawn as solid lines with a hollow triangle pointing to the parent or more general element.
  - Include: represent a relationship of dependency or inclusion between two use cases, where one use case (the base) includes the behavior of another use case (the inclusion) as part of its normal execution. They are drawn as dashed lines with an open arrowhead pointing to the included use case and a label <<include>>.
  - Extend: represent a relationship of dependency or extension between two use cases, where one use case (the extension) extends the behavior of another use case (the base) under some condition. They are drawn as dashed lines with an open arrowhead pointing to the extended use case and a label <<extend>>.

- An example of a use case diagram for a library system is shown below:

```markdown
![Use case diagram for a library system](use_case_diagram.png)

Figure 1: Use case diagram for a library system

The use case diagram shows the following elements:

- Actors: Library Member, Librarian, and Supplier.
- Use cases: Borrow Book, Return Book, Reserve Book, Search Book, Manage Book, Order Book, and Receive Book.
- Associations: Library Member is associated with Borrow Book, Return Book, Reserve Book, and Search Book. Librarian is associated with Manage Book and Order Book. Supplier is associated with Receive Book.
- System boundary: The system boundary is the rectangle labeled Library System that encloses the use cases and actors that are part of the system.
- Packages: The package labeled Book Management contains the use cases Manage Book, Order Book, and Receive Book.
- Generalization: Library Member is a generalization of Student and Faculty, which are not shown in the diagram. Borrow Book is a generalization of Borrow Physical Book and Borrow E-Book, which are also not shown in the diagram.
- Include: Borrow Book includes Search Book, which means that searching for a book is a necessary part of borrowing a book. Manage Book includes Search Book, which means that searching for a book is a necessary part of managing a book.
- Extend: Borrow Book is extended by Reserve Book, which means that reserving a book is an optional or conditional part of borrowing a book. Search Book is extended by Filter Book and Sort Book, which means that filtering and sorting the search results are optional or conditional parts of searching for a book.
```