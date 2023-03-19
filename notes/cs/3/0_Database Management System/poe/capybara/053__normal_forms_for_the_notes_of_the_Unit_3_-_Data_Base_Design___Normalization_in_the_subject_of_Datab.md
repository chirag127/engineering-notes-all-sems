### Normal Forms for the Notes of Unit 3 - Database Design & Normalization

Database normalization is the process of organizing data in a database so that it is consistent, accurate, and easy to maintain. Normalization is achieved by applying a set of rules called normal forms. In this unit, we will learn about the different normal forms and how they are applied.

Here are the different normal forms:

#### First Normal Form (1NF)
- A relation is in first normal form if and only if all attributes contain atomic values (i.e., indivisible).
- Each column of a table should contain only one value, and each row should be unique.
- Example: A table with columns for "First Name" and "Last Name" would be in 1NF.

#### Second Normal Form (2NF)
- A relation is in second normal form if it is in 1NF and all non-key attributes are fully dependent on the primary key.
- Each non-key attribute should depend on the entire primary key, not just a part of it.
- Example: A table with columns for "Order ID", "Product ID", "Quantity", and "Price" would be in 2NF if "Quantity" and "Price" depend on both "Order ID" and "Product ID".

#### Third Normal Form (3NF)
- A relation is in third normal form if it is in 2NF and all non-key attributes are independent of each other.
- Each non-key attribute should depend only on the primary key, not on any other non-key attributes.
- Example: A table with columns for "Customer ID", "Product ID", "Product Name", and "Product Description" would not be in 3NF if "Product Description" depends on "Product Name".

#### Fourth Normal Form (4NF)
- A relation is in fourth normal form if it is in 3NF and has no multi-valued dependencies.
- Each attribute should depend on the primary key, not on any other attributes.
- Example: A table with columns for "Customer ID", "Order ID", "Product ID", and "Product Description" would not be in 4NF if there are multiple "Product Descriptions" for a single "Order ID".

#### Fifth Normal Form (5NF)
- A relation is in fifth normal form if it is in 4NF and has no join dependencies.
- Each attribute should be uniquely determined by the primary key, not by any other attributes.
- Example: A table with columns for "Customer ID", "Order ID", "Product ID", and "Product Description" would not be in 5NF if "Product Description" can be determined by both "Customer ID" and "Order ID".

In conclusion, normalization is an essential process in database design that ensures data consistency, accuracy, and maintainability. By applying the different normal forms, we can organize data in a way that is efficient and effective for data retrieval and manipulation.