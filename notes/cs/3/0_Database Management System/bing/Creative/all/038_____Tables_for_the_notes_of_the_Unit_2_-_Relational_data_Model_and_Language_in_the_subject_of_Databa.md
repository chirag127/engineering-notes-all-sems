Hello, I am Sydney, your AI assistant. I can help you with your study material for the Unit 2 - Relational data Model and Language in the subject of Database Management System. Here are some tables that you can use for your notes:

### Tables for the notes of the Unit 2 - Relational data Model and Language

- A **relation** is a set of tuples that have the same attributes. A tuple is a single data item in a relation. An attribute is a column of a relation. A relation can be represented as a table with rows and columns.

- A **relational schema** is a set of relation schemas, where each relation schema defines the name, attributes, and constraints of a relation. A relation schema can be written as R(A1, A2, ..., An), where R is the name of the relation and A1, A2, ..., An are the attributes.

- A **relational database** is a collection of relations that conform to a relational schema. A relational database can be represented as a set of tables, where each table corresponds to a relation in the relational schema.

- A **relational algebra** is a set of operations that can be applied to relations or sets of relations to produce new relations. The basic operations of relational algebra are:

  - **Selection** (σ): selects a subset of tuples from a relation that satisfy a given condition. For example, σ<sub>age > 20</sub>(Student) selects the tuples from the Student relation where the age attribute is greater than 20.

  - **Projection** (π): selects a subset of attributes from a relation and eliminates duplicates. For example, π<sub>name, course</sub>(Student) selects the name and course attributes from the Student relation and removes any duplicate tuples.

  - **Union** (∪): combines two relations that have the same set of attributes and eliminates duplicates. For example, Student ∪ Teacher combines the Student and Teacher relations and removes any duplicate tuples.

  - **Intersection** (∩): selects the common tuples from two relations that have the same set of attributes. For example, Student ∩ Teacher selects the tuples that are both in the Student and Teacher relations.

  - **Difference** (-): selects the tuples from the first relation that are not in the second relation, where both relations have the same set of attributes. For example, Student - Teacher selects the tuples that are in the Student relation but not in the Teacher relation.

  - **Cartesian product** (×): combines every tuple from the first relation with every tuple from the second relation, where the two relations can have different sets of attributes. For example, Student × Course combines every tuple from the Student relation with every tuple from the Course relation.

  - **Join** (⋈): combines two relations based on a common attribute or a join condition. For example, Student ⋈<sub>Student.course = Course.id</sub> Course combines the Student and Course relations based on the condition that the course attribute of the Student relation matches the id attribute of the Course relation.

  - **Division** (÷): selects the tuples from the first relation that are associated with every tuple from the second relation, where the second relation is a subset of the first relation. For example, Student ÷ Course selects the tuples from the Student relation that are enrolled in every course in the Course relation.

- A **relational calculus** is a set of expressions that can be used to specify queries on a relational database. The expressions are based on logic and quantifiers. There are two types of relational calculus:

  - **Tuple relational calculus** (TRC): uses variables that range over tuples of a relation. For example, {T.name | Student(T) ∧ T.age > 20} is a TRC expression that returns the names of the students whose age is greater than 20.

  - **Domain relational calculus** (DRC): uses variables that range over domains of attributes. For example, {<x, y> | ∃z(Student(<x, y, z>) ∧ z > 20)} is a DRC expression that returns the pairs of name and course of the students whose age is greater than 20.