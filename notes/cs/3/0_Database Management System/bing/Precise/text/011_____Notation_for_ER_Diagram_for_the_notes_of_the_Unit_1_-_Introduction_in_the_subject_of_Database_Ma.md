### Notation for ER Diagram

An Entity-Relationship (ER) Diagram is a graphical representation of entities and their relationships to each other, typically used in computing in regard to the organization of data within databases or information systems. Here are some of the notations used in an ER Diagram:

1. **Entity**: An entity is represented by a rectangle with the entity name written inside. An entity represents a real-world object or concept, such as a customer or an order.

2. **Attribute**: An attribute is represented by an oval with the attribute name written inside. An attribute represents a characteristic or property of an entity, such as a customer's name or address.

3. **Relationship**: A relationship is represented by a diamond with the relationship name written inside. A relationship represents an association between two or more entities, such as a customer placing an order.

4. **Cardinality**: Cardinality is represented by a line connecting two entities, with a notation at each end indicating the minimum and maximum number of instances of one entity that can be associated with instances of the other entity. For example, a one-to-many relationship between a customer and an order would be represented by a line with a "1" at the customer end and a "many" symbol (usually represented by an "M" or a crow's foot) at the order end.

5. **Participation**: Participation is represented by a double line connecting two entities, indicating that instances of one entity must be associated with instances of the other entity. For example, a double line between a customer and an order would indicate that every order must be associated with a customer.

6. **Weak Entity**: A weak entity is represented by a double rectangle, with the entity name written inside. A weak entity is an entity that cannot be uniquely identified by its attributes alone and must rely on a relationship with another entity to be identified.

7. **Identifying Relationship**: An identifying relationship is represented by a double diamond, with the relationship name written inside. An identifying relationship is a relationship between a weak entity and its identifying entity, used to uniquely identify instances of the weak entity.

These are some of the common notations used in an ER Diagram. It is important to note that different sources may use slightly different notations, so it is always a good idea to check the specific notation being used in a given diagram.