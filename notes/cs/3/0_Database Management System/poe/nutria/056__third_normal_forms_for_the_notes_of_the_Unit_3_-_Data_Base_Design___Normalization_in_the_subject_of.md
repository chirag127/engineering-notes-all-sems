
### Third Normal Forms

* Third Normal Form (3NF) is a normal form used in relational database design. It is a refinement of the Second Normal Form (2NF).
* 3NF requires that all non-key attributes be non-transitively dependent on the primary key. 
* This means that all attributes must depend directly on the primary key and not on any other non-key attribute. 
* For example, if an attribute A depends on attribute B, and B depends on C, then A cannot depend on C. 
* 3NF also requires that all non-key attributes must be mutually independent. This means that no two non-key attributes should be functionally dependent on each other.
* 3NF is considered the most important normalization form, as it is the most restrictive. It is also the most widely used normal form in database design.