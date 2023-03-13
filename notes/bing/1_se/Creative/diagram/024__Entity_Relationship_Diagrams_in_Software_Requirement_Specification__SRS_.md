An entity relationship diagram (ERD) is a graphical representation of the entities and relationships in a system or database. It shows the types of entities, their attributes, and the cardinality and optionality of the relationships between them.

To draw an entity relationship diagram, you need to follow these steps:

1. Determine the entities in your system or database. Entities are the things or objects that you want to store information about, such as customers, products, orders, etc. They are usually represented by rectangles with the entity name inside.
2. Add attributes to each entity. Attributes are the properties or characteristics of each entity, such as name, address, price, quantity, etc. They are usually represented by ovals connected to the entity rectangle by a line.
3. Define the relationships between the entities. Relationships are the associations or interactions between the entities, such as customer places order, product belongs to category, order contains product, etc. They are usually represented by diamonds with the relationship name inside, connected to the entity rectangles by lines.
4. Specify the cardinality and optionality of each relationship. Cardinality is the number of instances of one entity that can be related to one instance of another entity, such as one-to-one, one-to-many, or many-to-many. Optionality is the degree of dependency or obligation of one entity to another entity, such as mandatory or optional. They are usually represented by symbols or words on the relationship lines, such as 1, M, N, (0,1), (1,1), etc.

### Entity Relationship Diagrams in Software Requirement Specification (SRS)

The following diagram illustrates the basic architecture of a simple online shopping system:

```
+-----------+         +------------+         +-----------+
| Customer  |         |   Order    |         |  Product  |
+-----------+         +------------+         +-----------+
| id        |         | id         |         | id        |
| name      |         | date       |         | name      |
| email     |         | total      |         | price     |
| address   |         | status     |         | category  |
+-----------+         +------------+         +-----------+
     | 1               / \ M                       / \ M
     |                 /   \                       /   \
     | places         /     \                     /     \
     |               /       \                   /       \
     |             /         \                 /         \
     |           /           \               /           \
     |         /             \             /             \
     |       /               \           /               \
     |     /                 \         /                 \
     |   /                   \       /                   \
     | /                     \     /                     \
     |                       |   |                       |
     |                       |   |                       |
     |                       |   |                       |
     |                       |   |                       |
+-----------+         +------------+         +-----------+
| Category  |         | OrderItem  |         | Supplier  |
+-----------+         +------------+         +-----------+
| id        |         | id         |         | id        |
| name      |         | quantity   |         | name      |
| description|        | subtotal   |         | contact   |
+-----------+         +------------+         +-----------+
     | 1               / \ M                       / \ M
     |                 /   \                       /   \
     | has            /     \                     /     \
     |               /       \                   /       \
     |             /         \                 /         \
     |           /           \               /           \
     |         /             \             /             \
     |       /               \           /               \
     |     /                 \         /                 \
     |   /                   \       /                   \
     | /                     \     /                     \
     |                       |   |                       |
     |                       |   |                       |
     |                       |   |                       |
     |                       |   |                       |
     +-----------+         +------------+         +-----------+
     |  Product  |         | OrderItem  |         | Supplier  |
     +-----------+         +------------+         +-----------+
     | id        |         | id         |         | id        |
     | name      |         | quantity   |         | name      |
     | price     |         | subtotal   |         | contact   |
     | category  |         +------------+         +-----------+
     +-----------+
```