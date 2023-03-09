 Here is the content in markdown format for the topic ### normal forms for the notes of the Unit 4 - Data Base Design & Normalization in the subject of Basics of Data Base Management System:

## Normal Forms
Normal forms are used to eliminate redundancy and ensure data integrity in a database. There are mainly three normal forms:

1. First Normal Form (1NF):
- The basic requirement is that the domain of an attribute must include only atomic values.
- Each attribute must contain a single value only.
- The table must have a primary key.

For example, consider a table with an attribute "Address" which holds values like "XYZ, ABC street, New Delhi". This violates 1NF as "Address" attribute contains multiple values. This can be corrected by splitting it into 3 attributes - "Street", "City" and "State".

2. Second Normal Form (2NF):
- Must be in 1NF.
- No partial dependency: No non-prime attribute should depend on a part of a candidate key.

For example, consider an employee table with attributes EmpID (PK), EmpName, DeptName, and City. This violates 2NF as "City" depends on "DeptName" which is part of the primary key (EmpID). This can be corrected by splitting it into two tables - one with EmpID & EmpName and other with DeptID, DeptName, and City.

3. Third Normal Form (3NF):
- Must be in 2NF.
- No transitive dependency: No non-prime attribute should depend on other non-prime attributes.

For example, consider an employee table with attributes EmpID, EmpName, DeptID (FK), and ManagerID (FK). This violates 3NF as "ManagerID" (non-prime attribute) depends on "DeptID" (another non-prime attribute). This can be corrected by splitting it into two tables - one with EmpID, EmpName, and DeptID; and other with DeptID and ManagerID.

Advantages:
- Minimizes data redundancy.
- Prevents data inconsistency.
- Increases database efficiency.

Examples and applications can also be included in the notes. Markdown tables, codes, etc can be added if necessary to illustrate the concepts. The notes can be made more formal by using complete sentences and a formal tone.