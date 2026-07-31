### Merging Data from Multiple Tables

When working with databases, it is common to have data stored in multiple tables. In such cases, it becomes necessary to merge data from multiple tables in order to retrieve meaningful information. In this section, we will discuss various techniques for merging data from multiple tables using Enterprise Java Bean (EJB).

#### Inner Join

An Inner join is a technique used to combine rows from two or more tables based on a related column between them. In this type of join, only the matching rows from both tables are returned. The syntax for Inner join in EJB is as follows:

```java
@PersistenceContext(unitName="YourUnit")
EntityManager em;

Query query = em.createQuery("SELECT e FROM Employee e INNER JOIN e.department d");
List<Employee> employees = query.getResultList();
```

#### Outer Join

An Outer join is a technique used to combine rows from two or more tables even if there is no matching row in one of the tables. In this type of join, all the rows from one table are returned along with matching rows from other tables or null values where there are no matches. The syntax for Outer join in EJB is as follows:

```java
@PersistenceContext(unitName="YourUnit")
EntityManager em;

Query query = em.createQuery("SELECT e FROM Employee e LEFT OUTER JOIN e.department d");
List<Employee> employees = query.getResultList();
```

#### Cross Join

A Cross join is a technique used to combine every row from one table with every row from another table. In this type of join, the resulting table will have a number of rows equal to the number of rows in the first table multiplied by the number of rows in the second table. The syntax for Cross join in EJB is as follows:

```java
@PersistenceContext(unitName="YourUnit")
EntityManager em;

Query query = em.createQuery("SELECT e FROM Employee e, Department d");
List<Employee> employees = query.getResultList();
```

#### Union

A Union is a technique used to combine the results of two or more select statements into a single result set. In this type of operation, the resulting table will have all the rows from the first select statement followed by all the rows from the second select statement and so on. The syntax for Union in EJB is as follows:

```java
@PersistenceContext(unitName="YourUnit")
EntityManager em;

Query query = em.createQuery("SELECT e FROM Employee e WHERE e.salary > 10000 UNION SELECT e FROM Employee e WHERE e.salary < 5000");
List<Employee> employees = query.getResultList();
```

In conclusion, merging data from multiple tables is an important aspect of working with databases. In EJB, we can use various techniques like Inner join, Outer join, Cross join, and Union to combine data from multiple tables and retrieve meaningful information.