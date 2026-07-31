### Update and Delete Operations for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- Update and delete operations are used to modify or remove existing data from a relational database.
- Update operations can change the values of one or more attributes in one or more tuples of a relation, based on a specified condition.
- Delete operations can remove one or more tuples from a relation, based on a specified condition.
- Both update and delete operations can affect the integrity and consistency of the database, so they must be performed carefully and with proper authorization.
- Update and delete operations can be expressed using the relational algebra operators of assignment, selection, projection, and set difference.
- For example, to update the salary of all employees in the EMPLOYEE relation who work in department 5 to 5000, we can write:

  EMPLOYEE := EMPLOYEE - (EMPLOYEE ⋈ DEPT_NO = 5) ∪ (π<EMP_NO, ENAME, JOB, MGR, HIRE_DATE, 5000, COMM, DEPT_NO>(EMPLOYEE ⋈ DEPT_NO = 5))

- To delete all employees in the EMPLOYEE relation who work in department 5, we can write:

  EMPLOYEE := EMPLOYEE - (EMPLOYEE ⋈ DEPT_NO = 5)

- Update and delete operations can also be expressed using the SQL language, which is a widely used standard for relational database manipulation.
- SQL provides the UPDATE and DELETE statements for performing update and delete operations, respectively.
- For example, to update the salary of all employees in the EMPLOYEE table who work in department 5 to 5000, we can write:

  UPDATE EMPLOYEE
  SET SALARY = 5000
  WHERE DEPT_NO = 5;

- To delete all employees in the EMPLOYEE table who work in department 5, we can write:

  DELETE FROM EMPLOYEE
  WHERE DEPT_NO = 5;

- SQL also provides the WHERE clause for specifying the condition for selecting the tuples to be updated or deleted.
- The condition can be a logical expression involving the attributes of the table, constants, comparison operators, logical operators, and parentheses.
- For example, to update the salary of all employees in the EMPLOYEE table who have a salary less than 3000 or more than 7000, we can write:

  UPDATE EMPLOYEE
  SET SALARY = SALARY * 1.1
  WHERE SALARY < 3000 OR SALARY > 7000;

- To delete all employees in the EMPLOYEE table who have a job title of 'CLERK' or 'SALESMAN', we can write:

  DELETE FROM EMPLOYEE
  WHERE JOB IN ('CLERK', 'SALESMAN');

- SQL also provides the SET clause for specifying the new values for the attributes to be updated.
- The new values can be constants, expressions involving the attributes of the table, or subqueries that return a single value.
- For example, to update the salary of all employees in the EMPLOYEE table to be equal to the average salary of their department, we can write:

  UPDATE EMPLOYEE
  SET SALARY = (SELECT AVG(SALARY) FROM EMPLOYEE E2 WHERE E2.DEPT_NO = EMPLOYEE.DEPT_NO);

- To delete all employees in the EMPLOYEE table who have a salary higher than the average salary of their department, we can write:

  DELETE FROM EMPLOYEE
  WHERE SALARY > (SELECT AVG(SALARY) FROM EMPLOYEE E2 WHERE E2.DEPT_NO = EMPLOYEE.DEPT_NO);