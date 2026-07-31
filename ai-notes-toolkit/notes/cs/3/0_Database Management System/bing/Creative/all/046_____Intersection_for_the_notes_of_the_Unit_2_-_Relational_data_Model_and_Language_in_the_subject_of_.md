# Intersection

- Intersection is a relational algebra operation that returns the common tuples (rows) of two relations.
- The symbol for intersection is ∩.
- The two relations must be union-compatible, meaning they have the same number and type of attributes (columns).
- The result of intersection has the same schema (attribute names and types) as the input relations.
- Intersection can be expressed using set difference as follows: R1 ∩ R2 = R1 - (R1 - R2).
- Intersection is commutative, meaning R1 ∩ R2 = R2 ∩ R1.
- Intersection is associative, meaning (R1 ∩ R2) ∩ R3 = R1 ∩ (R2 ∩ R3).
- Intersection is idempotent, meaning R ∩ R = R.

## Example

Suppose we have two relations R and S with the following tuples:

| R | S |
|---|---|
| a | a |
| b | c |
| c | d |
| d | e |

Then, R ∩ S = {a, c, d}. The result has the same schema as R and S, and contains only the tuples that are present in both relations.