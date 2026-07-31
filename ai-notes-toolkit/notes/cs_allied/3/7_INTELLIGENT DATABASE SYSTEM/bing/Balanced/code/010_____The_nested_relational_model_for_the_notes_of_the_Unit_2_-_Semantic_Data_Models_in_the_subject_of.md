### The nested relational model

- The nested relational model is an extension of the relational model in which domains may be either atomic or relation-valued .
- This allows a complex object to be represented by a single tuple of a nested relation, which has a one-to-one correspondence between data items and objects.
- A nested relation can be seen as a relation of relations, where each tuple may contain one or more sub-relations as attribute values.
- A nested relation schema can be defined recursively as follows:

  - A nested relation schema R is a set of attributes A1, A2, ..., An, where each attribute Ai has a name and a type.
  - The type of an attribute Ai can be either atomic or a nested relation schema Ri.
  - A nested relation schema R can be denoted as R(A1, A2, ..., An), where each Ai is either an atomic attribute or a nested relation schema Ri.

- A nested relation instance can be defined recursively as follows:

  - A nested relation instance r of a nested relation schema R is a set of tuples t, where each tuple t is an ordered list of values v1, v2, ..., vn, corresponding to the attributes A1, A2, ..., An of R.
  - The value of an attribute Ai in a tuple t can be either atomic or a nested relation instance ri of a nested relation schema Ri.
  - A nested relation instance r can be denoted as r{t1, t2, ..., tm}, where each ti is either an atomic tuple or a nested relation tuple ti{v1, v2, ..., vn}.

- An example of a nested relation schema and instance is shown below:

  - Schema: Employee(Name, Address, Phone, Projects)
  - Type: Employee(atomic, atomic, atomic, Project)
  - Type: Project(PName, Budget, Tasks)
  - Type: Task(TName, Hours, Employees)
  - Type: Employees(Employee)
  - Instance: Employee{e1, e2, e3}
  - e1: e1{Alice, 123 Main St, 555-1111, Project{p1, p2}}
  - p1: p1{X, 100000, Task{t1, t2}}
  - t1: t1{A, 40, Employees{e1, e2}}
  - t2: t2{B, 20, Employees{e1}}
  - p2: p2{Y, 50000, Task{t3}}
  - t3: t3{C, 10, Employees{e1, e3}}
  - e2: e2{Bob, 456 Main St, 555-2222, Project{p1}}
  - e3: e3{Carol, 789 Main St, 555-3333, Project{p2, p3}}
  - p3: p3{Z, 20000, Task{t4}}
  - t4: t4{D, 5, Employees{e3}}

- The nested relational model supports various operations to manipulate nested relations, such as projection, selection, join, union, aggregation, and unnesting .
- The nested relational model can be used to model complex data structures, such as hierarchies, networks, and graphs, in a relational database .
- The nested relational model can also be used to integrate heterogeneous data sources, such as relational, object-oriented, and XML databases, by mapping them to a common nested relation schema.