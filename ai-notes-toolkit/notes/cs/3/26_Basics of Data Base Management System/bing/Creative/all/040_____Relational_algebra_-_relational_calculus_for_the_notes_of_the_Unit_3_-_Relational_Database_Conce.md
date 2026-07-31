# Relational Algebra and Relational Calculus

- Relational algebra and relational calculus are two formal languages for manipulating relations in the relational model of data.
- Relational algebra is a procedural language that specifies how to construct a new relation from one or more existing relations in the database.
- Relational calculus is a declarative language that specifies what data to retrieve from the database without specifying how to do it.
- Both languages are equivalent in expressive power, meaning that any query that can be expressed in one language can also be expressed in the other language. This is known as Codd's theorem.

## Relational Algebra

- Relational algebra consists of a set of basic operations that take one or more relations as input and produce a new relation as output.
- The basic operations are:
  - Selection: selects a subset of tuples from a relation that satisfy a given condition.
  - Projection: selects a subset of attributes from a relation and eliminates duplicates.
  - Union: combines two relations with the same set of attributes and eliminates duplicates.
  - Set difference: returns the tuples that are in one relation but not in another relation with the same set of attributes.
  - Cartesian product: combines two relations by forming all possible pairs of tuples from both relations.
  - Rename: assigns a new name to a relation or an attribute.
- Relational algebra also defines additional operations that are derived from the basic operations, such as:
  - Intersection: returns the tuples that are common to both relations with the same set of attributes.
  - Join: combines two relations by matching tuples based on a join condition.
  - Division: returns the tuples from one relation that are associated with all tuples from another relation.
  - Aggregate functions: apply a function to a set of tuples and return a single value, such as sum, count, average, etc.
  - Grouping and sorting: group tuples by one or more attributes and sort them by one or more attributes.

## Relational Calculus

- Relational calculus consists of a set of formulas that define relations in terms of other relations in the database.
- The formulas are composed of variables, constants, logical connectives, quantifiers, and predicates that refer to relations and attributes in the database.
- There are two types of relational calculus: tuple relational calculus and domain relational calculus.
- Tuple relational calculus uses variables that range over tuples of a relation and predicates that involve the attributes of the relation.
- Domain relational calculus uses variables that range over the domains of attributes and predicates that involve the values of the attributes.
- Both types of relational calculus are equivalent in expressive power, meaning that any query that can be expressed in one type can also be expressed in the other type.
- Relational calculus is a safe language, meaning that any query that can be expressed in it will always return a finite set of tuples as a result.