 Here is the content in Markdown format without any emojis or external links:

### BCNF for the notes of the Unit 3 - Data Base Design & Normalization

1. BCNF stands for Boyce-Codd Normal Form. It is a higher version of 3NF.
2. A relation schema R is in BCNF if and only if for every one of its dependencies X → Y, at least one of the following holds:
- X → Y is a trivial functional dependency (Y ⊆ X)
- X is a superkey of R
3. BCNF deals with certain type of many-to-many relationship called overlapping candidate keys.
4. In BCNF, the left hand side(determinant) of every dependency must be a candidate key.
5. BCNF eliminates certain anomalies that are still possible with 3NF.
6. To convert a 3NF relation into BCNF, we keep finding non-prime attributes on the right hand side of functional dependencies and move them to the left hand side, thereby converting FDs to the required form. This may result in projecting out some attributes.
7. A relation schema R is in BCNF if for all functional dependencies X → Y, X is a superkey. This is a concise definition of the BCNF.

The content is written in formal tone with points and without any emojis or external links as instructed. Please let me know if you would like me to modify or expand the content in any way.