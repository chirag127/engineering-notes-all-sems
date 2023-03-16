# Notation for ER diagram

An ER diagram is a graphical representation of the entities, attributes and relationships in a database. It helps to explain the logical structure and design of the database. There are different notations and symbols used to draw ER diagrams, depending on the modeling methodology and the level of abstraction. Some of the common notations and symbols are:

- **Entities**: Entities are the basic objects or concepts in the database, such as customers, products, orders, etc. They are represented by rectangles with the entity name inside. For example:

![entity](https://www.guru99.com/images/1/101118_0530_ERDiagramT1.png)

- **Attributes**: Attributes are the properties or characteristics of the entities, such as name, age, price, quantity, etc. They are represented by ovals with the attribute name inside, connected to the entity by a line. For example:

![attribute](https://www.guru99.com/images/1/101118_0530_ERDiagramT2.png)

- **Relationships**: Relationships are the associations or interactions between the entities, such as buys, sells, owns, etc. They are represented by diamonds with the relationship name inside, connected to the entities by lines. For example:

![relationship](https://www.guru99.com/images/1/101118_0530_ERDiagramT3.png)

- **Cardinality**: Cardinality is the number of occurrences or instances of one entity that can be related to another entity in a relationship. It is usually expressed by the minimum and maximum number of entities that can participate in the relationship. For example, one customer can buy many products, but one product can be bought by only one customer. This is a one-to-many relationship. Cardinality can be represented by different notations, such as arrow notation, crow's foot notation, Chen notation, etc. For example:

![cardinality](https://www.gleek.io/blog/wp-content/uploads/2021/11/arrow-notation.png)

- **Keys**: Keys are the attributes that uniquely identify an entity or a relationship. They are used to enforce the integrity and consistency of the data. There are different types of keys, such as primary key, foreign key, candidate key, etc. For example, a primary key is an attribute that uniquely identifies each entity in an entity set, such as customer ID, product ID, etc. A foreign key is an attribute that references the primary key of another entity or relationship, such as product ID in the order entity. Keys are usually represented by underlining the attribute name or adding a key symbol next to it. For example:

![key](https://www.lucidchart.com/pages/assets/images/article/ERD/ERD-physical-notation.png)

- **Types**: Types are the data types or domains of the attributes, such as integer, string, date, etc. They specify the format and range of values that an attribute can take. Types are usually represented by adding the type name next to the attribute name or inside parentheses. For example:

![type](https://www.lucidchart.com/pages/assets/images/article/ERD/ERD-logical-notation.png)

These are some of the basic notations and symbols used to draw ER diagrams. Depending on the modeling methodology and the level of abstraction, there may be more notations and symbols to represent other concepts, such as generalization, specialization, aggregation, composition, etc. For more details and examples, you can refer to the following sources:

: Entity Relationship (ER) Diagram Model with DBMS Example - Guru99
: Guide to entity-relationship diagram notations & symbols - Gleek
: E-R NOTATION - Computer Notes
: Entity-Relationship Diagram Symbols and Notation | Lucidchart