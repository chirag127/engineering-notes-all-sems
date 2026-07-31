# Tuple and Domain Calculus

- Tuple and domain calculus are two types of relational calculus, which is a non-procedural query language for relational databases  .
- Relational calculus allows users to specify what data they want to retrieve from the database, without specifying how to do it .
- Tuple and domain calculus differ in the way they use variables to represent data in the database.

## Tuple Relational Calculus (TRC)

- Tuple relational calculus uses tuple variables that range over the tuples of a relation  .
- A tuple variable is denoted by a lowercase letter, such as t, and can be used to refer to the attribute values of a tuple.
- A tuple relational calculus query consists of a formula that evaluates to true or false for each tuple in the database .
- The result of a tuple relational calculus query is the set of all tuples that make the formula true .
- A tuple relational calculus formula can use logical connectives (and, or, not), comparison operators (=, <, >, etc.), and quantifiers (for all, there exists)  .
- A tuple relational calculus formula can also use subqueries, which are formulas that refer to other relations.
- An example of a tuple relational calculus query is:

  {t.name | Student(t) and t.age > 18}

  This query returns the names of all students who are older than 18.

## Domain Relational Calculus (DRC)

- Domain relational calculus uses domain variables that range over the values of a domain  .
- A domain is a set of possible values for an attribute, such as integers, strings, dates, etc.
- A domain variable is denoted by an uppercase letter, such as X, and can be used to refer to a single value in a domain.
- A domain relational calculus query consists of a formula that evaluates to true or false for each combination of values in the domains of the database .
- The result of a domain relational calculus query is the set of all combinations of values that make the formula true .
- A domain relational calculus formula can use logical connectives, comparison operators, and quantifiers, similar to tuple relational calculus .
- A domain relational calculus formula can also use subqueries, which are formulas that refer to other relations, but with domain variables instead of tuple variables.
- An example of a domain relational calculus query is:

  {X | Student(name, age) and X = name and age > 18}

  This query returns the names of all students who are older than 18.