 Here is the content in markdown format for the topic ### normal forms for the notes of the Unit 3 - Data Base Design & Normalization in the subject of Database Management System:

# Normal Forms

Normal forms are used to eliminate redundant data and ensure data dependencies make sense in a database table. They are used to normalize a database schema.

There are three main normal forms:

1. First Normal Form (1NF): Remove repeating groups, ensure each cell contains a single value
2. Second Normal Form (2NF): Meet 1NF, then remove subsets of data that depend on only part of a composite primary key
3. Third Normal Form (3NF): Meet 2NF, then remove columns that are dependent on other columns (not the primary key)

Additional normal forms (Boyce-Codd Normal Form, Fourth Normal Form, etc.) may also be used to handle more complex dependencies.

Following normal forms can bring many benefits to a database:

- Minimize duplicate data
- Reduce data update issues (inconsistency)
- Simplify queries
- Optimize storage space

However, there are some tradeoffs to keep in mind:

- Additional tables and relationships can make a schema more complex
- Denormalization may be needed for performance reasons
- Finding the "right" normalization level for an application involves balancing normalization benefits vs. complexity drawbacks

Examples of tables and transformations between normal forms can be used to demonstrate the normalization process. Practicing normalization on various schemas is helpful for learning the normal forms and seeing the impact on a database.

Overall, normal forms are an important concept in database design to build an efficient, robust, and flexible system. By following set guidelines for organizing data, many problems can be avoided and data integrity can be more easily maintained.