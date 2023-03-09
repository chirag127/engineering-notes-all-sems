 Here are the notes for Unit 4 - Data Base Design & Normalization in the subject of Basics of Data Base Management System:

### Data Base Design

- Database design is the process of producing a detailed data model of a database. This logical data model contains all the needed logical and physical design choices and physical storage parameters needed to generate a design in a Data Definition Language, which can then be used to create a database.
- The design of a database involves classifying data and identifying relationships between the data groups. The goals of database design are to make the database:
- Organized - Data is logically structured.
- Accessible - Data can be retrieved efficiently.
- Secure - Data is protected from unauthorized access.
- Robust - Data is consistent and accurate.
- The steps in database design are:

1. Analyze the purpose and structure of the database.
2. Determine the data to be stored in the database.
3. Identify relationships between data and group data into tables.
4. Choose appropriate data types for table columns.
5. Identify primary keys and foreign keys and ensure that referential integrity is maintained.
6. Normalize the table structure to minimize data redundancy.
7. Define views to provide different perspectives of the data.
8. Refine the design and create the physical database.

### Database Normalization

- Database normalization is the process of organizing data into tables in a database. The main goals of the normalization process are:
- Minimizing duplicate data
- Minimizing or avoiding data modification issues
- Simplifying queries

- There are three common forms of database normalization:

1. First normal form - The information is stored in a two-dimensional table with no repeating groups.
2. Second normal form - The table is in first normal form and all non-key columns depend on the primary key.
3. Third normal form - The table is in second normal form and all non-key columns must depend on the primary key and not on other non-key columns.

[Include detailed examples and diagrams if required]