### Displaying data from multiple tables

- To display data from multiple tables, you need to use **join** operations that link the tables based on common columns or conditions.
- There are different types of joins, such as **inner join**, **outer join**, **cross join**, and **self join**. Each type of join has a different syntax and result set.
- An **inner join** returns only the rows that match the join condition in both tables. For example, to display the details of employees and their departments, you can use an inner join as follows:

```sql
SELECT e.ename, e.sal, d.dname, d.loc
FROM emp e INNER JOIN dept d
ON e.deptno = d.deptno;
```

- An **outer join** returns all the rows that match the join condition, as well as the unmatched rows from one or both tables. There are three types of outer joins: **left outer join**, **right outer join**, and **full outer join**. For example, to display the details of employees and their managers, you can use a left outer join as follows:

```sql
SELECT e.ename, e.sal, m.ename AS manager
FROM emp e LEFT OUTER JOIN emp m
ON e.mgr = m.empno;
```

- A **cross join** returns the Cartesian product of the rows from both tables, meaning every row from one table is paired with every row from the other table. For example, to display the combinations of employees and departments, you can use a cross join as follows:

```sql
SELECT e.ename, d.dname
FROM emp e CROSS JOIN dept d;
```

- A **self join** is a special type of join that involves joining a table to itself. This is useful when you want to compare or relate rows within the same table. For example, to display the details of employees and their subordinates, you can use a self join as follows:

```sql
SELECT e.ename, e.sal, s.ename AS subordinate
FROM emp e JOIN emp s
ON e.empno = s.mgr;
```

- To display data from multiple tables, you also need to use the **SELECT** statement with the appropriate column names, table names, and aliases. You can also use the **WHERE**, **GROUP BY**, **HAVING**, **ORDER BY**, and **LIMIT** clauses to filter, aggregate, sort, and limit the result set. For example, to display the details of employees who work in the sales department and earn more than 3000, you can use the following statement:

```sql
SELECT e.ename, e.sal, d.dname
FROM emp e JOIN dept d
ON e.deptno = d.deptno
WHERE d.dname = 'SALES'
AND e.sal > 3000
ORDER BY e.sal DESC;
```

- To display data from multiple tables, you can also use **subqueries**, which are queries nested within another query. Subqueries can be used in the **SELECT**, **FROM**, or **WHERE** clauses of the main query. For example, to display the details of employees who earn more than the average salary of their department, you can use a subquery as follows:

```sql
SELECT e.ename, e.sal, d.dname
FROM emp e JOIN dept d
ON e.deptno = d.deptno
WHERE e.sal > (SELECT AVG(sal) FROM emp WHERE deptno = e.deptno);
```

- To display data from multiple tables, you need to use a database management system (DBMS) that supports SQL, such as Oracle or MySQL. You also need to create and populate the tables with the appropriate data types, constraints, and values. You can use the **CREATE TABLE** and **INSERT INTO** statements to do this. For example, to create and populate the emp and dept tables, you can use the following statements:

```sql
CREATE TABLE emp (
  empno INT PRIMARY KEY,
  ename VARCHAR(20),
  job VARCHAR(20),
  mgr INT,
  hiredate DATE,
  sal DECIMAL(10,2),
  comm DECIMAL(10,2),
  deptno INT REFERENCES dept(deptno)
);

INSERT INTO emp VALUES
(7369, 'SMITH', 'CLERK', 7902, '1980-12-17', 800, NULL, 20),
(7499, 'ALLEN', 'SALESMAN', 7698, '1981-02-20', 1600,

```
