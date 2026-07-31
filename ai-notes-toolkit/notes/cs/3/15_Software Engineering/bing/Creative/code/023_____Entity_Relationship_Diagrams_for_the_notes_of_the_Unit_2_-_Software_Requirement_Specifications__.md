### Entity Relationship Diagrams

- Entity Relationship Diagrams (ERDs) are graphical representations of the data and relationships in a database system.
- ERDs are used to model the logical structure and design of a database, as well as to document the requirements and constraints of the data.
- ERDs consist of three main components: entities, attributes, and relationships.
- Entities are the objects or concepts that are stored in the database, such as customers, products, orders, etc. Entities are represented by rectangles with the entity name inside.
- Attributes are the properties or characteristics of an entity, such as name, address, price, quantity, etc. Attributes are represented by ovals connected to the entity by a line. Some attributes may be composite, meaning they can be further divided into sub-attributes, such as name into first name and last name. Some attributes may be multivalued, meaning they can have more than one value for an entity, such as phone numbers or email addresses. Some attributes may be derived, meaning they can be calculated from other attributes, such as age from date of birth or total from quantity and price.
- Relationships are the associations or connections between entities, such as customer places order, product belongs to category, order contains product, etc. Relationships are represented by diamonds with the relationship name inside, connected to the entities by lines. The degree of a relationship is the number of entities involved in the relationship, such as binary (two entities), ternary (three entities), or n-ary (n entities). The cardinality of a relationship is the number of instances of one entity that can be associated with one instance of another entity, such as one-to-one, one-to-many, many-to-one, or many-to-many. The cardinality can be shown by placing symbols or numbers on the lines connecting the entities and the relationship, such as 1, N, M, or crow's feet. The participation of an entity in a relationship is the extent to which an entity must be involved in the relationship, such as total (mandatory) or partial (optional). The participation can be shown by placing a double line or a single line on the line connecting the entity and the relationship, respectively.

- Here is an example of an ERD for a simple online bookstore database:

![ERD example](https://i.imgur.com/2y0n0wG.png)

- The ERD shows that:
  - A customer can place zero or more orders, and an order must be placed by one and only one customer. This is a one-to-many relationship with total participation from order and partial participation from customer.
  - An order can contain one or more products, and a product can be contained in zero or more orders. This is a many-to-many relationship with total participation from both entities.
  - A product belongs to one and only one category, and a category can have zero or more products. This is a one-to-many relationship with total participation from product and partial participation from category.
  - A product has a composite attribute name, which consists of two sub-attributes: title and author. A product also has a derived attribute rating, which is calculated from the attribute reviews.
  - A customer has a multivalued attribute phone, which can have one or more values. A customer also has a derived attribute age, which is calculated from the attribute dob (date of birth).