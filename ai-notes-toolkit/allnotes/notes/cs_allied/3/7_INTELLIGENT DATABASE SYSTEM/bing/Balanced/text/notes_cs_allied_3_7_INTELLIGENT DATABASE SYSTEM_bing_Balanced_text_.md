

# INTELLIGENT DATABASE SYSTEM

- An intelligent database system is a system that manages information, rather than simple data, and presents it in such a way that is natural and informative for users.
- An intelligent database system goes beyond simple record keeping and has a higher capacity for data quality, data mining, and user interface.
- An intelligent database system consists of three levels of intelligence: high level tools, the user interface, and the database engine.
  - High level tools are responsible for ensuring data quality and automatically discovering relevant patterns in the data with a process called data mining.
  - The user interface is responsible for providing a natural and intuitive way for users to interact with the information and the system.
  - The database engine is responsible for storing, retrieving, and processing the information in an efficient and secure way.
- An intelligent database system can benefit from the use of artificial intelligence (AI) components that can interact with users and provide them with all relevant information.
- An intelligent database system can also benefit from the use of ontologies, which are formal representations of the concepts and relationships in a domain of knowledge.
- An intelligent database system can be applied to various domains and scenarios, such as business intelligence, e-commerce, health care, education, and more.



## Unit 1 - Introduction to IDBS

- IDBS stands for Integrated Database Systems, which is a course that covers the concepts and techniques of designing, implementing, and managing database systems.
- A database is a collection of data that is organized so that it can be easily accessed, managed, and updated.
- A database system is a software system that provides the functionality to create, manipulate, and query databases.
- A database system consists of two main components: the database and the database management system (DBMS).
- The database is the actual data stored in a structured format, such as tables, records, and fields.
- The DBMS is the software that controls the access and manipulation of the database, such as creating, deleting, updating, and querying data.
- The DBMS also provides other features, such as data security, data integrity, data backup and recovery, data concurrency, and data abstraction.
- There are different types of database systems, such as relational, hierarchical, network, object-oriented, and NoSQL databases, each with its own advantages and disadvantages.
- The most widely used type of database system is the relational database system, which organizes data into tables, where each table has a set of columns (attributes) and rows (tuples).
- A relational database system supports a query language called SQL (Structured Query Language), which is a standard and powerful language for manipulating and querying data in tables.
- A relational database system also supports a data model called the relational data model, which defines the structure and constraints of the data in tables, such as primary keys, foreign keys, and referential integrity.
- A relational database system can be further classified into different categories, such as centralized, distributed, parallel, and client-server databases, depending on how the data and the DBMS are distributed and accessed across multiple machines or networks.
- A database system can be used for various applications, such as business, education, health care, e-commerce, social media, and scientific research, where large amounts of data need to be stored, processed, and analyzed efficiently and effectively.



### Informal definition of the domain for the notes of the Unit 1 - Introduction to IDBS in the subject of INTELLIGENT DATABASE SYSTEM

- An **intelligent database system (IDBS)** is a database system that integrates artificial intelligence techniques, such as machine learning, natural language processing, knowledge representation and reasoning, with traditional database management concepts and technologies, such as data models, query languages, transactions, concurrency control, etc.
- The **domain** of an IDBS is the set of possible values that can be stored in the database, as well as the constraints and relationships among them. The domain defines the semantics and validity of the data, and influences the design and implementation of the IDBS.
- An **informal definition** of the domain is a natural language description of the domain, without using any formal notation or syntax. It is useful for communicating the general idea and scope of the domain, but it may not be precise or complete enough for specifying the details and requirements of the IDBS.
- For example, an informal definition of the domain for the notes of the Unit 1 - Introduction to IDBS in the subject of INTELLIGENT DATABASE SYSTEM could be:

  - The domain consists of the notes of the Unit 1, which cover the following topics: definition and motivation of IDBS, comparison of IDBS with conventional and deductive database systems, architecture and components of IDBS, challenges and applications of IDBS, and examples of IDBS.
  - The notes are organized into sections, subsections, and subsubsections, each with a title and a number. The notes also contain text, diagrams, tables, formulas, examples, exercises, and references.
  - The notes can be accessed, searched, modified, and annotated by the students and the instructor of the subject, using a web-based interface or a mobile app. The notes can also be exported to different formats, such as PDF, HTML, or Markdown.
  - The notes are stored in a relational database, with tables for sections, subsections, subsubsections, text, diagrams, tables, formulas, examples, exercises, and references. The tables have attributes for the title, number, content, and metadata of each element. The tables are linked by foreign keys, representing the hierarchical structure and the logical connections of the notes.
  - The notes are enhanced by artificial intelligence techniques, such as natural language processing, machine learning, knowledge representation and reasoning, to provide the following features: automatic summarization, keyword extraction, question answering, feedback generation, plagiarism detection, and personalization.



### General characteristics of IDBSs

- IDBS stands for Intelligent Database Systems, which are full-text databases with artificial intelligence components that interact with users to ensure that users are supplied all relevant information.
- IDBSs manage information (rather than data) in a way that appears natural to users and that goes beyond simple record keeping.
- IDBSs have intelligent database interfaces that are cache-based and designed to efficiently access one or more database management systems, remote or not. They provide a lot of choices and flexible options for conducting queries.
- IDBSs use techniques such as natural language processing, knowledge representation, reasoning, machine learning, and data mining to provide intelligent functionalities such as information retrieval, information extraction, information integration, information analysis, and information synthesis.
- IDBSs can handle complex, uncertain, incomplete, and dynamic information, and can adapt to changing user needs and preferences.



### Data models and the relational data model

- A data model is a way of representing the structure, organization, and relationships of data in a database system.
- Data models help to abstract the data from the physical storage and provide a logical view of the data for the users and applications.
- Data models also define the rules and constraints for data integrity, security, and consistency.
- There are different types of data models, such as hierarchical, network, relational, object-oriented, and dimensional.
- The relational data model is the most widely used data model in database systems.
- The relational data model was proposed by E.F. Codd in 1970.
- The relational data model is based on the concept of mathematical relations, which are sets of tuples (rows) with attributes (columns).
- The relational data model represents data as tables, where each table is a relation with a unique name and a set of attributes.
- The tables are also called relations, and the attributes are also called columns or fields.
- The tuples are also called rows or records, and each tuple has a value for each attribute in the table.
- The values in a table are atomic, meaning they cannot be further divided into smaller parts.
- The order of the tuples and the attributes in a table is irrelevant, meaning they can be arranged in any way without affecting the meaning of the data.
- The tables in a relational data model have relationships with each other, which are defined by using primary keys and foreign keys.
- A primary key is a set of one or more attributes that uniquely identifies each tuple in a table.
- A foreign key is a set of one or more attributes in a table that references the primary key of another table.
- The relationships between tables can be one-to-one, one-to-many, or many-to-many, depending on the cardinality of the primary and foreign keys.
- The relational data model supports the operations of data definition, data manipulation, and data control.
- Data definition operations are used to create, modify, and delete the tables and their attributes, constraints, and indexes.
- Data manipulation operations are used to insert, update, delete, and query the data in the tables.
- Data control operations are used to grant, revoke, and enforce the access rights and privileges for the users and applications on the tables and their data.
- The relational data model is based on the principles of data independence, data integrity, and data consistency.
- Data independence means that the data can be accessed and manipulated without knowing the details of how and where the data is physically stored.
- Data integrity means that the data is accurate, complete, and valid according to the rules and constraints defined in the data model.
- Data consistency means that the data is coherent and synchronized across the tables and the transactions that modify the data.



### A taxonomy of intelligent database systems

- An intelligent database system (IDBS) is a system that integrates database technology with artificial intelligence techniques to provide enhanced functionality and performance.
- A taxonomy of IDBSs can be based on different criteria, such as the origin of the efforts, the level of intelligence, the type of data, the type of reasoning, or the application domain.
- One possible taxonomy of IDBSs is based on the origin of the efforts, which can be either from the database (DB) context or the artificial intelligence (AI) context .
  - Efforts originated in the DB context aim to extend the capabilities of traditional database systems by adding static or dynamic extensions.
    - Static extensions enhance the expressive power of the data model by incorporating concepts such as objects, rules, constraints, or uncertainty.
    - Dynamic extensions introduce some form of reasoning inside the database engine, such as deductive, inductive, or abductive reasoning.
  - Efforts originated in the AI context aim to couple knowledge-based systems and database systems to achieve a better integration of data and knowledge.
    - Basic solutions use a loose coupling between a knowledge base and a database, where the knowledge base accesses the database through a query interface.
    - Advanced solutions use a tight coupling between a knowledge base and a database, where the knowledge base and the database share a common data model and a common query language.
- Another possible taxonomy of IDBSs is based on the level of intelligence, which can be divided into three layers: high level tools, user interface, and database engine.
  - High level tools manage data quality and automatically discover relevant patterns in the data with a process called data mining. This layer often relies on the use of artificial intelligence techniques, such as machine learning, neural networks, or genetic algorithms.
  - User interface provides natural and intuitive ways for users to interact with the system, such as natural language, speech, or graphics. This layer often relies on the use of natural language processing, speech recognition, or computer vision techniques.
  - Database engine implements the core functionality of the system, such as data storage, retrieval, manipulation, and integrity. This layer often relies on the use of logic programming, rule-based systems, or constraint satisfaction techniques.



### Guidelines for using intelligent database systems

- An intelligent database system (IDBS) is a system that manages information, rather than simple data, and presents it in such a way that is natural and informative for users .
- An IDBS can go beyond simple record keeping and provide features such as natural language processing, knowledge representation, reasoning, learning, and adaptation.
- An IDBS can also interface with one or more database management systems (DBMSs), remote or not, and provide flexible options for conducting queries.
- To use an IDBS effectively, one should follow some general guidelines, such as:
  - Define the information needs and goals of the users and the system clearly and precisely.
  - Choose an appropriate IDBS that matches the information needs and goals, and that can handle the complexity and diversity of the data sources and queries.
  - Design and implement a suitable information model and schema for the IDBS, using the tools and methods provided by the IDBS or its underlying DBMSs.
  - Populate the IDBS with relevant and reliable information from various data sources, using the techniques and mechanisms supported by the IDBS or its underlying DBMSs.
  - Test and evaluate the performance and accuracy of the IDBS, using the metrics and criteria defined by the users and the system.
  - Monitor and update the IDBS regularly, using the feedback and learning capabilities of the IDBS or its underlying DBMSs.
  - Provide user-friendly and natural interfaces for the IDBS, using the features and functions offered by the IDBS or its underlying DBMSs.



## Unit 2 - Semantic Data Models

- Semantic data models are conceptual data models that capture the meaning and relationships of data in a domain of interest.
- Semantic data models use high-level concepts, such as entities, attributes, and relationships, to represent data and their semantics.
- Semantic data models can be used to design databases, ontologies, knowledge bases, and other information systems that require a rich and expressive representation of data.
- Semantic data models can also be used to facilitate data integration, interoperability, and reasoning across different data sources and applications.
- Some examples of semantic data models are:

  - Entity-relationship model: A semantic data model that represents data as entities (things or objects) and relationships (associations or links) between them. Entities have attributes (properties or characteristics) that describe them. Relationships have cardinalities (constraints or rules) that specify how many entities can participate in them.
  - Semantic network: A semantic data model that represents data as nodes (concepts or terms) and links (relations or connections) between them. Nodes can have types (categories or classes) and attributes (features or values) that describe them. Links can have roles (functions or meanings) and constraints (conditions or restrictions) that specify how they connect nodes.
  - Ontology: A semantic data model that represents data as classes (sets or collections) and instances (members or elements) of those classes. Classes have properties (attributes or relations) that describe them and their instances. Properties have domains (sources or origins) and ranges (targets or destinations) that specify what classes they apply to and what values they can take. Ontologies can also define axioms (rules or statements) that express logical constraints and inferences on the data.



### Nested and semantic data models

- Nested data models are a way of representing hierarchical data structures, such as trees or graphs, in a relational database. Nested data models use nested sets, nested lists, or nested relations to store the parent-child relationships among the data elements. 
- Semantic data models are a way of describing the meaning and structure of data in a domain, using concepts, attributes, and relationships. Semantic data models use high-level abstractions, such as entities, types, classes, or ontologies, to capture the semantics of the data. 
- Nested and semantic data models are related in the following ways:
  - Both nested and semantic data models aim to overcome the limitations of the traditional relational data model, such as the impedance mismatch, the lack of expressiveness, and the need for complex queries and joins.  
  - Both nested and semantic data models can support complex data types, such as nested data, JSON, XML, or RDF, that are common in modern data sources, such as web, social media, or IoT.  
  - Both nested and semantic data models can benefit from a semantic layer, which is a logical abstraction that provides a consistent and unified view of the data across multiple sources and formats. A semantic layer can simplify data access, integration, analysis, and visualization for the end users.  
- Nested and semantic data models are different in the following ways:
  - Nested data models focus on the representation and storage of hierarchical data structures, while semantic data models focus on the description and understanding of the data meaning and context.  
  - Nested data models are more suitable for applications that require fast and efficient traversal of the data hierarchy, such as navigation, search, or aggregation. Semantic data models are more suitable for applications that require rich and flexible querying and reasoning of the data semantics, such as knowledge discovery, inference, or recommendation.  
  - Nested data models are more dependent on the physical implementation and the database system, while semantic data models are more independent and portable across different platforms and technologies.



### Introduction for the notes of the Unit 2 - Semantic Data Models in the subject of INTELLIGENT DATABASE SYSTEM

- Semantic data models are high-level conceptual models that capture the meaning and structure of data in a domain of interest.
- Semantic data models use concepts such as entities, attributes, relationships, and constraints to represent data and their semantics.
- Semantic data models are more expressive and intuitive than traditional data models, such as relational or hierarchical models, which focus on the physical representation and storage of data.
- Semantic data models can be used for various purposes, such as database design, data integration, data analysis, and knowledge representation.
- Semantic data models can be classified into two main categories: object-based and logic-based models.
- Object-based models use objects as the basic units of data abstraction. Objects have identity, properties, and behavior. Objects can be organized into classes, hierarchies, and networks. Examples of object-based models are Entity-Relationship (ER) model, Object-Oriented (OO) model, and Semantic Network (SN) model.
- Logic-based models use logic as the formalism to define data and their semantics. Logic-based models use predicates, variables, constants, and quantifiers to represent data and rules. Logic-based models can support complex queries, inference, and reasoning. Examples of logic-based models are Functional Data Model (FDM), Deductive Database (DDB), and Ontology.



### The nested relational model

- The nested relational model is an extension of the relational model in which domains may be either atomic or relation-valued .
- This allows a complex object to be represented by a single tuple of a nested relation, which has a one-to-one correspondence between data items and objects.
- A nested relation can be seen as a relation of relations, where each tuple may contain other tuples as attribute values.
- A nested relation schema can be defined recursively as follows:

  - A nested relation schema is either an atomic type or a set of attribute-name/type pairs, where each type is a nested relation schema.
  - A nested relation instance is either an atomic value or a set of tuples, where each tuple is an instance of a nested relation schema.

- For example, consider the following nested relation schema and instance:

  - Schema: `EMPLOYEE(Name, Address, Phone, Projects)`
  - Type of `Name`: `String`
  - Type of `Address`: `String`
  - Type of `Phone`: `String`
  - Type of `Projects`: `PROJECT(Pname, Budget, Members)`
  - Type of `Pname`: `String`
  - Type of `Budget`: `Number`
  - Type of `Members`: `String`
  - Instance:

| Name | Address | Phone | Projects |
| --- | --- | --- | --- |
| Alice | 123 Main St. | 555-1234 | { (P1, 1000, {Bob, Carol}), (P2, 2000, {Dave, Eve}) } |
| Bob | 456 Maple Ave. | 555-2345 | { (P1, 1000, {Alice, Carol}), (P3, 3000, {Frank, Grace}) } |
| Carol | 789 Elm St. | 555-3456 | { (P1, 1000, {Alice, Bob}), (P4, 4000, {Harry, Irene}) } |

- The nested relational model supports various operations to manipulate nested relations, such as:

  - Projection: selecting a subset of attributes from a nested relation.
  - Restriction: selecting a subset of tuples from a nested relation based on a condition.
  - Join: combining two nested relations based on a common attribute.
  - Unnest: flattening a nested relation by removing one level of nesting.
  - Nest: creating a nested relation by grouping tuples based on a common attribute.
  - Aggregate: applying a function to a set of values in a nested relation.

- The nested relational model can be used to model complex and hierarchical data, such as:

  - Documents: a document can be seen as a nested relation of sections, paragraphs, sentences, words, etc.
  - XML: an XML document can be seen as a nested relation of elements, attributes, text, etc.
  - JSON: a JSON object can be seen as a nested relation of key-value pairs, where the values can be nested relations themselves.
  - Graphs: a graph can be seen as a nested relation of nodes, edges, labels, etc.



### Semantic models for the notes of the Unit 2 - Semantic Data Models in the subject of INTELLIGENT DATABASE SYSTEM

- A semantic data model is a method of structuring data in order to represent it in a specific logical way. It is a conceptual data model that includes semantic information that adds a basic meaning to the data and the relationships that lie between them.
- A semantic data model works basically by creating relationships between data when the data is organized. This allows the data to have meaning without human intervention or additional processing. The data is organized into three essential parts—the first data element or object, the relationship, and then the second data element or object.
- A semantic data model provides users with significantly more useful abstractions than the SQL data model and queries. These abstractions are more composable and reusable than queries. A semantic data model also enables efficient data consumption by hiding the complexity and heterogeneity of the underlying data sources.
- There are four primary goals of semantic data models:
  - Data resource planning: The semantic data model can be used in the initial stages of project planning to provide the necessary data resources.
  - Data quality assurance: The semantic data model can help to identify and resolve data quality issues such as inconsistencies, redundancies, and incompleteness.
  - Data integration: The semantic data model can facilitate the integration of data from different sources by providing a common vocabulary and structure.
  - Data analysis and visualization: The semantic data model can support data analysis and visualization by providing meaningful and relevant information to the users.
- Semantic data models can be developed using various techniques and tools, such as:
  - Upper ontologies: These are general and abstract models that capture the common concepts and relationships across domains.
  - Design patterns: These are reusable and modular models that capture the best practices and solutions for specific problems or scenarios.
  - Standard and reference models: These are authoritative and agreed-upon models that define the terms and structures for specific domains or applications.
  - Public models and datasets: These are openly available and widely used models and datasets that provide rich and diverse information for various purposes.
  - Semantic model mining: This is the process of extracting and discovering semantic models from existing data sources using various methods and techniques.



### Hyper-semantic data models

- Hyper-semantic data models are a new class of models that combine the features of semantic data models and artificial intelligence concepts.
- Semantic data models are high-level models that capture the meaning and structure of an application environment using object-oriented concepts such as entities, attributes, relationships, and constraints.
- Artificial intelligence concepts include heuristics, uncertainty, rules, inference, and learning, which can enhance the expressiveness and functionality of data models.
- Hyper-semantic data models aim to facilitate the incorporation of knowledge and reasoning in data modeling, as well as to support complex and dynamic applications that require flexibility and adaptability.
- An example of a hyper-semantic data model is the Knowledge/Data Model (KDM), which extends the Entity-Relationship Model (ERM) with additional constructs such as knowledge entities, knowledge attributes, knowledge relationships, and knowledge constraints.
- The KDM allows the representation of different types of knowledge, such as factual, procedural, declarative, and probabilistic, as well as the specification of inference mechanisms, such as deduction, induction, and abduction.
- The KDM also supports the modeling of uncertainty, using fuzzy sets and possibility theory, and the modeling of heuristics, using production rules and meta-rules.
- The KDM can be used to design and implement intelligent database systems that can perform knowledge-based operations, such as querying, updating, learning, and explaining.



### Object-oriented approaches to semantic data modeling

- Semantic data modeling is a high-level database description and structuring formalism that captures more of the meaning of an application environment than conventional database models.
- Object-oriented modeling is a technique that uses objects as the basic units of data representation and manipulation, where an object is a combination of data and behavior.
- Object-oriented approaches to semantic data modeling aim to reduce the semantic gap between the system and the real world by using terminology that is consistent with the functions that users perform.
- Object-oriented approaches also support data abstraction, inheritance, and encapsulation, which are essential features for modeling complex and dynamic domains.
- Some examples of object-oriented approaches to semantic data modeling are:
  - The Feature Evolution Model (FEM), which represents spatiotemporal geographic data as objects that undergo state-event-state transitions.
  - The Object Data Model (ODM), which integrates the concepts and mechanisms of semantic and behaviorally object-oriented databases.
  - The Object-Oriented Semantic Association Model (OSAM), which extends the Entity-Relationship model with object-oriented concepts such as classes, inheritance, aggregation, and methods.



### Object-oriented database systems

- An object-oriented database (OOD) is a database system that can work with complex data objects — that is, objects that mirror those used in object-oriented programming languages .
- In object-oriented programming (OOP), everything is an object. An object has a unique identity, a state, and a behavior. An object can also have attributes (properties) and methods (functions) that define its characteristics and operations .
- An object-oriented database system (OODS) is a database management system (DBMS) that supports the modelling and creation of data as objects. An OODS allows users to define, store, manipulate, and query objects in a database .
- An OODS differs from a relational database system (RDBS) in several ways. An RDBS is based on the relational model, which organizes data into tables (relations) of rows (tuples) and columns (attributes). An RDBS uses structured query language (SQL) to manipulate data in tables .
- Some of the advantages of an OODS over an RDBS are :
  - An OODS can handle complex data types, such as multimedia, spatial, temporal, and graphical data, that are difficult to represent in tables.
  - An OODS can preserve the integrity and consistency of objects by enforcing encapsulation, inheritance, and polymorphism. Encapsulation means that an object's state and behavior are hidden from other objects. Inheritance means that an object can inherit the attributes and methods of another object. Polymorphism means that an object can behave differently depending on the context.
  - An OODS can improve the performance and scalability of applications by avoiding the impedance mismatch problem. Impedance mismatch is the difference between the object-oriented model and the relational model, which requires mapping objects to tables and vice versa. This mapping can be costly and error-prone.
  - An OODS can support object-oriented features, such as classes, methods, constructors, destructors, overloading, overriding, and exceptions, that are not available in SQL.
- Some of the disadvantages of an OODS over an RDBS are :
  - An OODS is less mature and standardized than an RDBS. There are fewer OODS products and tools available in the market, and they may not interoperate well with each other or with existing RDBS systems.
  - An OODS may have lower query efficiency and optimization than an RDBS. An OODS may not support declarative queries, such as SQL, that can be easily optimized by the DBMS. An OODS may rely on navigational queries, such as object traversal, that can be more complex and time-consuming.
  - An OODS may have lower data independence and security than an RDBS. Data independence means that the logical structure of data is independent of its physical storage and implementation. Data security means that the access and manipulation of data are controlled by the DBMS. An OODS may expose more details of the data objects and their implementation to the users, which can compromise data independence and security.



### Basic concepts of a core object-oriented data model

- A core object-oriented data model is a data model based on object-oriented programming, associating methods (procedures) with objects that can benefit from class hierarchies.
- A core object-oriented data model consists of the following basic object-oriented concepts:
  - Object and object identifier: Any real world entity is uniformly modeled as an object (associated with a unique id: used to pinpoint an object to retrieve).
  - Class and instance: A class is a collection of objects that share the same structure and behavior. An instance is a specific object that belongs to a class.
  - Attribute: An attribute is a property or characteristic of an object that describes its state or value.
  - Method: A method is a function or procedure that defines the behavior or operation of an object.
  - Inheritance: Inheritance is a mechanism that allows a class to inherit the structure and behavior of another class, called the superclass or parent class. The inheriting class is called the subclass or child class.
  - Polymorphism: Polymorphism is the ability of an object to exhibit different behaviors depending on the context or the type of the object. For example, a method can have different implementations in different subclasses of the same superclass.
  - Encapsulation: Encapsulation is the principle of hiding the internal details or implementation of an object from the outside world. Only the interface or the public methods of an object are exposed to other objects or users.
- A core object-oriented data model is based on real world situations. These situations are represented as objects, with different attributes. All these objects have multiple relationships between them.
- A core object-oriented data model can store complex data types, such as audio, video, images, etc., that are not suitable for relational databases.
- A core object-oriented data model employs standardized schemas and formal techniques. This provides a common, consistent, and predictable way of defining and managing data resources across an organization, or even beyond. Ideally, data models are living documents that evolve along with changing business needs.



### Comparison with other data models

- Semantic data models are a type of conceptual data models that aim to capture the meaning and structure of data in a domain.
- Semantic data models differ from other data models, such as relational, hierarchical, network, or object-oriented, in several aspects:
  - Semantic data models support **relationships** as first-class citizens, meaning that they can have properties, constraints, and inheritance. Other data models treat relationships as secondary or derived constructs, such as foreign keys, pointers, or references.
  - Semantic data models support **data abstraction**, meaning that they can define complex data types, such as sets, lists, or records, and hide their implementation details. Other data models rely on primitive data types, such as integers, strings, or booleans, and expose their physical representation.
  - Semantic data models support **inheritance**, meaning that they can define subtypes and supertypes of entities and relationships, and inherit their properties and constraints. Other data models do not have a direct mechanism for modeling generalization and specialization hierarchies.
  - Semantic data models support **constraints**, meaning that they can specify rules and conditions that must hold for the data to be valid and consistent. Other data models either have limited or no support for constraints, or delegate them to external procedures or triggers.
  - Semantic data models support **unstructured objects**, meaning that they can accommodate data that does not have a fixed schema or structure, such as documents, images, or videos. Other data models require data to conform to a predefined schema or structure, or store unstructured data as binary blobs or text.
  - Semantic data models support **dynamic properties**, meaning that they can capture the changes and evolution of data over time, such as history, versions, or states. Other data models assume that data is static or immutable, or handle dynamic properties as separate tables or attributes.



### Query languages and query processing for semantic data models

- A query language is a formal language that allows users to retrieve, manipulate, and analyze data from a database or a data source.
- A query processing is the process of translating a query from a high-level language to a low-level language that can be executed by the database system, and optimizing the query execution plan to minimize the cost and time of the query.
- A semantic data model is a data model that captures the meaning and relationships of the data, rather than the structure and format of the data. Semantic data models are often based on graphs, linked data, or triples, which enable the query to process the actual relationships between information and infer the answers from the network of data.
- Some examples of query languages and query processing for semantic data models are:

  - SPARQL: A standard query language for RDF (Resource Description Framework), a data model that uses triples to represent data as subject-predicate-object statements. SPARQL allows users to query RDF data sources using graph patterns, filters, and optional clauses. SPARQL also supports federated queries, which can combine data from multiple sources. SPARQL query processing involves parsing the query, transforming it into an algebraic expression, applying optimization techniques, and executing the query over the RDF data source .
  - Cypher: A declarative query language for property graphs, a data model that uses nodes, relationships, and properties to represent data as a graph. Cypher allows users to query property graphs using patterns, expressions, and clauses. Cypher also supports graph projections, which can create virtual graphs from existing graphs. Cypher query processing involves parsing the query, transforming it into an abstract syntax tree, applying optimization techniques, and executing the query over the property graph data source.
  - Datalog: A logic programming language for deductive databases, a data model that uses facts and rules to represent data as a set of logical assertions. Datalog allows users to query deductive databases using predicates, variables, and constants. Datalog also supports recursion, which can express complex queries using simple rules. Datalog query processing involves parsing the query, transforming it into a normal form, applying optimization techniques, and executing the query over the deductive database data source.



### Operational aspects of semantic data models

- Semantic data models (SDMs) are conceptual data models that describe the meaning and relationships of data in a domain of interest.
- SDMs aim to capture more of the semantics of an application environment than traditional data models, such as the relational or hierarchical models.
- SDMs use three basic components to represent data: objects, attributes, and relationships.
  - Objects are the entities or concepts that exist in the domain, such as customers, products, or orders.
  - Attributes are the properties or characteristics of objects, such as name, price, or quantity.
  - Relationships are the associations or connections between objects, such as customer has order, order contains product, or product belongs to category.
- SDMs can be represented graphically using diagrams that show the objects, attributes, and relationships in a domain, as well as the constraints and rules that govern them.
- SDMs can also be represented formally using languages or notations that specify the syntax and semantics of the model, such as the Entity-Relationship (ER) model, the Unified Modeling Language (UML), or the Resource Description Framework (RDF).
- SDMs can be used for various purposes, such as:
  - Data resource planning: SDMs can help identify and organize the data resources needed for a project or an organization, and provide a common vocabulary and understanding of the data among stakeholders.
  - Data analysis and design: SDMs can help analyze the data requirements and design the data structures and schemas for a database or a data warehouse, and ensure the data quality and integrity.
  - Data integration and interoperability: SDMs can help map and align the data from different sources and systems, and enable the data exchange and sharing among them.
  - Data querying and reasoning: SDMs can help formulate and execute queries and inferences over the data, and provide answers and insights to the users.



### Systems for the notes of the Unit 2 - Semantic Data Models in the subject of INTELLIGENT DATABASE SYSTEM

- A semantic data model is a high-level, conceptual data model that includes semantic information that adds a basic meaning to the data and the relationships that lie between them .
- A semantic data model is designed to capture more of the meaning of an application environment than is possible with contemporary database models.
- A semantic data model is an abstraction that defines how the stored symbols (the instance data) relate to the real world.
- A semantic data model can be used to express and exchange information that enables interoperability, integration, and reasoning.
- A semantic data model consists of three main components:
  - Classification: This classifies different objects in objective reality by using “instance of” relations, such as “John is an instance of a person” or “Paris is an instance of a city”.
  - Aggregation: Aggregation defines a new object from a set of objects that become its components using “has a” relations, such as “A car has a wheel” or “A book has a title”.
  - Generalization: Generalization defines a new object from a set of objects that share some common properties using “is a” relations, such as “A dog is a mammal” or “A triangle is a polygon”.
- A semantic data model can be represented using various graphical notations, such as entity-relationship diagrams, object-role modeling, or unified modeling language .
- A semantic data model can be mapped to a logical data model, such as hierarchical, network, or relational, that is implemented by a database management system.
- A semantic data model can provide benefits such as:
  - Improved data quality and consistency
  - Enhanced data analysis and discovery
  - Increased data reuse and sharing
  - Reduced data redundancy and complexity
  - Facilitated data integration and interoperability



### The ODMG standard for the notes of the Unit 2 - Semantic Data Models in the subject of INTELLIGENT DATABASE SYSTEM

- The ODMG standard is a set of specifications for object-oriented databases, developed by the Object Data Management Group (ODMG) from 1991 to 2001 .
- The ODMG standard consists of four components: the object model, the object definition language (ODL), the object query language (OQL), and the object manipulation language (OML) .
- The object model defines the basic concepts and constructs for representing data as objects, such as classes, attributes, methods, inheritance, polymorphism, encapsulation, and relationships .
- The object definition language (ODL) is a textual notation for specifying the schema of an object-oriented database, using the object model concepts .
- The object query language (OQL) is a declarative language for querying and manipulating data in an object-oriented database, using a syntax similar to SQL .
- The object manipulation language (OML) is a set of bindings for various programming languages, such as C++, Java, and Smalltalk, to access and manipulate data in an object-oriented database, using ODL and OQL .
- The ODMG standard aims to provide a common and portable way for programmers to use object-oriented databases, regardless of the underlying implementation or vendor .
- Semantic data models (SDMs) are high-level data models that capture the meaning and structure of an application domain, using concepts such as entities, attributes, relationships, and constraints.
- Semantic data models are often used as conceptual models for designing databases, as they provide a clear and intuitive representation of the real-world entities and their interrelationships.
- Semantic data models can be mapped to various logical and physical data models, such as relational, hierarchical, network, or object-oriented, depending on the requirements and capabilities of the database system.
- The ODMG standard can be seen as a semantic data model, as it uses object-oriented concepts to describe the data and its semantics, and supports complex and rich data types, such as collections, references, and user-defined types .
- The ODMG standard also supports various integrity constraints, such as uniqueness, cardinality, and referential integrity, to ensure the validity and consistency of the data .
- The ODMG standard can be compared and contrasted with other semantic data models, such as the entity-relationship model, the functional data model, and the semantic network model, based on their similarities and differences in terms of data representation, abstraction, and manipulation.



### The object-relational data model

- The object-relational data model is a hybrid of the object-oriented and the relational data models, which combines the features of both paradigms .
- The object-relational data model supports objects, classes, inheritance, methods, and polymorphism, as well as data types, tables, keys, constraints, and queries, like the relational data model .
- The object-relational data model allows the definition of complex data types, such as arrays, sets, lists, tuples, and user-defined types, which can be stored as attributes of objects or columns of tables .
- The object-relational data model also allows the definition of operations or functions that can be applied to the complex data types, such as aggregation, filtering, sorting, and transformation .
- The object-relational data model enables the inheritance of objects and tables, which means that new objects or tables can be created by extending the attributes and methods of existing ones .
- The object-relational data model supports the concept of references, which are pointers or links that can connect objects or tables across different schemas or databases .
- The object-relational data model provides a query language that can manipulate both the object-oriented and the relational aspects of the data, such as SQL or OQL  .

: Introduction to Object Relational Data Model - ProgramsBuzz
: Object-relational Data Model - tutorialspoint.com
: Object–relational database - Wikipedia



### Java and databases for the notes of the Unit 2 - Semantic Data Models in the subject of INTELLIGENT DATABASE SYSTEM

- Semantic data model (SDM) is a high-level semantics-based database description and structuring formalism (database model) for databases.
- This database model is designed to capture more of the meaning of an application environment than is possible with contemporary database models.
- A semantic data model works basically by creating relationships between data when the data is organized. This allows the data to have meaning without human intervention or additional processing.
- The data is organized into three essential parts—the first data element or object, the relationship, and then the second data element or object.
- A semantic model acts like a translation layer between your application and your underlying data structures. You can use this metrics-oriented data layer that the semantic model exposes directly with APIs, with embedded visualizations, or from other analytics tools to support your enterprise's advanced analytics applications.
- The semantic model helps data management manage and oversee the company's overall data, thus increasing decision-making capabilities.
- There are four primary goals of SDMs:
  - Data resource planning: The SDM can be used in the initial stages of project planning to provide the necessary data resources.
  - Data integration: The SDM can be used to integrate data from different sources and formats, such as relational, XML, JSON, etc.
  - Data quality: The SDM can be used to ensure the consistency, accuracy, and completeness of the data.
  - Data governance: The SDM can be used to define the rules, policies, and standards for the data, such as security, privacy, compliance, etc.
- Java is a popular programming language that can be used to create applications that interact with databases using various APIs and frameworks, such as JDBC, JPA, Hibernate, Spring Data, etc.
- Java can also be used to create semantic web applications that use RDF, OWL, SPARQL, and other standards to represent and query data in a semantic way.
- A semantic database engine can address some of the drawbacks of traditional relational databases, such as:
  - Automating SQL query generation: Hides the hierarchy and table joins.
  - Automating SQL inserts: Managing all the necessary FK ID’s.
  - Improving Performance: Caching queries so the engine doesn’t have to re-create the SQL statement every time.



### Conclusions for the notes of the Unit 2 - Semantic Data Models in the subject of INTELLIGENT DATABASE SYSTEM

- Semantic data models are conceptual data models that capture the meaning and relationships of data in a domain of interest.
- Semantic data models use high-level constructs such as entities, attributes, relationships, constraints, and rules to represent data and its semantics.
- Semantic data models can be classified into three categories: entity-relationship models, functional models, and object-oriented models.
- Entity-relationship models are based on the notion of entities and relationships among them. Entities are objects or concepts that can be identified and distinguished in the domain. Relationships are associations or links between entities that express some semantic meaning or dependency.
- Functional models are based on the notion of functions and arguments. Functions are operations or transformations that map arguments (input values) to results (output values). Arguments and results can be atomic values, sets, or other functions. Functional models use functions to represent both data and behavior of the domain.
- Object-oriented models are based on the notion of objects and classes. Objects are instances of classes that encapsulate data and behavior. Classes are abstractions or generalizations of objects that define their common properties and methods. Object-oriented models use inheritance, polymorphism, and encapsulation to support reusability, extensibility, and modularity of data and behavior.
- Semantic data models have several advantages over traditional data models, such as:
  - They provide a natural and intuitive way of modeling data that is closer to the user's perception and understanding of the domain.
  - They capture the semantics and constraints of the domain explicitly and declaratively, which can facilitate data validation, integrity, and consistency.
  - They support complex and rich data types, such as collections, nested structures, multimedia, and spatial data, which can enhance the expressiveness and functionality of the data model.
  - They enable the integration and interoperability of heterogeneous data sources, by providing a common conceptual schema that can map different data models and formats.
  - They facilitate the development of intelligent applications, such as knowledge-based systems, expert systems, and decision support systems, by providing a logical and declarative representation of data and its semantics.



### Active database systems

- An active database system is a database system that includes an **event-driven architecture** (often in the form of **ECA rules**) which can respond automatically to conditions both inside and outside the database .
- ECA rules are composed of three components: **event**, **condition**, and **action**. An event is a change in the state of the database or the environment, such as an update, a timer, or a message. A condition is a predicate that evaluates to true or false based on the event and the current state of the database. An action is a sequence of operations that are executed when the event occurs and the condition is true .
- Active database systems can be used for various purposes, such as **security monitoring**, **alerting**, **statistics gathering**, and **authorization** . For example, an active database system can monitor the transactions of a bank account and alert the owner if there is a suspicious activity, or it can enforce access control policies based on the user's role and the data's sensitivity .
- Active database systems are different from **passive database systems**, which only store and manipulate data based on user queries, and do not initiate any actions on their own . Active database systems are also different from **reactive database systems**, which can react to external events but do not have a condition component in their rules .
- Active database systems are challenging to design, implement, and maintain, because of the complexity and unpredictability of the interactions among the rules, the data, and the environment . Some of the issues that need to be addressed are: **rule specification**, **rule execution**, **rule analysis**, **rule optimization**, and **rule management** .



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



### Issues for the notes of the Unit 2 - Semantic Data Models in the subject of INTELLIGENT DATABASE SYSTEM

- Semantic data models are high-level conceptual data models that include semantic information to describe the meaning and relationships of data.
- Semantic data models can be used to capture more of the application domain semantics than traditional data models, such as hierarchical, network, or relational.
- Semantic data models can also facilitate data integration, interoperability, and exchange by providing a common understanding of the data across different systems and applications.
- Some of the issues that semantic data models need to address are:

  - How to represent different types of objects and their properties, such as entities, attributes, values, classes, subclasses, etc.
  - How to represent different types of relationships and their properties, such as associations, aggregations, generalizations, specializations, etc.
  - How to represent different types of constraints and rules that govern the data, such as cardinality, participation, inheritance, etc.
  - How to represent different types of operations and functions that manipulate the data, such as queries, updates, transactions, etc.
  - How to represent different types of views and perspectives that access the data, such as schemas, sub-schemas, mappings, etc.
  - How to ensure the consistency, validity, and integrity of the data and the model, such as normalization, verification, validation, etc.
  - How to ensure the efficiency, performance, and scalability of the data and the model, such as indexing, partitioning, caching, etc.
  - How to ensure the security, privacy, and confidentiality of the data and the model, such as encryption, authentication, authorization, etc.

- Some of the examples of semantic data models are:

  - Entity-relationship model: A semantic data model that represents data as entities and relationships, and uses diagrams to visualize the data structure.
  - Object-oriented model: A semantic data model that represents data as objects and classes, and uses inheritance, polymorphism, and encapsulation to model the data behavior.
  - Semantic network model: A semantic data model that represents data as nodes and links, and uses semantic nets, frames, and scripts to model the data meaning.
  - Ontology model: A semantic data model that represents data as concepts and relations, and uses logic, inference, and reasoning to model the data knowledge.



### Architectures for Semantic Data Models

- Semantic data models are high-level conceptual models that capture the meaning and relationships of data in an application domain.
- Semantic data models are based on the principles of abstraction, classification, aggregation, and generalization.
- Semantic data models can be classified into three main types: entity-relationship models, functional models, and object-oriented models.

#### Entity-Relationship Models

- Entity-relationship models represent data as entities (objects or concepts) and relationships (associations or links) between them.
- Entities have attributes (properties or characteristics) that describe them, and relationships have cardinalities (constraints or rules) that specify how many entities can participate in them.
- Entity-relationship models can be represented graphically using diagrams, where entities are shown as rectangles, relationships are shown as diamonds, and attributes are shown as ovals.
- Entity-relationship models can be used to design relational databases, where entities are mapped to tables, relationships are mapped to foreign keys, and attributes are mapped to columns.

#### Functional Models

- Functional models represent data as functions (operations or transformations) and arguments (inputs or outputs) of those functions.
- Functions have domains (sets of possible arguments) and ranges (sets of possible values) that define their behavior, and arguments have types (categories or classes) that define their structure.
- Functional models can be represented graphically using diagrams, where functions are shown as circles, arguments are shown as arrows, and types are shown as labels.
- Functional models can be used to design functional programming languages, where functions are first-class values, arguments are immutable, and types are inferred.

#### Object-Oriented Models

- Object-oriented models represent data as objects (instances or examples) and classes (templates or prototypes) of those objects.
- Objects have state (values or data) and behavior (methods or functions) that define their identity, and classes have attributes (variables or fields) and operations (procedures or methods) that define their structure.
- Object-oriented models can be represented graphically using diagrams, where objects are shown as icons, classes are shown as boxes, and inheritance (specialization or generalization) is shown as lines.
- Object-oriented models can be used to design object-oriented programming languages, where objects are encapsulated, classes are polymorphic, and inheritance is dynamic.

: Semantic data model - Wikipedia



### Research relational prototypes—the Starburst Rule System

- The Starburst Rule System is an active database rules facility integrated into the Starburst extensible relational database system at the IBM Almaden Research Center  .
- The Starburst Rule System is based on arbitrary database state transitions rather than tuple- or statement-level changes, yielding a clear and flexible execution semantics  .
- The Starburst Rule System supports set-oriented production rules, which are triggered by a set of tuples that satisfy a condition and execute an action on the entire set .
- The Starburst Rule System is implemented as an extension to the Starburst query processor, using its extensibility features such as user-defined functions, access methods, and rewrite rules .
- The Starburst Rule System provides a declarative and efficient way of expressing complex database operations, such as integrity constraints, derived data, triggers, alerts, and workflows  .



### Commercial relational approaches for the notes of the Unit 2 - Semantic Data Models in the subject of INTELLIGENT DATABASE SYSTEM

- A relational data model is a data model that represents data as a collection of tables or relations, where each table consists of a set of rows and columns.
- A semantic data model is a data model that captures the meaning and relationships of the data in a more natural and intuitive way, using concepts such as objects, attributes, and associations.
- A commercial relational approach is a way of implementing a semantic data model using a relational database system, such as Oracle, SQL Server, or MySQL.
- Some of the advantages of a commercial relational approach are:
  - It leverages the existing and mature technology of relational databases, which are widely used and supported in the industry.
  - It allows for efficient and flexible querying and manipulation of data using SQL, a standard and powerful query language.
  - It supports data integrity and security through mechanisms such as primary keys, foreign keys, constraints, triggers, and views.
  - It enables data integration and interoperability with other systems and applications that use relational databases or SQL.
- Some of the challenges of a commercial relational approach are:
  - It may require complex and redundant data structures to represent the semantic data model, such as join tables, surrogate keys, and null values.
  - It may lose some of the semantic information and expressiveness of the data model, such as inheritance, aggregation, and generalization.
  - It may introduce performance and scalability issues due to the increased number of tables and joins, especially for large and complex data sets.
  - It may require additional tools and techniques to maintain and evolve the data model, such as data dictionaries, schema mapping, and data migration.



## Unit 3 - Knowledge-Based Systems - AI Context

- A knowledge-based system (KBS) is a form of artificial intelligence (AI) that aims to capture the knowledge of human experts to support decision-making  .
- A KBS stores knowledge in the form of rules, facts, concepts, or other representations, which are then used to generate solutions to specific problems .
- A KBS consists of two main components: a knowledge base and an inference engine  .
  - A knowledge base is a collection of knowledge that is relevant to a specific problem domain, such as medicine, law, engineering, etc.
  - An inference engine is a software program that applies logical rules and reasoning methods to the knowledge base to derive new knowledge or conclusions.
- A KBS can have different types and uses, depending on the nature and complexity of the problem domain and the knowledge representation .
  - Examples of types of KBS are expert systems, case-based reasoning systems, fuzzy logic systems, neural network systems, etc.
  - Examples of uses of KBS are diagnosis, planning, scheduling, design, configuration, tutoring, etc.
- A KBS can have various advantages and disadvantages, depending on the quality and quantity of the knowledge, the efficiency and accuracy of the inference engine, and the usability and reliability of the system .
  - Advantages of KBS are that they can provide consistent, fast, and scalable solutions, that they can preserve and transfer human expertise, that they can explain their reasoning and justify their decisions, and that they can learn from new data and feedback.
  - Disadvantages of KBS are that they can be costly and time-consuming to develop and maintain, that they can be limited by the availability and validity of the knowledge, that they can be prone to errors and biases, and that they can face ethical and social issues.



### Characteristics and classification of the knowledge-based systems

A knowledge-based system (KBS) is a computer program that reasons and uses a knowledge base to solve complex problems. The term is broad and refers to many different kinds of systems. The one common theme that unites all knowledge based systems is an attempt to represent knowledge explicitly and a reasoning system that allows it to derive new knowledge from the existing one.

Some of the characteristics of knowledge-based systems are:

- They are domain-specific, meaning they focus on a particular area of expertise or problem-solving.
- They are interactive, meaning they can communicate with users or other systems through natural language or graphical interfaces.
- They are adaptive, meaning they can learn from new data or feedback and modify their behavior accordingly.
- They are explanatory, meaning they can provide justification or evidence for their conclusions or recommendations.

Some of the classification of knowledge-based systems are:

- Case-based systems: These systems use case-based reasoning, which involves reviewing past knowledge of similar situations and applying it to new ones. They can also store and retrieve cases for future use.
- Expert systems: These systems use rule-based reasoning, which involves applying a set of rules or heuristics to infer new facts or actions from the given facts. They can also use backward chaining or forward chaining to reach a goal or a solution.
- Hypertext manipulation systems: These systems use hypertext, which is a way of organizing and linking information in a non-linear and dynamic way. They can also use hypermedia, which is a combination of text, graphics, audio, video, and other media.
- Intelligent tutoring systems: These systems use artificial intelligence techniques to provide personalized and adaptive instruction to learners. They can also monitor and assess the learner's progress and provide feedback and guidance.
- Rule-based systems: These systems use a set of rules or conditions to perform actions or make decisions. They can also use inference engines, which are programs that apply the rules to the facts in the knowledge base.



### Introduction for the notes of the Unit 3 - Knowledge-Based Systems- AI Context in the subject of INTELLIGENT DATABASE SYSTEM

- A knowledge-based system (KBS) is a computer system that uses artificial intelligence (AI) techniques to solve problems that normally require human expertise.
- A KBS consists of two main components: a knowledge base and an inference engine.
- A knowledge base is a collection of facts, rules, and heuristics that represent the domain knowledge of a specific problem area.
- An inference engine is a software module that applies logical reasoning to the knowledge base to derive new information or conclusions.
- A KBS can also have other components, such as a user interface, a knowledge acquisition module, a knowledge representation language, and a knowledge validation module.
- A KBS can be classified into different types based on the nature of the knowledge, the reasoning method, and the application domain.
- Some examples of KBS types are expert systems, case-based reasoning systems, rule-based systems, fuzzy systems, neural networks, genetic algorithms, and hybrid systems.
- A KBS can provide various benefits, such as improving decision making, enhancing productivity, reducing errors, saving costs, and facilitating learning and training.
- A KBS can also face various challenges, such as acquiring and maintaining knowledge, dealing with uncertainty and inconsistency, ensuring reliability and validity, and coping with ethical and social issues.



### The resolution principle

- The resolution principle is a general rule of inference that can be used to derive new conclusions from a set of premises .
- It is based on the idea of resolving two clauses that contain complementary literals, i.e., a literal and its negation, into a new clause that contains the remaining literals .
- For example, if we have the clauses `p v q` and `¬p v r`, we can resolve them on `p` and obtain the new clause `q v r`.
- The resolution principle can be applied to propositional logic and predicate logic, with some modifications .
- In propositional logic, the resolution principle can be used to perform automated theorem proving by converting all the sentences and the negated conclusion to conjunctive normal form (CNF) and then applying the resolution rule repeatedly until either a contradiction (the empty clause) is derived or no more clauses can be added .
- In predicate logic, the resolution principle requires the use of unification, a process of finding a substitution for the variables in the clauses that makes them identical .
- For example, if we have the clauses `P(x) v Q(y)` and `¬Q(a) v R(z)`, we can unify them on `Q` by substituting `y` with `a` and obtain the new clause `P(x) v R(z)`.
- The resolution principle is the basis of logic programming and production rules paradigms in artificial intelligence.



### Inference by inheritance for the notes of the Unit 3 - Knowledge-Based Systems- AI Context in the subject of INTELLIGENT DATABASE SYSTEM

- Inference is the process of generating conclusions from evidence and facts using logic and reasoning.
- Inference by inheritance is a type of inference that uses hierarchical relationships between concepts to derive new information from existing knowledge.
- Inference by inheritance is based on the principle of **generalization** and **specialization**, which means that a subclass inherits the properties and attributes of its superclass, and a superclass can be generalized from its subclasses.
- Inference by inheritance can be applied to knowledge-based systems, which are systems that use a knowledge base of facts and rules to solve problems and answer queries.
- Inference by inheritance can help knowledge-based systems to:
  - **Reduce redundancy** by avoiding the repetition of common facts and rules for different subclasses.
  - **Increase consistency** by ensuring that the subclasses follow the same logic and constraints as their superclass.
  - **Enhance flexibility** by allowing the addition or modification of subclasses without affecting the superclass or other subclasses.
  - **Improve efficiency** by reducing the search space and the number of inference steps required to reach a conclusion.
- Inference by inheritance can be implemented using different methods, such as:
  - **Frame-based systems**, which use frames as data structures to represent concepts and their attributes, and use inheritance links to connect frames in a hierarchy.
  - **Semantic networks**, which use nodes to represent concepts and their instances, and use arcs to represent relationships and properties, and use inheritance paths to propagate information along the network.
  - **Description logics**, which use formal languages to define concepts and their properties, and use logical operators and axioms to infer new information from existing knowledge.
- Inference by inheritance can also be combined with other types of inference, such as:
  - **Deductive inference**, which uses rules and facts to derive conclusions that are logically valid and certain.
  - **Inductive inference**, which uses examples and patterns to derive generalizations and hypotheses that are probable and uncertain.
  - **Abductive inference**, which uses observations and background knowledge to derive explanations and causes that are plausible and consistent.



### Conclusion for the notes of the Unit 3 - Knowledge-Based Systems- AI Context in the subject of INTELLIGENT DATABASE SYSTEM

- Knowledge-based systems (KBS) are computer systems that use artificial intelligence techniques to solve complex problems that normally require human expertise.
- KBS consist of two main components: a knowledge base and an inference engine. The knowledge base stores the domain knowledge in a structured and declarative form, such as rules, facts, frames, or ontologies. The inference engine applies logical reasoning and search methods to the knowledge base to derive new knowledge or solutions.
- KBS can be classified into different types based on the nature of the knowledge, the reasoning method, or the application domain. Some common types of KBS are expert systems, case-based reasoning systems, rule-based systems, fuzzy systems, neural networks, genetic algorithms, and hybrid systems.
- KBS can be developed using various tools and methodologies, such as knowledge acquisition, knowledge representation, knowledge validation, knowledge maintenance, and knowledge sharing. Some examples of KBS development tools are Prolog, CLIPS, KEE, Protégé, and Rete.
- KBS can be applied to various domains and tasks, such as diagnosis, planning, scheduling, design, configuration, decision support, education, and natural language processing. Some examples of KBS applications are MYCIN, DENDRAL, R1/XCON, CYC, and Watson.
- KBS face some challenges and limitations, such as knowledge elicitation, knowledge verification, knowledge consistency, knowledge completeness, knowledge scalability, knowledge security, knowledge explanation, and knowledge evolution. Some possible solutions or directions for overcoming these challenges are knowledge engineering, knowledge integration, knowledge discovery, knowledge reuse, knowledge visualization, and knowledge learning.



### Deductive Database Systems

- A deductive database is a database system that can make deductions (i.e. conclude additional facts) based on rules and facts stored in the (deductive) database.
- Deductive databases offer elegant and powerful ways of managing complex data in a declarative way, especially for information that is derived by use of recursion.
- Deductive systems typically provide a declarative query language such as a logic programming language (e.g., Prolog) that allows users to specify what they want to know, rather than how to compute it.
- Deductive database systems can be seen as bringing together mainstream data models with logic programming languages for querying and analyzing database data.
- Deductive databases have many applications in areas such as artificial intelligence, knowledge representation, natural language processing, data mining, and semantic web.
- Some examples of commercial deductive database systems are Oracle, IBM DB2, and Microsoft SQL Server.



### Basic concepts for the notes of the Unit 3 - Knowledge-Based Systems- AI Context in the subject of INTELLIGENT DATABASE SYSTEM

- A knowledge-based system (KBS) is a computer program that uses artificial intelligence techniques to store and retrieve knowledge .
- The system is designed to solve complex problems by applying knowledge to a specific problem domain .
- The system stores knowledge in the form of rules, which are then used to generate solutions to specific problems.
- The system has two distinguishing features: a knowledge base and an inference engine.
- A knowledge base is an established collection of information and resources, such as facts, rules, ontologies, and data .
- An inference engine is the backend component of a KBS that applies logic rules (as assertions and conditions) to the knowledge base to derive new knowledge and solutions .
- A user interface is the user-facing component that allows the user to interact with the system, such as by posing queries, providing feedback, or receiving explanations.
- A KBS can have different types, such as rule-based systems, case-based systems, expert systems, or hybrid systems, depending on the nature and representation of the knowledge and the reasoning methods.
- A KBS can have different uses, such as diagnosis, planning, scheduling, design, configuration, or decision support, depending on the problem domain and the user needs .



### DATALOG language

- Datalog is a **declarative logic programming language** that is based on **function-free Horn clauses** .
- Datalog is often used as a **query language for deductive databases** , which are databases that can derive new facts from existing facts using logical rules.
- Datalog is syntactically a **subset of Prolog**, but it differs from Prolog in its **evaluation model** and **properties** .
- Datalog uses a **bottom-up evaluation model** , which means that it starts from the facts in the database and applies the rules to derive new facts until no more facts can be derived.
- Datalog has the property of **stratified negation**, which means that it can handle negated predicates in a consistent and efficient way by dividing the rules into different levels or strata.
- Datalog has the property of **finite domain**, which means that it can only deal with a finite number of constants and variables in the database and the queries.
- Datalog has the property of **decidability**, which means that it can always determine whether a query is true or false in a finite amount of time.
- Datalog has the property of **expressiveness**, which means that it can express complex queries and computations using a concise and elegant syntax.
- Datalog has found new applications in various domains such as **data integration, information extraction, networking, program analysis, security, cloud computing and machine learning**.



### Deductive database systems and logic programming systems—differences

- Deductive database systems are systems that combine relational databases with logic programming to support a powerful and declarative formalism for managing complex data.
- Logic programming systems are systems that use a subset of logic to express programs as a set of rules and facts that can be queried and reasoned about.
- Some of the main differences between deductive database systems and logic programming systems are:

  - Order sensitivity and procedurality: In logic programming systems, such as Prolog, the order of rules and facts in the program and the order of parts of rules can affect the program execution and efficiency. In deductive database systems, such as Datalog, the order of rules and facts is irrelevant and the system can optimize the evaluation of queries.
  - Special predicates: In logic programming systems, programmers can use special predicates, such as cut, fail, assert, retract, etc., to control the execution flow and modify the program dynamically. In deductive database systems, these predicates are either not allowed or have a different semantics, as they violate the declarative and logical nature of the system.
  - Negation: In logic programming systems, negation is usually implemented by negation as failure, which means that a goal is considered false if it cannot be proven true. This can lead to incomplete or incorrect results in some cases. In deductive database systems, negation is usually implemented by stratified negation, which means that a goal is considered false if it can be proven false by using only positive information. This ensures that the system is sound and complete.
  - Recursion: In logic programming systems, recursion is a powerful and expressive feature that allows defining rules that refer to themselves or to other rules that depend on them. Recursion can be used to express complex computations and relations. In deductive database systems, recursion is also supported, but it has to be stratified, which means that there is a clear ordering of rules and predicates that avoids circular dependencies and ensures termination.



### Architectural approaches for the notes of the Unit 3 - Knowledge-Based Systems- AI Context in the subject of INTELLIGENT DATABASE SYSTEM

- A knowledge-based system (KBS) is a computer system that uses artificial intelligence techniques to solve problems that normally require human expertise .
- The typical architecture of a KBS consists of two main components: a knowledge base and an inference engine .
- The knowledge base contains a collection of facts, rules, heuristics, and other forms of knowledge in a given domain, such as medical diagnosis, engineering design, or legal reasoning .
- The inference engine is a software module that applies logical rules and reasoning methods to the knowledge base to derive new information, conclusions, or recommendations .
- There are different types of KBS, depending on the nature of the knowledge, the inference methods, and the application domain. Some examples are:
  - Expert systems: KBS that emulate the reasoning and decision-making of human experts in a specific field . They often use rule-based or case-based reasoning to solve problems or provide advice.
  - Knowledge representation and reasoning systems: KBS that focus on the formalization and manipulation of knowledge using logic, ontologies, and other symbolic methods . They often use deductive, inductive, or abductive reasoning to infer new knowledge or answer queries.
  - Knowledge discovery and data mining systems: KBS that extract useful patterns, trends, or insights from large and complex data sets using statistical, machine learning, or other methods . They often use classification, clustering, association, or regression techniques to discover knowledge or make predictions.
  - Knowledge management systems: KBS that facilitate the creation, storage, retrieval, and sharing of knowledge among individuals or organizations . They often use databases, document management systems, collaborative tools, or semantic web technologies to support knowledge management processes.
- The architectural knowledge systems approach is a specific type of KBS that aims to understand and preserve the traditional knowledge systems of architecture and cultural heritage. It is based on the premise that problems with our heritage today can be solved if we understand the underlying principles, values, and practices of the past.
- The architectural knowledge systems approach uses various methods and tools to capture, represent, analyze, and reuse the knowledge embedded in the architectural forms, structures, and processes of different cultures and regions. Some examples are:
  - Geometric knowledge-based systems: KBS that use geometric models and algorithms to represent and manipulate the spatial and structural aspects of architectural forms and images . They often use shape grammars, graph grammars, or other formal methods to generate, classify, or transform architectural designs or patterns .
  - Semantic knowledge-based systems: KBS that use ontologies, vocabularies, and annotations to represent and reason about the meaning and context of architectural concepts and elements . They often use semantic web technologies, natural language processing, or other methods to extract, query, or integrate architectural knowledge from various sources .
  - Historical knowledge-based systems: KBS that use temporal models and methods to represent and analyze the evolution and variation of architectural styles and traditions over time and space . They often use chronologies, timelines, maps, or other tools to visualize, compare, or trace the historical development and influence of architectural movements or cultures .



### Research prototypes for the notes of the Unit 3 - Knowledge-Based Systems- AI Context in the subject of INTELLIGENT DATABASE SYSTEM

- A research prototype is a preliminary version of a system that is used to test and evaluate its feasibility, functionality, performance, and usability in a specific domain or problem.
- A research prototype can be used to demonstrate the potential of a new approach, technique, or technology, or to explore the design space and user needs of a system.
- A research prototype can also be used to collect feedback and data from users, experts, or stakeholders, and to refine and improve the system based on the findings.
- A knowledge-based system (KBS) is a system that uses artificial intelligence techniques to represent and manipulate knowledge, such as facts, rules, heuristics, and models, in order to solve complex problems that require human expertise.
- A knowledge-based system consists of two main components: a knowledge base, which stores the domain-specific knowledge, and an inference engine, which applies logical reasoning and problem-solving methods to the knowledge base.
- A knowledge-based system can be classified into different types, such as expert systems, case-based reasoning systems, knowledge-based databases, and knowledge-based simulation systems, depending on the nature and structure of the knowledge and the inference methods used.
- A research prototype for a knowledge-based system aims to demonstrate the feasibility and effectiveness of using knowledge representation and reasoning techniques to solve a specific problem or task in a given domain.
- A research prototype for a knowledge-based system can also be used to evaluate the quality and completeness of the knowledge base, the efficiency and accuracy of the inference engine, and the usability and usefulness of the system for the intended users or applications.
- Some examples of research prototypes for knowledge-based systems are:

  - A prototype knowledge-based simulation support system, which was developed to support a senior level course in industrial engineering and to study the feasibility of an expert simulation support system .
  - A prototype knowledge-based system for fingerprint image classification, which used geometric knowledge representation and reasoning techniques to classify fingerprint images into different categories.
  - A prototype knowledge-based system for music composition, which used a rule-based approach to generate musical pieces based on the user's preferences and constraints.



### Updates in deductive databases for the notes of the Unit 3 - Knowledge-Based Systems- AI Context in the subject of INTELLIGENT DATABASE SYSTEM

- A deductive database is a database system that can make deductions (i.e. conclude additional facts) based on rules and facts stored in the (deductive) database.
- Deductive databases offer elegant and powerful ways of managing complex data in a declarative way, especially for information that is derived by use of recursion.
- Deductive systems typically provide a declarative query language such as a logic programming language (e.g., Prolog) or a variant of it (e.g., Datalog).
- Some of the updates in deductive databases are:

  - The development of efficient and scalable algorithms for evaluating recursive queries and rules, such as semi-naive evaluation, magic sets, and tabling.
  - The integration of deductive databases with other paradigms, such as object-oriented, relational, and XML databases, to support heterogeneous and complex data types.
  - The application of deductive databases to various domains, such as data integration, data mining, knowledge representation, and semantic web.
  - The extension of deductive databases with features such as negation, aggregates, constraints, and probabilistic reasoning, to enhance their expressiveness and functionality.
  - The design of deductive database systems that can handle dynamic and uncertain data, such as data streams, temporal data, and probabilistic data.



### Integration of deductive database and object database technologies

- Deductive databases are databases that use logic programming and rules to support declarative queries and inferences over data. They can express complex queries and constraints in a concise and natural way. 
- Object databases are databases that use object-oriented concepts and techniques to model and store complex and structured data. They can support inheritance, polymorphism, encapsulation and user-defined types. 
- The integration of deductive and object databases aims to combine the benefits of both paradigms and provide a unified framework for intelligent and flexible data management. 
- Some of the advantages of the integration are:
  - It can support both data and knowledge models, and allow for reasoning and learning from data. 
  - It can handle complex and heterogeneous data, such as spatial, temporal, multimedia and web data.  
  - It can enhance the expressiveness and usability of queries and rules, and support multiple paradigms of computation, such as logic, functional and imperative. 
- Some of the challenges of the integration are:
  - It requires efficient and scalable algorithms and architectures to handle large and dynamic data sets. 
  - It needs to address the semantic and syntactic issues of combining different data models and languages. 
  - It has to deal with the trade-offs and conflicts between different design goals, such as consistency, completeness, performance and usability.



### Constraint databases

- Constraint databases are a type of database that use constraints to represent and query data.
- Constraints are logical expressions that define the properties or relationships of data values.
- Constraint databases can store and manipulate data that is not easily represented by tables or tuples, such as geometric shapes, spatial regions, temporal intervals, or infinite sets.
- Constraint databases provide extra expressive power over relational databases in a largely hidden way. They keep the view of the database for a user or application programmer almost as simple as in relational databases.
- Constraint databases are shown to be powerful and simple tools for data modeling and querying in application areas -- such as environmental modeling, bioinformatics, and computer vision -- that are not suitable for relational databases.
- Some examples of constraint databases are:
  - GeoSQL: a constraint database system for spatial data that supports spatial operators and predicates.
  - Tempura: a constraint database system for temporal data that supports temporal operators and predicates.
  - CLP(R): a constraint logic programming system that integrates relational and constraint databases.
- Some advantages of constraint databases are:
  - They can handle complex and multidimensional data types and queries.
  - They can support declarative and efficient query languages based on logic and constraints.
  - They can ensure data integrity and consistency by enforcing constraints at the database level.
- Some challenges of constraint databases are:
  - They require specialized algorithms and data structures to store and manipulate constraints.
  - They may suffer from performance and scalability issues due to the complexity and size of constraints.
  - They may have limited support for updates, transactions, and concurrency control.



### Conclusions for the notes of the Unit 3 - Knowledge-Based Systems- AI Context in the subject of INTELLIGENT DATABASE SYSTEM

- Knowledge-based systems (KBS) are a type of artificial intelligence (AI) system that use a knowledge base and an inference engine to solve problems that require human expertise.
- A knowledge base is a collection of facts, rules, and heuristics that represent the domain knowledge of a specific problem area.
- An inference engine is a software component that applies logical reasoning to the knowledge base to derive new facts or conclusions.
- KBS can be classified into two main types: rule-based systems and case-based systems.
- Rule-based systems use a set of if-then rules to represent the knowledge and the inference engine applies forward chaining or backward chaining to infer new facts or goals.
- Case-based systems use a set of past cases or examples to represent the knowledge and the inference engine applies similarity measures and adaptation methods to find the most relevant case or solution for a new problem.
- KBS can be applied to various domains, such as diagnosis, planning, scheduling, design, configuration, and tutoring.
- KBS have some advantages, such as capturing and reusing human expertise, providing explanations and justifications, and facilitating knowledge acquisition and maintenance.
- KBS also have some limitations, such as dealing with uncertainty, inconsistency, incompleteness, and common sense knowledge, as well as requiring a large amount of domain knowledge and human involvement.



## Unit 4 - Advanced Knowledge-Based Systems

- A knowledge-based system (KBS) is a computer program that reasons and uses a knowledge base to solve complex problems.
- The knowledge base consists of facts and rules that represent the domain knowledge explicitly.
- The reasoning system, also called the inference engine, applies the rules to the facts and derives new facts or conclusions.
- A KBS can be classified into different types, such as expert systems, case-based reasoning systems, ontological systems, etc.
- Expert systems are KBS that emulate the decision-making ability of a human expert in a specific domain.
- Case-based reasoning systems are KBS that solve new problems by retrieving and adapting solutions from previous similar cases.
- Ontological systems are KBS that use a formal representation of the concepts and relations in a domain, called an ontology, to support reasoning and knowledge sharing.
- The most recent advancement of KBS has been to adopt the technologies, especially a kind of logic called description logic, for the development of systems that use the internet.
- The internet often has to deal with complex, unstructured data that cannot be relied on to fit a specific data model.
- Description logic allows the representation and reasoning of such data in a flexible and scalable way.
- Some examples of KBS that use description logic are semantic web, linked data, and knowledge graphs.
- KBS are a step towards an intelligent system, and can be justified when a few individuals have the majority of the knowledge.
- KBS can also help in the development of various domains, such as education, health, agriculture, etc.
- KBS can provide benefits such as increased efficiency, consistency, reliability, and accessibility of knowledge.
- KBS can also face challenges such as knowledge acquisition, validation, maintenance, and explanation.
- KBS are designed to follow coded rules using simple if-then logic, which is known as a production rule.
- KBS can also use other techniques, such as fuzzy logic, neural networks, genetic algorithms, etc., to enhance their performance and capabilities.
- KBS are an interdisciplinary and international field of artificial intelligence, and are constantly evolving and improving.



### Introduction for the notes of the Unit 4 - Advanced Knowledge-Based Systems in the subject of INTELLIGENT DATABASE SYSTEM

- A knowledge-based system (KBS) is a computer system that uses artificial intelligence techniques to solve problems that normally require human expertise.
- A KBS consists of two main components: a knowledge base and an inference engine.
- A knowledge base is a collection of facts and rules that represent the domain knowledge of a specific problem area.
- An inference engine is a software module that applies logical reasoning to the knowledge base to derive new facts and conclusions.
- A KBS can also have other components, such as a user interface, a knowledge acquisition module, a knowledge representation language, and a knowledge validation module.
- A KBS can be classified into different types based on the nature of the knowledge, the reasoning method, and the application domain.
- Some examples of KBS types are expert systems, case-based reasoning systems, neural networks, fuzzy systems, genetic algorithms, and hybrid systems.
- A KBS can provide various benefits, such as improving decision making, enhancing productivity, reducing errors, and facilitating learning and knowledge transfer.
- A KBS can also face various challenges, such as knowledge acquisition, knowledge representation, knowledge maintenance, knowledge verification, and knowledge validation.
- A KBS can be evaluated using different criteria, such as correctness, completeness, consistency, efficiency, usability, and reliability.



### Architectural solutions for the notes of the Unit 4 - Advanced Knowledge-Based Systems in the subject of INTELLIGENT DATABASE SYSTEM

- A knowledge-based system (KBS) is a computer system that uses artificial intelligence techniques to solve problems that require human expertise.
- A KBS consists of two main components: a knowledge base and an inference engine.
- A knowledge base is a collection of facts, rules, heuristics, and other forms of knowledge that represent the domain of the problem.
- An inference engine is a software module that applies logical reasoning to the knowledge base to derive conclusions or recommendations.
- There are different types of KBS, such as expert systems, decision support systems, planning systems, diagnosis systems, etc., depending on the purpose and functionality of the system.
- There are also different architectural solutions for designing and implementing a KBS, such as rule-based, frame-based, logic-based, object-oriented, neural network, fuzzy logic, etc., depending on the representation and processing of the knowledge.
- One of the most common and widely used architectural solutions for KBS is the blackboard architecture, which is based on the metaphor of a group of experts working together on a common problem by writing and erasing information on a shared blackboard.
- The blackboard architecture consists of three main components: a blackboard, a set of knowledge sources, and a control unit.
- The blackboard is a global data structure that stores the current state of the problem, the partial solutions, the goals, the hypotheses, and other relevant information.
- The knowledge sources are independent and specialized modules that contain the domain knowledge and the problem-solving strategies for a specific aspect of the problem.
- The control unit is a module that coordinates the activities of the knowledge sources, selects the most relevant and promising ones to apply, and updates the blackboard accordingly.
- The blackboard architecture allows for a modular, flexible, and cooperative approach to problem-solving, where the knowledge sources can communicate and cooperate with each other through the blackboard, and the control unit can dynamically adapt to the changing state of the problem.



### The 'general bridge' solution for the notes of the Unit 4 - Advanced Knowledge-Based Systems in the subject of INTELLIGENT DATABASE SYSTEM

- An intelligent database system (IDBS) is a database system that integrates artificial intelligence techniques, such as knowledge representation, reasoning, learning, and natural language processing, with database management capabilities, such as data modeling, storage, retrieval, and manipulation .
- A general bridge solution is a method of connecting two or more heterogeneous data sources or systems, such as databases, ontologies, web services, or applications, by using a common representation or interface that allows for data exchange and interoperability .
- A general bridge solution can be implemented in different ways, depending on the level of abstraction, the degree of integration, and the type of communication between the data sources or systems. Some possible approaches are:
  - Data-level integration: This approach involves transforming the data from different sources into a common format or schema, and storing them in a centralized or distributed repository. This allows for uniform access and querying of the data, but requires a high degree of coordination and maintenance among the data sources.
  - Schema-level integration: This approach involves mapping the schemas or structures of different data sources into a common schema or ontology, and using a mediator or broker to translate queries and results between the sources and the common schema. This allows for flexible and dynamic access and querying of the data, but requires a high degree of semantic consistency and alignment among the data sources.
  - Service-level integration: This approach involves exposing the data sources or systems as web services or APIs, and using a service-oriented architecture (SOA) or a web service composition framework to orchestrate and coordinate the interactions and transactions between the services. This allows for loose coupling and scalability of the data sources or systems, but requires a high degree of standardization and interoperability among the services.
- A general bridge solution can be applied to various scenarios and domains, such as:
  - Data warehousing and business intelligence: This involves integrating data from multiple sources, such as operational databases, external sources, or legacy systems, into a data warehouse or a data mart, and providing analytical and reporting capabilities to support decision making and business processes.
  - Semantic web and linked data: This involves publishing and linking data from different sources, such as databases, ontologies, web pages, or web services, on the web using common standards and formats, such as RDF, OWL, and SPARQL, and providing semantic and reasoning capabilities to support knowledge discovery and information retrieval.
  - Enterprise application integration (EAI) and enterprise information integration (EII): This involves integrating data and functionality from different applications or systems, such as ERP, CRM, SCM, or BI, within or across organizations, and providing a unified and consistent view and access to the data and functionality.



### Extending a KBS with components proper to a DBMS

- A Knowledge-Based System (KBS) is a system that uses artificial intelligence techniques to solve problems that require human expertise.
- A Database Management System (DBMS) is a software tool that enables users to create and manage databases, which are collections of data organized in a structured way.
- Extending a KBS with components proper to a DBMS means integrating the two technologies to achieve better performance, functionality, and usability.
- Some of the benefits of extending a KBS with components proper to a DBMS are:
  - Improved data management: A DBMS can provide efficient and reliable storage, retrieval, and manipulation of large amounts of data, which can enhance the knowledge base of a KBS.
  - Enhanced knowledge representation: A DBMS can support various data models and query languages, which can facilitate the representation and reasoning of complex and diverse knowledge in a KBS.
  - Increased scalability and portability: A DBMS can handle distributed and heterogeneous data sources, which can enable a KBS to scale up and adapt to different environments and platforms.
  - Reduced development and maintenance costs: A DBMS can offer standard and reusable components, such as data structures, algorithms, and interfaces, which can simplify the development and maintenance of a KBS.
- Some of the challenges of extending a KBS with components proper to a DBMS are:
  - Semantic mismatch: A DBMS and a KBS may have different assumptions and interpretations of the data and the knowledge, which can cause inconsistencies and conflicts.
  - Performance trade-off: A DBMS and a KBS may have different requirements and preferences for the speed, accuracy, and completeness of the data and the knowledge, which can affect the overall performance of the system.
  - Complexity and diversity: A DBMS and a KBS may have different levels and types of complexity and diversity in the data and the knowledge, which can increase the difficulty and cost of integration.



### The 'tight coupling' approach for the notes of the Unit 4 - Advanced Knowledge-Based Systems in the subject of INTELLIGENT DATABASE SYSTEM

- A knowledge-based system (KBS) is a system that uses artificial intelligence techniques to solve problems that normally require human expertise.
- A KBS can be coupled with a large data store, such as a database or a data warehouse, to access and manipulate the data needed for reasoning and inference.
- Coupling refers to the degree of integration and interaction between the KBS and the data store.
- There are two main types of coupling: loose coupling and tight coupling.
- Loose coupling means that the KBS and the data store are separate and independent entities, and they communicate through a standard interface, such as SQL queries or API calls.
- Tight coupling means that the KBS and the data store are closely integrated and interdependent, and they share a common data model, representation, and logic.
- The advantages of tight coupling are:
  - Faster and more efficient data access and manipulation, as there is no need for data conversion or translation between the KBS and the data store.
  - Higher consistency and integrity of data, as there is a single source of truth and a common set of rules and constraints for the data.
  - Easier maintenance and evolution of the system, as there is less redundancy and complexity in the system architecture and design.
- The disadvantages of tight coupling are:
  - Higher dependency and coupling between the KBS and the data store, which reduces the flexibility and modularity of the system and makes it harder to change or replace one component without affecting the other.
  - Higher risk of performance degradation and failure, as the system becomes more complex and vulnerable to errors and anomalies in the data or the logic.
  - Higher difficulty and cost of development and implementation, as the system requires more specialized and customized solutions and integrations.
- An example of a tight coupling approach is the deductive database, which combines the features of a relational database and a logic programming language, such as Prolog, to support both data management and knowledge representation and reasoning.



### Conclusion for the notes of the Unit 4 - Advanced Knowledge-Based Systems in the subject of INTELLIGENT DATABASE SYSTEM

- In this unit, we learned about the concepts and applications of advanced knowledge-based systems, such as expert systems, neural networks, fuzzy logic, genetic algorithms, and hybrid systems.
- We discussed the characteristics, components, and development process of expert systems, which are computer programs that emulate the reasoning and decision making of human experts in a specific domain.
- We explored the principles and architectures of neural networks, which are computational models that simulate the learning and processing capabilities of biological neurons.
- We introduced the theory and techniques of fuzzy logic, which is a form of multi-valued logic that deals with uncertainty and imprecision in human knowledge and reasoning.
- We examined the basic concepts and operators of genetic algorithms, which are optimization methods that mimic the natural processes of evolution and selection.
- We also looked at some examples of hybrid systems, which are systems that combine two or more of the above approaches to achieve better performance and robustness.
- We concluded that advanced knowledge-based systems are powerful tools for solving complex and ill-defined problems that require human-like intelligence and adaptability.



### Advanced solutions for the notes of the Unit 4 - Advanced Knowledge-Based Systems in the subject of INTELLIGENT DATABASE SYSTEM

- A knowledge-based system (KBS) is a computer program that reasons and uses a knowledge base to solve complex problems.
- A knowledge base is a collection of facts, rules, and heuristics that represent the knowledge of a domain expert.
- A knowledge-based system consists of two main components: a knowledge base and an inference engine.
- An inference engine is a software module that applies logical rules to the knowledge base to derive new knowledge or conclusions.
- There are different types of knowledge-based systems, such as expert systems, case-based reasoning systems, ontology-based systems, and semantic web systems .
- Expert systems are knowledge-based systems that emulate the reasoning and decision making of a human expert in a specific domain .
- Case-based reasoning systems are knowledge-based systems that solve new problems by retrieving and adapting solutions from previous similar cases .
- Ontology-based systems are knowledge-based systems that use a formal and explicit representation of the concepts and relationships in a domain, called an ontology, to facilitate knowledge sharing and reuse .
- Semantic web systems are knowledge-based systems that use web standards and technologies, such as RDF, OWL, and SPARQL, to represent and query knowledge on the internet .
- Knowledge-based systems can be used for various purposes, such as diagnosis, planning, design, education, and decision support  .
- Knowledge-based systems have some advantages, such as:
  - They can capture and preserve the knowledge of domain experts, which may be scarce or expensive .
  - They can provide consistent and reliable solutions, which may reduce errors and risks .
  - They can enhance human learning and performance, by providing explanations and feedback .
  - They can handle complex and dynamic problems, which may be beyond the capabilities of conventional systems .
- Knowledge-based systems also have some challenges, such as:
  - They require a lot of effort and expertise to acquire, represent, and maintain the knowledge base .
  - They may face issues of validity, reliability, and scalability, as the knowledge base grows and changes .
  - They may encounter ethical, legal, and social implications, such as accountability, transparency, and trust .



### Introduction for the notes of the Unit 4 - Advanced Knowledge-Based Systems in the subject of INTELLIGENT DATABASE SYSTEM

- A knowledge-based system (KBS) is a computer system that uses artificial intelligence techniques to solve problems that normally require human expertise.
- A KBS consists of two main components: a knowledge base and an inference engine.
- A knowledge base is a collection of facts, rules, heuristics, and other forms of knowledge representation that capture the domain knowledge of a human expert.
- An inference engine is a software module that applies logical reasoning to the knowledge base to derive new facts, conclusions, or recommendations.
- A KBS can also have other components, such as a user interface, a knowledge acquisition module, a knowledge validation module, and a knowledge explanation module.
- A KBS can be classified into different types based on the nature of the knowledge, the reasoning method, and the application domain.
- Some examples of KBS types are rule-based systems, case-based systems, model-based systems, neural networks, fuzzy systems, genetic algorithms, and hybrid systems.
- A KBS can provide various benefits, such as improving the quality and consistency of decision making, enhancing productivity and efficiency, reducing costs and errors, and facilitating knowledge sharing and learning.
- A KBS can also face various challenges, such as acquiring and maintaining the knowledge, ensuring the validity and reliability of the knowledge, dealing with uncertainty and incompleteness of the knowledge, and explaining the reasoning process and the results to the users.
- A KBS can be applied to various domains, such as diagnosis, planning, scheduling, design, configuration, optimization, simulation, control, monitoring, learning, and tutoring.



### A 'knowledge level' approach to the interaction with an IAS- TELOS

- IAS- TELOS stands for Intelligent Assistant System - Task Environment Language for Organizing Systems.
- It is a framework for developing knowledge-based systems that can interact with users and other systems in a natural language.
- It consists of three main components: a knowledge base, a problem solver, and a communication module.
- The knowledge base contains the domain knowledge and the meta-knowledge about the problem solving methods and the communication strategies.
- The problem solver applies the problem solving methods to the user's goals and queries, using the domain knowledge and the meta-knowledge.
- The communication module handles the natural language input and output, using the meta-knowledge and the communication strategies.
- The 'knowledge level' approach to the interaction with an IAS- TELOS is based on the idea that the system and the user share a common understanding of the domain and the problem solving methods, and that the communication is guided by the meta-knowledge and the communication strategies.
- The 'knowledge level' approach has the following advantages:
  - It allows the system to explain its reasoning and actions, and to justify its answers and recommendations.
  - It enables the system to adapt to the user's preferences, needs, and feedback, and to learn from the user's behavior and knowledge.
  - It facilitates the system's cooperation and coordination with other systems and agents, and the integration of multiple sources of knowledge and data.
  - It enhances the system's transparency, reliability, and trustworthiness, and the user's satisfaction and confidence.



### A language for implementing very large 'integral approach' systems

- An integral approach is a way of thinking that seeks to integrate all human knowledge disciplines into a single framework that can account for both objective and subjective aspects of reality .
- An integral approach can be applied to systems engineering, which is the discipline of designing, developing, and managing complex systems that involve people, technology, and environment .
- An integral approach to systems engineering can combine subjective methods and tools (such as values, culture, ethics, emotions, intuition, creativity, etc.) with existing objective methods and tools (such as mathematics, logic, physics, engineering, etc.) to create more human-centric, creative, and effective solutions.
- A language for implementing very large integral approach systems is a formal notation that can express both the subjective and objective aspects of a system, and can support the analysis, design, implementation, and evaluation of such systems.
- A possible language for implementing very large integral approach systems is the Integral Systems Language (ISL), which is based on the Integral Theory of Ken Wilber.
- ISL uses four quadrants to represent the four dimensions of reality: the individual subjective (I), the individual objective (IT), the collective subjective (WE), and the collective objective (ITS).
- ISL also uses levels, lines, states, and types to represent the different stages, domains, modes, and varieties of development and expression of each quadrant.
- ISL can be used to model the structure, behavior, and dynamics of integral systems, and to guide the integration of subjective and objective methods and tools in systems engineering.
- ISL can also be used to communicate and collaborate with different stakeholders and experts in integral systems engineering, and to facilitate the learning and adaptation of integral systems.



### The CYC project

- The CYC project is a long-term artificial intelligence project that aims to assemble a comprehensive ontology and knowledge base that spans the basic concepts and rules about how the world works.
- The project began in 1984 under the auspices of the Microelectronics and Computer Technology Corporation, a consortium of American computer, semiconductor, and electronics manufacturers, to advance work on artificial intelligence.
- In 1995, Douglas Lenat, the CYC project director, spun off the project as Cycorp, Inc., based in Austin, Texas.
- The project intends to capture common sense knowledge, as well as domain-specific knowledge, that other AI platforms may take for granted.
- The project uses a declarative language called CycL to represent the knowledge and the inference procedures in the system.
- The project also uses a natural language interface called Cyc NL to allow users to query and interact with the system.
- The project has produced several versions of the Cyc knowledge base, such as ResearchCyc, EnterpriseCyc, and OpenCyc.
- OpenCyc is a subset of the Cyc knowledge base and functionality that was released to the public in 2002.
- OpenCyc has around 240,000 concepts and 2,000,000 assertions as of 2012.
- The project aims to enable AI applications to reason like humans and to support a wide range of tasks, such as natural language understanding, information retrieval, data integration, and decision support.



### Other projects based on a 'conceptual representation' approach

- Conceptual representation is a technique for representing knowledge in a structured and meaningful way, using concepts and their relationships as the basic units of information.
- Conceptual representation can be used for building knowledge-based systems, which are systems that use explicit and formal knowledge to perform tasks that require human expertise or intelligence.
- Some examples of projects that use conceptual representation for knowledge-based systems are:

  - **Conceptual graphs**: A graphical notation for representing knowledge as a network of nodes and links, where nodes represent concepts and links represent relations between concepts. Conceptual graphs can be used for natural language understanding, reasoning, and knowledge acquisition .
  - **Frames**: A data structure for representing knowledge as a collection of attributes and values, where each attribute represents a feature or property of a concept, and each value represents a possible instantiation or specification of that attribute. Frames can be used for modeling complex and dynamic domains, such as planning, diagnosis, and learning .
  - **Logic**: A formal language for representing knowledge as a set of statements or propositions, where each statement expresses a fact or a rule about the domain. Logic can be used for deductive and inductive reasoning, as well as for querying and updating knowledge bases .
  - **Term-rewriting systems**: A computational model for representing knowledge as a set of symbols and rules, where each symbol represents a concept or an expression, and each rule specifies how to transform one symbol into another. Term-rewriting systems can be used for symbolic manipulation, algebraic computation, and program synthesis .



### Lexical approaches to the construction of large KBs

- Lexical approaches are methods that use natural language texts as sources of knowledge for building large-scale knowledge bases (KBs).
- KBs are collections of facts and rules that represent the domain knowledge of a system, such as a knowledge-based system (KBS).
- KBSs are systems that use artificial intelligence techniques to solve complex problems by reasoning with the knowledge stored in the KBs.
- Lexical approaches can be divided into two main categories: definitional and non-definitional.
- Definitional approaches use definitions of terms and concepts as the main source of knowledge. They extract the necessary information from dictionaries, glossaries, encyclopedias, textbooks, etc.
- Non-definitional approaches use other types of texts, such as news articles, scientific papers, web pages, etc. They rely on natural language processing techniques, such as parsing, semantic analysis, information extraction, etc.
- Lexical approaches have some advantages over other methods of KB construction, such as manual, semi-automatic, or logic-based methods. They can:
  - exploit the large amount of existing texts that cover various domains and topics;
  - reduce the human effort and cost involved in creating and maintaining the KBs;
  - capture the common sense and domain-specific knowledge that is implicit in natural language texts;
  - handle the ambiguity, vagueness, and inconsistency of natural language texts by using various techniques, such as disambiguation, normalization, validation, etc.
- Lexical approaches also have some challenges and limitations, such as:
  - dealing with the quality and reliability of the texts as sources of knowledge;
  - extracting the relevant and accurate information from the texts while filtering out the noise and redundancy;
  - representing the extracted knowledge in a formal and consistent way that can be used by the KBSs;
  - ensuring the completeness, correctness, and coherence of the KBs;
  - updating and maintaining the KBs as the texts and the domain knowledge change over time.



## Unit 5 - Applications in IDBS

- IDBS stands for **Integrated Database Systems**, which are systems that combine database management and application development capabilities in a single environment.
- IDBS can be used to create various types of applications, such as **data-intensive applications**, **decision support systems**, **expert systems**, **knowledge-based systems**, **multimedia applications**, and **web applications**.
- Data-intensive applications are applications that require large amounts of data to perform complex operations, such as **data analysis**, **data mining**, **data warehousing**, **data visualization**, and **data integration**.
- Decision support systems are applications that help users make decisions based on data and models, such as **business intelligence**, **online analytical processing**, **data dashboards**, and **reporting tools**.
- Expert systems are applications that use artificial intelligence techniques to emulate human expertise in a specific domain, such as **diagnosis**, **planning**, **scheduling**, **recommendation**, and **classification**.
- Knowledge-based systems are applications that use knowledge representation and reasoning techniques to manipulate and infer knowledge from data, such as **semantic web**, **ontology engineering**, **knowledge graphs**, and **natural language processing**.
- Multimedia applications are applications that involve multiple types of media, such as **text**, **images**, **audio**, **video**, and **animation**, and require special techniques for **storage**, **retrieval**, **processing**, and **presentation** of multimedia data.
- Web applications are applications that run on the internet and use web technologies, such as **HTML**, **CSS**, **JavaScript**, **PHP**, **ASP.NET**, and **Java Servlets**, to create dynamic and interactive web pages and web services.



### Introduction for the notes of the Unit 5 - Applications in IDBS in the subject of INTELLIGENT DATABASE SYSTEM

- Intelligent database systems (IDBS) are systems that integrate database management techniques with artificial intelligence methods to provide intelligent data management and processing capabilities.
- IDBS can support various applications that require complex data analysis, knowledge discovery, decision making, and problem solving.
- Some of the applications of IDBS are:
  - Data mining and knowledge discovery: IDBS can use techniques such as machine learning, neural networks, genetic algorithms, fuzzy logic, and rule-based systems to discover patterns, trends, associations, and rules from large and heterogeneous data sets.
  - Expert systems and decision support systems: IDBS can use techniques such as knowledge representation, inference, and explanation to provide expert advice and guidance to users in specific domains, such as medical diagnosis, financial planning, or engineering design.
  - Natural language processing and information retrieval: IDBS can use techniques such as natural language understanding, generation, and translation, as well as information extraction, summarization, and retrieval to process and access natural language data, such as text, speech, or images.
  - Multimedia and web databases: IDBS can use techniques such as image processing, computer vision, speech recognition, and synthesis, as well as web mining, crawling, and indexing to manage and query multimedia and web data, such as audio, video, graphics, or hypertext.
  - Spatial and temporal databases: IDBS can use techniques such as spatial reasoning, temporal logic, and spatio-temporal indexing to handle and manipulate data that have spatial and temporal dimensions, such as geographic information systems, moving object databases, or sensor networks.
  - Bioinformatics and biometric databases: IDBS can use techniques such as sequence analysis, phylogenetic analysis, and pattern recognition to deal with data that are related to biological and biometric phenomena, such as DNA, proteins, genes, or fingerprints.



### Temporal databases

- A temporal database is a database that has certain features that support time-sensitive status for entries .
- A temporal database can store data relating to past, present and future time instances.
- A temporal database can also track the history of data changes, such as when a fact was inserted, updated or deleted .
- A temporal database can be classified into different types based on the temporal aspects it supports:
  - Uni-temporal: A database that supports only one temporal aspect, such as valid time or transaction time.
  - Bi-temporal: A database that supports both valid time and transaction time.
  - Tri-temporal: A database that supports valid time, transaction time and decision time (the time when a fact was recorded in the database).
- A temporal database can offer temporal data types, such as date, time, interval, period, etc., and temporal operators, such as overlap, before, after, etc., to manipulate and query temporal data .
- A temporal database can also provide temporal integrity constraints, such as temporal primary keys, temporal foreign keys, temporal uniqueness, etc., to ensure the consistency and validity of temporal data.
- A temporal database can have various applications, such as historical analysis, auditing, data warehousing, temporal reasoning, etc .



### Basic concepts for the notes of the Unit 5 - Applications in IDBS in the subject of INTELLIGENT DATABASE SYSTEM

- An intelligent database is a full-text database with artificial intelligence (AI) components that interact with users to ensure that users are supplied all relevant information.
- An intelligent database system (IDBS) is a system that manages information (rather than data) in a way that appears natural to users and which goes beyond simple record keeping.
- An IDBS has three levels of intelligence: high level tools, the user interface and the database engine.
- High level tools manage data quality and automatically discover relevant patterns in the data with a process called data mining.
- The user interface provides natural language processing, speech recognition, graphical visualization and multimedia capabilities to facilitate user interaction.
- The database engine supports advanced data models, query optimization, concurrency control, transaction management and security features to ensure efficient and reliable data access.
- Some of the applications of IDBS are:
  - Business intelligence: IDBS can help businesses analyze their data and gain insights for decision making, planning and forecasting.
  - Knowledge management: IDBS can help organizations capture, store, share and reuse their knowledge assets, such as documents, reports, best practices and lessons learned.
  - Personalization: IDBS can help customize the content and services delivered to users based on their preferences, behavior and feedback.
  - Recommendation systems: IDBS can help suggest relevant items or actions to users based on their needs, interests and context.
  - Fraud detection: IDBS can help detect and prevent fraudulent activities, such as credit card fraud, insurance fraud and identity theft, by analyzing the data and identifying anomalies and patterns.
  - Healthcare: IDBS can help improve the quality and efficiency of healthcare services, such as diagnosis, treatment, prevention and monitoring, by integrating and analyzing the data from various sources, such as electronic health records, medical images, sensors and wearable devices.
  - Education: IDBS can help enhance the learning outcomes and experiences of students and teachers, by providing adaptive and personalized learning content, feedback and assessment, as well as collaborative and interactive learning environments.



### Temporal Data Models

- Temporal data models are data models that capture the changes of data over time, as well as the time references that indicate when the data are valid or recorded.
- Temporal data models exist at three abstraction levels:
  - The conceptual level, in which the data models are generally extensions of the Entity-Relationship Model (ERM).
  - The logical level, in which the data models are generally extensions of the relational data model or of an object-oriented data model.
  - The physical level, in which the data model details how the data are to be stored.
- Temporal data models can be classified according to the type of time they capture :
  - Valid time, which is the time when the data are true in the real world.
  - Transaction time, which is the time when the data are recorded in the database.
  - Decision time, which is the time when the data are used for decision making.
- Temporal data models can also be classified according to the number of time dimensions they capture:
  - Uni-temporal, which capture only one type of time (either valid time or transaction time).
  - Bi-temporal, which capture both valid time and transaction time.
  - Tri-temporal, which capture valid time, transaction time and decision time.
- Temporal data models require special data types, operations and constraints to handle time values and intervals  .
  - Temporal data types include date, time, timestamp, interval and period.
  - Temporal operations include temporal selection, projection, join, aggregation, grouping and ordering.
  - Temporal constraints include temporal primary keys, foreign keys, referential integrity and temporal consistency.
- Temporal data models have various applications in intelligent database systems, such as data warehousing, data mining, temporal reasoning, temporal query processing and temporal data visualization .



### Temporal Query Languages

- A temporal query language is a database query language that offers some form of built-in support for the querying and modification of time-referenced data, as well as enabling the specification of assertions and constraints on such data.
- Time-referenced data is data that has temporal attributes, such as valid time, transaction time, or both, that indicate when the data is valid or when it was stored in the database.
- Temporal query languages can be classified into two main categories: temporal extensions of existing query languages, such as SQL, and novel query languages designed specifically for temporal data.
- Temporal extensions of existing query languages aim to preserve the syntax and semantics of the original query language, while adding new temporal features, such as temporal data types, temporal predicates, temporal operators, and temporal modifiers.
- Novel query languages for temporal data are based on different data models and paradigms, such as logic programming, functional programming, or stream processing, and offer different expressive power and performance characteristics.
- Some examples of temporal extensions of SQL are TSQL2, ATSQL2, IXSQL, ATSQL, and SQL/TP . TSQL2 represents an effort to design a consensus data model and query language, and it includes many of the concepts that were proposed by earlier temporal data models and query languages.
- Some examples of novel query languages for temporal data are Tempura, TQuel, TLP, TFL, and Trill. Trill is an open source .NET library designed to process one trillion events a day, and it provides a temporal query language enabling you to embed real-time analytics in your own application.



### Ontologies for the notes of the Unit 5 - Applications in IDBS in the subject of INTELLIGENT DATABASE SYSTEM

- An ontology is a formal system for modeling concepts and their relationships in a given domain.
- Ontologies are useful for expressing data in which the relationships between objects are important, unlike relational database systems, which are based on interconnected tables.
- Ontologies store the information in a graph database, or triplestore, which consists of triples of the form (subject, predicate, object), where each element is a resource identified by a URI.
- Ontologies can be used to improve the effectiveness of the human-computer communication, by allowing users to pose queries based on terms from the ontology, and get answers that incorporate the term hierarchy or other logical features of the ontology .
- Ontologies can also be used to perform integration across distributed, heterogeneous ontology databases using an inference-based framework.
- Ontologies can be implemented using several semantic languages, such as RDF, RDF Schema, OWL, and SPARQL .
- Ontologies can be developed and maintained using various methods and tools, such as ontology editors, ontology learning, ontology alignment, ontology evaluation, and ontology evolution.



### Ontology theoretical foundations

- Ontology is the philosophical study of being, as well as related concepts such as existence, becoming, and reality.
- Ontology addresses questions like how entities are grouped into categories and which of these entities exist on the most fundamental level.
- Ontology is also a branch of knowledge engineering, artificial intelligence and computer science, where it refers to a formal representation of the concepts and relations in a domain of interest.
- Ontology can be used for knowledge management, natural language processing, e-commerce, intelligent information integration, information retrieval, and other applications that require a common understanding of the domain.
- Ontology can be developed from top-down or bottom-up approaches, depending on the level of generality and specificity required.
- At the highest level of generality, there are the foundational ontologies, which span across many fields and model the very basic and general concepts and relations that make up the world, such as object, event, parthood relation, etc.  .
- Foundational ontologies provide a high-level categorization about the kinds of things that will be represented in the ontology, such as process and physical object, relations that are useful across subject domains, such as participation and parthood, and (what are and) how to represent ‘attributes’ in a particular subject domain, such as Color and Height, which can be done, e.g., as quality or some kind of dependent continuant or trope .
- Foundational ontologies can be used as a basis for developing more specific domain ontologies, which capture the concepts and relations that are relevant for a particular field or application, such as medicine, biology, geography, etc.  .
- Domain ontologies can be further refined into application ontologies, which are tailored to the needs and requirements of a specific system or task, such as diagnosis, planning, recommendation, etc.  .
- Ontology development involves several steps, such as defining the scope and purpose of the ontology, identifying the relevant sources of knowledge, extracting and analyzing the concepts and relations, formalizing and representing the ontology in a suitable language, validating and evaluating the ontology, and maintaining and updating the ontology .
- Ontology development also requires a clear understanding of the research paradigm, which is the idea of how knowledge is produced and validated, and which involves the ontology, epistemology and methodology of the research .
- Ontology, in the context of research paradigm, refers to the assumptions and beliefs about the nature of reality and what can be known about it .
- Epistemology refers to the theory of knowledge and how it can be acquired and justified .
- Methodology refers to the methods and techniques used to collect and analyze data and to test hypotheses .
- Different research paradigms have different implications for ontology development, such as positivism, interpretivism, critical realism, pragmatism, etc. .



### Environments for building ontologies

- An ontology is a formal representation of the concepts and relationships in a domain of interest.
- Ontologies are used for various purposes, such as knowledge sharing, semantic interoperability, information integration, and reasoning.
- Building ontologies requires a systematic and rigorous process that involves analysis, design, implementation, and evaluation of the ontology.
- Environments for building ontologies are software tools that support the ontology development process by providing functionalities such as editing, browsing, visualizing, querying, and validating ontologies.
- Some examples of environments for building ontologies are:

  - OntoEdit: a graphical ontology editor that supports multiple ontology languages and allows collaborative ontology development.
  - WebODE: a web-based ontology development environment that provides a suite of services for ontology creation, management, and reuse.
  - Protege: an open-source ontology editor and framework that supports various ontology formats and plugins for ontology engineering tasks .
  - Hozo: an ontology engineering environment that focuses on the role and relationship concepts in ontologies and supports ontology modularization and integration .

- Environments for building ontologies can be evaluated based on several criteria, such as usability, functionality, scalability, interoperability, and extensibility.
- Environments for building ontologies can be applied to various domains, such as environmental monitoring, bioinformatics, education, and nanotechnology .



### Structured, semi-structured and unstructured data

- Structured data is data that has a predefined schema, format and organization, typically stored in a relational database or a spreadsheet. Structured data is easy to query, analyze and manipulate using standard tools and languages, such as SQL. Examples of structured data are customer records, product catalogs, sales transactions, etc.    
- Semi-structured data is data that has some degree of organization, but does not follow a rigid schema or format. Semi-structured data often uses self-describing formats, such as JSON, XML or CSV, that can store different types of data together. Semi-structured data is more flexible and scalable than structured data, but also more challenging to query and process. Examples of semi-structured data are web logs, social media posts, email messages, etc.    
- Unstructured data is data that has no predefined schema, format or organization, and is stored in its native form. Unstructured data is the most complex and diverse type of data, and often contains rich and qualitative information, such as text, images, audio, video, etc. Unstructured data is difficult to query, analyze and manipulate using standard tools and languages, and requires specialized techniques, such as natural language processing, text mining, computer vision, etc. Examples of unstructured data are books, articles, reviews, tweets, photos, videos, etc.     

: https://www.indeed.com/career-advice/career-development/structured-vs-unstructured-vs-semi-structured-data
: https://www.michael-gramlich.com/what-is-structured-semi-structured-and-unstructured-data/
: https://k21academy.com/microsoft-azure/dp-900/structured-data-vs-unstructured-data-vs-semi-structured-data/
: https://www.geeksforgeeks.org/difference-between-structured-semi-structured-and-unstructured-data/
: https://www.forbes.com/sites/bernardmarr/2019/10/18/whats-the-difference-between-structured-semi-structured-and-unstructured-data/



### Multimedia database

- A multimedia database (MMDB) is a collection of related multimedia data that includes one or more primary media data types such as text, images, graphic objects, audio, video, and animation .
- Multimedia data are broadly categorized into three classes:
  - Static media (time-independent): image and graphic object
  - Dynamic media (time-dependent): audio, video, and animation
  - Dimensional media: virtual reality and holograms
- Multimedia databases should address the following requirements:
  - Integration: data items do not need to be duplicated for different programs or applications
  - Data independence: separate the database structure and content from the programs that access it
  - Consistency: ensure that the data items are valid and accurate
  - Security: protect the data items from unauthorized access or modification
  - Backup and recovery: provide mechanisms to restore the data items in case of failure or damage
  - Querying: allow users to retrieve and manipulate the data items based on their content and properties
- Multimedia databases face some challenges that are different from traditional databases, such as :
  - Large data size: multimedia data require more storage space and bandwidth than alphanumeric data
  - Complex data types: multimedia data have diverse formats, structures, and semantics that are difficult to represent and manipulate
  - Content-based retrieval: multimedia data need to be accessed based on their features and similarity, not just their identifiers or keywords
  - Temporal and spatial relationships: multimedia data have temporal and spatial dimensions that need to be preserved and synchronized
  - Quality of service: multimedia data have different requirements for delivery, presentation, and adaptation depending on the user and the environment
- Multimedia databases have many applications in various domains, such as:
  - Documents and record management: industries and businesses that keep detailed records and variety of documents
  - Knowledge dissemination: multimedia databases are effective tools for knowledge dissemination in terms of providing information, education, and training
  - Entertainment and art: multimedia databases are used to create and distribute multimedia content for entertainment and art purposes, such as movies, games, music, and paintings
  - Medical and health care: multimedia databases are used to store and analyze medical images, videos, and records for diagnosis, treatment, and research
  - Surveillance and security: multimedia databases are used to monitor and detect suspicious activities and events using multimedia sensors and cameras
  - Geographical information systems: multimedia databases are used to store and process geographical data, such as maps, satellite images, and weather data



### Semi-structured data

- Semi-structured data is a form of structured data that does not obey the tabular structure of data models associated with relational databases or other forms of data tables   .
- Semi-structured data contains tags or other markers to separate semantic elements and enforce hierarchies of records and fields within the data   .
- Semi-structured data is often qualitative, or textual, and can include data that has an organizational structure understandable to both machines and humans.
- Examples of semi-structured data are email, HTML, XML, JSON, online images and videos, social media posts, web logs, etc .
- Benefits of semi-structured data are:
  - It can capture complex and heterogeneous data that cannot be easily represented in a relational database .
  - It can accommodate changes in data schema without requiring extensive modifications .
  - It can enable faster and more flexible data analysis and integration by using tools such as NoSQL databases, Hadoop, Spark, etc .
- Challenges of semi-structured data are:
  - It can be difficult to validate, query, and extract information from semi-structured data due to the lack of a fixed or rigid schema .
  - It can require more storage space and processing power than structured data due to the overhead of tags and metadata .
  - It can pose security and privacy risks if the data contains sensitive or personal information that is not properly protected or anonymized .



### Mediators for the notes of the Unit 5 - Applications in IDBS in the subject of INTELLIGENT DATABASE SYSTEM

- A mediator is a software component that provides a uniform interface to heterogeneous data sources, such as databases, legacy systems, web services, etc. 
- A mediator can perform various tasks, such as data integration, query processing, data transformation, data analysis, etc. 
- A mediator can be classified into two types: wrapper mediators and integrator mediators. 
  - A wrapper mediator is a mediator that encapsulates a single data source and provides a common data model and query language for accessing it. 
  - An integrator mediator is a mediator that combines data from multiple wrapper mediators and provides a global view of the integrated data. 
- A mediator can be used for various applications in intelligent database systems, such as:
  - Providing convenient and flexible access to heterogeneous and distributed data sources. 
  - Supporting complex queries and reasoning over data and metadata. 
  - Enhancing the functionality and performance of existing database systems. 
  - Enabling interoperability and collaboration among different systems and users. 
  - Facilitating the development and maintenance of intelligent applications.



### Motivation for the notes of the Unit 5 - Applications in IDBS in the subject of INTELLIGENT DATABASE SYSTEM

- Intelligent database systems (IDBS) are systems that combine database management and artificial intelligence techniques to provide intelligent data management and processing capabilities.
- IDBS can support various applications that require complex data analysis, decision making, knowledge discovery, and reasoning over large and heterogeneous data sources.
- Some of the applications of IDBS are:
  - Data mining and knowledge discovery: IDBS can use machine learning, statistical, and logical methods to discover patterns, rules, associations, clusters, and anomalies from data, and to extract useful and actionable knowledge for various domains and tasks.
  - Data integration and interoperability: IDBS can use ontologies, semantic web technologies, and natural language processing to integrate and query data from multiple and diverse sources, and to enable semantic interoperability and data exchange among different systems and users.
  - Data quality and cleaning: IDBS can use data quality metrics, data cleaning algorithms, and data provenance techniques to assess, improve, and maintain the quality and consistency of data, and to handle data errors, missing values, duplicates, and outliers.
  - Data security and privacy: IDBS can use encryption, authentication, access control, and anonymization techniques to protect data from unauthorized access, modification, and disclosure, and to preserve the privacy and confidentiality of data owners and users.
  - Data visualization and exploration: IDBS can use graphical, interactive, and immersive methods to present data in various forms and levels of abstraction, and to enable users to explore, understand, and communicate data and insights.



### Architecture for the notes of the Unit 5 - Applications in IDBS in the subject of INTELLIGENT DATABASE SYSTEM

- An Intelligent Database System (IDBS) is a database system that incorporates Artificial Intelligence (AI) techniques to enhance its functionality and performance .
- An IDBS can be seen as an extension of a conventional database system with additional components such as a knowledge base, an inference engine, and a user interface.
- The architecture of an IDBS can be based on different paradigms, such as the expert system paradigm, the deductive database paradigm, the active database paradigm, or the hybrid paradigm.
- The expert system paradigm is based on the organization of an expert system, which consists of a fact database, a rule base, and an inference engine. The fact database stores the data, the rule base stores the domain knowledge, and the inference engine applies the rules to the data to derive new facts or conclusions.
- The deductive database paradigm is based on the integration of logic programming and database systems, which allows the definition and manipulation of data using logic rules and queries. The deductive database system can perform deductive reasoning on the data and infer new facts or answers.
- The active database paradigm is based on the incorporation of triggers and rules into the database system, which can specify actions to be performed automatically in response to certain events or conditions. The active database system can monitor the data and react to changes or updates.
- The hybrid paradigm is based on the combination of different paradigms, such as the expert system paradigm and the deductive database paradigm, or the active database paradigm and the deductive database paradigm. The hybrid database system can exploit the advantages of different paradigms and provide more functionality and flexibility.
- The applications of IDBS can be found in various domains, such as decision support systems, data mining, data warehousing, information retrieval, natural language processing, image processing, multimedia, and web databases  .
- The benefits of IDBS include improved data quality, data consistency, data integration, data analysis, data interpretation, data presentation, and user satisfaction .



### Application of mediators to heterogeneous systems for the notes of the Unit 5 - Applications in IDBS in the subject of INTELLIGENT DATABASE SYSTEM

- A mediator is a software component that provides a uniform interface to access heterogeneous data sources, such as relational databases, XML files, web services, etc.
- A mediator can perform various tasks, such as data transformation, query processing, data integration, data analysis, etc.
- A mediator can be classified into two types: wrapper-based and ontology-based.
- A wrapper-based mediator relies on wrappers, which are software components that translate the data and queries between the mediator and the data sources. A wrapper-based mediator can handle syntactic and structural heterogeneity, but not semantic heterogeneity.
- An ontology-based mediator relies on ontologies, which are formal representations of the concepts and relationships in a domain. An ontology-based mediator can handle semantic heterogeneity, as well as syntactic and structural heterogeneity, by using ontologies to map the data and queries between the mediator and the data sources.
- A mediator can be used for various applications in intelligent database systems, such as:
  - Intelligent monitoring of distributed, heterogeneous data sources, which involves creating and executing standing requests for information (SRIs) that detect changes in the data sources that are relevant to a plan or a goal.
  - Intelligent data integration from heterogeneous relational databases containing incomplete and uncertain information, which involves using a flexible mediator system that can handle different types of incompleteness and uncertainty in the data and queries.
  - Intelligent semantic integration of heterogeneous proteomic data, which involves using a mediator system that leverages the Apache Spark framework to perform data transformation and query execution over four sources of proteomic data: UniProt, String, PDB and PubMed.



### Proposals for the notes of the Unit 5 - Applications in IDBS in the subject of INTELLIGENT DATABASE SYSTEM

- An intelligent database is a full-text database with artificial intelligence (AI) components that interact with users to ensure that users are supplied all relevant information.
- An intelligent database system (IDBS) is a system that manages information (rather than data) in a way that appears natural to users and which goes beyond simple record keeping.
- An IDBS has three levels of intelligence: high level tools, the user interface and the database engine.
- High level tools manage data quality and automatically discover relevant patterns in the data with a process called data mining.
- The user interface provides natural language processing, speech recognition, graphical visualization and multimedia capabilities to facilitate user interaction with the system.
- The database engine supports advanced data models, query optimization, concurrency control, transaction management and security features to ensure efficient and reliable data access and manipulation.
- Some of the applications of IDBS are:
  - Business intelligence: IDBS can help businesses analyze their data and gain insights into their performance, customers, competitors and market trends.
  - E-commerce: IDBS can enable online transactions, personalized recommendations, fraud detection and customer loyalty programs.
  - Health care: IDBS can assist in diagnosis, treatment, drug discovery, medical records and patient monitoring.
  - Education: IDBS can provide adaptive learning, intelligent tutoring, assessment and feedback.
  - Social media: IDBS can analyze user behavior, preferences, sentiments and social networks to provide relevant content, advertisements and recommendations.
  - Smart cities: IDBS can integrate data from various sources, such as sensors, cameras, vehicles and citizens, to optimize urban planning, traffic management, public safety and environmental sustainability.
- Microsoft Intelligent Data Platform is an example of an integrated data and AI platform that enables users to unlock the value of their data and reduce costs. It provides various services and tools, such as:
  - Azure Synapse Analytics: a unified analytics service that combines data warehousing, data lake, data integration and big data analytics.
  - Azure Purview: a unified data governance service that helps users discover, catalog, map and manage their data assets across on-premises, cloud and hybrid environments.
  - Azure Machine Learning: a cloud-based service that helps users build, train, deploy and manage machine learning models at scale.
  - Azure Cognitive Services: a collection of AI services that enable users to add vision, speech, language, decision and web search capabilities to their applications.
  - Azure Databricks: a fast, easy and collaborative analytics platform based on Apache Spark that supports data engineering, data science and machine learning.
  - Azure SQL Database: a fully managed relational database service that supports intelligent performance, security and availability features.
  - Azure Cosmos DB: a fully managed NoSQL database service that supports multiple data models, APIs and consistency levels, as well as global distribution and scalability.
  - Power BI: a business analytics service that helps users create and share interactive dashboards and reports.



### Multi-Agent Systems for the Notes of the Unit 5 - Applications in IDBS in the Subject of Intelligent Database Systems

- A multi-agent system (MAS) is a computerized system composed of multiple interacting intelligent agents that can solve problems that are difficult or impossible for an individual agent or a monolithic system to solve.
- Multi-agent systems are a subfield of distributed artificial intelligence (DAI) that studies how agents can coordinate their actions and knowledge in a distributed environment.
- Multi-agent systems have many applications in intelligent database systems, such as:
  - Data integration: agents can cooperate to integrate heterogeneous and distributed data sources and provide a unified view to the users.
  - Data mining: agents can collaborate to discover patterns and knowledge from large and complex data sets and share their findings with other agents or users.
  - Data quality: agents can monitor and improve the quality of data by detecting and resolving inconsistencies, errors, and outliers.
  - Data security: agents can protect the data from unauthorized access and malicious attacks by enforcing access control policies and encryption mechanisms.
  - Data analysis and decision support: agents can provide intelligent and personalized support to the users for data analysis and decision making by using techniques such as reasoning, learning, and optimization.
- Multi-agent systems can also benefit from intelligent database systems, such as:
  - Data storage and retrieval: agents can use intelligent database systems to store and retrieve their data and knowledge efficiently and effectively.
  - Data communication and coordination: agents can use intelligent database systems to communicate and coordinate their actions and goals with other agents and users.
  - Data adaptation and evolution: agents can use intelligent database systems to adapt and evolve their data and knowledge according to the changes in the environment and the user preferences.
- Multi-agent systems face many challenges and issues in intelligent database systems, such as:
  - Data heterogeneity and inconsistency: agents have to deal with different data formats, schemas, and semantics, and resolve possible conflicts and contradictions among them.
  - Data complexity and scalability: agents have to handle large and complex data sets that may require high computational and communication resources.
  - Data privacy and trust: agents have to respect the privacy and confidentiality of the data owners and users, and establish trust and reputation among themselves.
  - Data coordination and cooperation: agents have to coordinate and cooperate their actions and goals with other agents and users, and avoid or resolve possible conflicts and competition among them.



### Main issues in designing a multi-agent system

A multi-agent system (MAS) is a computerized system composed of multiple interacting intelligent agents that can solve problems that are difficult or impossible for an individual agent or a monolithic system to solve. Designing a MAS involves several challenges and issues, such as:

- **Defining the system goals and requirements**: The designer needs to specify the overall objectives and constraints of the MAS, as well as the individual and collective behaviors of the agents. The system goals and requirements should be clear, consistent, and verifiable.
- **Identifying the roles and responsibilities of the agents**: The designer needs to determine the types and number of agents that are needed to achieve the system goals and requirements, as well as their roles and responsibilities. The roles and responsibilities should be aligned with the agent capabilities and the system structure.
- **Designing the agent architecture and behavior**: The designer needs to choose or develop an appropriate agent architecture and behavior model for each type of agent, taking into account the agent's goals, beliefs, preferences, and interactions. The agent architecture and behavior should be modular, flexible, and adaptable.
- **Designing the communication and coordination mechanisms**: The designer needs to design the communication and coordination protocols and mechanisms that enable the agents to exchange information, negotiate, cooperate, and coordinate their actions. The communication and coordination mechanisms should be efficient, reliable, and secure.
- **Designing the system structure and organization**: The designer needs to design the system structure and organization that defines the relationships and dependencies among the agents and the environment. The system structure and organization should be scalable, robust, and resilient.
- **Implementing and testing the MAS**: The designer needs to implement and test the MAS using appropriate tools and platforms, and evaluate its performance and functionality. The implementation and testing should follow the system specifications and requirements, and identify and resolve any errors or issues.



### Open problems for the notes of the Unit 5 - Applications in IDBS in the subject of INTELLIGENT DATABASE SYSTEM

- Intelligent database systems (IDBS) are databases that incorporate artificial intelligence techniques, such as machine learning, natural language processing, and knowledge representation, to provide advanced functionalities and services to users and applications.
- IDBS have many potential applications in various domains, such as business intelligence, e-commerce, health care, education, and social media.
- However, IDBS also face many open problems and challenges that need to be addressed by researchers and practitioners. Some of these problems are:

  - **Data quality and consistency**: IDBS need to ensure that the data they store and process are accurate, complete, and consistent, especially when dealing with heterogeneous, dynamic, and noisy data sources. Data quality and consistency issues can affect the performance and reliability of IDBS and the validity of the results they produce. IDBS need to employ effective data cleaning, validation, and integration techniques to handle data quality and consistency problems .
  - **Data security and privacy**: IDBS need to protect the data they manage from unauthorized access, modification, or disclosure, especially when dealing with sensitive or personal data. Data security and privacy issues can affect the trust and confidence of users and applications that rely on IDBS. IDBS need to employ appropriate data encryption, authentication, and access control techniques to handle data security and privacy problems.
  - **Data scalability and performance**: IDBS need to handle large volumes of data and support high concurrency and availability of users and applications, especially when dealing with distributed, cloud-based, or edge-based data sources. Data scalability and performance issues can affect the efficiency and effectiveness of IDBS and the satisfaction of users and applications. IDBS need to employ scalable data storage, indexing, and query processing techniques to handle data scalability and performance problems .
  - **Data analysis and mining**: IDBS need to provide advanced data analysis and mining capabilities to users and applications, such as data summarization, classification, clustering, association, prediction, and recommendation. Data analysis and mining issues can affect the quality and usefulness of the insights and knowledge that IDBS can generate from data. IDBS need to employ suitable data mining algorithms, models, and frameworks to handle data analysis and mining problems .
  - **Data interpretation and presentation**: IDBS need to provide intuitive and interactive data interpretation and presentation interfaces to users and applications, such as natural language, visualization, and dialogue. Data interpretation and presentation issues can affect the understandability and usability of the information and knowledge that IDBS can communicate to users and applications. IDBS need to employ appropriate data visualization, natural language generation, and dialogue systems techniques to handle data interpretation and presentation problems .



### Internet indexing and retrieval

- Internet indexing and retrieval is the process of collecting, organizing, and accessing information from the Internet, which is a vast and heterogeneous collection of documents, multimedia, and other data sources.
- Internet indexing and retrieval involves two main components: search engines and web browsers.
- Search engines are software systems that crawl the Internet, index the content and metadata of web pages, and rank them according to their relevance to user queries.
- Web browsers are software applications that allow users to interact with the Internet, view web pages, and submit queries to search engines.
- Internet indexing and retrieval has many applications in intelligent database systems (IDBS), which are database systems that use artificial intelligence techniques to enhance their functionality and performance.
- Some of the applications of Internet indexing and retrieval in IDBS are:

  - Web mining: the extraction of useful information and knowledge from web data, such as web content, web structure, web usage, and web users.
  - Web personalization: the customization of web content and services according to the preferences and needs of individual users or groups of users.
  - Web recommendation: the provision of suggestions for web items or actions that are likely to be of interest or benefit to users, based on their profiles, behavior, or context.
  - Web analytics: the measurement, analysis, and reporting of web data for the purpose of understanding and optimizing web usage and performance.
  - Web security: the protection of web data and systems from unauthorized access, modification, or damage, using techniques such as encryption, authentication, authorization, and intrusion detection.



### Basic indexing methods for the notes of the Unit 5 - Applications in IDBS in the subject of INTELLIGENT DATABASE SYSTEM

- Indexing is a technique to optimize the performance of a database by reducing the number of disk accesses required to process a query.
- Indexing creates a data structure that allows faster and easier access to the data in a database table.
- Indexing is based on the indexing attributes, which are the columns or fields used to search, sort, or join the data.
- There are two main types of indexing methods: primary indexing and secondary indexing.
- Primary indexing is defined on an ordered data file, where the data file is sorted on a key field, which is usually the primary key of the table.
- Primary indexing has two subtypes: dense indexing and sparse indexing.
- Dense indexing creates an index record for every search key value in the database, and each index record contains the search key value and a pointer to the actual record in the data file.
- Sparse indexing creates an index record only for some of the search key values, and each index record contains the search key value and a pointer to the first data block that contains that value.
- Secondary indexing is defined on a field that is not the primary key of the table, and it can be either a candidate key or a non-key field.
- Secondary indexing creates an index file that contains the values of the secondary key and pointers to the records that have that value.
- Secondary indexing can be used to support queries that do not involve the primary key, or to create multiple access paths to the data.
- There are other types of indexing methods, such as clustering indexing, multilevel indexing, hash-based indexing, bitmap indexing, etc., that are designed for specific purposes or data types.
- Indexing in intelligent database systems can also involve techniques such as semantic indexing, content-based indexing, or similarity-based indexing, that use the meaning, content, or similarity of the data to create indexes.



### Search engines or meta-searchers for the notes of the Unit 5 - Applications in IDBS in the subject of INTELLIGENT DATABASE SYSTEM

- A search engine is a software system that allows users to find information on the web by entering keywords or queries. A search engine typically consists of three components: a crawler, an indexer, and a query processor. A crawler is a program that visits web pages and follows links to discover new pages. An indexer is a program that analyzes the content and structure of web pages and stores them in a database. A query processor is a program that matches user queries with the indexed pages and returns the most relevant results.
- A meta-search engine is a type of search engine that does not have its own database or index, but instead aggregates results from multiple other search engines. A meta-search engine may use different methods to combine and rank the results, such as applying its own algorithms, filtering, clustering, or summarizing. A meta-search engine may offer some advantages over a single search engine, such as broader coverage, faster response, and more diverse perspectives.
- Some examples of search engines are Google, Bing, and Yahoo. Some examples of meta-search engines are Dogpile, Metacrawler, and Yippy. 
- Search engines and meta-search engines can be used for various applications in intelligent database systems (IDBS), which are database systems that incorporate artificial intelligence techniques to enhance their functionality and performance. Some of the applications are:

  - Information retrieval: This is the process of finding relevant information from a large collection of documents or data. Search engines and meta-search engines can help users to retrieve information by providing various features, such as natural language processing, query expansion, relevance feedback, ranking, and personalization.
  - Information extraction: This is the process of extracting structured or semi-structured information from unstructured or semi-structured sources, such as web pages, text, images, or audio. Search engines and meta-search engines can help users to extract information by providing various features, such as named entity recognition, relation extraction, sentiment analysis, and summarization.
  - Information integration: This is the process of combining information from multiple sources and presenting it in a unified way. Search engines and meta-search engines can help users to integrate information by providing various features, such as data fusion, data cleaning, data mapping, and data visualization.
  - Information analysis: This is the process of discovering patterns, trends, or insights from information. Search engines and meta-search engines can help users to analyze information by providing various features, such as data mining, machine learning, natural language generation, and recommendation systems.



### Internet spiders

- An Internet spider is a program designed to "crawl" over the World Wide Web, the portion of the Internet most familiar to general users, and retrieve locations of Web pages.
- It is sometimes referred to as a webcrawler, a search bot or simply a bot.
- Many search engines use webcrawlers to obtain links, which are filed away in an index.
- Their purpose is to index the content of websites all across the Internet so that those websites can appear in search engine results .
- Web crawlers copy pages for processing by a search engine, which indexes the downloaded pages so that users can search more efficiently.
- Web crawlers can also be used for other purposes, such as data mining, web scraping, web archiving, web testing, etc.
- Web crawlers follow a set of rules or policies to determine which pages to visit, how often to visit them, and how to download them.
- Some of the challenges faced by web crawlers are scalability, politeness, freshness, quality, and diversity.
- Web crawlers can be classified into different types based on their functionality, such as focused crawlers, incremental crawlers, deep crawlers, distributed crawlers, etc.
- Web crawlers can also be customized for specific domains or applications, such as academic crawlers, news crawlers, social media crawlers, etc.
- Web crawlers are an essential component of intelligent database systems, as they enable the collection and integration of data from heterogeneous and distributed sources on the Web.



### Data mining for the notes of the Unit 5 - Applications in IDBS in the subject of INTELLIGENT DATABASE SYSTEM

- Data mining is a process of discovering patterns in a large set of data and data warehouses using various techniques such as regression analysis, association, and clustering, classification, and outlier analysis.
- Data mining is a crucial component of successful analytics initiatives in organizations, as it can provide useful insights for business intelligence, advanced analytics, and real-time analytics applications .
- Data mining can be applied to various domains and industries, such as marketing, finance, healthcare, education, manufacturing, and security.
- Some of the common data mining applications are:
  - Customer segmentation: Data mining can help identify different groups of customers based on their demographics, preferences, behavior, and loyalty, and tailor marketing strategies accordingly.
  - Fraud detection: Data mining can help detect anomalous transactions, activities, or patterns that may indicate fraud, misuse, or abuse of resources, and alert the authorities or take preventive measures.
  - Recommendation systems: Data mining can help analyze the past purchases, ratings, or feedback of customers and recommend products, services, or content that may suit their needs or interests.
  - Text mining: Data mining can help extract useful information from unstructured text data, such as documents, emails, social media posts, or reviews, and perform tasks such as sentiment analysis, topic modeling, or summarization.
  - Web mining: Data mining can help analyze the data generated by web users, such as browsing history, search queries, or clicks, and perform tasks such as web personalization, web content analysis, or web structure analysis.
- Intelligent data mining is a subfield of data mining that incorporates intelligent techniques, such as artificial neural networks, fuzzy logic, genetic algorithms, or evolutionary computation, to enhance the performance, accuracy, or interpretability of data mining algorithms .
- Intelligent data mining can be applied to various intelligent systems and data mining problems, such as :
  - Intelligent data preprocessing: Intelligent data mining can help perform tasks such as data cleaning, data integration, data transformation, or data reduction, to improve the quality and usability of data for data mining.
  - Intelligent data analysis: Intelligent data mining can help perform tasks such as data exploration, data visualization, data modeling, or data evaluation, to discover and understand the patterns and relationships in data.
  - Intelligent data postprocessing: Intelligent data mining can help perform tasks such as data interpretation, data validation, data presentation, or data utilization, to communicate and apply the results of data mining to decision making or problem solving.
- Intelligent data mining can also be integrated with other intelligent techniques, such as expert systems, knowledge-based systems, or multi-agent systems, to create more advanced and complex intelligent data mining systems .



### Data mining tasks

Data mining is a computer-assisted technique used in analytics to process and explore large data sets. With data mining tools and methods, organizations can discover hidden patterns and relationships in their data. Data mining transforms raw data into practical knowledge.

Data mining tasks are designed to be semi-automatic or fully automatic and on large data sets to uncover patterns such as groups or clusters, unusual or over the top data called anomaly detection and dependencies such as association and sequential pattern.

Data mining tasks can be classified into two types: descriptive and predictive.

- Descriptive mining tasks define the common features of the data in the database, such as summary statistics, data visualization, clustering, and association analysis.
- Predictive mining tasks act in inference on the current information to develop predictions, such as classification, regression, and time-series analysis.

Some of the common data mining tasks are:

- Classification: It is the process of assigning a label or category to an object based on its features. For example, classifying an email as spam or not spam based on its content and sender.
- Prediction: It is the process of estimating the value of a variable or attribute for a new or unknown object based on its features. For example, predicting the price of a house based on its location, size, and amenities.
- Time-series analysis: It is the process of analyzing data that is collected over time to identify trends, patterns, cycles, and outliers. For example, analyzing the stock market data to forecast the future prices or movements.
- Association: It is the process of finding rules or patterns that describe the co-occurrence or correlation of items or events in a data set. For example, finding the products that are frequently bought together by customers in a supermarket.
- Clustering: It is the process of grouping objects that are similar to each other based on their features. For example, clustering customers based on their demographics, preferences, and behavior.
- Summarization: It is the process of creating a concise and meaningful representation of a large or complex data set. For example, summarizing the main topics or themes of a collection of documents or articles.

Data mining tasks are applied in various domains and applications, such as business, science, engineering, medicine, education, and social media. Some of the examples of data mining applications are:

- Customer segmentation and retention: Data mining can help businesses to identify and target their most profitable customers, as well as to retain them by offering personalized services or products.
- Fraud detection and prevention: Data mining can help detect and prevent fraudulent activities, such as credit card fraud, insurance fraud, or cyberattacks, by analyzing the patterns and anomalies in the data.
- Recommender systems: Data mining can help provide personalized recommendations to users based on their preferences, interests, and behavior, such as products, movies, books, or music.
- Sentiment analysis: Data mining can help analyze the opinions, emotions, and attitudes of people expressed in text, such as reviews, tweets, or comments, and classify them as positive, negative, or neutral.
- Text mining: Data mining can help extract useful information and knowledge from unstructured text data, such as keywords, topics, entities, relations, or summaries.
- Image analysis: Data mining can help process and analyze images to extract features, patterns, and objects, such as faces, logos, or scenes.



### Data mining tools for the notes of the Unit 5 - Applications in IDBS in the subject of INTELLIGENT DATABASE SYSTEM

- Data mining is the process of discovering useful patterns, trends, and relationships from large and complex data sets .
- Data mining tools are software applications that enable data analysts and business users to perform data mining tasks, such as data preparation, data modeling, data evaluation, and data visualization .
- Data mining tools can be classified into different categories based on their functionality, such as:
  - Statistical tools: These tools use statistical methods, such as regression, correlation, and hypothesis testing, to analyze data and identify significant variables and relationships. Examples of statistical tools are R, SAS, and SPSS.
  - Machine learning tools: These tools use artificial intelligence techniques, such as neural networks, decision trees, and support vector machines, to learn from data and make predictions or classifications. Examples of machine learning tools are TensorFlow, Scikit-learn, and Weka.
  - Visualization tools: These tools use graphical representations, such as charts, graphs, and maps, to display data and reveal patterns, trends, and outliers. Examples of visualization tools are Tableau, Power BI, and QlikView.
  - Database tools: These tools use database management systems, such as SQL Server, Oracle, and MongoDB, to store, query, and manipulate data. Examples of database tools are SQL Server Analysis Services, Oracle Data Mining, and MongoDB Compass.
- Data mining tools can be used for various applications in intelligent database systems, such as:
  - Customer segmentation: This application involves grouping customers based on their characteristics, preferences, and behaviors, to tailor marketing strategies and improve customer loyalty .
  - Fraud detection: This application involves identifying anomalous or suspicious transactions, activities, or behaviors, to prevent or minimize losses and risks .
  - Recommendation systems: This application involves suggesting relevant products, services, or content to customers or users, based on their past or current interactions, preferences, or feedback .
  - Text mining: This application involves extracting useful information, such as keywords, topics, sentiments, or entities, from unstructured text data, such as documents, emails, or social media posts .
  - Time series analysis: This application involves analyzing data that changes over time, such as sales, stock prices, or weather, to identify patterns, trends, cycles, or anomalies .



### Medical and legal information systems

- Medical information systems are systems that collect, store, process, and communicate health-related data for various purposes, such as diagnosis, treatment, research, and public health.
- Legal information systems are systems that deal with the creation, interpretation, application, and enforcement of laws and regulations, especially in the context of health informatics.
- Some of the applications of medical and legal information systems in intelligent database systems (IDBS) are:
  - Electronic medical records (EMRs), which are digital versions of patients' medical histories, diagnoses, treatments, medications, allergies, and other clinical information.
  - Clinical decision support systems (CDSSs), which are software tools that provide guidance and recommendations to health care providers based on evidence-based rules, algorithms, and data analysis.
  - Medical imaging systems, which are systems that capture, process, and display images of the human body using various modalities, such as X-ray, ultrasound, MRI, and CT scan.
  - Medical expert systems, which are systems that use artificial intelligence techniques, such as rule-based reasoning, machine learning, and natural language processing, to mimic the knowledge and skills of human experts in specific domains, such as diagnosis, prognosis, and therapy.
  - Health information exchange (HIE), which is the process of sharing health-related data among different organizations, such as hospitals, clinics, pharmacies, and laboratories, using standardized formats and protocols.
  - Health information privacy and security, which are the legal and ethical issues that arise from the collection, storage, use, and disclosure of personal health information, such as the protection of patients' rights, the compliance with laws and regulations, and the prevention of data breaches and cyberattacks   .



### Medical Information Systems

- Medical information systems are computer-based systems that store, process, and communicate health-related data for clinical, administrative, and research purposes.
- Medical information systems can support various functions in healthcare, such as patient care, diagnosis, treatment, decision making, quality improvement, and research.
- Medical information systems can be classified into different types, such as:
  - Electronic medical records (EMRs), which are digital versions of paper-based medical charts that contain patient demographics, medical history, medications, allergies, laboratory results, and other clinical data.
  - Electronic health records (EHRs), which are interoperable and integrated systems that allow the exchange of patient information across different healthcare providers and settings.
  - Personal health records (PHRs), which are patient-controlled systems that allow individuals to access, manage, and share their own health information with authorized parties.
  - Clinical decision support systems (CDSSs), which are systems that provide clinicians with evidence-based recommendations, alerts, reminders, and feedback to improve the quality and safety of patient care.
  - Health information exchange (HIE), which is the process of electronically transferring health information among different organizations and systems.
  - Telemedicine and telehealth, which are the use of information and communication technologies to deliver healthcare services and education remotely.
  - Wireless medical devices, which are devices that use wireless technologies to monitor, diagnose, or treat patients, such as wearable sensors, implantable devices, and mobile apps.
  - Artificial intelligence and machine learning, which are the use of advanced algorithms and data analysis techniques to perform tasks that normally require human intelligence, such as diagnosis, prognosis, treatment planning, and drug discovery.
- Medical information systems can provide various benefits for healthcare, such as:
  - Improving the efficiency and accuracy of data collection, storage, and retrieval.
  - Enhancing the coordination and continuity of care among different providers and settings.
  - Empowering patients to participate in their own health management and education.
  - Supporting clinical decision making and reducing errors and adverse events.
  - Facilitating quality improvement and performance measurement.
  - Enabling research and innovation in healthcare.
- Medical information systems also face various challenges and limitations, such as:
  - Protecting the privacy and security of health information from unauthorized access, use, or disclosure.
  - Ensuring the reliability, validity, and completeness of health data.
  - Addressing the ethical, legal, and social implications of health information technology.
  - Overcoming the technical, organizational, and cultural barriers to the adoption and use of health information systems.
  - Evaluating the effectiveness, impact, and cost-effectiveness of health information systems.



### Legal information systems

- Legal information systems are systems that store, process, and retrieve legal information, such as legislation, case law, and scholarly works.
- Legal information systems are important for providing access to the law to laymen and legal professionals, as well as for supporting legal tasks such as research, drafting, negotiation, consulting, management, and argumentation.
- Legal information systems face several challenges, such as:
  - Dealing with law-specific words and phrases, which may have different meanings in legal or common-speech contexts, or which may exist solely in law.
  - Handling the complexity and diversity of legal sources, which may vary in structure, format, language, jurisdiction, and authority.
  - Incorporating legal reasoning and argumentation, which may involve logic, analogy, precedent, policy, and evidence.
  - Adapting to the dynamic and evolving nature of the law, which may change due to new legislation, judicial decisions, or social norms.
- Legal information systems can be classified into different types, such as:
  - Legal information retrieval systems, which aim to find and rank relevant legal documents or passages based on a user query.
  - Legal information extraction systems, which aim to identify and extract specific information or entities from legal texts, such as names, dates, facts, or arguments.
  - Legal information analysis systems, which aim to analyze and summarize legal texts, such as by identifying the main issues, arguments, or outcomes of a case.
  - Legal information generation systems, which aim to produce legal texts, such as by drafting contracts, pleadings, or opinions.
  - Legal information management systems, which aim to organize and store legal information, such as by creating databases, indexes, or ontologies.
  - Legal information briefing systems, which aim to provide legal information and advice to users, such as by answering questions, explaining concepts, or suggesting actions.
- Legal information systems can benefit from various techniques and methods, such as:
  - Natural language processing, which enables the processing of natural language texts, such as by parsing, tagging, or translating them.
  - Information retrieval, which enables the searching and ranking of relevant documents or passages, such as by using keywords, vectors, or graphs.
  - Machine learning, which enables the learning and prediction of patterns or outcomes from data, such as by using classification, clustering, or regression.
  - Knowledge representation and reasoning, which enables the representation and inference of facts, rules, or arguments, such as by using logic, ontologies, or argumentation frameworks.
  - Artificial intelligence, which enables the simulation of human intelligence and behavior, such as by using agents, planning, or dialogue.



### Conclusions for the notes of the Unit 5 - Applications in IDBS in the subject of INTELLIGENT DATABASE SYSTEM

- Intelligent database systems (IDBS) are systems that integrate database management systems (DBMS) with artificial intelligence (AI) techniques to provide enhanced functionality, performance, and usability.
- IDBS can be classified into three categories based on the level of integration between DBMS and AI: loosely coupled, tightly coupled, and fully integrated.
- Loosely coupled IDBS are systems that use separate DBMS and AI components that communicate through a common interface. They are easy to implement and maintain, but have limited interoperability and efficiency.
- Tightly coupled IDBS are systems that embed AI techniques into the DBMS or vice versa. They have better interoperability and efficiency, but are more complex and difficult to implement and maintain.
- Fully integrated IDBS are systems that merge DBMS and AI into a single unified system. They have the highest level of interoperability and efficiency, but are very challenging to design and develop.
- IDBS have various applications in different domains, such as decision support, knowledge discovery, natural language processing, multimedia, spatial and temporal data, and web data.
- Decision support IDBS are systems that assist users in making complex and uncertain decisions by providing relevant information, analysis, and recommendations. They use techniques such as expert systems, fuzzy logic, neural networks, and genetic algorithms.
- Knowledge discovery IDBS are systems that discover useful and novel patterns, rules, and trends from large and complex data sets. They use techniques such as data mining, machine learning, and data visualization.
- Natural language processing IDBS are systems that enable users to interact with databases using natural language queries and responses. They use techniques such as natural language understanding, natural language generation, and speech recognition and synthesis.
- Multimedia IDBS are systems that store, retrieve, and manipulate multimedia data, such as images, audio, video, and text. They use techniques such as content-based retrieval, feature extraction, and compression.
- Spatial and temporal IDBS are systems that handle data that have spatial and temporal dimensions, such as geographic information systems (GIS) and time series databases. They use techniques such as spatial and temporal indexing, querying, and reasoning.
- Web data IDBS are systems that deal with data that are distributed, heterogeneous, and dynamic on the web. They use techniques such as web crawling, web mining, web querying, and web services.

