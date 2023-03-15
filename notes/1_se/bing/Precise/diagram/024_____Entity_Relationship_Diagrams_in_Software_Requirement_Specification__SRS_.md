### Entity Relationship Diagrams in Software Requirement Specification (SRS)

An Entity Relationship Diagram (ERD) is a visual representation of the relationships between entities in a database. It is commonly used in the design of database systems and is an important part of a Software Requirement Specification (SRS) document.

Here is an example of an ERD in ASCII art:

```
+-------------+       +-------------+
|    User     |       |    Order    |
+-------------+       +-------------+
| - user_id   |       | - order_id  |
| - name      |       | - user_id   |
| - email     |       | - date      |
| - address   |       | - total     |
+-------------+       +-------------+
       |                    |
       |                    |
       +--------------------+
```

In this example, the `User` entity has attributes such as `user_id`, `name`, `email`, and `address`. The `Order` entity has attributes such as `order_id`, `user_id`, `date`, and `total`. The relationship between the two entities is represented by the line connecting them, indicating that a `User` can have many `Orders`.
