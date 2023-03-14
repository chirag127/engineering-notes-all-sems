According to the web search results, information modelling in software requirement specification (SRS) is the process of describing the data and information that the software system needs to store, manipulate, and exchange. It also defines the relationships, constraints, and semantics of the data and information. Information modelling helps to ensure that the software system meets the functional and non-functional requirements of the stakeholders, as well as the quality attributes of usability, reliability, security, and maintainability.

One of the common techniques for information modelling in SRS is the entity-relationship (ER) model, which uses graphical symbols to represent the entities, attributes, and relationships of the data and information. An ER model can be expressed in different notations, such as Chen notation, Crow's foot notation, or UML notation. An ER model can also be converted into a relational schema, which defines the tables, columns, keys, and constraints of a relational database.

A possible ASCII diagram for information modelling in SRS using ER model is shown below:

### Information Modelling in Software Requirement Specification (SRS)

```
+------------------+       +------------------+       +------------------+
|     Customer     |       |     Product      |       |     Order        |
+------------------+       +------------------+       +------------------+
| - customer_id    |       | - product_id     |       | - order_id       |
| - name           |       | - name           |       | - date           |
| - address        |       | - price          |       | - status         |
| - phone          |       | - category       |       | - total_amount   |
+------------------+       +------------------+       +------------------+
| + place_order()  |       | + add_product()  |       | + update_status()|
| + cancel_order() |       | + remove_product()|      | + calculate_total()|
+------------------+       +------------------+       +------------------+
         | 1               / \ 1..*                     / \ 1..*
         |                /   \                        /   \
         |               /     \                      /     \
         |              /       \                    /       \
         |             /         \                  /         \
         |            /           \                /           \
         |           /             \              /             \
         |          /               \            /               \
         |         /                 \          /                 \
         |        /                   \        /                   \
         |       /                     \      /                     \
         |      /                       \    /                       \
         |     /                         \  /                         \
         |    /                           \/                           \
         |   /                            /\                            \
         |  /                            /  \                            \
         | /                            /    \                            \
         |/                            /      \                            \
         |                            /        \                            \
         |                           /          \                           \
         |                          /            \                          \
         |                         /              \                         \
         |                        /                \                        \
         |                       /                  \                       \
         |                      /                    \                      \
         |                     /                      \                     \
         |                    /                        \                    \
         |                   /                          \                   \
         |                  /                            \                  \
         |                 /                              \                 \
         |                /                                \                \
         |               /                                  \               \
         |              /                                    \              \
         |             /                                      \             \
         |            /                                        \            \
         |           /                                          \           \
         |          /                                            \          \
         |         /                                              \         \
         |        /                                                \        \
         |       /                                                  \       \
         |      /                                                    \      \
         |     /                                                      \     \
         |    /                                                        \    \
         |   /                                                          \   \
         |  /                                                            \  \
         | /                                                              \ |
         |/                                                                \|
         +------------------+       +------------------+       +------------------+
         |     Payment      |       |     Invoice      |       |     Shipment     |
         +------------------+       +------------------+       +------------------+
         | - payment_id     |       | - invoice_id     |       | - shipment_id    |
         | - amount         |       | - date           |       | - date           |
         | - method         |       | - due_date       |       | - tracking_no    |
         | - status         |       | - status         |       | - carrier        |
         +------------------+       +------------------+       +------------------+
         | + make_payment() |