 Here is the content in markdown format for the topic ### third normal forms for the notes of the Unit 4 - Data Base Design & Normalization in the subject of Basics of Data Base Management System:

## Third Normal Form (3NF)

- A relation is in third normal form if it is in second normal form and no non-prime attribute is dependent on other non-prime attributes.
- This means that every non-prime attribute must depend on the primary key alone, not on other non-prime attributes.
- Having relations in third normal form has the following advantages:
    - It avoids undesirable redundancy in data.
    - It makes it easier to maintain data integrity and consistency since there is no redundant data.
    - It makes it easier to modify schemas without causing inconsistencies.

For example, consider a relation with attributes ( stud_id, stud_name, branch, sem ) where stud_id is the primary key.
This relation is in third normal form only if:

- stud_name depends on stud_id (ok)
- branch depends on stud_id (ok)
- sem does NOT depend on branch

If sem depends on branch, the relation violates third normal form. To convert it to 3NF, we break it into two relations:
( stud_id, stud_name, branch ) and ( stud_id, sem )

Where sem only depends on stud_id.

In summary, a relation is in third normal form if:

1. It is in second normal form
2. No non-prime attribute is dependent on other non-prime attributes

Following third normal form has the advantages of removing all redundancies and anomalies in relations, making the database more consistent and efficient.