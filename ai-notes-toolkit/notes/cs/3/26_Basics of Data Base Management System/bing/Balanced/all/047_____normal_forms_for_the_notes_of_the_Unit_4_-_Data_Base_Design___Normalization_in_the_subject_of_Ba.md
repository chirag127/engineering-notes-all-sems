# Normal Forms for the Notes of the Unit 4 - Data Base Design & Normalization in the Subject of Basics of Data Base Management System

- Normal forms are a set of rules or guidelines for designing relational databases in a way that reduces data redundancy and improves data integrity  .
- Normal forms are based on the concept of functional dependency, which is a relationship between two sets of attributes in a relation such that the values of one set determine the values of the other set .
- There are several normal forms, each with a higher degree of normalization than the previous one. The most common normal forms are: first normal form (1NF), second normal form (2NF), third normal form (3NF), and Boyce-Codd normal form (BCNF)   .
- A relation is said to be in a certain normal form if it satisfies the conditions or requirements of that normal form. A relation can be converted from a lower normal form to a higher normal form by applying certain normalization techniques  .
- The main benefits of normalization are: avoiding data anomalies, such as insertion, deletion, and update anomalies; ensuring data consistency and accuracy; and facilitating efficient data retrieval and manipulation  .
- The main drawbacks of normalization are: increased complexity and overhead of database design and maintenance; possible loss of performance due to more joins and queries; and possible loss of information due to decomposition of relations .

## First Normal Form (1NF)

- A relation is in 1NF if it does not contain any composite or multi-valued attributes, i.e., each attribute has a single atomic value .
- To convert a relation to 1NF, we need to remove any composite or multi-valued attributes and create separate relations for them, with appropriate foreign keys to link them to the original relation .
- For example, consider the following relation that contains a composite attribute (Address) and a multi-valued attribute (Phone):

| Student_ID | Name | Address | Phone |
| --- | --- | --- | --- |
| 101 | Alice | 123 Main St, Seattle, WA | 555-1111, 555-2222 |
| 102 | Bob | 456 Elm St, Portland, OR | 555-3333 |
| 103 | Carol | 789 Pine St, San Francisco, CA | 555-4444, 555-5555 |

- To convert this relation to 1NF, we need to split the Address attribute into its components (Street, City, State) and create a separate relation for Phone, with Student_ID as a foreign key:

| Student_ID | Name | Street | City | State |
| --- | --- | --- | --- | --- |
| 101 | Alice | 123 Main St | Seattle | WA |
| 102 | Bob | 456 Elm St | Portland | OR |
| 103 | Carol | 789 Pine St | San Francisco | CA |

| Student_ID | Phone |
| --- | --- |
| 101 | 555-1111 |
| 101 | 555-2222 |
| 102 | 555-3333 |
| 103 | 555-4444 |
| 103 | 555-5555 |

## Second Normal Form (2NF)

- A relation is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key, i.e., there is no partial dependency .
- To convert a relation to 2NF, we need to identify any partial dependencies and remove them by creating separate relations for them, with appropriate foreign keys to link them to the original relation .
- For example, consider the following relation that contains a composite primary key (Student_ID, Course_ID) and a partial dependency (Course_Name -> Course_Credit):

| Student_ID | Course_ID | Course_Name | Course_Credit | Grade |
| --- | --- | --- | --- | --- |
| 101 | CS101 | Introduction to Computer Science | 3 | A |
| 101 | CS102 | Data Structures and Algorithms | 4 | B |
| 102 | CS101 | Introduction to Computer Science | 3 |