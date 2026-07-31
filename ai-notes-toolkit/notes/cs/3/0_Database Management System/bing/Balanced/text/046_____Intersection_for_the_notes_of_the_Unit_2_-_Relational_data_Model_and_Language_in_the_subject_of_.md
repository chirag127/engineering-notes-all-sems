### Intersection

- Intersection is a relational algebra operation that returns the common tuples from two relations.
- The symbol for intersection is ∩.
- The intersection of two relations R and S, denoted by R ∩ S, is the relation that contains all the tuples that are in both R and S.
- The intersection operation is commutative, meaning that R ∩ S = S ∩ R.
- The intersection operation is associative, meaning that (R ∩ S) ∩ T = R ∩ (S ∩ T).
- The intersection operation is idempotent, meaning that R ∩ R = R.
- The intersection operation is distributive over union, meaning that R ∩ (S ∪ T) = (R ∩ S) ∪ (R ∩ T).
- The intersection operation requires that the two relations have the same degree (number of attributes) and the same domain (type of values) for each attribute.
- The intersection operation preserves the attribute names and the order of the attributes from the first relation.
- The intersection operation can be implemented using a nested loop join algorithm, a hash join algorithm, or a sort-merge join algorithm.