### Relationship of Higher Degree

- A relationship of higher degree is a relationship that involves more than two entities.
- For example, a ternary relationship is a relationship of degree three, which means it relates three entities.
- A common example of a ternary relationship is the **enrolls** relationship between **student**, **course**, and **section** entities. A student enrolls in a section of a course, and a section belongs to a course.
- A relationship of higher degree can be represented in an entity-relationship (ER) diagram using a diamond-shaped symbol with the name of the relationship and the degree as a subscript.
- For example, the **enrolls** relationship can be represented as:

![enrolls](https://i.imgur.com/7w0f0ZL.png)

- A relationship of higher degree can also be converted into an equivalent set of binary relationships by introducing a new entity that represents the combination of the original entities.
- For example, the **enrolls** relationship can be converted into two binary relationships by introducing a new entity called **enrollment** that has the primary keys of **student**, **course**, and **section** as its attributes.
- The new ER diagram would look like:

![enrollment](https://i.imgur.com/0ZL3Z3L.png)

- The advantage of converting a relationship of higher degree into binary relationships is that it simplifies the design and implementation of the database schema.
- The disadvantage is that it may introduce redundancy and inconsistency in the data, as the same information may be stored in multiple places.