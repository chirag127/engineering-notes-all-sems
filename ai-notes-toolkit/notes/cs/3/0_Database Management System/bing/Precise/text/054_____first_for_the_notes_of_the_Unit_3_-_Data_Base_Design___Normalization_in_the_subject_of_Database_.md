### Unit 3 - Data Base Design & Normalization

1. **Database Design:** Database design is the process of producing a detailed data model of a database. This data model contains all the needed logical and physical design choices and physical storage parameters needed to generate a design in a data definition language, which can then be used to create a database.

2. **Normalization:** Normalization is the process of organizing a database in a way that reduces redundancy and dependency. It is a technique used to design a database so that it meets certain requirements, such as minimizing duplicate data and ensuring that data is stored in the most appropriate way.

3. **First Normal Form (1NF):** A relation is in first normal form if and only if the domain of each attribute contains only atomic (indivisible) values, and the value of each attribute contains only a single value from that domain.

4. **Second Normal Form (2NF):** A relation is in second normal form if it is in first normal form and every non-prime attribute of the relation is dependent on the whole of every candidate key.

5. **Third Normal Form (3NF):** A relation is in third normal form if it is in second normal form and every non-prime attribute of the relation is non-transitively dependent on every key of the relation.

6. **Boyce-Codd Normal Form (BCNF):** A relation is in Boyce-Codd normal form if and only if for every one of its non-trivial functional dependencies X → Y, X is a superkey.

7. **Fourth Normal Form (4NF):** A relation is in fourth normal form if and only if, for every one of its non-trivial multivalued dependencies X →→ Y, X is a superkey.

8. **Fifth Normal Form (5NF):** A relation is in fifth normal form, also known as project-join normal form, if and only if it is in fourth normal form and every join dependency in it is implied by the candidate keys.