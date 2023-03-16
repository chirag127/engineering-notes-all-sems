### Basic concepts for the notes of the Unit 2 - Semantic Data Models in the subject of INTELLIGENT DATABASE SYSTEM

- A semantic data model is a high-level, conceptual data model that includes semantic information that adds a basic meaning to the data and the relationships that lie between them .
- A semantic data model is designed to capture more of the meaning of an application environment than is possible with contemporary database models, such as relational, hierarchical, or network models.
- A semantic data model is an abstraction that defines how the stored symbols (the instance data) relate to the real world, and how they can be manipulated to infer new information.
- A semantic data model consists of three components: entities, attributes, and relationships.
  - Entities are the objects or concepts that are represented in the data, such as customers, products, or orders. Entities have unique identifiers and can have multiple instances.
  - Attributes are the properties or characteristics of the entities, such as name, age, or price. Attributes can have different data types and can be single-valued or multi-valued.
  - Relationships are the associations or connections between the entities, such as customer orders product, product belongs to category, or category is a subcategory of another category. Relationships can have different cardinalities and can be mandatory or optional.
- A semantic data model can be represented graphically using a semantic data model diagram, which shows the entities, attributes, and relationships using symbols and labels.
  - Entities are represented by rectangles with the entity name inside.
  - Attributes are represented by ovals connected to the entity by a line. The attribute name is written inside the oval. Single-valued attributes have a single line, while multi-valued attributes have a double line. Derived attributes, which are computed from other attributes, have a dashed line.
  - Relationships are represented by diamonds connected to the entities by a line. The relationship name is written inside the diamond. The cardinality of the relationship is indicated by a number or a symbol on the line. For example, 1:1 means one-to-one, 1:N means one-to-many, N:1 means many-to-one, and N:M means many-to-many. The optionality of the relationship is indicated by a circle or a bar on the line. For example, a circle means optional, while a bar means mandatory.
- A semantic data model can be used to express and exchange information that enables interoperability, integration, and reasoning across different data sources and applications .
  - Interoperability means the ability of different systems or components to communicate and exchange data using common standards and protocols.
  - Integration means the process of combining data from different sources into a unified view or representation.
  - Reasoning means the process of inferring new information or knowledge from existing data using logical rules and principles.