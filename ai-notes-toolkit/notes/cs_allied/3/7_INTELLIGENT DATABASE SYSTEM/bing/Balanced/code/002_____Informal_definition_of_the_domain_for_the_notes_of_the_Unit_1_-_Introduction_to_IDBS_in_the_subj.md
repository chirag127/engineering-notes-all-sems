### Informal definition of the domain for the notes of the Unit 1 - Introduction to IDBS in the subject of INTELLIGENT DATABASE SYSTEM

- An **intelligent database system (IDBS)** is a database system that integrates artificial intelligence techniques, such as machine learning, natural language processing, knowledge representation and reasoning, with traditional database management systems.
- The **domain** of an IDBS is the set of possible values that can be stored in the database, as well as the constraints and relationships among them.
- The domain of an IDBS can be defined informally by describing the following aspects:
  - The **entities** that are represented in the database, such as customers, products, orders, etc.
  - The **attributes** that describe the properties of each entity, such as name, price, quantity, etc.
  - The **data types** that specify the format and range of values for each attribute, such as integer, string, date, etc.
  - The **primary keys** that uniquely identify each entity in the database, such as customer ID, product ID, order ID, etc.
  - The **foreign keys** that link entities across different tables, such as customer ID in the order table, product ID in the order detail table, etc.
  - The **constraints** that enforce the validity and consistency of the data, such as not null, unique, check, etc.
  - The **relationships** that express the logical connections among entities, such as one-to-many, many-to-many, etc.
  - The **rules** that define the behavior and functionality of the database, such as triggers, stored procedures, functions, etc.
  - The **knowledge** that captures the domain-specific information and expertise, such as ontologies, rules, facts, etc.
- For example, an informal definition of the domain for a simple IDBS that stores information about books and authors could be:

  - There are two entities: book and author.
  - The book entity has the following attributes: book ID (integer, primary key, not null, unique), title (string, not null), genre (string, not null), publication year (integer, not null, check between 1900 and 2023), author ID (integer, foreign key, references author ID in the author table, not null).
  - The author entity has the following attributes: author ID (integer, primary key, not null, unique), name (string, not null), nationality (string, not null), birth year (integer, not null, check between 1800 and 2023).
  - There is a one-to-many relationship between author and book, meaning that one author can write many books, but each book has only one author.
  - There is a rule that calculates the age of each author based on their birth year and the current year.
  - There is a knowledge base that contains facts and rules about the genres and subgenres of books, such as fantasy, science fiction, horror, etc.