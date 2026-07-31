### Relational Data Model and Language

- Relational Data Model and Language is a way of organizing and manipulating data in a relational database using tables and SQL commands.
- A relational database is a collection of relations (tables) that store data in rows (tuples) and columns (attributes).
- A relation has a name and a set of attributes. Each attribute has a name and a domain (a set of possible values).
- A tuple is a row of a relation that represents an entity or a relationship. Each tuple has a value for each attribute of the relation.
- A key is a set of one or more attributes that uniquely identifies a tuple in a relation. A primary key is a key that is chosen to be the main identifier of a relation. A foreign key is a key that references a primary key of another relation.
- A relational schema is a set of relation names and their attributes. A relational database schema is a set of relational schemas that defines the structure of a relational database.
- A relational algebra is a set of operations that can be applied to relations or sets of relations to produce new relations. The basic operations are selection, projection, union, set difference, Cartesian product, and rename. The derived operations are join, intersection, division, and assignment.
- A relational calculus is a declarative language that can be used to specify queries on relations. The basic form of a relational calculus expression is {t | P(t)}, where t is a tuple variable and P(t) is a predicate that defines the conditions for selecting tuples. There are two types of relational calculus: tuple relational calculus and domain relational calculus.
- SQL (Structured Query Language) is a standard language for defining, manipulating, and querying data in a relational database. SQL has three main components: data definition language (DDL), data manipulation language (DML), and data query language (DQL).
- DDL is used to create, modify, and delete database objects such as tables, views, indexes, and constraints.
- DML is used to insert, update, and delete data in tables.
- DQL is used to retrieve data from tables using SELECT, FROM, WHERE, GROUP BY, HAVING, and ORDER BY clauses. SQL also supports various functions, operators, and clauses for performing calculations, aggregations, joins, subqueries, and other operations on data.