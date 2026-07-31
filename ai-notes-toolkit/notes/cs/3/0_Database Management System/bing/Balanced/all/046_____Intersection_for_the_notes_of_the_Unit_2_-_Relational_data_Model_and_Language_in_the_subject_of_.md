# Intersection

- Intersection is a relational operator that returns the common tuples (rows) that are present in both of two union-compatible (same columns and same type) relations A and B, denoted by A ∩ B .
- Intersection can be expressed using set difference operator as follows; R1 ∩ R2 = R1 – (R1 – R2) .
- Intersection is a commutative and associative operation, that is, A ∩ B = B ∩ A and (A ∩ B) ∩ C = A ∩ (B ∩ C) .
- Intersection can be implemented using a nested loop join algorithm, where for each tuple in R1, we check if it exists in R2, and if so, we add it to the result .
- Intersection can be used to find the common values of attributes in two relations, such as finding the students who are enrolled in both Math and Physics courses.