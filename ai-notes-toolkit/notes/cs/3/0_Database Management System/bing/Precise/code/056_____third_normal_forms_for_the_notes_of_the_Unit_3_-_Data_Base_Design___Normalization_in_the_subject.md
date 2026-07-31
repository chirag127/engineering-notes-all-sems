### Third Normal Form (3NF)
Third normal form (3NF) is a database schema design approach for relational databases which uses normalization rules to reduce data redundancy and prevent certain types of inconsistencies that can occur in the data.

A relation is in third normal form if it satisfies the following conditions:
1. It is in second normal form (2NF).
2. There are no transitive functional dependencies between non-prime attributes.

A transitive functional dependency occurs when a non-prime attribute is dependent on another non-prime attribute, which is in turn dependent on the primary key. In other words, if attribute A determines attribute B, and attribute B determines attribute C, then attribute C is transitively dependent on attribute A.

To convert a relation into third normal form, we need to identify any transitive dependencies and remove them by splitting the relation into two or more relations. This process is known as decomposition.

An example of a relation that is not in third normal form is as follows:

| Student ID | Student Name | Course ID | Course Name | Instructor ID | Instructor Name |
|------------|--------------|-----------|-------------|---------------|-----------------|
| 1          | Alice        | 101       | Math        | 1001          | Bob             |
| 2          | Bob          | 102       | English     | 1002          | Charlie         |
| 3          | Charlie      | 103       | Science     | 1003          | Dave            |

In this relation, the primary key is `Student ID`. The non-prime attributes are `Student Name`, `Course ID`, `Course Name`, `Instructor ID`, and `Instructor Name`. There is a transitive dependency between `Course Name` and `Instructor Name`, as `Course Name` is dependent on `Course ID`, which is in turn dependent on `Instructor ID`.

To convert this relation into third normal form, we can decompose it into two relations as follows:

| Student ID | Student Name | Course ID |
|------------|--------------|-----------|
| 1          | Alice        | 101       |
| 2          | Bob          | 102       |
| 3          | Charlie      | 103       |

| Course ID | Course Name | Instructor ID | Instructor Name |
|-----------|-------------|---------------|-----------------|
| 101       | Math        | 1001          | Bob             |
| 102       | English     | 1002          | Charlie         |
| 103       | Science     | 1003          | Dave            |

Now, both relations are in third normal form, as there are no transitive dependencies between non-prime attributes. This design reduces data redundancy and prevents certain types of inconsistencies that can occur in the data.