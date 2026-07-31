# Notation for ER Diagram

An ER diagram is a graphical representation of the entities, attributes and relationships in a database. It helps to explain the logical structure and design of the database. There are different notations and symbols used to draw an ER diagram, depending on the modeling methodology and the level of abstraction. Some of the common notations and symbols are:

- **Entities**: Entities are the basic objects or concepts in the database, such as customers, products, orders, etc. They are represented by rectangles with the entity name inside. For example:

![entity](https://www.guru99.com/images/1/092118_0613_ERDiagramTut1.png)

- **Attributes**: Attributes are the properties or characteristics of the entities, such as name, age, price, quantity, etc. They are represented by ovals with the attribute name inside, connected to the entity by a line. For example:

![attribute](https://www.guru99.com/images/1/092118_0613_ERDiagramTut2.png)

- **Relationships**: Relationships are the associations or interactions between the entities, such as buys, sells, owns, etc. They are represented by diamonds with the relationship name inside, connected to the entities by lines. For example:

![relationship](https://www.guru99.com/images/1/092118_0613_ERDiagramTut3.png)

- **Cardinality**: Cardinality is the number of occurrences or instances of one entity that can be related to another entity in a relationship. It can be one-to-one, one-to-many, many-to-one or many-to-many. It is represented by different symbols or notations depending on the modeling methodology. For example, in arrow notation, a single-headed arrow with an open circle on the line means zero or one, a single-headed arrow with a closed circle on the line means one and only one, a double-headed arrow means one or many, and a line without an arrow means many. For example:

![cardinality](https://www.gleek.io/blog/wp-content/uploads/2021/11/arrow-notation-er-diagram.png)

- **Keys**: Keys are the attributes that uniquely identify an entity or a relationship. They can be primary keys, foreign keys, composite keys or candidate keys. They are represented by different symbols or notations depending on the modeling methodology. For example, in Chen notation, a primary key is underlined, a foreign key is dashed, a composite key is a combination of two or more attributes, and a candidate key is a potential primary key. For example:

![key](https://www.lucidchart.com/pages/assets/images/article/ERD/ERD-Primary-Key.png)

- **Types**: Types are the data types or domains of the attributes, such as integer, string, date, etc. They are represented by different symbols or notations depending on the modeling methodology. For example, in Crow's foot notation, a type is shown as a small label next to the attribute name. For example:

![type](https://www.lucidchart.com/pages/assets/images/article/ERD/ERD-Data-Type.png)

These are some of the basic notations and symbols for ER diagrams. There are other notations and symbols that can be used to represent more complex or specific aspects of the database, such as generalization, specialization, aggregation, composition, etc. Different modeling methodologies may have different notations and symbols for the same concept, or different concepts for the same notation and symbol. Therefore, it is important to choose a consistent and appropriate notation and symbol for the ER diagram, and to document the meaning and usage of each notation and symbol.