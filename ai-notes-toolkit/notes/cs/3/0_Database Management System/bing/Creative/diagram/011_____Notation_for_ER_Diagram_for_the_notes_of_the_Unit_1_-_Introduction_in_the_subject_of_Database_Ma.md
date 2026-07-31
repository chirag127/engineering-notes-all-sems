### Notation for ER Diagram

An ER diagram is a graphical representation of the entities, attributes and relationships in a database. It helps to explain the logical structure and design of the database. There are different notations and symbols used to draw an ER diagram, depending on the modeling methodology and the level of abstraction. Some of the common notations and symbols are:

- **Entities**: Entities are the basic objects or concepts in the database, such as customers, products, orders, etc. Entities are represented by rectangles with the entity name inside. For example:

![entity](https://www.guru99.com/images/1/122118_0535_ERDiagramTu1.png)

- **Attributes**: Attributes are the properties or characteristics of the entities, such as name, age, price, quantity, etc. Attributes are represented by ovals with the attribute name inside, and are connected to the entity by a line. For example:

![attribute](https://www.guru99.com/images/1/122118_0535_ERDiagramTu2.png)

- **Relationships**: Relationships are the associations or interactions between the entities, such as buys, sells, owns, etc. Relationships are represented by diamonds with the relationship name inside, and are connected to the entities by lines. For example:

![relationship](https://www.guru99.com/images/1/122118_0535_ERDiagramTu3.png)

- **Cardinality**: Cardinality is the number of occurrences or instances of an entity that are associated with another entity in a relationship. Cardinality is represented by symbols or numbers on the lines connecting the entities and the relationships. For example:

![cardinality](https://www.gleek.io/blog/wp-content/uploads/2021/11/arrow-notation-er-diagram.png)

There are different ways to show the cardinality, such as:

  - **Arrow notation**: Arrow notation uses single-headed or double-headed arrows, with or without open circles, to indicate the minimum and maximum number of relationships. For example, a single-headed arrow with an open circle means zero or one, a single-headed arrow without a circle means one and only one, a double-headed arrow with an open circle means zero or many, and a double-headed arrow without a circle means one or many.
  - **Barker's notation**: Barker's notation uses a single line, a double line, or a triple line to indicate the minimum and maximum number of relationships. For example, a single line means zero or one, a double line means one and only one, and a triple line means one or many.
  - **Crow's foot notation**: Crow's foot notation uses symbols such as a dash, a circle, or a crow's foot to indicate the minimum and maximum number of relationships. For example, a dash means one and only one, a circle means zero or one, and a crow's foot means one or many.

- **Keys**: Keys are the attributes that uniquely identify an entity or a relationship. Keys are represented by underlining the attribute name or by adding a key symbol next to the attribute. For example:

![key](https://www.lucidchart.com/pages/assets/img/article/ERD/ERD-key.png)

There are different types of keys, such as:

  - **Primary key**: A primary key is an attribute or a combination of attributes that uniquely identifies each instance of an entity or a relationship. For example, customer_id is a primary key for the customer entity.
  - **Foreign key**: A foreign key is an attribute or a combination of attributes that references the primary key of another entity or relationship. For example, customer_id is a foreign key for the order entity, as it references the primary key of the customer entity.
  - **Composite key**: A composite key is a combination of two or more attributes that uniquely identifies each instance of an entity or a relationship. For example, order_id and product_id are a composite key for the order_details entity, as they reference the primary keys of the order and product entities.

- **Types**: Types are the categories or domains of the attributes, such as integer, string, date, etc. Types are represented by adding the type name in parentheses next to the attribute name. For example:

![type](https://www.lucidchart.com/pages/assets/img/article/ERD/ERD-type.png)

- **Generalization**: Generalization is the process of grouping common attributes and relationships of two or more entities into a higher-level entity. Generalization is represented by a triangle with the word "is a" inside