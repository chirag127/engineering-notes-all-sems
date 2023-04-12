## Identifying Domain Classes from the Problem Statements for the notes of the Software Engineering Mapping with Virtual Lab Lab in the subject of Software Engineering

- A domain class is a representation of a real-world entity or concept that is relevant to the problem domain of a software system.
- A domain class has attributes (properties or characteristics) and methods (operations or behaviors) that describe its state and functionality.
- Identifying domain classes from the problem statements is a key step in the object-oriented analysis and design process, as it helps to define the scope and requirements of the system.
- To identify domain classes from the problem statements, the following steps can be followed:

  - Read the problem statement carefully and identify the nouns and noun phrases that represent potential domain classes.
  - Eliminate the nouns and noun phrases that are irrelevant, vague, or out of scope for the system.
  - Eliminate the nouns and noun phrases that are synonyms, attributes, or collections of other domain classes.
  - For each remaining noun or noun phrase, determine if it is a domain class or a subclass of another domain class. A subclass is a specialized version of a domain class that inherits its attributes and methods.
  - For each domain class and subclass, define its attributes and methods based on the problem statement and the common sense knowledge of the domain.
  - Draw a class diagram that shows the domain classes, subclasses, attributes, methods, and relationships among them. Use the appropriate notation and symbols for the class diagram.

- Example: Consider the following problem statement for a library management system:

  - The library has books and journals that can be borrowed by the members. The books and journals have titles, authors, publishers, and ISBN numbers. The books also have editions and categories. The journals also have volumes and issues. The members have names, addresses, phone numbers, and email addresses. The members can borrow up to three books and two journals at a time for a period of two weeks. The members can also reserve books and journals that are currently unavailable. The library charges fines for overdue items. The library also has staff who manage the inventory, circulation, and reservation of the items.

- The following are the steps to identify the domain classes from the problem statement:

  - Identify the nouns and noun phrases: library, books, journals, members, titles, authors, publishers, ISBN numbers, editions, categories, volumes, issues, names, addresses, phone numbers, email addresses, items, period, fines, staff, inventory, circulation, reservation.
  - Eliminate the irrelevant, vague, or out of scope nouns and noun phrases: library, titles, authors, publishers, ISBN numbers, editions, categories, volumes, issues, names, addresses, phone numbers, email addresses, items, period, fines, inventory, circulation, reservation.
  - Eliminate the synonyms, attributes, or collections of other domain classes: titles, authors, publishers, ISBN numbers, editions, categories, volumes, issues, names, addresses, phone numbers, email addresses, items, period, fines.
  - Determine the domain classes and subclasses: books, journals, members, staff. Books and journals are subclasses of a superclass called item. Members and staff are subclasses of a superclass called person.
  - Define the attributes and methods of each domain class and subclass:

    - Item: a superclass that represents any item that can be borrowed from the library.
      - Attributes: title, author, publisher, ISBN, status (available, borrowed, reserved).
      - Methods: borrow, return, reserve, cancelReservation, checkStatus, calculateFine.
    - Book: a subclass of item that represents a book.
      - Attributes: edition, category.
      - Methods: inherit from item.
    - Journal: a subclass of item that represents a journal.
      - Attributes: volume, issue.
      - Methods: inherit from item.
    - Person: a superclass that represents any person who is associated with the library.
      - Attributes: name, address, phone, email.
      - Methods: none.
    - Member: a subclass of person that represents a member of the library.
      - Attributes: membershipId, borrowedItems, reservedItems.
      - Methods: borrowItem, returnItem, reserveItem, cancelReservation, checkBorrowedItems, checkReservedItems, payFine.
    - Staff: a subclass of person that represents a staff of the library.
      - Attributes: staffId, role, salary.
      - Methods: manageInventory, manageCirculation, manageReservation, collectFine.

  - Draw a class diagram:

    ```mermaid
    classDiagram
    Item <|-- Book
    Item <|-- Journal
    Person <|-- Member
    Person <|-- Staff
    Item : +title
    Item : +author
    Item

```
