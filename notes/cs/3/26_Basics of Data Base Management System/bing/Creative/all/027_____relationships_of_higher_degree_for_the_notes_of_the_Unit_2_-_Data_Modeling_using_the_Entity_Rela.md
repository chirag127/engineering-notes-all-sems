# Relationships of Higher Degree

- A relationship is an association between two or more entities in an ER model.
- The degree of a relationship is the number of entities that participate in it.
- A binary relationship has a degree of two, meaning it involves two entities.
- A ternary relationship has a degree of three, meaning it involves three entities.
- A higher degree relationship has a degree of more than three, meaning it involves more than three entities.
- Higher degree relationships are rare and complex, and they should be avoided if possible.
- Higher degree relationships can be converted into binary relationships by introducing new entity types or relationship types.
- For example, a quaternary relationship R between entities A, B, C, and D can be replaced by a new entity type E and four binary relationships between E and A, E and B, E and C, and E and D.
- To read a higher degree relationship, we need to isolate two out of the participating entities and see how they relate to the third one, and repeat this for all possible pairs.
- For example, to read a ternary relationship R between entities A, B, and C, we need to see how A and B relate to C, how A and C relate to B, and how B and C relate to A.