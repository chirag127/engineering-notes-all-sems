### Information Modelling in Software Requirement Specification (SRS)

- Information modelling is a process of creating an abstract, formal representation of the data and concepts related to a specific domain of discourse.
- Information modelling helps to specify the data semantics, constraints, rules, and operations that define the meaning and behaviour of the information in the domain.
- Information modelling is an important part of software requirement specification (SRS), which is a document that describes what the software will do and how it will be expected to perform.
- SRS is an official document that shows the detail about the performance and functionality of the expected system. It also shows the needs and expectations of the stakeholders (business, users, etc.).
- Information modelling in SRS can help to:
  - Clarify the requirements and avoid ambiguity and inconsistency.
  - Communicate the requirements to the developers and the customers.
  - Validate and verify the requirements and the design of the system.
  - Support the implementation, testing, and maintenance of the system.
- Information modelling in SRS can be done using different techniques and notations, such as:
  - Entity-relationship (ER) model: A graphical representation of the entities (things) and their relationships in the domain. An entity can have attributes (properties) and a relationship can have cardinality (number of occurrences). For example:

```
+----------------+       +----------------+
|    Customer    |       |    Product     |
+----------------+       +----------------+
| - customer_id  |       | - product_id   |
| - name         |       | - name         |
| - address      |       | - price        |
+----------------+       +----------------+
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         +-----------------------+
               purchases
             (0..*, 0..*)
```

  - Class diagram: A graphical representation of the classes (types) and their associations in the domain. A class can have attributes and methods (operations) and an association can have multiplicity and role names. For example:

```
+----------------+       +----------------+
|    Customer    |       |    Product     |
+----------------+       +----------------+
| - customer_id  |       | - product_id   |
| - name         |       | - name         |
| - address      |       | - price        |
+----------------+       +----------------+
| + buy()        |       | + sell()       |
+----------------+       +----------------+
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         +-----------------------+
               purchases
             (0..*, 0..*)
```

  - Data dictionary: A textual representation of the data elements and their definitions, formats, domains, and constraints in the domain. For example:

```
Customer
  - customer_id: A unique identifier for a customer. Integer. Required. Primary key.
  - name: The name of a customer. String. Required. Maximum length: 50 characters.
  - address: The address of a customer. String. Optional. Maximum length: 100 characters.

Product
  - product_id: A unique identifier for a product. Integer. Required. Primary key.
  - name: The name of a product. String. Required. Maximum length: 50 characters.
  - price: The price of a product. Decimal. Required. Positive.

purchases: A relationship between Customer and Product that indicates which customer bought which product. Optional for both entities. Many-to-many cardinality.
```

- A mnemonic to remember the benefits of information modelling in SRS is: C3V3S (Clarify, Communicate, Validate, Verify, Support).
- A learning trick to understand the difference between ER model and class diagram is: ER model focuses on what entities and relationships are, while class diagram focuses on what classes and associations do.