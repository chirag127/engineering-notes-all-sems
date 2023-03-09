 Here is the content in markdown format for the given topic:

### Functional Dependencies for the notes of the Unit 4 - Data Base Design & Normalization

1. Functional Dependency: It is a relationship between two attributes (columns) of a relation (table). It states that the value of an attribute X depends on the value of attribute Y. It is denoted as X -> Y which is read as X determines Y.

2. Example: Consider a relation Students(RollNo, Name, Class). Here RollNo -> Name which means that RollNo determines Name. Similarly RollNo -> Class which means that RollNo determines Class.

3. Key Constraints: A functional dependency X -> Y holds in a relation R if removal of any attribute A from X results in a loss of the dependency. Attribute X is called the Determinant Set and Y is called the Dependent Attribute.

4. Trivial Functional Dependency: A functional dependency of the form R -> R is called a Trivial Functional Dependency. This dependency always holds in any relation. These dependencies are ignored while designing databases.

5. Nontrivial Functional Dependency: Any functional dependency other than a Trivial Functional Dependency is called a Nontrivial Functional Dependency. These dependencies are considered while designing databases.

6. Closure of Attributes: The attributes(columns) which can be determined by a given set of attributes are called the Closure of attributes. The closure is denoted using a '+' sign. For a set of attributes X, the closure is denoted as X+.

7. Candidate Keys: A candidate key is a minimal set of attributes(columns) which can uniquely identify a tuple(row) in a relation. A relation can have multiple candidate keys. Primary key is selected from the candidate keys.

[Detailed explanations, examples and diagrams can be included here for better understanding]

[Markdown tables, codes and applications of the concept can be included for exam preparation]