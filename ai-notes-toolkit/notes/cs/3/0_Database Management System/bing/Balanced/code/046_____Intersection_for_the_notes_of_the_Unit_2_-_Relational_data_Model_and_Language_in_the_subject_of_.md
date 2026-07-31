### Intersection

- Intersection is a relational algebra operation that returns the common tuples (rows) of two relations.
- The symbol for intersection is ∩.
- The two relations must be union-compatible, meaning they have the same number and type of attributes (columns).
- The result of intersection has the same schema (attribute names and types) as the input relations.
- Intersection can be expressed using set difference as follows: R1 ∩ R2 = R1 - (R1 - R2).
- Intersection is commutative, meaning R1 ∩ R2 = R2 ∩ R1.
- Intersection is associative, meaning (R1 ∩ R2) ∩ R3 = R1 ∩ (R2 ∩ R3).
- Intersection is idempotent, meaning R ∩ R = R.

Example:

| Student | Course |
|---------|--------|
| Alice   | CS101  |
| Bob     | CS101  |
| Carol   | CS102  |
| Dave    | CS103  |

| Student | Course |
|---------|--------|
| Alice   | CS101  |
| Bob     | CS102  |
| Carol   | CS102  |
| Eve     | CS103  |

The intersection of the two relations is:

| Student | Course |
|---------|--------|
| Alice   | CS101  |
| Carol   | CS102  |