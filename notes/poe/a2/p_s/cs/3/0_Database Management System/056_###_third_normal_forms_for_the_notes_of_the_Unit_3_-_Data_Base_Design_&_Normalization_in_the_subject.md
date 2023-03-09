 Here is the content in markdown format for the topic ### third normal forms for the notes of the Unit 3 - Data Base Design & Normalization in the subject of Database Management System:

## Third Normal Form (3NF)

- A relation is in third normal form if it is in second normal form and no non-prime attribute is dependent on other non-prime attributes.
- That is, every non-prime attribute must depend on the whole primary key.
- Violation of 3NF occurs when a non-prime attribute depends on another non-prime attribute instead of depending on the primary key.
- For example, consider a relation with attributes ( stud_id, stud_name, dept_name, building ). Here, the attribute "building" depends on "dept_name" instead of depending on the primary key "stud_id". Therefore, this relation is not in 3NF.
- To convert this relation to 3NF, we decompose it into two relations:
( stud_id, stud_name, dept_name )
( dept_name, building )

Advantages of 3NF:
- Removes all transitive dependencies.
- Prevents unwanted data redundancy.
- Increases data consistency.
- Makes the relational design more simple.

Applications of 3NF:
- Useful in database design for relational data models to achieve greater data integrity.
- Helps in maintaining the databases by removing modification, insertion and deletion anomalies.
- Provides a foundation for more advanced normal forms like Boyce-Codd Normal Form (BCNF) and Fourth Normal Form (4NF).

[You can include diagrams, examples, codes or other details here if required to help understand 3NF better.]