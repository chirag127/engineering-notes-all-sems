# Relationships of Higher Degree

- A relationship in an ER model is an association between two or more entity sets.
- The degree of a relationship is the number of entity sets involved in the relationship .
- A relationship of degree two is called a binary relationship, and it is the most common type of relationship in ER models.
- A relationship of degree three is called a ternary relationship, and it involves three entity sets.
- A relationship of degree n is called an n-ary relationship, and it involves n entity sets.
- Higher degree relationships (n > 2) are more complex and less common than binary relationships, and they may be difficult to convert to relational tables.
- Higher degree relationships can sometimes be replaced by a combination of binary relationships using an associative entity set  .
- An associative entity set is an entity set that represents the association between two or more other entity sets, and it may have its own attributes and relationships .
- For example, a ternary relationship between entity sets Student, Course, and Instructor can be replaced by an associative entity set Enrollment that has relationships with Student, Course, and Instructor, and has an attribute Grade .
- The advantage of using an associative entity set is that it simplifies the ER model and makes it easier to convert to a relational model .
- The disadvantage of using an associative entity set is that it may introduce redundancy and inconsistency in the data, and it may lose some information about the original higher degree relationship .