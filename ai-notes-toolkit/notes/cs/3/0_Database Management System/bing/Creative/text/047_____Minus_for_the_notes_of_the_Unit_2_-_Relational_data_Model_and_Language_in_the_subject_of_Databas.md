### Relational Data Model and Language

- Relational Data Model and Language is a way of organizing and manipulating data in a relational database using tables and SQL .
- A relational database is a collection of relations (tables) that store data in rows (tuples) and columns (attributes)  .
- A relation has a name and a set of attributes. Each attribute has a name and a domain (a set of possible values) .
- A tuple is a row of a relation that represents an entity or a relationship. Each tuple has a value for each attribute of the relation .
- A key is a set of attributes that uniquely identifies a tuple in a relation. A primary key is a key that is chosen to be the main identifier of a relation. A foreign key is a key that references a primary key of another relation .
- A relational schema is a set of relation names and their attributes. A relational database schema is a set of relational schemas that defines the structure of a relational database .
- A relational instance is a set of tuples for each relation in a relational schema. A relational database instance is a set of relational instances that represents the state of a relational database at a given time .
- A relational algebra is a set of operations that can be applied to relations or sets of relations to produce new relations. Relational algebra operations include selection, projection, union, intersection, difference, product, join, division, and renaming .
- A relational calculus is a declarative language that can be used to express queries on relations. Relational calculus uses logical formulas to specify the conditions for selecting tuples from relations. There are two types of relational calculus: tuple relational calculus and domain relational calculus .
- SQL (Structured Query Language) is a widely used language for defining, manipulating, and querying data in relational databases. SQL has three main components: Data Definition Language (DDL), Data Manipulation Language (DML), and Data Query Language (DQL)  .
- DDL is used to create, alter, and drop relations and other database objects. DDL commands include CREATE, ALTER, and DROP .
- DML is used to insert, update, and delete data in relations. DML commands include INSERT, UPDATE, and DELETE .
- DQL is used to retrieve data from relations based on certain criteria. DQL commands include SELECT, FROM, WHERE, GROUP BY, HAVING, and ORDER BY .
- SQL also supports other features such as constraints, indexes, views, functions, triggers, transactions, and authorization .