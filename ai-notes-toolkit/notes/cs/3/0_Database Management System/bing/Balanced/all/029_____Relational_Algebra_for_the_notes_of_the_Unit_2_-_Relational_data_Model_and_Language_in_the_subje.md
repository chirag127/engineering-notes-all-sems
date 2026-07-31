# Relational Algebra

Relational algebra is a theory that uses algebraic structures for modeling data, and defining queries on it with a well founded semantics. The main application of relational algebra is to provide a theoretical foundation for relational databases, particularly query languages for such databases, chief among which is SQL.

Relational algebra is considered as a procedural query language, where the user tells the system to carry out a set of operations to obtain the desired results. Relational algebra operations are designed to do the most common things that we need to do with relations in a database.

Some of the basic relational algebra operations are:

- **SELECT** (σ): The SELECT operation is used for selecting a subset of the tuples according to a given selection condition . For example, σ<sub>age > 20</sub>(Student) selects all the tuples from the Student relation where the age attribute is greater than 20.
- **PROJECT** (π): The PROJECT operation is used for selecting a subset of the attributes of a relation . For example, π<sub>name, course</sub>(Student) selects only the name and course attributes from the Student relation.
- **UNION** (∪): The UNION operation is used for combining two relations that have the same set of attributes . For example, Student ∪ Teacher returns a relation that contains all the tuples from both Student and Teacher relations.
- **INTERSECTION** (∩): The INTERSECTION operation is used for selecting the common tuples from two relations that have the same set of attributes . For example, Student ∩ Teacher returns a relation that contains only the tuples that are present in both Student and Teacher relations.
- **DIFFERENCE** (-): The DIFFERENCE operation is used for selecting the tuples that are present in one relation but not in another relation that have the same set of attributes . For example, Student - Teacher returns a relation that contains only the tuples that are present in Student relation but not in Teacher relation.
- **CARTESIAN PRODUCT** (×): The CARTESIAN PRODUCT operation is used for combining every tuple of one relation with every tuple of another relation . For example, Student × Course returns a relation that contains all the possible combinations of tuples from Student and Course relations.
- **JOIN** (⋈): The JOIN operation is used for combining two relations based on a common attribute or a join condition . For example, Student ⋈<sub>Student.course = Course.id</sub> Course returns a relation that contains the tuples from Student and Course relations that have the same value for the course and id attributes, respectively.
- **DIVISION** (÷): The DIVISION operation is used for selecting the tuples from one relation that are associated with all the tuples of another relation . For example, Student ÷ Course returns a relation that contains the tuples from Student relation that have taken all the courses in the Course relation.

There are also some additional relational algebra operations that can be derived from the basic ones, such as:

- **RENAME** (ρ): The RENAME operation is used for changing the name of a relation or an attribute . For example, ρ<sub>Enrolled(name, course)</sub>(Student) changes the name of the Student relation to Enrolled, and the attributes to name and course.
- **SET DIFFERENCE** (∖): The SET DIFFERENCE operation is used for selecting the tuples that are present in one relation but not in another relation that have the same set of attributes . It is equivalent to the DIFFERENCE operation. For example, Student ∖ Teacher is the same as Student - Teacher.
- **NATURAL JOIN** (⋈): The NATURAL JOIN operation is used for combining two relations based on the common attributes . It is equivalent to the JOIN operation with an implicit join condition. For example, Student ⋈ Course is the same as Student ⋈<sub>Student.course = Course.id</sub> Course.
- **SEMI-JOIN** (⋉): The SEMI-JOIN operation is used for selecting the tuples from one relation that have a matching tuple in another relation [^3^