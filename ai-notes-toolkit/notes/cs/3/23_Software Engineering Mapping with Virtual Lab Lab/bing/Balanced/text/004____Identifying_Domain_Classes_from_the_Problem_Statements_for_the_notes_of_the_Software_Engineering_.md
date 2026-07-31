## Identifying Domain Classes from the Problem Statements for the notes of the Software Engineering Mapping with Virtual Lab Lab in the subject of Software Engineering

- A domain class is a representation of a real-world entity or concept that is relevant to the problem domain of a software system.
- A domain class has attributes (properties or characteristics) and operations (behaviors or actions) that describe its state and behavior in the problem domain.
- Identifying domain classes from the problem statements is a process of analyzing the textual description of the problem domain and extracting the nouns and verbs that represent the entities and actions involved in the problem.
- The steps for identifying domain classes from the problem statements are:

  - Read the problem statement carefully and identify the nouns and verbs that are relevant to the problem domain.
  - Eliminate the nouns and verbs that are irrelevant, ambiguous, or redundant.
  - Group the remaining nouns and verbs into categories based on their similarity or relationship.
  - For each category, select a representative noun as the name of the domain class and list the attributes and operations that correspond to the nouns and verbs in the category.
  - Refine the domain classes by checking for completeness, consistency, and clarity.
  - Draw a domain model diagram that shows the domain classes and their associations.

- An example of identifying domain classes from the problem statement of a library management system is:

  - Problem statement: A library management system allows the librarian to manage the books and the borrowers. The librarian can add, delete, update, and search for books and borrowers. The librarian can also issue, return, and renew books. The system keeps track of the book details, borrower details, and transaction details.
  - Nouns and verbs: librarian, manage, books, borrowers, add, delete, update, search, issue, return, renew, system, track, book details, borrower details, transaction details.
  - Eliminated nouns and verbs: system, track, details.
  - Categories: 
    - Librarian: librarian, manage
    - Book: book, add, delete, update, search, issue, return, renew
    - Borrower: borrower, add, delete, update, search
    - Transaction: transaction, issue, return, renew
  - Domain classes:
    - Librarian: attributes: id, name, password; operations: manageBooks, manageBorrowers, manageTransactions
    - Book: attributes: id, title, author, publisher, status; operations: addBook, deleteBook, updateBook, searchBook, issueBook, returnBook, renewBook
    - Borrower: attributes: id, name, address, phone, email; operations: addBorrower, deleteBorrower, updateBorrower, searchBorrower
    - Transaction: attributes: id, bookId, borrowerId, issueDate, returnDate, dueDate, fine; operations: issueBook, returnBook, renewBook, calculateFine
  - Domain model diagram:

    ```mermaid
    classDiagram
      Librarian --|> Book
      Librarian --|> Borrower
      Librarian --|> Transaction
      Book "1" -- "0..*" Transaction : issued to
      Borrower "1" -- "0..*" Transaction : borrowed by
      class Librarian{
        -id : int
        -name : string
        -password : string
        +manageBooks()
        +manageBorrowers()
        +manageTransactions()
      }
      class Book{
        -id : int
        -title : string
        -author : string
        -publisher : string
        -status : string
        +addBook()
        +deleteBook()
        +updateBook()
        +searchBook()
        +issueBook()
        +returnBook()
        +renewBook()
      }
      class Borrower{
        -id : int
        -name : string
        -address : string
        -phone : string
        -email : string
        +addBorrower()
        +deleteBorrower()
        +updateBorrower()
        +searchBorrower()
      }
      class Transaction{
        -id : int
        -bookId : int
        -borrowerId : int
        -issueDate : date
        -returnDate : date
        -dueDate : date
        -fine : double
        +issueBook()
        +returnBook()
        +renewBook()
        +calculateFine()
      }
    ```