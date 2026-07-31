# Reduction of an ER Diagram to Tables

- An ER diagram is a graphical representation of the entities and relationships in a database.
- A table is a collection of rows and columns that store data in a database.
- The process of converting an ER diagram to tables is also known as mapping or mapping schema.
- The purpose of converting an ER diagram to tables is to create a logical schema of the database that can be implemented in a relational database management system (RDBMS).
- The basic rules for converting an ER diagram to tables are :

  - Convert all the entities in the diagram to tables. All the entities represented in the rectangular box in the ER diagram become independent tables in the database.
  - Convert all the attributes in the diagram to columns. All the attributes represented in the oval shape in the ER diagram become columns in the corresponding tables.
  - Convert all the primary keys in the diagram to primary keys in the tables. All the attributes that are underlined in the ER diagram become primary keys in the corresponding tables. A primary key is a column or a combination of columns that uniquely identifies a row in a table.
  - Convert all the relationships in the diagram to foreign keys or new tables. All the relationships represented in the diamond shape in the ER diagram can be mapped to foreign keys or new tables depending on the cardinality and participation of the entities involved. A foreign key is a column or a combination of columns that references a primary key in another table. A new table is created when a relationship has attributes or when it is a many-to-many relationship.

- The following are some examples of converting different types of relationships in the ER diagram to tables  :

  - One-to-one relationship: A one-to-one relationship is a relationship between two entities where each entity can be related to at most one instance of the other entity. For example, a person can have at most one passport and a passport can belong to at most one person. To convert a one-to-one relationship to tables, we can choose one of the entities and add the primary key of the other entity as a foreign key in its table. Alternatively, we can create a new table for the relationship and include the primary keys of both entities as foreign keys in the new table. For example, the ER diagram below shows a one-to-one relationship between PERSON and PASSPORT entities.

    ![One-to-one relationship](https://www.w3cschoool.com/images/one-to-one-relationship.png)

    To convert this ER diagram to tables, we can choose the PERSON entity and add the PASSPORT_NO attribute as a foreign key in its table. Alternatively, we can create a new table for the relationship and include the PERSON_ID and PASSPORT_NO attributes as foreign keys in the new table. The tables are shown below.

    | PERSON_ID | NAME | AGE | PASSPORT_NO |
    |-----------|------|-----|-------------|
    | 101       | Alice| 25  | P123        |
    | 102       | Bob  | 30  | P456        |
    | 103       | Carol| 28  | P789        |

    | PASSPORT_NO | ISSUE_DATE | EXPIRY_DATE |
    |-------------|------------|-------------|
    | P123        | 01-01-2020 | 31-12-2025  |
    | P456        | 15-02-2020 | 14-02-2026  |
    | P789        | 10-03-2020 | 09-03-2026  |

    | PERSON_PASSPORT | PERSON_ID | PASSPORT_NO |
    |-----------------|-----------|-------------|
    | 1               | 101       | P123        |
    | 2               | 102       | P456        |
    | 3               | 103       | P789        |

  - One-to-many relationship: A one-to-many relationship is a relationship between two entities where one entity can be related to many instances of the other entity, but the other entity can be related to at most one instance of the first entity. For example, a department can have many employees, but an employee can belong to at most one department. To convert a one-to-many relationship to tables, we can choose the entity on the many side and add the primary key of the entity on the one side as a foreign key in its table. For example, the ER diagram below shows a one-to-many relationship between DEPARTMENT and EMPLOYEE entities.

    ![One-to-many relationship](