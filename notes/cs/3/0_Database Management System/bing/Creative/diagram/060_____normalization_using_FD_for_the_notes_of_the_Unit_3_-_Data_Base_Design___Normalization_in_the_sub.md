### Normalization using FD

Normalization is the process of designing a relational database schema to minimize redundancy and anomalies. It involves decomposing a relation into smaller relations that satisfy certain properties or normal forms. Normal forms are defined based on the concept of functional dependencies (FDs).

A functional dependency (FD) is a constraint that describes the relationship between attributes in a relation. It has the form X -> Y, where X and Y are sets of attributes of the relation. It means that the values of Y are determined by the values of X. In other words, if two tuples have the same values for X, they must also have the same values for Y.

For example, consider the following relation R with attributes A, B, C, and D:

| A | B | C | D |
|---|---|---|---|
| 1 | 2 | 3 | 4 |
| 1 | 2 | 5 | 6 |
| 7 | 8 | 9 | 10 |

The FD A -> B holds in R, because whenever two tuples have the same value for A, they also have the same value for B. However, the FD A -> C does not hold in R, because there are two tuples with the same value for A but different values for C.

The FDs that hold in a relation are either given by the semantics of the attributes or derived from other FDs using inference rules. Some common inference rules are:

- Reflexivity: If Y is a subset of X, then X -> Y
- Augmentation: If X -> Y, then XZ -> YZ for any Z
- Transitivity: If X -> Y and Y -> Z, then X -> Z

Using these rules, we can derive more FDs from the given ones. For example, if A -> B and B -> C, then we can derive A -> C by transitivity.

The goal of normalization is to find a set of relations that are in a desirable normal form, such as Boyce-Codd normal form (BCNF) or third normal form (3NF). These normal forms are based on the notion of keys and superkeys.

A superkey of a relation is a set of attributes that uniquely identifies each tuple in the relation. A key is a minimal superkey, meaning that no proper subset of it is a superkey. For example, in the relation R above, {A, C} is a superkey, but not a key, because {A} is also a superkey and a proper subset of {A, C}. {A} is a key of R.

A relation is in BCNF if for every non-trivial FD X -> Y that holds in the relation, X is a superkey. A relation is in 3NF if for every non-trivial FD X -> Y that holds in the relation, either X is a superkey or Y is a subset of some key.

To normalize a relation using FDs, we can use the following steps:

1. Find a minimal cover of the FDs that hold in the relation. A minimal cover is a set of FDs that is equivalent to the original set, but has no redundant FDs or attributes. To find a minimal cover, we can apply the following rules:
    - Eliminate extraneous attributes from the left-hand side of each FD. An attribute is extraneous if it can be removed without changing the closure of the FD set. To check if an attribute A is extraneous in X -> Y, we can see if (X - {A})+ includes Y, where + denotes the closure of a set of attributes with respect to the FD set.
    - Eliminate redundant FDs from the FD set. An FD is redundant if it can be removed without changing the closure of the FD set. To check if an FD X -> Y is redundant, we can see if Y is included in (X - Y)+, where + denotes the closure of a set of attributes with respect to the FD set without X -> Y.
    - Combine FDs with the same left-hand side. If there are two FDs X -> Y and X -> Z, we can replace them with a single FD X -> YZ.
2. Find a canonical cover of the FDs that hold in the relation. A canonical cover is a set of FDs that is equivalent to the original set, but has no attributes that are transitively dependent on a key. To find a canonical cover, we can apply the following rule:
    - Split FDs with multiple attributes on the right-hand side. If there is an FD X