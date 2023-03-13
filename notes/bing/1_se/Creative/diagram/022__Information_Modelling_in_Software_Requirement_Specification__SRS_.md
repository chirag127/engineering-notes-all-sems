Information Modelling in Software Requirement Specification (SRS) is the process of identifying and defining the data and information that are relevant and necessary for the software product to be developed. It involves creating a conceptual model of the data and information, as well as their relationships, constraints, and operations. Information Modelling helps to ensure that the software requirements are clear, complete, consistent, and verifiable.

One of the common techniques for Information Modelling is the Entity-Relationship (ER) model, which uses graphical symbols to represent the entities, attributes, and relationships in the information domain. An entity is a thing or object that has significance for the software product, such as a customer, a product, or an order. An attribute is a property or characteristic of an entity, such as a name, a price, or a quantity. A relationship is an association or link between two or more entities, such as a customer placing an order, or a product belonging to a category.

The following diagram illustrates the basic structure of an ER model using ASCII symbols:

### Information Modelling in Software Requirement Specification (SRS)

```
+----------------+        +----------------+        +----------------+
|    Customer    |        |     Order      |        |    Product     |
+----------------+        +----------------+        +----------------+
| - CustomerID   |        | - OrderID      |        | - ProductID    |
| - Name         |        | - Date         |        | - Name         |
| - Address      |        | - Total        |        | - Price        |
| - Phone        |        | - Status       |        | - Category     |
+----------------+        +----------------+        +----------------+
|                |        |                |        |                |
|                |        |                |        |                |
|                |        |                |        |                |
|                |        |                |        |                |
|                |        |                |        |                |
|                |        |                |        |                |
|                |        |                |        |                |
|                |        |                |        |                |
|                |        |                |        |                |
|                |        |                |        |                |
+----------------+        +----------------+        +----------------+
     | 1              * |                      | *              1 |
     |                  |                      |                  |
     |                  |                      |                  |
     |                  |                      |                  |
     |                  |                      |                  |
     |                  |                      |                  |
     |                  |                      |                  |
     |                  |                      |                  |
     |                  |                      |                  |
     |                  |                      |                  |
     +------------------+                      +------------------+
```

The diagram shows that a customer can place zero or more orders, and each order can contain one or more products. Each product can belong to one category. The numbers on the lines indicate the cardinality of the relationships, which means the minimum and maximum number of occurrences of one entity for each occurrence of the related entity. For example, the 1 on the line between Customer and Order means that each order must have one and only one customer, while the * on the same line means that each customer can have zero or more orders. The attributes of each entity are listed below the entity name, preceded by a dash. The primary key of each entity, which is the attribute that uniquely identifies each instance of the entity, is underlined. For example, the primary key of Customer is CustomerID, which means that no two customers can have the same CustomerID.

Some additional information that can be added to the ER model are the data types and constraints of the attributes, the names of the relationships, and the optional or mandatory participation of the entities in the relationships. For example, the data type of CustomerID could be integer, the name of the relationship between Customer and Order could be places, and the participation of Order in the places relationship could be optional, meaning that a customer can exist without placing any order. These details can be shown using different symbols or notations, depending on the convention or standard used for ER modelling.