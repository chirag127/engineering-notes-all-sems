An information model is an abstract, formal representation of entity types that may include their properties, relationships and the operations that can be performed on them. It is used to specify data semantics for a chosen domain of discourse. An information model is part of a software requirement specification (SRS), which is a document that describes what the software will do and how it will be expected to perform. An SRS shows the detail about the performance of the expected system and the functionality the product needs to fulfill the needs of all stakeholders  .

A possible diagram for information modelling in SRS is shown below. It uses the entity-relationship (ER) notation to represent the entity types, their attributes, and the relationships among them. The diagram also shows the cardinality and participation constraints for each relationship. The diagram is not exhaustive and may vary depending on the specific domain and requirements of the software.

### Information Modelling in Software Requirement Specification (SRS)

```
+-----------------+       +-----------------+       +-----------------+
|    Customer     |       |     Product     |       |     Order       |
+-----------------+       +-----------------+       +-----------------+
| - customer_id   |       | - product_id    |       | - order_id      |
| - name          |       | - name          |       | - date          |
| - address       |       | - price         |       | - quantity      |
| - phone         |       | - description   |       | - total_amount  |
+-----------------+       +-----------------+       +-----------------+
       | 1               / \ 1                     / \ 1
       |                /   \                     /   \
       |               /     \                   /     \
       |              /       \                 /       \
       |             /         \               /         \
       |            /           \             /           \
       |           /             \           /             \
       |          /               \         /               \
       |         /                 \       /                 \
       |        /                   \     /                   \
       |       /                     \   /                     \
       |      /                       \ /                       \
       |     /                         X                         \
       |    /                        / \                        \
       |   /                        /   \                        \
       |  /                        /     \                        \
       | /                        /       \                        \
       |/                        /         \                        \
+-----------------+       +-----------------+       +-----------------+
|     Review      |       |     Category    |       |     Payment     |
+-----------------+       +-----------------+       +-----------------+
| - review_id     |       | - category_id   |       | - payment_id    |
| - rating        |       | - name          |       | - method        |
| - comment       |       | - description   |       | - status        |
| - date          |       +-----------------+       | - amount        |
+-----------------+              | 1                +-----------------+
       | 1                       |                       | 1
       |                         |                       |
       |                         |                       |
       |                         |                       |
       |                         |                       |
       |                         |                       |
       |                         |                       |
       |                         |                       |
       |                         |                       |
       |                         |                       |
       |                         |                       |
       |                         |                       |
       |                         |                       |
       |                         |                       |
       |                         |                       |
       +-------------------------+-----------------------+
```