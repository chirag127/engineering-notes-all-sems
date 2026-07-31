Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of Update and Delete Operations for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System.

### Update and Delete Operations

- Update and delete operations are used to modify or remove existing data from a relational database.
- Update operations can change the values of one or more attributes in one or more tuples of a relation, based on a specified condition.
- Delete operations can remove one or more tuples from a relation, based on a specified condition.
- Both update and delete operations can affect the integrity and consistency of the database, so they must be performed carefully and with proper authorization.
- Update and delete operations can be expressed using the relational algebra operators of assignment, selection, projection, and difference.

#### Update Operation

- An update operation can be written as:

  R := R - {t} + {t'}

  where R is a relation, t is a tuple in R that satisfies a condition C, and t' is a modified version of t with some attribute values changed.

- Alternatively, an update operation can be written as:

  R := π<sub>A</sub>(R) ∪ (π<sub>B</sub>(R) - π<sub>B</sub>(σ<sub>C</sub>(R)) ∪ {t'})

  where A and B are disjoint sets of attributes of R, such that A ∪ B = R, and t' is a tuple with the same values as t for the attributes in A, and new values for the attributes in B.

- For example, to update the salary of an employee with ID 1234 to 5000 in the relation EMPLOYEE, we can write:

  EMPLOYEE := EMPLOYEE - {<1234, John, Smith, 4000>} + {<1234, John, Smith, 5000>}

  or

  EMPLOYEE := π<sub>ID, FName, LName</sub>(EMPLOYEE) ∪ (π<sub>Salary</sub>(EMPLOYEE) - π<sub>Salary</sub>(σ<sub>ID=1234</sub>(EMPLOYEE)) ∪ {<5000>})

#### Delete Operation

- A delete operation can be written as:

  R := R - σ<sub>C</sub>(R)

  where R is a relation and C is a condition that selects the tuples to be deleted from R.

- For example, to delete all the employees with salary less than 3000 from the relation EMPLOYEE, we can write:

  EMPLOYEE := EMPLOYEE - σ<sub>Salary<3000</sub>(EMPLOYEE)