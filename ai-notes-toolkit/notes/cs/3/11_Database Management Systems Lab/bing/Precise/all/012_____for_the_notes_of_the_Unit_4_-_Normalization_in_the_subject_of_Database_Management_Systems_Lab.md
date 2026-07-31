### Unit 4 - Normalization in Database Management Systems Lab

Normalization is the process of organizing data in a database. This includes creating tables and establishing relationships between those tables according to rules designed to protect the data and make the database more flexible by eliminating redundancy and inconsistent dependency.

- **Redundant data** wastes disk space and creates maintenance problems. If data that exists in more than one place must be changed, the data must be changed in exactly the same way in all locations.
- A **customer address change** is much easier to implement if that data is stored only in the Customers table and nowhere else in the database.
- There are a few rules for database normalization. Each rule is called a "normal form." If the first rule is observed, the database is said to be in "first normal form." If the first three rules are observed, the database is considered to be in "third normal form." Although other levels of normalization are possible, third normal form is considered the highest level necessary for most applications.

The normal forms are:

1. **First Normal Form (1NF):** Each field in a table contains different information. For example, in an employee list, each table would contain only one birthdate field.
2. **Second Normal Form (2NF):** Each field in a table that is not a determiner of the contents of another field must itself be a function of the other fields in the table.
3. **Third Normal Form (3NF):** No duplicate information is permitted. So, for example, if two tables both require a birthdate field, the birthdate information would be separated into a separate table, and the two other tables would then access the birthdate information via an index field in the birthdate table. Any change to a birthdate would automatically be reflected in all tables that link to the birthdate table.

There are additional normalization levels, such as **Boyce-Codd Normal Form (BCNF), Fourth Normal Form (4NF), and Fifth Normal Form (5NF)**, also known as **Project-Join Normal Form (PJNF)**. However, Third Normal Form is usually sufficient for most practical purposes.

Normalization is an important part of database design. A well-normalized database is more flexible to changes and has a simpler structure than a non-normalized database. It is also easier to use and maintain. However, normalization should not be the only consideration when designing a database. Performance and ease of use are also important factors to consider.