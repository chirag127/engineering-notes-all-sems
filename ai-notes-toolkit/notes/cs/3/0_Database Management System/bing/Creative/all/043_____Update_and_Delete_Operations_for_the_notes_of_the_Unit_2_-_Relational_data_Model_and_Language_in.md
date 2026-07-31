Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of update and delete operations for the notes of the unit 2 - relational data model and language in the subject of database management system.

# Update and Delete Operations

- Update and delete operations are used to modify or remove existing data from a relational database.
- Update operations can change the values of one or more attributes for a set of tuples that satisfy a given condition.
- Delete operations can remove one or more tuples that satisfy a given condition from a relation.
- Both update and delete operations can affect the integrity and consistency of the database, so they must be performed carefully and with proper authorization.

## Update Operation

- An update operation can be expressed in the form:

```
UPDATE relation_name
SET attribute_name = expression
WHERE condition;
```

- The relation_name specifies the name of the relation to be updated.
- The attribute_name specifies the name of the attribute whose value is to be changed.
- The expression specifies the new value for the attribute, which can be a constant, a variable, or a function of other attributes.
- The condition specifies the criteria for selecting the tuples to be updated.
- The update operation modifies the values of the attribute for all the tuples that satisfy the condition in the relation.
- If the condition is omitted, the update operation applies to all the tuples in the relation.

- For example, the following update operation changes the salary of all the employees in the EMPLOYEE relation who work in the department number 5 by 10%:

```
UPDATE EMPLOYEE
SET SALARY = SALARY * 1.1
WHERE DNO = 5;
```

## Delete Operation

- A delete operation can be expressed in the form:

```
DELETE FROM relation_name
WHERE condition;
```

- The relation_name specifies the name of the relation from which the tuples are to be deleted.
- The condition specifies the criteria for selecting the tuples to be deleted.
- The delete operation removes all the tuples that satisfy the condition from the relation.
- If the condition is omitted, the delete operation removes all the tuples from the relation.

- For example, the following delete operation removes all the employees in the EMPLOYEE relation who have a salary less than 30000:

```
DELETE FROM EMPLOYEE
WHERE SALARY < 30000;
```

## Integrity and Consistency Constraints

- Update and delete operations can violate the integrity and consistency constraints of the database, such as primary key, foreign key, domain, and semantic constraints.
- A primary key constraint requires that the value of the primary key attribute(s) of a relation must be unique and not null for each tuple.
- A foreign key constraint requires that the value of the foreign key attribute(s) of a relation must either match the value of the primary key attribute(s) of another relation, or be null.
- A domain constraint requires that the value of an attribute must belong to a predefined set of values, or a range of values, or a data type.
- A semantic constraint requires that the value of an attribute must satisfy some logical or business rules that are not enforced by the database system.

- For example, the following update operation violates the primary key constraint of the EMPLOYEE relation, as it tries to assign the same SSN value to two different tuples:

```
UPDATE EMPLOYEE
SET SSN = '123456789'
WHERE LNAME = 'Smith' OR LNAME = 'Jones';
```

- The following delete operation violates the foreign key constraint of the DEPARTMENT relation, as it tries to remove a tuple that is referenced by another tuple in the EMPLOYEE relation:

```
DELETE FROM DEPARTMENT
WHERE DNUMBER = 5;
```

- The following update operation violates the domain constraint of the SALARY attribute of the EMPLOYEE relation, as it tries to assign a negative value to it:

```
UPDATE EMPLOYEE
SET SALARY = -1000
WHERE SSN = '123456789';
```

- The following update operation violates the semantic constraint of the BDATE attribute of the EMPLOYEE relation, as it tries to assign a future date to it:

```
UPDATE EMPLOYEE
SET BDATE = '2023-01-01'
WHERE SSN = '123456789';
```

- To prevent the violation of integrity and consistency constraints, the database system must check the validity of the update and delete operations before executing them, and reject them if they are invalid.
- Alternatively, the database system can perform some corrective actions to restore the integrity and consistency of the database, such as cascading the update or delete operations to the related relations, or setting the values of the affected attributes to null.