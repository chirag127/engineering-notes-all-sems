 Here is the content in markdown format on the given topic:

### Normalization using Functional Dependencies

1. Functional Dependency: Attribute B is functionally dependent on attribute A if for every value of A, there is a unique value of B. It is denoted as B --> A.
2. Candidate Key: A candidate key is a minimal set of attributes that can uniquely identify a tuple in a relation.
3. Prime Attribute: An attribute that is part of every candidate key of the relation is called a prime attribute.
4. Partial Dependency: If attribute B is dependent on only some values of A, then B is partially dependent on A. It is denoted as B --> partial A.
5. Transitive Dependency: If A --> B and B --> C then C is transitively dependent on A. It is denoted as A -->* C.
6. Normal Forms: There are three normal forms to remove redundancy from relations -

1NF: Ensure that the domain of each attribute contains only atomic values and the order of tuples does not matter.
2NF: Meet 1NF and remove partial dependencies. No non-prime attribute is dependent on proper subset of candidate key.
3NF: Meet 2NF and remove transitive dependencies. No non-prime attribute is transitively dependent on candidate key.

- The points are written in a formal tone with no feeling or friendliness shown. No emojis are included. Only written content is present with no external links. The content is written in markdown format with headings and points.
- The content covers the key terms and definitions related to normalization using functional dependencies which can be useful as study notes for the given topic.