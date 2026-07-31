### Notation for ER Diagram

Entity Relationship (ER) diagram is a graphical representation of entities and their relationships to each other in a database. ER diagrams use symbols to represent entities, attributes, relationships, and cardinality. The following are the notations commonly used to create ER diagrams:

- Entity: An entity is a real-world object or concept that has attributes and can be uniquely identified. Entities are represented as rectangles with their name written inside the rectangle. For example, a customer entity can be represented as follows:

```
            +------------+
            |   Customer |
            +------------+
```

- Attribute: An attribute is a property or characteristic of an entity. Attributes are represented as ovals connected to the entity rectangle with a line. For example, the customer entity may have attributes such as name, address, and phone number, which can be represented as follows:

```
            +------------+
            |   Customer |
            +------------+
            |   Name     |
            |   Address  |
            |   Phone    |
            +------------+
```

- Relationship: A relationship is a connection between two or more entities. Relationships are represented as diamonds connected to the entities with lines. The type of relationship (one-to-one, one-to-many, many-to-many) can be indicated by the cardinality notation. For example, a customer can place many orders, but an order can only be placed by one customer. This relationship can be represented as follows:

```
            +------------+         +------+
            |   Customer |         |Order |
            +------------+         +------+
                |                      |
                +----------------------+
```

- Cardinality notation: The cardinality notation is used to indicate the number of instances of an entity that can be associated with another entity. The following symbols are used:

    - One-to-one relationship: A line is drawn between the entities with a symbol "1" on one end and "1" on the other end. For example, a customer can have only one address, and an address can belong to only one customer. This relationship can be represented as follows:

    ```
                +------------+         +--------+
                |   Customer |         | Address|
                +------------+         +--------+
                      1                      1
    ```

    - One-to-many relationship: A line is drawn between the entities with a symbol "1" on one end and a crows foot on the other end. For example, a customer can place many orders, but an order can only be placed by one customer. This relationship can be represented as follows:

    ```
                +------------+         +------+
                |   Customer |         |Order |
                +------------+         +------+
                      1                  crow's foot
    ```

    - Many-to-many relationship: A line is drawn between the entities with a crows foot on both ends. For example, a student can enroll in many courses, and a course can have many students. This relationship can be represented as follows:

    ```
                +-----------+              +-------+
                |   Student |              | Course|
                +-----------+              +-------+
                 crow's foot                  crow's foot
    ```

ER diagrams are an essential tool for database design and modeling. By using these notations, developers can create a visual representation of the data model and understand the relationships between entities.