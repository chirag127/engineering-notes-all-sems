# Relational Algebra - Relational Calculus

Relational algebra and relational calculus are two formal query languages for relational databases. They are used to manipulate and retrieve data from a relational database.

## Relational Algebra

Relational algebra is a procedural query language, which means that it specifies a sequence of operations to be performed on the database in order to retrieve the desired result. The basic operations of relational algebra are:

1. **Selection**: This operation selects a subset of rows from a relation based on a given condition.
2. **Projection**: This operation selects a subset of columns from a relation.
3. **Union**: This operation combines two relations by taking the union of their rows.
4. **Difference**: This operation returns the rows that are in one relation but not in the other.
5. **Cartesian Product**: This operation combines two relations by taking the Cartesian product of their rows.
6. **Join**: This operation combines two relations by matching rows based on a given condition.

## Relational Calculus

Relational calculus is a non-procedural query language, which means that it specifies the desired result without specifying the sequence of operations to be performed on the database. There are two types of relational calculus:

1. **Tuple Relational Calculus**: This type of relational calculus uses variables to represent tuples and specifies the desired result in terms of these variables.
2. **Domain Relational Calculus**: This type of relational calculus uses variables to represent values from the domains of the attributes and specifies the desired result in terms of these variables.

Both types of relational calculus use logical expressions to specify the desired result. These expressions can include quantifiers, such as "for all" and "there exists", and logical connectives, such as "and", "or", and "not".

In summary, relational algebra and relational calculus are two formal query languages for relational databases. Relational algebra is a procedural query language, while relational calculus is a non-procedural query language. Both languages can be used to manipulate and retrieve data from a relational database.