# Notation for ER Diagram

An Entity-Relationship (ER) Diagram is a graphical representation of entities and their relationships to each other, typically used in computing in regard to the organization of data within databases or information systems. The following are the standard notations used in an ER Diagram:

1. **Entity**: An entity is represented by a rectangle with the entity name written inside. An entity represents a real-world object or concept, such as a customer or an order.

2. **Attribute**: An attribute is represented by an oval with the attribute name written inside. An attribute represents a characteristic or property of an entity, such as a customer's name or address.

3. **Relationship**: A relationship is represented by a diamond with the relationship name written inside. A relationship represents an association between two or more entities, such as a customer placing an order.

4. **Cardinality**: Cardinality is represented by a line connecting two entities, with a notation indicating the minimum and maximum number of instances of one entity that can be associated with instances of the other entity. For example, a one-to-many relationship between a customer and an order would be represented by a line connecting the customer and order entities, with a "1" near the customer entity and a "N" near the order entity.

5. **Participation**: Participation is represented by a line connecting an entity and a relationship, with a notation indicating whether the participation of the entity in the relationship is total or partial. For example, if every customer must have at least one order, the participation of the customer entity in the relationship with the order entity would be total, and would be represented by a double line.

These are the basic notations used in an ER Diagram. It is important to note that different textbooks and software tools may use slightly different notations, but the underlying concepts remain the same.