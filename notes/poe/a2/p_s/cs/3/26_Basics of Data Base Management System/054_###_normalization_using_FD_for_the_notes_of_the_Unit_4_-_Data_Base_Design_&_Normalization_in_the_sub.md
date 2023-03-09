 Here is the content in markdown format for the topic -

### Normalization using Functional Dependencies (FDs)

- Functional Dependency (FD): A functional dependency is a constraint between two attributes (or sets of attributes) of a relation. It specifies that one attribute (or set of attributes) functionally determines the other attribute.

For example:
- In a `Student` relation, ` RollNo → Name` indicates that roll number functionally determines the name of a student. Here, `RollNo` is called the determinant attribute and `Name` is called the dependent attribute.
- In a `Employee` relation, ` EmpID → Salary` indicates that employee ID functionally determines the salary of an employee.

- Normalization using FDs: The process of organizing data into tables to remove redundancy and undesirable characteristics like data duplication, etc. is known as normalization. The main steps are:

1. Remove Repeating Groups: The first step is to identify and remove repeating groups of attributes.
2. Removing partial dependency: After step 1, check if remaining attributes are partially dependent on each other. If yes, break into further tables. This is done to remove undesirable effects of data updation anomalies.
3. Check FDs and BCNF: Finally, check if the relations that resulted from step 2 satisfy the constraints of First Normal Form (1NF), Second Normal Form (2NF) and Boyce-Codd Normal Form (BCNF). If any violation occurs, further normalization steps are applied.

The detailed steps and examples can be found in any database textbook or course material. The main aim is to break complex relations into simpler ones and remove data redundancy to ensure data integrity, consistency, and avoid anomalies. Normalization has its pros and cons and may not always be feasible or result in best performance. The final normalized database design depends on the requirements and usage of the database.