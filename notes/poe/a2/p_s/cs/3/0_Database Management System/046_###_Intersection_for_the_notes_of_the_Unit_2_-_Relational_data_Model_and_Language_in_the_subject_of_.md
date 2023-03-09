 Here is the content in markdown format for the given topic:

### Intersection

Intersection is a relational algebra operator which gives the common tuples of two relations. In other words, it returns the tuples which are common to both the input relations.

**Syntax:**

R INTERSECT S

Where R and S are input relations.

**Example:**

Let's take two relations:

R = {(1, 'A'), (2, 'B'), (3, 'C')}
S = {(2, 'D'), (4, 'E'), (3, 'F')}

Then,

R INTERSECT S = {(3, 'C')}

It gives the common tuple (3, 'C') which is present in both the input relations R and S.

**Properties:**

-   Output cardinality ≤ min(R, S)
-   It is commutative: R INTERSECT S = S INTERSECT R
-   It is associative: (R INTERSECT S) INTERSECT T = R INTERSECT (S INTERSECT T)

**Applications:**

-   To find common records/tuples from two relations.
-   To perform set intersection on two relations.
-   To find the intersection of two queries which gives the common results.

**Advantages:**

-   Gives the common tuples between two relations.
-   Easy to understand and implement.

**Disadvantages:**

-   Output size can be large if relations are large.
-   Performance can degrade if relations are not indexed.