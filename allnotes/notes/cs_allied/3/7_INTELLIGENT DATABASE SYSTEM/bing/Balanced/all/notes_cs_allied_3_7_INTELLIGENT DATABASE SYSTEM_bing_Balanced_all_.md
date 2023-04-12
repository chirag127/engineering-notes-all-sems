

# INTELLIGENT DATABASE SYSTEM

- An intelligent database system is a system that manages information, rather than simple data, and presents it in such a way that is natural and informative for users .
- An intelligent database system has three levels of intelligence: high level tools, the user interface and the database engine.
- High level tools manage data quality and automatically discover relevant patterns in the data with a process called data mining.
- The user interface provides natural language processing, speech recognition, graphical visualization and other features to facilitate user interaction .
- The database engine supports advanced data models, such as object-oriented, semantic and deductive, and provides efficient query processing and optimization .
- An intelligent database system can also integrate artificial intelligence components, such as expert systems, neural networks, fuzzy logic and genetic algorithms, to enhance its functionality and performance .
- An intelligent database system can provide benefits such as improved data quality, reduced data redundancy, increased user satisfaction, faster decision making and lower costs .



## Unit 1 - Introduction to IDBS

- IDBS stands for Integrated Data and Business Systems. It is a software platform that enables organizations to manage, analyze, and share data across different domains and applications.
- IDBS provides a unified environment for data capture, processing, visualization, and collaboration. It supports various types of data, such as text, images, audio, video, and structured data.
- IDBS can be used for various purposes, such as research and development, quality control, regulatory compliance, business intelligence, and decision making.
- IDBS consists of several components, such as:

  - IDBS Hub: The core component that provides the infrastructure and services for data management and integration. It includes features such as data storage, security, access control, audit trail, workflow, and search.
  - IDBS Apps: The applications that run on top of the IDBS Hub and provide specific functionality for different domains and use cases. For example, IDBS E-WorkBook is an app that allows users to create, edit, and share electronic notebooks for scientific experiments.
  - IDBS Connectors: The tools that enable data exchange and integration between IDBS and external systems, such as databases, instruments, web services, and cloud platforms.
  - IDBS SDK: The software development kit that allows developers to create custom apps and connectors for IDBS using various programming languages and frameworks.

- IDBS can be deployed on-premise, in the cloud, or in a hybrid mode. It can also be accessed through various devices, such as desktops, laptops, tablets, and smartphones.



### Informal definition of the domain for the notes of the Unit 1 - Introduction to IDBS in the subject of INTELLIGENT DATABASE SYSTEM

- A domain is a set of possible values for an attribute or a variable in a database or a program.
- An informal definition of a domain is a description of the meaning, type, format, and constraints of the values in a natural language, such as English.
- For example, an informal definition of the domain for the attribute `name` in a table of students could be: "The name of the student, consisting of a first name and a last name, separated by a space. The name should not be empty or contain any numbers or special characters."
- An informal definition of the domain for the variable `x` in a program that calculates the area of a circle could be: "The radius of the circle, a positive real number."
- An informal definition of the domain helps to understand the semantics and the validity of the data or the input, but it is not precise or formal enough to be used by a computer system.



# General characteristics of IDBSs

- IDBS stands for Intelligent Database Systems, which are full-text databases with artificial intelligence components that interact with users to ensure that users are supplied all relevant information.
- IDBSs manage information (rather than data) in a way that appears natural to users and which goes beyond simple record keeping.
- IDBSs have intelligent database interfaces that are cache-based and can efficiently access one or more database management systems, remote or not, and provide flexible options for conducting queries.
- IDBSs use techniques such as natural language processing, knowledge representation, reasoning, machine learning, and data mining to provide intelligent functionalities such as information retrieval, information extraction, information integration, information analysis, and information synthesis.
- IDBSs can handle complex, uncertain, incomplete, and dynamic information, and can adapt to changing user needs and preferences.
- IDBSs can support various applications such as decision support systems, collaborative systems, natural language processing systems, image and text processing systems, and Internet technologies.



# Data models and the relational data model

## Data models
- A data model is a **conceptual representation** of the data, their relationships, and the rules that govern them.
- A data model helps to **organize**, **understand**, and **communicate** the data and their meaning.
- A data model also provides a way to **implement** the data in a physical system, such as a database or a data warehouse.
- There are different types of data models, such as **hierarchical**, **network**, **relational**, **entity-relationship**, **object-oriented**, and **dimensional**.

## Relational data model
- The relational data model is the most widely used data model for data storage and processing.
- The relational data model was proposed by **E.F. Codd** in 1970.
- The relational data model is based on the **mathematical concept** of a relation, which is a **set of tuples** (or rows) with the same **attributes** (or columns).
- In the relational data model, data are stored as **tables** (or relations), where each row represents an **entity** (or an instance of data) and each column represents an **attribute** (or a property of the entity).
- The tables are related to each other by **keys**, which are attributes that uniquely identify each row in a table.
- A **primary key** is a key that identifies each row in a table, and a **foreign key** is a key that references a primary key in another table.
- The relational data model supports the operations of **data definition**, **data manipulation**, and **transaction management** .
- Data definition allows the creation, modification, and deletion of tables and their attributes.
- Data manipulation allows the insertion, update, deletion, and retrieval of data from the tables.
- Transaction management ensures the **consistency**, **isolation**, **durability**, and **atomicity** of the data operations.
- The relational data model is based on a set of **relational algebra** operations, such as **selection**, **projection**, **join**, **union**, **intersection**, and **difference**, that can be applied to the tables to manipulate and query the data.
- The relational data model can be expressed using a **relational schema**, which is a **diagram** that shows the tables, their attributes, and their relationships.
- The relational schema can also include **constraints**, which are **rules** that specify the **validity** and **integrity** of the data in the tables.
- An example of a constraint is a **domain constraint**, which defines the **range of values** that an attribute can take.
- Another example is a **referential integrity constraint**, which ensures that a foreign key value in one table matches a primary key value in another table .
- The relational data model can be implemented using a **relational database management system (RDBMS)**, which is a software system that provides the functionality of data definition, data manipulation, and transaction management for the relational data model.
- Some examples of RDBMS are **Oracle**, **MySQL**, **PostgreSQL**, and **SQLite** .



# A taxonomy of intelligent database systems

Intelligent database systems (IDBSs) are systems that combine database and artificial intelligence techniques to provide enhanced data management and analysis capabilities. IDBSs can support various tasks such as data quality, data mining, data integration, data visualization, natural language processing, and knowledge representation and reasoning.

There are different ways to classify IDBSs based on their origin, architecture, functionality, and application domain. One possible taxonomy of IDBSs is as follows  :

- **Efforts originated in a database context**: These are IDBSs that extend the traditional database systems with some form of intelligence, either statically or dynamically.
  - **Static extensions**: These are IDBSs that extend the expressive power of traditional database data models, such as relational, object-oriented, or XML, with additional features such as rules, constraints, triggers, views, or semantic annotations. Examples of static extensions are deductive databases, active databases, and semantic databases.
  - **Dynamic extensions**: These are IDBSs that introduce some form of reasoning inside the database management systems (DBMSs), such as inference engines, learning algorithms, or optimization techniques. Examples of dynamic extensions are fuzzy databases, probabilistic databases, and evolutionary databases.
- **Efforts originated in an artificial intelligence context**: These are IDBSs that use artificial intelligence systems, such as knowledge-based systems, expert systems, or neural networks, to access, manipulate, or analyze data stored in database systems.
  - **Basic solutions**: These are IDBSs that couple knowledge-based systems and DBMSs, either loosely or tightly, to provide a unified interface for data and knowledge access and manipulation. Examples of basic solutions are KIDS, KRAFT, and K-REP.
  - **Advanced solutions**: These are IDBSs that attempt to use artificial intelligence systems as the core of the data management and analysis, rather than as an add-on component. Examples of advanced solutions are KODAMA, LOOM, and CYC.

Another possible taxonomy of IDBSs is based on their application domain, such as:

- **Business intelligence**: These are IDBSs that support decision making, planning, forecasting, and analysis of business data, such as sales, marketing, finance, or operations. Examples of business intelligence IDBSs are OLAP, data warehousing, data mining, and business rules systems.
- **Scientific intelligence**: These are IDBSs that support scientific research, experimentation, simulation, and discovery of scientific data, such as biology, chemistry, physics, or astronomy. Examples of scientific intelligence IDBSs are bioinformatics, cheminformatics, physics-based modeling, and scientific workflows.
- **Social intelligence**: These are IDBSs that support social interaction, communication, collaboration, and understanding of social data, such as text, images, videos, or audio. Examples of social intelligence IDBSs are natural language processing, information extraction, sentiment analysis, and recommender systems.



# Guidelines for using intelligent database systems

- An intelligent database system (IDBS) is a system that manages information, rather than simple data, and presents it in such a way that is natural and informative for users .
- An IDBS can perform tasks such as data analysis, knowledge discovery, natural language processing, reasoning, learning, and adaptation.
- An IDBS can also provide intelligent interfaces that allow users to interact with the system in a flexible and efficient way.
- Some of the benefits of using an IDBS are:
  - It can handle complex and dynamic data and queries that traditional databases cannot.
  - It can provide more accurate and relevant results by incorporating domain knowledge and user preferences.
  - It can improve the usability and accessibility of the system by using natural language and graphical representations.
  - It can enhance the performance and scalability of the system by using caching and parallel processing techniques.
- Some of the challenges of using an IDBS are:
  - It requires more sophisticated and robust algorithms and techniques to deal with uncertainty, inconsistency, and incompleteness of data and information.
  - It involves more complex and heterogeneous data sources and formats that need to be integrated and harmonized.
  - It demands more computational and storage resources and higher security and privacy standards.
  - It faces more ethical and social issues regarding the trustworthiness, accountability, and transparency of the system.
- Some of the guidelines for using an IDBS are:
  - Identify the goals and requirements of the system and the users, and choose the appropriate IDBS architecture and components.
  - Design and implement the IDBS using the best practices and standards of software engineering, data management, and artificial intelligence.
  - Evaluate and test the IDBS using appropriate metrics and methods, and collect feedback from the users and stakeholders.
  - Monitor and maintain the IDBS, and update it regularly to cope with the changes and challenges of the data and information environment.



## Unit 2 - Semantic Data Models

- Semantic data models are conceptual data models that capture the meaning and relationships of data in a domain of interest.
- Semantic data models use high-level concepts, such as entities, attributes, and relationships, to represent data and their semantics.
- Semantic data models can be used to design databases, ontologies, knowledge bases, and other information systems that require a rich and expressive representation of data.
- Semantic data models can also be used to facilitate data integration, interoperability, and reasoning across different data sources and applications.
- Semantic data models can be classified into two main categories: entity-relationship models and semantic network models.

### Entity-relationship models

- Entity-relationship models are semantic data models that use entities, attributes, and relationships to represent data and their semantics.
- Entities are the basic units of data that have a unique identity and a set of properties or attributes.
- Attributes are the characteristics or features of entities that describe their state or value.
- Relationships are the associations or connections between entities that express their logical or semantic dependencies.
- Entity-relationship models can be represented graphically using entity-relationship diagrams (ERDs) or textually using entity-relationship schemas (ERSs).
- Entity-relationship models can be used to design relational databases, which store data in tables consisting of rows (records) and columns (fields).
- Entity-relationship models can also be used to design object-oriented databases, which store data in objects consisting of attributes (fields) and methods (functions).

### Semantic network models

- Semantic network models are semantic data models that use nodes, links, and labels to represent data and their semantics.
- Nodes are the basic units of data that can represent entities, concepts, events, or any other meaningful unit of information.
- Links are the connections or associations between nodes that express their logical or semantic relationships.
- Labels are the names or symbols that identify nodes and links and specify their types or roles.
- Semantic network models can be represented graphically using semantic network diagrams (SNDs) or textually using semantic network schemas (SNSs).
- Semantic network models can be used to design ontologies, which are formal and explicit specifications of the concepts and relationships in a domain of interest.
- Semantic network models can also be used to design knowledge bases, which are collections of facts and rules that can be used for reasoning and inference.



# Nested and Semantic Data Models

- Nested data models are a way of representing hierarchical data structures, such as trees or graphs, in a relational database. Nested data models allow data to be stored in a nested manner, where each record can have one or more subrecords within it. Nested data models can be useful for storing complex data that has a natural hierarchy, such as XML or JSON documents, or for modeling recursive relationships, such as parent-child or ancestor-descendant.
- Semantic data models are a way of representing the meaning and context of data, rather than just the structure and syntax. Semantic data models use concepts, attributes, and relationships to describe the data and its semantics, rather than tables, columns, and keys. Semantic data models can be useful for capturing the business logic and rules of an application domain, or for enabling interoperability and integration of data across different sources and systems.
- Nested and semantic data models are related in the sense that both aim to provide a higher level of abstraction and expressiveness than the traditional relational data model. However, they differ in their focus and scope. Nested data models are mainly concerned with how to store and manipulate hierarchical data efficiently and effectively, while semantic data models are mainly concerned with how to describe and understand the data and its meaning. Nested data models are more suitable for data-intensive applications that deal with complex and nested data structures, while semantic data models are more suitable for knowledge-intensive applications that deal with diverse and heterogeneous data sources.



# Introduction for the notes of the Unit 2 - Semantic Data Models in the subject of INTELLIGENT DATABASE SYSTEM

- Semantic data models are high-level conceptual models that capture the meaning and structure of data in a domain of interest.
- Semantic data models use concepts such as entities, attributes, relationships, and constraints to represent data and their semantics.
- Semantic data models are more expressive and intuitive than traditional data models, such as relational or hierarchical models, which focus on the physical representation and storage of data.
- Semantic data models can be used for various purposes, such as database design, data integration, data analysis, and knowledge representation.
- Semantic data models can be classified into two main categories: object-based and logic-based models.
- Object-based models use objects as the basic units of data abstraction. Objects have identity, properties, and behavior. Objects can be organized into classes, hierarchies, and networks. Examples of object-based models are Entity-Relationship (ER) model, Object-Oriented (OO) model, and Semantic Network (SN) model.
- Logic-based models use logic as the basis for data representation and manipulation. Logic-based models use predicates, variables, constants, and quantifiers to express facts, rules, and queries about data. Examples of logic-based models are Functional Data Model (FDM), Deductive Database (DDB), and Description Logic (DL) model.



# The nested relational model

- The nested relational model is an extension of the relational model in which domains may be either atomic or relation-valued .
- This allows a complex object to be represented by a single tuple of a nested relation, which has a one-to-one correspondence between data items and objects.
- A nested relation can be seen as a relation of relations, where each tuple may contain one or more sub-relations as attribute values.
- A nested relation can be flattened into a conventional relation by applying a join operation on the sub-relations.
- A nested relation can also be constructed from a conventional relation by applying a group operation, which partitions the tuples into sub-relations based on some grouping attributes.
- The nested relational model can support more complex data structures and queries than the standard relational model, such as recursive queries, aggregation, and inheritance .
- The nested relational model can also be seen as a special case of the object-relational model, which allows more general types of attributes and methods .



# Semantic models for the notes of the Unit 2 - Semantic Data Models in the subject of INTELLIGENT DATABASE SYSTEM

- A semantic data model is a method of structuring data in order to represent it in a specific logical way. It is a conceptual data model that includes semantic information that adds a basic meaning to the data and the relationships that lie between them.
- A semantic data model works basically by creating relationships between data when the data is organized. This allows the data to have meaning without human intervention or additional processing. The data is organized into three essential parts—the first data element or object, the relationship, and then the second data element or object.
- A semantic data model provides users with significantly more useful abstractions than the SQL data model and queries. These abstractions are more composable and reusable than queries. A semantic data model also enables efficient data consumption by hiding the complexity and heterogeneity of the underlying data sources.
- A semantic data model helps data management manage and oversee the company's overall data, thus increasing decision-making capabilities. There are four primary goals of semantic data models:
  - Data resource planning: The semantic data model can be used in the initial stages of project planning to provide the necessary data resources.
  - Data integration: The semantic data model can be used to integrate data from different sources and formats, and to resolve semantic conflicts and inconsistencies.
  - Data quality: The semantic data model can be used to ensure the accuracy, completeness, timeliness, and relevance of the data.
  - Data governance: The semantic data model can be used to define the roles, responsibilities, policies, and standards for the data lifecycle.
- A semantic data model is a high-level semantics-based database description and structuring formalism (database model) for databases. This database model is designed to capture more of the meaning of an application environment than is possible with contemporary database models.
- A semantic data model can be developed using various techniques, such as:
  - Upper ontologies: These are general and abstract models that capture the common concepts and relations across domains.
  - Design patterns: These are reusable and modular models that capture the best practices and solutions for specific problems or scenarios.
  - Standard and reference models: These are authoritative and normative models that define the common terms and structures for a domain or industry.
  - Public models and datasets: These are openly available and widely used models and datasets that provide rich and diverse sources of knowledge and information.
  - Semantic model mining: This is the process of extracting, analyzing, and transforming semantic models from various sources, such as text, databases, web pages, etc.



# Hyper-semantic data models

- Hyper-semantic data models are a new class of models that combine the features of semantic data models and artificial intelligence concepts .
- Semantic data models are high-level models that capture the meaning and structure of an application environment using object-oriented concepts such as entities, attributes, relationships, and constraints.
- Artificial intelligence concepts include heuristics, uncertainty, inference, and learning, which can enhance the expressiveness and usability of data models .
- Hyper-semantic data models can be used to represent complex and dynamic domains that require knowledge-based reasoning and decision making .
- An example of a hyper-semantic data model is the Knowledge/Data Model (KDM), which extends the Entity-Relationship Model (ERM) with additional constructs such as rules, probabilities, and fuzzy sets  .
- Hyper-semantic data models can provide the following benefits  :
  - Data resource planning: They can help in the initial stages of project planning to identify the necessary data resources and their interrelationships.
  - Data analysis and design: They can facilitate the analysis and design of data structures and schemas that reflect the semantics and logic of the application domain.
  - Data manipulation and querying: They can support data manipulation and querying operations that incorporate knowledge and uncertainty, such as inference, aggregation, and classification.
  - Data integration and interoperability: They can enable the integration and interoperability of heterogeneous and distributed data sources that have different levels of abstraction and representation.



# Object-oriented approaches to semantic data modeling

- Semantic data modeling is a high-level database description and structuring formalism that captures more of the meaning of an application environment than conventional database models.
- Object-oriented modeling is a technique that uses objects as the basic units of data representation and manipulation, where an object is a combination of data and behavior.
- Object-oriented approaches to semantic data modeling aim to decrease the semantic gap between the system and the real world by using terminology that is the same as the functions that users perform.
- Some of the benefits of object-oriented approaches to semantic data modeling are:
  - They support data abstraction, inheritance, and encapsulation, which are important for data integrity, reusability, and extensibility.
  - They can represent complex and dynamic data structures, such as spatiotemporal data, multimedia data, and network data, by using object identity, object classes, and object relationships.
  - They can facilitate query processing and optimization by using object methods, polymorphism, and overloading.
- Some of the challenges of object-oriented approaches to semantic data modeling are:
  - They require a clear and consistent definition of the semantics of objects, classes, and relationships, which may not be easy or universal for different domains and applications.
  - They may introduce some redundancy and inconsistency in the data representation and manipulation, such as multiple inheritance, multiple representation, and update anomalies.
  - They may not be compatible with existing relational database systems and standards, which may require data conversion, mapping, or integration.



# Object-oriented database systems

- An object-oriented database (OOD) is a database system that can work with complex data objects — that is, objects that mirror those used in object-oriented programming languages .
- In object-oriented programming (OOP), everything is an object. An object has a unique identity, a state, and a behavior. An object can also have attributes (properties) and methods (functions) that define its characteristics and operations .
- An object-oriented database management system (OODBMS) is a database management system (DBMS) that supports the modelling and creation of data as objects .
- An OODBMS allows users to define their own data types, classes, and inheritance hierarchies, and to store, retrieve, and manipulate objects using object-oriented query languages .
- An OODBMS also supports features such as encapsulation, polymorphism, and dynamic binding, which enable data abstraction, modularity, and reusability .
- An OODBMS is different from a relational database (RDB), which is based on tables, rows, and columns. A relational database stores data in a normalized form, which reduces data redundancy but also requires complex joins and foreign keys to represent relationships between entities .
- A third type of database, called object-relational database (ORDB), is a hybrid of both approaches. An ORDB extends the relational model with object-oriented features, such as user-defined types, inheritance, and methods. An ORDB can store both structured and unstructured data, and can use both SQL and object-oriented query languages .
- Some examples of object-oriented databases are MongoDB, db4o, ObjectDB, and Versant Object Database. Some examples of object-relational databases are PostgreSQL, Oracle, and SQL Server .



# Basic concepts of a core object-oriented data model

- A core object-oriented data model is a data model based on object-oriented programming, associating methods (procedures) with objects that can benefit from class hierarchies.
- A core object-oriented data model consists of the following basic object-oriented concepts:
  - Object and object identifier: Any real world entity is uniformly modeled as an object (associated with a unique id: used to pinpoint an object to retrieve).
  - Class and instance: A class is a collection of objects that share the same structure and behavior. An instance is a specific object that belongs to a class.
  - Attribute: An attribute is a property or characteristic of an object that describes its state or value.
  - Method: A method is a function or procedure that defines the behavior or operation of an object.
  - Inheritance: Inheritance is a mechanism that allows a class to inherit the structure and behavior of another class, called the superclass or parent class. The inheriting class is called the subclass or child class.
  - Polymorphism: Polymorphism is the ability of an object to exhibit different behaviors depending on the context or situation. For example, a method can have different implementations in different subclasses, but can be invoked by the same name.
  - Encapsulation: Encapsulation is the principle of hiding the internal details or implementation of an object from the outside world. Only the interface or contract of the object is exposed to other objects or users.
- A core object-oriented data model is based on real world situations. These situations are represented as objects, with different attributes. All these objects have multiple relationships between them.
- A core object-oriented data model can store complex data types, such as audio, video, images, etc., that are not suitable for relational databases.
- A core object-oriented data model employs standardized schemas and formal techniques. This provides a common, consistent, and predictable way of defining and managing data resources across an organization, or even beyond. Ideally, data models are living documents that evolve along with changing business needs.



# Comparison with other data models

Semantic data models are a type of conceptual data models that aim to capture the meaning and structure of data in a domain. They differ from other data models in several aspects, such as:

- They support relationships, data abstraction, inheritance, constraints, unstructured objects, and dynamic properties of an application.
- They use high-level concepts, such as entities, attributes, and relationships, to describe the data and its semantics.
- They can represent complex data types, such as multimedia, spatial, temporal, and fuzzy data.
- They can integrate data from multiple sources and provide a unified view of the data.

Some examples of semantic data models are:

- Entity-relationship model: A graphical representation of entities and their relationships in a domain. It is widely used for database design and analysis.
- Functional data model: A representation of data as functions that map values from one domain to another. It is based on the mathematical theory of functions and can express complex data transformations.
- Object-oriented data model: A representation of data as objects that have attributes and methods. It supports inheritance, polymorphism, encapsulation, and abstraction. It is suitable for modeling complex and dynamic data.
- Semantic network: A representation of data as nodes and links that have labels and properties. It can capture semantic associations and hierarchies among data elements. It is useful for knowledge representation and reasoning.
- Ontology: A representation of data as concepts and their relationships in a domain. It can define the vocabulary, axioms, and rules of a domain. It is used for semantic interoperability and data integration.



# Query languages and query processing for semantic data models

- A query language is a formal language that allows users to specify queries and manipulate data in a database.
- A query processing is the process of translating a query into a sequence of operations that can be executed efficiently by the database system.
- A semantic data model is a data model that captures the meaning and relationships of the data, rather than the structure and format.
- Semantic data models can be classified into two main categories: graph-based and logic-based.
- Graph-based semantic data models use nodes and edges to represent entities and relationships, such as RDF, property graphs, and conceptual graphs.
- Logic-based semantic data models use predicates and rules to represent facts and inference, such as Datalog, Prolog, and description logic.
- Query languages and query processing for semantic data models differ from those for relational data models in several aspects, such as:
  - The use of identifiers, labels, and types to distinguish entities and relationships.
  - The support for complex data structures, such as nested collections, hierarchies, and networks.
  - The ability to express semantic queries, such as path queries, pattern matching, and reasoning.
  - The challenges of optimizing semantic queries, such as query rewriting, indexing, and parallelization.
- Some examples of query languages and query processing for semantic data models are:
  - SPARQL, a standard query language for RDF graphs, which supports graph pattern matching, optional and filter clauses, and aggregation functions.
  - Cypher, a declarative query language for property graphs, which supports pattern matching, projections, and subqueries.
  - Datalog, a logic programming language for deductive databases, which supports recursive rules, negation, and stratified semantics.
  - ATLaS, an extension of SQL for data mining, which supports sequences, episodes, and association rules.
  - CQL, a query language for data streams, which supports window specifications, stream-to-relation and relation-to-stream operators, and continuous queries.



# Operational aspects of semantic data models

Semantic data models (SDMs) are high-level conceptual models that describe the meaning and structure of data in a domain. They use concepts such as objects, classes, attributes, relationships, and constraints to represent the data and its semantics. SDMs can be used for various purposes, such as database design, data integration, data analysis, and data visualization.

Some of the operational aspects of SDMs are:

- **Classification**: This is the process of grouping objects in a domain by their common characteristics or properties. For example, a class of employees can be defined by their attributes such as name, salary, department, etc. Classification can also involve defining subclasses and superclasses, which represent more specific or general concepts, respectively. For example, a subclass of employees can be managers, who have additional attributes such as subordinates, budget, etc. Classification can use the "instance of" relation to link objects to their classes.
- **Aggregation**: This is the process of defining a new object from a set of objects that become its components or parts. For example, a project can be defined as an aggregation of tasks, resources, and deadlines. Aggregation can use the "has a" relation to link objects to their components. Aggregation can also involve defining composite and atomic objects, which represent objects that can or cannot be further decomposed, respectively. For example, a task can be a composite object that has subtasks, while a resource can be an atomic object that has no components.
- **Association**: This is the process of defining a relationship between two or more objects that are not components of each other. For example, an employee can be associated with a project by the role they play in it, such as leader, member, or reviewer. Association can use the "related to" relation to link objects by their roles. Association can also involve defining cardinality and participation constraints, which specify how many objects can be involved in a relationship and whether they are mandatory or optional, respectively. For example, a project must have at least one leader and one member, but can have zero or more reviewers.
- **Generalization**: This is the process of defining a common concept or abstraction that covers multiple specific concepts or cases. For example, a person can be a generalization of an employee, a customer, a supplier, etc. Generalization can use the "is a" relation to link objects by their commonality. Generalization can also involve defining inheritance and polymorphism, which specify how attributes and behaviors are shared or overridden by subclasses and instances, respectively. For example, a person inherits the attribute of name, but a customer overrides the behavior of buying products.



# Systems for the notes of the Unit 2 - Semantic Data Models in the subject of INTELLIGENT DATABASE SYSTEM

- A semantic data model is a high-level, conceptual data model that includes semantic information that adds a basic meaning to the data and the relationships that lie between them .
- A semantic data model is designed to capture more of the meaning of an application environment than is possible with contemporary database models.
- A semantic data model is an abstraction that defines how the stored symbols (the instance data) relate to the real world.
- A semantic data model can express and exchange information that enables interoperability and integration of heterogeneous data sources.
- A semantic data model can support natural language queries, reasoning, and inference over the data.
- A semantic data model can use various techniques to structure the data, such as:
  - Classification: This classifies different objects in objective reality by using “instance of” relations, such as “John is an instance of Person”.
  - Aggregation: Aggregation defines a new object from a set of objects that become its components using “has a” relations, such as “A car has a wheel”.
  - Generalization: Generalization defines a new object from a set of objects that share some common properties using “is a” relations, such as “A dog is a mammal”.
  - Association: Association defines a new object from a set of objects that are related by some criterion using “is related to” relations, such as “A book is related to an author”.
- A semantic data model can use various notations to represent the data, such as:
  - Entity-relationship diagrams: These use graphical symbols to show the entities, attributes, and relationships in the data.
  - Semantic networks: These use nodes and links to show the concepts and relations in the data.
  - Frames: These use slots and fillers to show the properties and values of the data.
  - Ontologies: These use formal logic and vocabularies to show the concepts, relations, and axioms in the data.



# The ODMG Standard for Semantic Data Models

- The ODMG (Object Database Management Group) was a consortium of object database vendors that aimed to provide a standard data model for object databases, similar to SQL for relational databases .
- The ODMG standard consisted of four components:
  - The Object Model: a data model that defines the basic concepts of objects, literals, collections, types, inheritance, relationships, and operations.
  - The Object Definition Language (ODL): a language for specifying the schema of an object database, based on the object model.
  - The Object Query Language (OQL): a language for querying and manipulating data in an object database, based on the object model and ODL.
  - The Object Interchange Format (OIF): a format for exchanging data between different object databases or other systems, based on the object model and ODL.
- The ODMG standard also provided language bindings for C++, Java, and Smalltalk, to allow programmers to use the ODMG components in their applications.
- The ODMG standard was intended to support semantic data models, which are high-level data models that capture more of the meaning and constraints of an application domain than conventional data models.
- Semantic data models use concepts such as entities, attributes, relationships, and rules to describe the data and its semantics.
- Semantic data models can be mapped to the ODMG object model, by using objects to represent entities and attributes, collections to represent relationships, types and inheritance to represent categories and subcategories, and operations to represent rules and constraints.
- The ODMG standard was completed in 2001 and was disbanded, as it did not gain widespread acceptance by the object database vendors or the market. However, some of its concepts and features have influenced other standards and technologies, such as XML, RDF, and UML.



# The object-relational data model

- The object-relational data model is a hybrid of the object-oriented and the relational data models, which combines the features of both paradigms.
- The object-relational data model supports objects, classes, inheritance, methods, and polymorphism, as well as data types, tables, keys, constraints, and queries of the relational model.
- The object-relational data model allows users to define complex data types and operations on them, as well as to inherit and extend existing types and operations.
- The object-relational data model aims to overcome the limitations of the relational model, such as the impedance mismatch, the lack of support for complex and nested data, and the difficulty of expressing semantic constraints and integrity rules.
- The object-relational data model is implemented by object-relational database management systems (ORDBMS), which are similar to relational database management systems (RDBMS), but with extensions for object-oriented features.
- The object-relational data model is also supported by object-relational mapping (ORM) tools, which are software libraries that facilitate the conversion of data between object-oriented programming languages and relational databases.



# Java and Databases for Semantic Data Models

Semantic data models (SDMs) are high-level database models that capture the meaning and relationships of data in an application domain. SDMs can be used to design, query, and manipulate databases that store data in a semantic way. Some of the benefits of using SDMs are:

- They provide a natural and intuitive way of representing data that is closer to the user's perspective and needs.
- They can support complex queries and reasoning over data, such as inference, aggregation, and classification.
- They can facilitate data integration and interoperability across different sources and formats, by using common vocabularies and ontologies.
- They can enhance data quality and consistency, by enforcing constraints and rules on the data.

There are different types of SDMs, such as entity-relationship models, object-oriented models, and semantic web models. In this unit, we will focus on the semantic web models, which are based on the standards and technologies of the semantic web. The semantic web is an extension of the current web, where data is structured and linked in a way that can be understood and processed by machines. The main components of the semantic web are:

- Resource Description Framework (RDF): A standard for representing data as triples of subject, predicate, and object, where each element can be identified by a unique URI (Uniform Resource Identifier).
- RDF Schema (RDFS): A standard for defining vocabularies and schemas for RDF data, such as classes, properties, and hierarchies.
- Web Ontology Language (OWL): A standard for expressing richer and more expressive semantics for RDF data, such as logical axioms, restrictions, and rules.
- SPARQL Protocol and RDF Query Language (SPARQL): A standard for querying and manipulating RDF data, using a syntax similar to SQL.

Java is a popular and widely used programming language that can be used to create applications that interact with semantic data models. Java provides several libraries and frameworks that support the development of semantic web applications, such as:

- Apache Jena: A Java framework for building semantic web and linked data applications. It provides APIs for reading, writing, and querying RDF data, as well as tools for reasoning, inference, and ontology management.
- Apache Sesame: A Java framework for storing, querying, and reasoning with RDF and RDFS data. It provides APIs for accessing different types of RDF repositories, such as memory-based, file-based, or database-backed.
- OWL API: A Java API for creating, manipulating, and querying OWL ontologies. It supports various OWL syntaxes, such as RDF/XML, OWL/XML, Manchester Syntax, and Functional Syntax.
- Pellet: A Java-based OWL reasoner that can perform various types of reasoning tasks, such as consistency checking, classification, and query answering.

In this unit, you will learn how to use Java and these libraries and frameworks to create and access semantic data models. You will also learn how to perform various operations on semantic data, such as:

- Creating and populating RDF graphs and OWL ontologies
- Querying and updating RDF data using SPARQL
- Applying reasoning and inference on OWL data using Pellet
- Integrating and mapping semantic data from different sources and formats

The following are the main topics and subtopics of this unit:

- Introduction to Semantic Data Models
  - What are semantic data models and why are they useful?
  - What are the main components and standards of the semantic web?
  - What are the main challenges and opportunities of semantic data modeling?
- Java and RDF
  - How to use Java and Apache Jena to create and manipulate RDF graphs
  - How to use Java and Apache Sesame to store and access RDF data
  - How to use Java and SPARQL to query and update RDF data
- Java and OWL
  - How to use Java and OWL API to create and manipulate OWL ontologies
  - How to use Java and Pellet to reason and infer with OWL data
  - How to use Java and OWL tools to validate and visualize OWL data
- Semantic Data Integration and Mapping
  - How to use Java and RDF tools to integrate and map semantic data from different sources and formats
  - How to use Java and OWL tools to align and merge semantic data from different ontologies
  - How to use Java and semantic web services to access and provide semantic data over the web



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some conclusions for the notes of the Unit 2 - Semantic Data Models in the subject of INTELLIGENT DATABASE SYSTEM:

# Conclusions

- Semantic data models are conceptual data models that capture the meaning and relationships of the data in a domain of interest.
- Semantic data models use high-level constructs such as entities, attributes, relationships, constraints, and rules to represent the data and its semantics.
- Semantic data models can be classified into three categories: entity-relationship models, functional models, and object-oriented models.
- Entity-relationship models are based on the notion of entities and relationships among them. Entities are real-world objects or concepts that have properties and identifiers. Relationships are associations between entities that have cardinality and participation constraints.
- Functional models are based on the notion of functions and arguments. Functions are mappings from a set of arguments to a value. Arguments are entities or other functions. Functions can have properties, constraints, and rules that define their behavior and semantics.
- Object-oriented models are based on the notion of objects and classes. Objects are instances of classes that have attributes and methods. Classes are collections of objects that share a common structure and behavior. Classes can have inheritance, aggregation, and association relationships with other classes.



# Active Database Systems

- An active database is a database that includes an event-driven architecture (often in the form of ECA rules) which can respond to conditions both inside and outside the database .
- ECA stands for Event-Condition-Action, which means that a rule specifies an event that triggers the rule, a condition that must be satisfied for the rule to fire, and an action that is performed by the rule .
- Active databases are useful for applications that require automatic and timely responses to changes in data or environment, such as security monitoring, alerting, statistics gathering and authorization .
- Active databases are also called reactive databases, rule-based databases, or deductive databases .
- Active databases are special forms of ASMs, which are abstract state machines that can model the behavior of any discrete system.
- Active databases are very difficult to be maintained because of the complexity that arises in understanding the effect of these triggers.
- Active databases can be classified into two types: active relational databases and active object-oriented databases.
- Active relational databases extend the relational model with ECA rules that can operate on relations and tuples.
- Active object-oriented databases extend the object-oriented model with ECA rules that can operate on objects and methods.
- Some examples of active database systems are Oracle, PostgreSQL, and IBM DB2 .



# Basic concepts for the notes of the Unit 2 - Semantic Data Models in the subject of INTELLIGENT DATABASE SYSTEM

- A semantic data model (SDM) is a high-level semantics-based database description and structuring formalism (database model) for databases.
- This database model is designed to capture more of the meaning of an application environment than is possible with contemporary database models.
- A semantic data model is a conceptual data model that includes semantic information that adds a basic meaning to the data and the relationships that lie between them.
- A semantic data model is an abstraction that defines how the stored symbols (the instance data) relate to the real world.
- A semantic data model can express and exchange information that enables interoperability, integration, and reasoning.
- A semantic data model can use various techniques to represent the data and the relationships, such as:
  - Classification: This classifies different objects in objective reality by using “instance of” relations, such as “John is an instance of Person”.
  - Aggregation: Aggregation defines a new object from a set of objects that become its components using “has a” relations, such as “A car has a wheel”.
  - Generalization: Generalization defines a new object from a set of objects that share some common characteristics using “is a” relations, such as “A dog is a mammal”.
  - Association: Association defines a new relationship between two or more objects using “related to” relations, such as “Alice is related to Bob”.
- A semantic data model can use various notations to represent the data and the relationships, such as:
  - Entity-relationship diagrams (ERDs): These use graphical symbols to show the entities, attributes, and relationships in a database.
  - Unified Modeling Language (UML): This is a standard language for modeling software systems that can also be used to model databases.
  - Resource Description Framework (RDF): This is a framework for representing information on the web using triples of subject, predicate, and object.
  - Web Ontology Language (OWL): This is a language for defining and reasoning about ontologies, which are formal descriptions of concepts and their relationships.
- A semantic data model can provide various benefits, such as:
  - Improving the communication and understanding between the users and the developers of a database system.
  - Enhancing the quality and consistency of the data and the relationships.
  - Facilitating the integration and interoperability of heterogeneous data sources.
  - Enabling the inference and discovery of new knowledge from the existing data.



# Issues for the notes of the Unit 2 - Semantic Data Models in the subject of INTELLIGENT DATABASE SYSTEM

- A semantic data model is a high-level, conceptual data model that includes semantic information that adds a basic meaning to the data and the relationships that lie between them .
- A semantic data model is designed to capture more of the meaning of an application environment than is possible with contemporary database models.
- A semantic data model is an abstraction that defines how the stored symbols (the instance data) relate to the real world.
- A semantic data model can express and exchange information that enables interoperability, integration, and reasoning.
- A semantic data model can use various techniques to represent the data and the relationships, such as classification, aggregation, generalization, specialization, and association.
- A semantic data model can be implemented using different data structures, such as graphs, trees, tables, or frames.
- Some of the advantages of a semantic data model are:
  - It can provide a natural and intuitive way of modeling the data and the domain knowledge.
  - It can facilitate data integration and sharing across different sources and applications.
  - It can enable semantic querying and analysis of the data using logical inference and rules.
  - It can support data quality and consistency by enforcing constraints and validations.
- Some of the challenges of a semantic data model are:
  - It can be difficult to define and agree on a common vocabulary and ontology for the data and the domain.
  - It can be complex and costly to maintain and update the semantic data model and the associated metadata.
  - It can require specialized tools and skills to create, manipulate, and query the semantic data model.
  - It can face scalability and performance issues when dealing with large and dynamic data sets.



# Architectures for Semantic Data Models

Semantic data models are high-level conceptual data models that include semantic information to describe the meaning and relationships of data. Semantic data models can be used to design databases, exchange information, and support knowledge representation and reasoning. Semantic data models can be classified into three main architectures:

- **Entity-relationship model**: This is the most common and widely used semantic data model. It represents data as entities (objects or concepts) and relationships (associations or links) between them. Entities have attributes (properties or characteristics) and relationships have cardinalities (constraints or rules) that specify the number of entities that can participate in a relationship. Entity-relationship models can be represented graphically using diagrams or textually using schemas. Entity-relationship models are suitable for modeling structured and semi-structured data, such as relational databases, XML documents, and RDF graphs.  

- **Object-oriented model**: This is a semantic data model that extends the entity-relationship model by adding inheritance, encapsulation, and polymorphism. Inheritance allows entities to inherit attributes and relationships from other entities (superclasses or parents) and to define new ones (subclasses or children). Encapsulation hides the internal details of entities and exposes only the relevant operations (methods or functions) that can be performed on them. Polymorphism allows entities to have different behaviors (implementations or versions) depending on their context (type or state). Object-oriented models can be represented using diagrams such as UML or textually using languages such as Java or C++. Object-oriented models are suitable for modeling complex and dynamic data, such as software systems, multimedia, and simulations.  

- **Ontology model**: This is a semantic data model that represents data as concepts (classes or categories) and relations (properties or predicates) between them. Concepts have attributes (data or literals) and relations have domains (source concepts) and ranges (target concepts) that specify the types of concepts that can participate in a relation. Ontology models can be represented using diagrams such as OWL or textually using languages such as RDF or SPARQL. Ontology models are suitable for modeling unstructured and heterogeneous data, such as natural language, images, and web data. Ontology models can also support logical inference and reasoning, such as classification, subsumption, and consistency checking.  

: Semantic data model - Wikipedia
: What is the Semantic Data Model? - Definition from Techopedia
: What Is a Semantic Data Model? | GoodData
: Data model - Wikipedia



# Research relational prototypes—the Starburst Rule System

- The Starburst Rule System is an active database rules facility integrated into the Starburst extensible relational database system at the IBM Almaden Research Center   .
- The Starburst Rule System is based on arbitrary database state transitions rather than tuple- or statement-level changes, yielding a clear and flexible execution semantics  .
- The Starburst Rule System supports set-oriented production rules, which are triggered by SQL queries and actions and can execute SQL queries and actions as well .
- The Starburst Rule System is implemented as an extension to the Starburst query processing framework, using its extensibility features such as user-defined functions, access methods, and rewrite rules .
- The Starburst Rule System provides a graphical user interface for rule definition and management, as well as a rule debugger and a rule optimizer  .
- The Starburst Rule System has been used for various applications, such as integrity constraint enforcement, materialized view maintenance, alerters, and workflow management   .



# Commercial Relational Approaches for Semantic Data Models

- Semantic data models (SDMs) are high-level database models that capture the meaning and structure of data in an application domain.
- SDMs use concepts such as entities, attributes, relationships, and constraints to represent data and their semantics.
- SDMs are different from relational data models (RDMs) which use tables, columns, keys, and foreign keys to represent data and their structure.
- SDMs have some advantages over RDMs, such as:
  - They are more expressive and intuitive, as they can capture complex data types, hierarchies, inheritance, and aggregation.
  - They are more flexible and adaptable, as they can accommodate changes to data requirements without affecting the physical schema.
  - They are more interoperable and reusable, as they can support data integration and sharing across different applications and domains.
- However, SDMs also have some challenges, such as:
  - They are more complex and abstract, as they require more modeling skills and tools to design and implement.
  - They are less efficient and scalable, as they may incur more overhead and performance issues when translated to relational databases.
  - They are less standardized and mature, as they lack a common notation and methodology for modeling and querying.
- Therefore, some commercial relational approaches have been developed to bridge the gap between SDMs and RDMs, such as:
  - Object-relational mapping (ORM), which is a technique that maps objects and their properties to tables and columns in a relational database, and vice versa.
  - Semantic graph databases, which are a type of graph databases that store data as nodes and edges with labels and properties, and support semantic queries and reasoning.
  - Semantic models, which are a type of metadata models that present data for analysis according to the structure and meaning of the business domain, and support subject areas, hierarchies, and measures.



## Unit 3 - Knowledge-Based Systems - AI Context

- A knowledge-based system (KBS) is a form of artificial intelligence (AI) that aims to capture the knowledge of human experts to support decision-making .
- A KBS stores knowledge in the form of rules, facts, concepts, or other representations, which are then used to generate solutions to specific problems .
- A KBS consists of two main components: a knowledge base and an inference engine .
  - A knowledge base is a collection of knowledge that is relevant to a specific problem domain, such as medicine, law, engineering, etc.
  - An inference engine is a software program that applies logical reasoning to the knowledge base to derive new knowledge or conclusions.
- A KBS can have different types, depending on the nature and source of the knowledge, such as :
  - Expert systems, which are KBS that emulate the reasoning of human experts in a specific domain, such as diagnosing diseases, planning routes, or designing products.
  - Case-based reasoning systems, which are KBS that use past cases or examples to solve new problems, such as recommending products, solving legal disputes, or finding similar images.
  - Ontology-based systems, which are KBS that use formal and explicit definitions of concepts and relations in a domain, such as representing the structure and meaning of web pages, documents, or data.
  - Neural network systems, which are KBS that use artificial neural networks to learn from data and perform tasks, such as recognizing patterns, classifying objects, or predicting outcomes.
- A KBS can have different uses, depending on the purpose and function of the system, such as :
  - Decision support systems, which are KBS that assist human decision-makers with information, analysis, or recommendations, such as choosing investments, selecting courses, or evaluating options.
  - Intelligent tutoring systems, which are KBS that provide personalized and adaptive instruction to learners, such as teaching languages, skills, or concepts.
  - Knowledge management systems, which are KBS that capture, store, and share organizational knowledge, such as best practices, lessons learned, or expertise.
  - Knowledge discovery systems, which are KBS that extract useful and novel knowledge from large and complex data sets, such as finding patterns, trends, or anomalies.



# Characteristics and classification of the knowledge-based systems

A knowledge-based system (KBS) is a computer program that reasons and uses a knowledge base to solve complex problems. The term is broad and refers to many different kinds of systems. The one common theme that unites all knowledge based systems is an attempt to represent knowledge explicitly and a reasoning system that allows it to derive new knowledge from the existing one.

## Characteristics of knowledge-based systems

Some of the main characteristics of knowledge-based systems are:

- They are domain-specific, meaning they focus on a particular area of expertise or problem-solving.
- They are based on declarative knowledge, meaning they represent facts, rules, concepts, and relationships in a symbolic form that can be manipulated by the system.
- They use an inference engine, meaning they apply logical rules or heuristics to the knowledge base to infer new knowledge or conclusions.
- They can explain their reasoning, meaning they can provide justification or evidence for their answers or actions.
- They can learn from new data or feedback, meaning they can update or revise their knowledge base to improve their performance or accuracy .

## Classification of knowledge-based systems

There are many ways to classify knowledge-based systems, depending on the criteria used. One possible classification is based on the type of knowledge representation and reasoning used by the system. Some of the common types are:

- Case-based systems: These systems use case-based reasoning, which involves reviewing past knowledge of similar situations. Based on what it finds, the system can adapt or reuse the previous solutions to new problems.
- Expert systems: These systems use rule-based reasoning, which involves applying a set of if-then rules to the knowledge base to reach a conclusion or recommendation. Expert systems are often used to emulate human experts in specific domains, such as medical diagnosis or legal advice.
- Hypertext manipulation systems: These systems use hypertext reasoning, which involves linking and navigating through different pieces of information in a non-linear way. Hypertext manipulation systems are often used to provide interactive access to large and complex knowledge bases, such as encyclopedias or manuals.
- Intelligent tutoring systems: These systems use pedagogical reasoning, which involves providing guidance and feedback to learners based on their goals, preferences, and progress. Intelligent tutoring systems are often used to provide personalized and adaptive learning experiences, such as online courses or games.
- Rule-based systems: These systems use rule-based reasoning, which involves applying a set of if-then rules to the knowledge base to reach a conclusion or recommendation. Rule-based systems are often used to emulate human experts in specific domains, such as medical diagnosis or legal advice .

Some other possible types of knowledge-based systems are:

- Neural network systems: These systems use neural network reasoning, which involves processing data through a network of interconnected nodes that simulate the functioning of biological neurons. Neural network systems are often used to perform tasks that require pattern recognition, such as image recognition or natural language processing.
- Fuzzy logic systems: These systems use fuzzy logic reasoning, which involves dealing with uncertainty and imprecision by using degrees of truth rather than binary values. Fuzzy logic systems are often used to model human common sense and intuition, such as in control systems or decision making.
- Ontology-based systems: These systems use ontology reasoning, which involves using a formal and explicit specification of the concepts, properties, and relations in a domain of interest. Ontology-based systems are often used to facilitate interoperability and communication among different systems or agents, such as in the semantic web or knowledge management .



# Introduction for the notes of the Unit 3 - Knowledge-Based Systems- AI Context in the subject of INTELLIGENT DATABASE SYSTEM

- A knowledge-based system (KBS) is a computer system that uses artificial intelligence (AI) techniques to solve problems that normally require human expertise.
- A KBS consists of two main components: a knowledge base and an inference engine.
- A knowledge base is a collection of facts, rules, and heuristics that represent the domain knowledge of a specific problem area.
- An inference engine is a software module that applies logical reasoning to the knowledge base to derive new information or conclusions.
- A KBS can also have other components, such as a user interface, a knowledge acquisition module, a knowledge representation language, and a knowledge validation module.
- A KBS can be classified into different types based on the nature of the knowledge, the reasoning method, and the application domain.
- Some examples of KBS types are expert systems, case-based reasoning systems, rule-based systems, fuzzy systems, neural networks, genetic algorithms, and hybrid systems.
- A KBS can provide various benefits, such as improving decision making, enhancing productivity, reducing errors, saving costs, and facilitating learning and training.
- A KBS can also face various challenges, such as knowledge acquisition, knowledge representation, knowledge validation, knowledge maintenance, knowledge integration, and knowledge sharing.
- A KBS can be applied to various domains, such as diagnosis, planning, scheduling, design, configuration, monitoring, control, simulation, education, and entertainment.



# The resolution principle

- The resolution principle is a general rule of inference that can be used to derive new conclusions from a set of premises .
- It is based on the idea of resolving two clauses that contain complementary literals, i.e., literals that are the negation of each other .
- For example, if we have the clauses `p v q` and `¬p v r`, we can resolve them on the literal `p` and obtain the new clause `q v r` .
- The resolution principle can be applied to propositional logic, predicate logic, and other forms of logic  .
- In artificial intelligence, resolution is a technique for automated theorem proving, and more generally for automated deduction .
- It can be used to check the validity or satisfiability of a formula, or to prove that a formula follows from a set of axioms .
- The resolution principle can also be used to transform a given problem into another problem that is easier to solve, by reducing the number of variables, adding new constraints, or changing the problem representation.
- The resolution principle underpins the logic programming and production rules paradigms, which are widely used in artificial intelligence applications .



# Inference by inheritance for the notes of the Unit 3 - Knowledge-Based Systems- AI Context in the subject of INTELLIGENT DATABASE SYSTEM

- Inference by inheritance is a technique of reasoning that uses the hierarchical structure of concepts to derive new facts or conclusions from existing knowledge.
- Inference by inheritance is based on the principle of **subsumption**, which states that if a concept A is a subclass of a concept B, then A inherits all the properties and relations of B, unless explicitly stated otherwise.
- For example, if we know that a dog is a subclass of an animal, and that an animal has a heart, then we can infer that a dog has a heart by inheritance.
- Inference by inheritance can be applied to different types of knowledge representation systems, such as semantic networks, frames, and ontologies.
- Semantic networks are graphs that represent concepts as nodes and relations as edges. Inference by inheritance can be performed by following the links from a specific node to its superclasses and applying the subsumption principle.
- Frames are data structures that represent concepts as collections of attributes and values. Inference by inheritance can be performed by accessing the values of the attributes from the frames of the superclasses and applying the subsumption principle.
- Ontologies are formal specifications of the concepts and relations in a domain of interest. Inference by inheritance can be performed by using logical rules and axioms that define the subsumption relation and the properties of the concepts and relations.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the conclusion for the notes of the Unit 3 - Knowledge-Based Systems- AI Context in the subject of Intelligent Database System:

# Conclusion

- Knowledge-based systems (KBS) are computer systems that use artificial intelligence techniques to solve complex problems that normally require human expertise.
- KBS consist of two main components: a knowledge base and an inference engine. The knowledge base stores the domain knowledge in a formal representation, such as rules, frames, or ontologies. The inference engine applies logical reasoning to the knowledge base and the user's input to derive conclusions or recommendations.
- KBS can be classified into different types based on their functionality, such as expert systems, decision support systems, intelligent tutoring systems, natural language processing systems, etc.
- KBS can also be classified into different types based on their architecture, such as rule-based systems, frame-based systems, logic-based systems, etc.
- KBS face several challenges, such as knowledge acquisition, knowledge representation, knowledge validation, knowledge maintenance, knowledge integration, etc.
- KBS can benefit from the integration with database systems, which can provide efficient storage, retrieval, and manipulation of large amounts of structured data. Database systems can also support the implementation of KBS by providing query languages, transaction management, concurrency control, security, etc.
- KBS can also benefit from the integration with other AI techniques, such as machine learning, neural networks, fuzzy logic, genetic algorithms, etc. These techniques can enhance the capabilities of KBS by providing learning, adaptation, uncertainty handling, optimization, etc.



# Deductive Database Systems

- A deductive database is a database system that can make deductions (i.e. conclude additional facts) based on rules and facts stored in the (deductive) database.
- Deductive databases offer elegant and powerful ways of managing complex data in a declarative way, especially for information that is derived by use of recursion.
- Deductive systems typically provide a declarative query language such as a logic programming language (e.g., Prolog).
- Deductive database systems can be seen as bringing together mainstream data models with logic programming languages for querying and analyzing database data.
- Deductive databases have many applications in areas such as artificial intelligence, knowledge representation, natural language processing, data mining, etc.
- Some examples of commercial deductive database systems are Oracle, IBM DB2, Microsoft SQL Server, etc.



# Basic concepts for the notes of the Unit 3 - Knowledge-Based Systems- AI Context in the subject of INTELLIGENT DATABASE SYSTEM

- A **knowledge-based system (KBS)** is a form of artificial intelligence (AI) that aims to capture the knowledge of human experts to support decision-making  .
- A KBS consists of two main components: a **knowledge base** and an **inference engine**  .
- A **knowledge base** is a collection of facts, rules, and other information that represents the knowledge of a specific domain  .
- An **inference engine** is a software component that applies logical reasoning to the knowledge base to generate solutions or answers to specific problems  .
- Examples of knowledge-based systems include **expert systems**, which are so called because of their reliance on human expertise, and **intelligent tutoring systems**, which are designed to provide personalized instruction and feedback to learners  .
- The main advantages of knowledge-based systems are that they can provide consistent, accurate, and reliable solutions to complex problems, and that they can preserve and reuse the knowledge of human experts  .
- The main challenges of knowledge-based systems are that they require a lot of effort and resources to acquire, represent, and maintain the knowledge, and that they may face issues of validity, scalability, and explainability  .
- Knowledge-based systems are an important and active research area in the field of artificial intelligence, and they have many applications in various domains, such as medicine, engineering, education, and business    .



# DATALOG Language

Datalog is a declarative logic programming language that is based on Horn clauses. It is a subset of Prolog, but it uses a bottom-up evaluation model instead of a top-down one. Datalog is often used as a query language for deductive databases, which are databases that can derive new facts from existing facts using logical rules. Datalog can also be used for other applications, such as data integration, information extraction, program analysis, security, and machine learning.

Some of the main features of Datalog are:

- Datalog programs consist of a set of facts and rules. Facts are statements that are true in the database, such as `parent(alice, bob)`. Rules are statements that define how new facts can be derived from existing facts, such as `ancestor(X, Y) :- parent(X, Y)`.
- Datalog queries are also rules, but they have a special symbol `?` in the head of the clause, such as `?- ancestor(X, bob)`. Queries ask for the values of the variables that make the rule true in the database.
- Datalog uses a bottom-up evaluation model, which means that it starts from the facts and applies the rules repeatedly until no new facts can be derived. This process is called fixpoint computation. The result of a query is the set of facts that match the query rule in the final database state.
- Datalog is a logic language, which means that it is based on formal logic and has a well-defined semantics. Datalog programs are declarative, which means that they specify what the desired result is, not how to compute it. Datalog programs are also relational, which means that they use relations (or predicates) to represent data and queries.
- Datalog has some limitations compared to Prolog, such as the absence of function symbols, negation, and recursion through negation. These limitations make Datalog more efficient and easier to analyze, but also less expressive. However, there are some extensions of Datalog that overcome some of these limitations, such as Datalog with negation, Datalog with aggregates, and Datalog with constraints.



# Deductive database systems and logic programming systems—differences

- Deductive database systems are systems that combine relational databases with logic programming to support a powerful and declarative formalism for querying and manipulating data.
- Logic programming systems are systems that use a subset of logic to represent and execute programs, usually based on the resolution principle and unification.
- Some of the main differences between deductive database systems and logic programming systems are:

  - Order sensitivity and procedurality: In logic programming systems, such as Prolog, the order of rules and the order of parts of rules affect the program execution and the efficiency. In deductive database systems, such as Datalog, the order of rules and the order of parts of rules are irrelevant, as the system computes the minimal model of the program.
  - Special predicates: In logic programming systems, programmers can use special predicates, such as cut, fail, assert, retract, etc., to control the execution flow and modify the program dynamically. In deductive database systems, these predicates are not allowed, as they violate the declarative semantics and the monotonicity of the logic.
  - Negation: In logic programming systems, negation is usually implemented by negation as failure, which is a procedural and non-monotonic technique that relies on the closed-world assumption. In deductive database systems, negation is usually implemented by stratified negation, which is a declarative and monotonic technique that relies on the well-founded semantics.
  - Recursion: In logic programming systems, recursion is unrestricted and can be used to express complex computations and algorithms. In deductive database systems, recursion is restricted to stratified programs, which ensure the existence and uniqueness of the minimal model.



# Architectural approaches for the notes of the Unit 3 - Knowledge-Based Systems- AI Context in the subject of INTELLIGENT DATABASE SYSTEM

- A knowledge-based system (KBS) is a computer system that uses artificial intelligence to solve problems within a specialized domain that ordinarily requires human expertise .
- The typical architecture of a KBS consists of two main components: a knowledge base and an inference engine .
- The knowledge base contains a collection of facts, rules, heuristics, and other forms of knowledge representation that capture the domain expertise .
- The inference engine is a software module that applies logical rules and reasoning methods to the knowledge base to derive new information or solutions .
- There are different types of KBS architectures, depending on the nature of the knowledge base, the inference engine, and the interaction with the user or other systems .
- Some of the common KBS architectures are:

  - Rule-based systems: These systems use a set of if-then rules to represent the knowledge base and a forward or backward chaining algorithm to perform the inference . An example of a rule-based system is MYCIN, a medical diagnosis system for infectious diseases .
  - Frame-based systems: These systems use a hierarchical network of frames to represent the knowledge base and a slot-and-filler mechanism to perform the inference . A frame is a data structure that contains a set of attributes and values that describe an entity or a concept . An example of a frame-based system is KEE, a knowledge engineering environment for building expert systems .
  - Logic-based systems: These systems use a formal logic language, such as propositional logic, predicate logic, or description logic, to represent the knowledge base and a theorem prover or a model checker to perform the inference . An example of a logic-based system is PROLOG, a programming language for logic programming .
  - Case-based systems: These systems use a database of past cases or examples to represent the knowledge base and a similarity measure or a retrieval algorithm to perform the inference . A case is a record of a problem and its solution that can be reused or adapted for new situations . An example of a case-based system is CHEF, a cooking system that generates recipes based on user preferences and ingredients .
  - Neural network systems: These systems use a network of interconnected nodes or neurons to represent the knowledge base and a learning algorithm or a activation function to perform the inference . A neural network is a computational model that mimics the structure and function of the biological brain . An example of a neural network system is ALVINN, a self-driving car system that learns from human drivers .

- Some of the challenges and issues in designing and developing KBS architectures are:

  - Knowledge acquisition: This is the process of eliciting, analyzing, and encoding the domain knowledge from human experts or other sources into a suitable form for the knowledge base . This is often a difficult and time-consuming task, as the knowledge may be tacit, incomplete, inconsistent, or evolving .
  - Knowledge representation: This is the process of choosing an appropriate language or format to express the domain knowledge in the knowledge base . This involves trade-offs between expressiveness, efficiency, and scalability of the representation .
  - Knowledge reasoning: This is the process of applying logical rules and methods to the knowledge base to infer new information or solutions . This requires a balance between soundness, completeness, and tractability of the reasoning .
  - Knowledge validation: This is the process of verifying and validating the correctness and reliability of the knowledge base and the inference engine . This involves testing, debugging, and evaluating the performance and accuracy of the KBS .
  - Knowledge maintenance: This is the process of



# Research prototypes for the notes of the Unit 3 - Knowledge-Based Systems- AI Context in the subject of INTELLIGENT DATABASE SYSTEM

- A research prototype is a preliminary version of a system that is used to test and evaluate its feasibility, functionality, performance, and usability in a specific domain or problem.
- A knowledge-based system (KBS) is a system that uses artificial intelligence techniques to solve problems that normally require human expertise and reasoning.
- A knowledge-based system consists of two main components: a knowledge base and an inference engine.
- A knowledge base is a collection of facts, rules, heuristics, and other forms of knowledge that represent the domain of the problem and the solution methods.
- An inference engine is a software component that applies logical rules and methods to the knowledge base to derive new facts, conclusions, or recommendations.
- A knowledge-based system can be classified into different types based on the nature of the knowledge, the reasoning method, the application domain, and the user interface.
- Some examples of knowledge-based system types are expert systems, case-based reasoning systems, rule-based systems, fuzzy systems, neural networks, genetic algorithms, and hybrid systems.
- A research prototype for a knowledge-based system can be developed using various tools and methods, such as programming languages, frameworks, libraries, databases, ontologies, and graphical user interfaces.
- A research prototype for a knowledge-based system should be evaluated using appropriate criteria and metrics, such as accuracy, efficiency, reliability, scalability, usability, and user satisfaction.
- A research prototype for a knowledge-based system should also be compared and contrasted with existing systems or methods in the same domain or problem, and identify the strengths, weaknesses, opportunities, and challenges of the proposed system or method.
- Some examples of research prototypes for knowledge-based systems are:

  - A prototype knowledge-based simulation support system that was developed to support a senior level course in industrial engineering and to study the feasibility of an expert simulation support system .
  - A prototype knowledge-based system that uses geometric features and rules to classify fingerprint images into five categories.
  - A prototype knowledge-based system that uses natural language processing and ontologies to generate summaries of scientific articles.
  - A prototype knowledge-based system that uses experience prototypes and social action prototyping to design and evaluate interactive products and services.



# Updates in deductive databases for the notes of the Unit 3 - Knowledge-Based Systems- AI Context in the subject of INTELLIGENT DATABASE SYSTEM

- A deductive database is a database system that can make deductions (i.e. conclude additional facts) based on rules and facts stored in the (deductive) database.
- Deductive databases offer elegant and powerful ways of managing complex data in a declarative way, especially for information that is derived by use of recursion.
- Deductive databases typically use a logic programming language such as Datalog to specify facts, rules and queries .
- Some of the updates in deductive databases are:

  - The development of efficient and scalable query evaluation algorithms for recursive queries, such as semi-naive evaluation, magic sets, and tabling.
  - The integration of deductive databases with other paradigms, such as object-oriented, relational, and XML databases.
  - The application of deductive databases to various domains, such as data integration, data mining, knowledge representation, and semantic web.
  - The extension of deductive databases with features such as negation, aggregates, constraints, and probabilistic reasoning.
  - The formalization of the semantics and properties of deductive databases, such as soundness, completeness, and complexity.



# Integration of deductive database and object database technologies

- Deductive databases extend relational databases with inherent support for powerful rules that provide for the declarative specification of deductive rules and integrity constraints.
- Object-oriented databases provide complex data structuring including class hierarchies and inheritance.
- The integration of the two technologies aims to provide an expressive and efficient framework for building intelligent and knowledge-based systems .
- Some of the benefits of the integration are:
  - The ability to model complex objects and relationships using object-oriented concepts such as classes, methods, inheritance, polymorphism, etc.
  - The ability to specify and reason about the semantics and constraints of the data and the domain using deductive rules and logic programming.
  - The ability to support various kinds of queries and inferences, such as deductive, recursive, aggregate, spatial, temporal, etc.
  - The ability to support automatic knowledge acquisition or learning from databases directly in deductive database systems.
- Some of the challenges of the integration are:
  - The design of a suitable data model and query language that can capture both the object-oriented and the deductive features.
  - The implementation of efficient and scalable algorithms and techniques for storing, indexing, querying, and reasoning over large and complex data sets.
  - The development of applications and tools that can demonstrate the usefulness and effectiveness of the integrated approach.




# Constraint databases

- Constraint databases are a type of database that use constraints to represent and query data.
- Constraints are logical expressions that specify the properties or relationships of data values.
- Constraint databases can handle complex and multidimensional data that are not suitable for relational databases, such as spatial, temporal, geometric, or symbolic data.
- Constraint databases provide extra expressive power over relational databases in a largely hidden way. They keep the view of the database for a user or application programmer almost as simple as in relational databases.
- Constraint databases are shown to be powerful and simple tools for data modeling and querying in application areas -- such as environmental modeling, bioinformatics, and computer vision -- that are not suitable for relational databases.
- Some examples of constraint databases are:
  - GeoSQL: a constraint database system for spatial data that supports spatial operators and predicates.
  - Dedale: a constraint database system for temporal data that supports temporal operators and predicates.
  - C-Store: a constraint database system for geometric data that supports geometric operators and predicates.
- Some advantages of constraint databases are:
  - They can represent infinite sets of data with finite expressions.
  - They can support declarative and efficient querying of complex data.
  - They can support data integration and interoperability among heterogeneous data sources.
- Some challenges of constraint databases are:
  - They require specialized algorithms and data structures to manipulate and store constraints.
  - They may suffer from performance and scalability issues due to the complexity of constraint evaluation and optimization.
  - They may have limited support for updates and transactions due to the difficulty of maintaining consistency and integrity of constraints.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some possible conclusions for the notes of the Unit 3 - Knowledge-Based Systems- AI Context in the subject of Intelligent Database System:

### Conclusions

- Knowledge-based systems (KBS) are computer systems that use artificial intelligence techniques to solve complex problems that normally require human expertise.
- KBS consist of a knowledge base, which stores the domain knowledge, and an inference engine, which applies logical rules to the knowledge base to derive new facts or conclusions.
- KBS can be classified into different types based on the nature of the knowledge, the reasoning method, and the application domain. Some common types are expert systems, case-based reasoning systems, neural networks, fuzzy systems, and hybrid systems.
- KBS can be developed using various tools and languages, such as Prolog, Lisp, CLIPS, KEE, and Protégé. These tools provide features such as knowledge representation, inference, explanation, and user interface.
- KBS can be integrated with database systems to enhance the functionality and performance of both systems. Some benefits of KBS-database integration are data consistency, data integrity, data security, data sharing, and data analysis.
- KBS can also be integrated with other AI techniques, such as natural language processing, computer vision, machine learning, and data mining, to create intelligent applications that can interact with users, process multimedia data, learn from data, and discover new knowledge.



## Unit 4 - Advanced Knowledge-Based Systems

- A knowledge-based system (KBS) is a computer system that uses artificial intelligence techniques to solve problems that normally require human expertise.
- A KBS consists of two main components: a knowledge base and an inference engine.
- A knowledge base is a collection of facts, rules, heuristics, and other forms of knowledge representation that capture the domain knowledge of a human expert.
- An inference engine is a software module that applies logical reasoning to the knowledge base to derive new facts, conclusions, or recommendations.
- A KBS can also have other components, such as a user interface, a knowledge acquisition module, a knowledge validation module, and a knowledge explanation module.
- A KBS can be classified into different types based on the nature of the knowledge, the reasoning method, or the application domain.
- Some common types of KBS are expert systems, case-based reasoning systems, rule-based systems, fuzzy logic systems, neural network systems, genetic algorithm systems, and hybrid systems.
- Expert systems are KBS that emulate the problem-solving behavior of a human expert in a specific domain, such as medical diagnosis, financial planning, or chess playing.
- Case-based reasoning systems are KBS that use past cases or examples to solve new problems by finding similarities, adapting solutions, and learning from feedback.
- Rule-based systems are KBS that use a set of if-then rules to represent and manipulate knowledge, such as deductive rules, inductive rules, or production rules.
- Fuzzy logic systems are KBS that use fuzzy sets and fuzzy rules to deal with uncertainty, vagueness, and imprecision in knowledge, such as linguistic terms, fuzzy numbers, or fuzzy relations.
- Neural network systems are KBS that use artificial neural networks to learn from data and perform tasks such as classification, regression, clustering, or pattern recognition.
- Genetic algorithm systems are KBS that use evolutionary computation techniques to search for optimal or near-optimal solutions in large and complex spaces, such as optimization, scheduling, or design problems.
- Hybrid systems are KBS that combine two or more of the above types to exploit their strengths and overcome their limitations, such as neuro-fuzzy systems, genetic fuzzy systems, or rule-based neural networks.



# Introduction for the notes of the Unit 4 - Advanced Knowledge-Based Systems in the subject of INTELLIGENT DATABASE SYSTEM

- A knowledge-based system (KBS) is a computer system that uses artificial intelligence techniques to solve problems that require human expertise.
- A knowledge-based system consists of two main components: a knowledge base and an inference engine.
- A knowledge base is a collection of facts and rules that represent the domain knowledge of a human expert.
- An inference engine is a software module that applies logical reasoning to the knowledge base to derive new facts and conclusions.
- A knowledge-based system can also have other components, such as a user interface, a knowledge acquisition module, a knowledge representation language, and a knowledge validation module.
- A knowledge-based system can be classified into different types, such as rule-based systems, case-based systems, model-based systems, and hybrid systems, depending on the structure and content of the knowledge base and the inference engine.
- A knowledge-based system can be applied to various domains, such as diagnosis, planning, scheduling, design, configuration, and decision support.
- A knowledge-based system can provide several benefits, such as increased productivity, consistency, reliability, and explainability, as well as reduced costs, errors, and training time.
- A knowledge-based system can also face several challenges, such as knowledge acquisition, knowledge representation, knowledge maintenance, knowledge verification, and knowledge validation, as well as ethical, social, and legal issues.



# Architectural solutions for the notes of the Unit 4 - Advanced Knowledge-Based Systems in the subject of INTELLIGENT DATABASE SYSTEM

- A knowledge-based system (KBS) is a computer system that uses artificial intelligence techniques to solve complex problems that normally require human expertise.
- A KBS consists of two main components: a knowledge base and an inference engine.
- A knowledge base is a repository of facts, rules, heuristics, and other forms of knowledge that represent the domain of the problem.
- An inference engine is a software module that applies logical reasoning to the knowledge base to derive new conclusions or solutions.
- A KBS can support architectural design by providing intelligent objects, project net-constraints, and collaborative work.
- Intelligent objects are entities that have both geometric and semantic properties, and can interact with other objects and the environment according to predefined rules and constraints.
- Project net-constraints are global conditions that must be satisfied by the design solution, such as functional, structural, environmental, and aesthetic requirements.
- Collaborative work is the process of involving multiple stakeholders, such as architects, engineers, clients, and users, in the design process, and facilitating communication, coordination, and negotiation among them.
- A KBS can also support architectural design by applying knowledge-based approaches, such as knowledge capture and representation, knowledge reuse, knowledge sharing, knowledge reasoning, and knowledge recovery.
- Knowledge capture and representation are the processes of eliciting, formalizing, and storing the knowledge of experts and other sources in a suitable format for the KBS.
- Knowledge reuse is the process of applying existing knowledge to new problems or contexts, and adapting it as needed.
- Knowledge sharing is the process of making the knowledge available and accessible to other stakeholders, such as other KBSs, humans, or external systems.
- Knowledge reasoning is the process of applying logical rules and methods to the knowledge to infer new knowledge, validate solutions, or explain results.
- Knowledge recovery is the process of extracting and recovering the knowledge embedded in legacy systems, documents, or artifacts.



# The 'general bridge' solution for the notes of the Unit 4 - Advanced Knowledge-Based Systems in the subject of INTELLIGENT DATABASE SYSTEM

- A knowledge-based system (KBS) is a type of computer system that analyzes knowledge, data and other information from sources to generate new knowledge.
- A knowledge-based system uses AI concepts to solve problems, which may be useful for assisting with human learning and making decisions.
- A knowledge-based system consists of two main components: a knowledge base and an inference engine.
- A knowledge base is a collection of facts, rules, and other information that represents the domain knowledge of the system.
- An inference engine is a software component that applies logical reasoning to the knowledge base to derive new knowledge or conclusions.
- A general bridge solution is a method of integrating a knowledge-based system with a conventional database system.
- A general bridge solution allows the knowledge-based system to access and manipulate the data stored in the database system, and vice versa.
- A general bridge solution consists of four main components: a database, a knowledge base, a database interface, and a knowledge base interface.
- A database is a collection of data organized in a structured way, such as tables, records, and fields.
- A database interface is a software component that provides the knowledge-based system with the ability to query, update, and modify the data in the database.
- A knowledge base interface is a software component that provides the database system with the ability to query, update, and modify the knowledge in the knowledge base.
- A general bridge solution can be implemented using various techniques, such as SQL, ODBC, JDBC, or API calls.
- A general bridge solution can offer several benefits, such as increased efficiency, consistency, and flexibility of the system, as well as improved data quality and integrity.
- A general bridge solution can also pose some challenges, such as complexity, compatibility, and security issues, as well as potential conflicts between the data and the knowledge.



# Extending a KBS with components proper to a DBMS

- A Knowledge-Based System (KBS) is a system that uses artificial intelligence techniques to solve problems that require human expertise.
- A Database Management System (DBMS) is a software tool that enables users to create and manage databases, which are collections of data organized in a structured way.
- Extending a KBS with components proper to a DBMS means integrating the two technologies to achieve better performance, functionality, and usability.
- Some of the benefits of extending a KBS with components proper to a DBMS are:
  - Improved data management: A DBMS can provide efficient and reliable storage, retrieval, and manipulation of large amounts of data, which can enhance the knowledge base of a KBS.
  - Enhanced reasoning capabilities: A DBMS can support complex queries, inference rules, and deductive reasoning, which can improve the problem-solving and decision-making abilities of a KBS.
  - Increased interoperability: A DBMS can facilitate the communication and integration of a KBS with other systems and data sources, such as the web, legacy systems, or external databases.
  - Reduced development and maintenance costs: A DBMS can provide standard tools and interfaces for developing and maintaining a KBS, which can reduce the need for specialized skills and resources.
- Some of the challenges of extending a KBS with components proper to a DBMS are:
  - Semantic mismatch: A DBMS and a KBS may have different representations and interpretations of data and knowledge, which can cause inconsistencies and conflicts.
  - Structural mismatch: A DBMS and a KBS may have different schemas and structures for organizing data and knowledge, which can affect the compatibility and efficiency of the integration.
  - Functional mismatch: A DBMS and a KBS may have different functionalities and capabilities for processing data and knowledge, which can limit the potential of the integration.
  - Performance trade-off: A DBMS and a KBS may have different requirements and constraints for achieving optimal performance, which can result in a trade-off between speed, accuracy, and scalability.
- Some of the approaches for extending a KBS with components proper to a DBMS are:
  - Coupling: This approach involves connecting a KBS and a DBMS through an interface or a middleware, which allows them to exchange data and knowledge without modifying their internal architectures.
  - Enhancement: This approach involves adding new features or modules to a KBS or a DBMS, which enable them to perform some of the functions of the other system.
  - Integration: This approach involves merging a KBS and a DBMS into a single system, which combines the advantages of both technologies and eliminates the need for a separate interface or middleware.



# The 'tight coupling' approach for the notes of the Unit 4 - Advanced Knowledge-Based Systems in the subject of INTELLIGENT DATABASE SYSTEM

- Tight coupling means that a data mining system is smoothly integrated into the database/data warehouse system.
- The data mining subsystem is treated as one functional component of the information system.
- The data warehouse is treated as an information retrieval component of a data mining system using integration.
- All the features of a database or data warehouse are used to perform data mining tasks.
- This architecture provides system scalability, high performance, and integrated information.
- In tight coupling, the text data type is supported from the storage system just like a built-in data type.
- The query processor can efficiently handle queries involving both structured data and text data.
- This approach involves creating a centralized repository or data warehouse to store the integrated data.
- The data is extracted from various sources, transformed and loaded into a data warehouse.
- This approach requires a novel structure of the IR index as well as tightly-coupled query processing algorithms.
- The advantages of this approach are:
  - It avoids data duplication and inconsistency.
  - It supports complex and sophisticated data mining techniques.
  - It enables fast and efficient access to large amounts of data.
- The disadvantages of this approach are:
  - It requires high initial investment and maintenance cost.
  - It may not support heterogeneous and dynamic data sources.
  - It may not be flexible enough to accommodate different user needs and preferences.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the conclusion for the notes of the Unit 4 - Advanced Knowledge-Based Systems in the subject of Intelligent Database System.

# Conclusion

- Advanced knowledge-based systems are systems that can perform complex tasks that require human expertise, such as diagnosis, planning, design, and decision making.
- Advanced knowledge-based systems use various techniques to represent and manipulate knowledge, such as logic, rules, frames, semantic networks, ontologies, and case-based reasoning.
- Advanced knowledge-based systems can also incorporate learning, reasoning, and explanation capabilities to improve their performance and usability.
- Advanced knowledge-based systems can be integrated with databases, data mining, and data warehousing to provide intelligent data analysis and management.
- Advanced knowledge-based systems can be applied to various domains, such as medicine, engineering, business, education, and law.



# Advanced solutions for the notes of the Unit 4 - Advanced Knowledge-Based Systems in the subject of INTELLIGENT DATABASE SYSTEM

- A knowledge-based system (KBS) is a computer program that reasons and uses a knowledge base to solve complex problems.
- A knowledge base is a collection of facts, rules, and heuristics that represent the domain knowledge of a specific field or application.
- A knowledge-based system consists of two main components: a knowledge base and an inference engine.
- An inference engine is a software module that applies logical rules to the knowledge base to derive new knowledge or conclusions.
- A knowledge-based system can also have other components, such as a user interface, a knowledge acquisition module, a knowledge representation language, and a knowledge validation module.
- Knowledge-based systems can be classified into different types, such as expert systems, case-based reasoning systems, neural networks, fuzzy systems, genetic algorithms, and ontologies .
- Expert systems are knowledge-based systems that emulate the reasoning and decision-making of human experts in a specific domain .
- Case-based reasoning systems are knowledge-based systems that solve new problems by retrieving and adapting solutions from previous similar cases .
- Neural networks are knowledge-based systems that learn from data and mimic the structure and function of biological neurons .
- Fuzzy systems are knowledge-based systems that deal with uncertainty and imprecision by using fuzzy logic and fuzzy sets .
- Genetic algorithms are knowledge-based systems that use evolutionary principles and operators to search for optimal solutions in large and complex spaces .
- Ontologies are knowledge-based systems that represent the concepts and relationships of a domain in a formal and machine-readable way .
- Knowledge-based systems can be used for various purposes, such as diagnosis, planning, scheduling, design, control, optimization, simulation, education, and decision support  .
- Knowledge-based systems can provide benefits such as increased efficiency, accuracy, consistency, reliability, flexibility, and adaptability .
- Knowledge-based systems can also face challenges such as knowledge acquisition, knowledge representation, knowledge validation, knowledge maintenance, knowledge integration, and knowledge sharing .
- Knowledge-based systems can be developed using various tools and software, such as Prolog, Lisp, Java, Python, CLIPS, Jess, Drools, Protégé, and SWI-Prolog .
- Knowledge-based systems are a step towards an intelligent system, and can be applied to various domains, such as medicine, engineering, law, business, education, and science   .
- Knowledge-based systems are also influenced by and integrated with other artificial intelligence techniques, such as natural language processing, computer vision, machine learning, data mining, and semantic web .



# Introduction for the notes of the Unit 4 - Advanced Knowledge-Based Systems in the subject of INTELLIGENT DATABASE SYSTEM

- A knowledge-based system (KBS) is a computer system that uses artificial intelligence techniques to solve problems that require human expertise.
- A knowledge-based system consists of two main components: a knowledge base and an inference engine.
- A knowledge base is a collection of facts, rules, and heuristics that represent the domain knowledge of a human expert.
- An inference engine is a software module that applies logical reasoning to the knowledge base to derive new facts or conclusions.
- A knowledge-based system can also have other components, such as a user interface, a knowledge acquisition module, a knowledge representation language, and a knowledge validation module.
- A knowledge-based system can be classified into different types based on the nature of the knowledge, the reasoning method, and the application domain.
- Some examples of knowledge-based systems are expert systems, case-based reasoning systems, neural networks, fuzzy systems, genetic algorithms, and hybrid systems.
- A knowledge-based system can provide various benefits, such as improving decision making, enhancing productivity, reducing errors, and facilitating learning and training.
- A knowledge-based system can also face various challenges, such as knowledge acquisition, knowledge representation, knowledge verification, knowledge maintenance, and knowledge integration.
- A knowledge-based system can be evaluated using different criteria, such as correctness, completeness, consistency, efficiency, usability, and adaptability.



# A 'knowledge level' approach to the interaction with an IAS- TELOS

- A 'knowledge level' approach to the interaction with an IAS- TELOS is a way of designing and implementing intelligent information systems that combine symbolic and connectionist components.
- An IAS- TELOS is an Intelligent Application System that uses TELOS as its knowledge representation language. TELOS stands for TELefonika Ontology System, and it is a framework for representing knowledge about information systems, such as databases, software, and networks.
- A 'knowledge level' approach is based on the idea that the appropriateness of any form of knowledge depends on the telos, or purpose, it serves. For example, the purpose of a theoretical discipline is to pursue truth through contemplation, while the purpose of a practical discipline is to solve problems through action.
- A 'knowledge level' approach aims to balance the trade-off between data and knowledge, and between symbolic and connectionist processing, depending on the specific application and domain. Symbolic processing is more suitable for abstract and logical reasoning, while connectionist processing is more suitable for perceptual and associative learning.
- A 'knowledge level' approach involves the following steps:
  - Define the problem and the goal of the IAS- TELOS.
  - Identify the relevant data and knowledge sources, and the appropriate level of abstraction and granularity for each source.
  - Choose a suitable problem solving method, which may consist of symbolic and connectionist components, and map the data and knowledge sources to the method.
  - Implement the problem solving method using TELOS as the knowledge representation language, and integrate the symbolic and connectionist components using neurosymbolic techniques.
  - Evaluate the performance and accuracy of the IAS- TELOS, and refine the data, knowledge, and method as needed.



# A language for implementing very large 'integral approach' systems

- An integral approach is a way of understanding and designing systems that takes into account all the dimensions of reality, such as objective, subjective, individual, and collective .
- An integral approach can be applied to any domain of human activity, such as business, education, health, or engineering.
- An integral approach can help to create more holistic, human-centric, and effective solutions that address the complex challenges of the 21st century .
- A language for implementing very large 'integral approach' systems is a programming language that supports the development of systems that use the integral approach as a guiding framework.
- A language for implementing very large 'integral approach' systems should have the following features:

  - It should be able to handle multiple levels of abstraction, from low-level details to high-level concepts, and allow the integration of different types of data, such as quantitative, qualitative, symbolic, or narrative.
  - It should be able to support multiple perspectives, such as first-person, second-person, third-person, and fourth-person, and allow the representation of different values, beliefs, and worldviews.
  - It should be able to facilitate communication and collaboration among different stakeholders, such as developers, users, clients, and experts, and allow the negotiation of trade-offs and conflicts .
  - It should be able to incorporate feedback and learning mechanisms, such as testing, evaluation, adaptation, and improvement, and allow the evolution of the system over time .

- Some examples of languages that could be used for implementing very large 'integral approach' systems are:

  - Lisp: a general-purpose, functional, and symbolic language that supports multiple paradigms, such as procedural, object-oriented, logic, and meta-programming, and allows the manipulation of data and code as the same type of objects.
  - Python: a general-purpose, interpreted, and high-level language that supports multiple paradigms, such as imperative, functional, object-oriented, and dynamic, and allows the integration of various libraries and frameworks for data analysis, visualization, web development, and machine learning.
  - Prolog: a declarative, logic, and relational language that supports multiple paradigms, such as constraint, probabilistic, and meta-programming, and allows the representation of facts, rules, and queries as the same type of objects.



# The CYC project

- The CYC project is a long-term artificial intelligence project that aims to assemble a comprehensive ontology and knowledge base that spans the basic concepts and rules about how the world works.
- The project was started in 1984 by Douglas Lenat at MCC, a consortium of American computer, semiconductor, and electronics manufacturers, to advance work on artificial intelligence. In 1995, Lenat spun off the project as Cycorp, Inc., based in Austin, Texas.
- The main goal of the CYC project is to capture common sense knowledge, which is the implicit knowledge that other AI platforms may take for granted. For example, Cyc can infer that if a person is in a room, then the room is not empty, or that if a person is dead, then they are not alive.
- The CYC project uses a formal language called CycL to represent the ontology and knowledge base. CycL is a logic-based language that allows for expressing facts, rules, queries, and explanations. CycL also supports higher-order logic, which allows for reasoning about reasoning.
- The CYC project consists of two main components: the Cyc ontology and the Cyc knowledge base. The Cyc ontology is a hierarchy of concepts that covers various domains of human knowledge, such as mathematics, physics, biology, geography, history, culture, etc. The Cyc knowledge base is a collection of facts and rules that are associated with the concepts in the ontology.
- The CYC project has several applications in various fields, such as computer network risk assessment, abductive reasoning and scenario generation for terrorist threat anticipation, military and commercial intelligence analysis support, decision support for space launch facilities, learning-by-teaching, simulation of realistic emotional responses, natural language understanding and generation, etc.



# Other projects based on a 'conceptual representation' approach

- Conceptual representation is a way of describing the data and its relationships in a database without using a specific implementation or technology.
- Conceptual representation can help to understand the domain and the requirements of the database, as well as to communicate with stakeholders and users.
- Conceptual representation can also facilitate the design and development of the database, as well as the integration and interoperability of different data sources.
- Some examples of projects that use a conceptual representation approach for intelligent database systems are:

  - **Conceptual Graphs**: A system of logic based on the existential graphs of Charles Sanders Peirce and the semantic networks of artificial intelligence. They express meaning in a form that is logically precise, humanly readable, and computationally tractable.
  - **Ontologies**: A formal specification of the concepts, relations, and constraints in a domain of interest. They provide a common vocabulary and a shared understanding of the domain for humans and machines. They can also support reasoning and inference over the data.
  - **Knowledge Graphs**: A network of entities and their relations, enriched with semantic annotations and metadata. They can capture the context and the meaning of the data, as well as the provenance and the quality of the data sources. They can also enable complex queries and analytics over the data.
  - **Conceptual Data Models**: A high-level view of the data used to identify items and their connections. They define what is in and what is out of the database in a highly abstract manner. They can also help to scope and arrange the data elements and their interactions without considering the implementation details  .



# Lexical approaches to the construction of large KBs

- Lexical approaches are methods that use natural language texts as sources of knowledge for building large-scale knowledge bases (KBs).
- KBs are collections of facts and rules that represent the domain knowledge of a system, such as a knowledge-based system (KBS).
- KBSs are systems that use artificial intelligence techniques to solve complex problems by reasoning with the knowledge stored in the KBs.
- Lexical approaches can be divided into two categories: definitional and non-definitional.
- Definitional approaches use definitions of terms and concepts as the main source of knowledge extraction. They rely on linguistic and logical analysis of the definitions to extract the relevant facts and rules.
- Non-definitional approaches use other types of texts, such as encyclopedias, news articles, books, etc., as sources of knowledge extraction. They rely on natural language processing and machine learning techniques to identify and extract the relevant facts and rules.
- Lexical approaches have some advantages and disadvantages compared to other methods of KB construction, such as manual, semi-automatic, or ontology-based methods.
- Advantages:
  - They can exploit the large amount of textual data available on the web and other sources.
  - They can capture the diversity and richness of natural language expressions and meanings.
  - They can reduce the human effort and cost involved in KB construction.
- Disadvantages:
  - They can introduce errors and inconsistencies due to the low quality of the raw data and the limitations of the extraction techniques.
  - They can miss some implicit or contextual knowledge that is not explicitly stated in the texts.
  - They can face challenges in dealing with ambiguity, vagueness, and variability of natural language.



## Unit 5 - Applications in IDBS

- IDBS stands for Integrated Database Systems, which are systems that combine database management and application development capabilities in a single environment.
- IDBS can be used to develop various types of applications, such as data analysis, data visualization, data mining, data warehousing, decision support, and business intelligence.
- IDBS can also be used to create web-based applications that can access and manipulate data stored in databases through a web browser.
- Some of the benefits of using IDBS are:
  - Reduced development time and cost, as the same tool can be used for both database design and application development.
  - Increased consistency and quality, as the data and the application logic are integrated and managed by the same system.
  - Enhanced performance and scalability, as the system can optimize the data access and processing according to the application needs.
  - Improved security and reliability, as the system can enforce data integrity and backup policies, and handle concurrency and recovery issues.
- Some of the challenges of using IDBS are:
  - Increased complexity and learning curve, as the system may have its own syntax and features that differ from standard SQL and programming languages.
  - Reduced portability and interoperability, as the system may not be compatible with other database systems or platforms.
  - Limited flexibility and customization, as the system may impose some restrictions or limitations on the data model or the application functionality.
- Some of the examples of IDBS are:
  - Oracle Database, which provides a comprehensive platform for data management, application development, and business intelligence, with features such as PL/SQL, Oracle Forms, Oracle Reports, Oracle Application Express, and Oracle Business Intelligence Suite.
  - Microsoft Access, which is a desktop database system that allows users to create and use databases and applications, with features such as Visual Basic for Applications, Microsoft Forms, Microsoft Reports, and Microsoft Query.
  - FileMaker, which is a cross-platform database system that enables users to create and deploy custom applications, with features such as FileMaker Script, FileMaker Layout, FileMaker Chart, and FileMaker WebDirect.



### Introduction for the notes of the Unit 5 - Applications in IDBS in the subject of INTELLIGENT DATABASE SYSTEM

- Intelligent database systems (IDBS) are systems that integrate database management techniques with artificial intelligence methods to provide enhanced functionality and performance.
- IDBS can support various applications that require complex data analysis, knowledge discovery, decision making, and reasoning.
- Some of the applications of IDBS are:
  - Data mining and knowledge discovery: IDBS can use techniques such as clustering, classification, association rule mining, and anomaly detection to discover patterns and insights from large and heterogeneous data sources.
  - Expert systems and decision support systems: IDBS can use techniques such as rule-based systems, fuzzy logic, neural networks, and genetic algorithms to model domain knowledge and provide recommendations and solutions to users.
  - Natural language processing and information retrieval: IDBS can use techniques such as natural language understanding, natural language generation, information extraction, and text summarization to process and retrieve information from natural language texts and documents.
  - Multimedia and image processing: IDBS can use techniques such as image segmentation, feature extraction, face recognition, and content-based retrieval to process and analyze multimedia and image data.
  - Spatial and temporal databases: IDBS can use techniques such as spatial indexing, spatial query processing, spatial data mining, and temporal logic to manage and manipulate spatial and temporal data.
  - Web and social media databases: IDBS can use techniques such as web crawling, web mining, sentiment analysis, and recommender systems to collect and analyze data from the web and social media platforms.
- In this unit, we will learn about some of the IDBS applications in detail and understand their challenges and benefits.



# Temporal databases

- A temporal database is a database that has certain features that support time-sensitive status for entries .
- A temporal database can store data relating to past, present and future time instances.
- A temporal database can also track the history of data changes and support queries over different time dimensions  .
- Temporal databases can be classified into different types based on the time dimensions they support:
  - Uni-temporal: A database that supports only one time dimension, either valid time or transaction time.
  - Bi-temporal: A database that supports both valid time and transaction time dimensions.
  - Tri-temporal: A database that supports valid time, transaction time and decision time dimensions.
- Valid time is the time period during or event time at which a fact is true in the real world .
- Transaction time is the time period during which a fact is stored in the database .
- Decision time is the time point at which a fact is recorded or decided in the database.
- Temporal databases can offer various benefits for applications that need to handle time-sensitive data, such as auditing, historical analysis, trend detection, data recovery, compliance, etc .
- Temporal databases can also pose some challenges, such as increased storage requirements, complex query processing, data consistency, temporal integrity, etc.



# Basic concepts for the notes of the Unit 5 - Applications in IDBS in the subject of INTELLIGENT DATABASE SYSTEM

- An **intelligent database system** (IDBS) is a system that manages **information**, rather than simple data, and presents it in a way that is **natural and informative** for users .
- An IDBS goes beyond simple record keeping and provides **high level tools** for data quality, data mining, data analysis, data visualization, and data integration .
- An IDBS also has an **intelligent user interface** that adapts to the user's needs, preferences, and context, and provides **natural language processing**, **speech recognition**, and **multimodal interaction** .
- An IDBS also has an **intelligent database engine** that supports **advanced data models**, **query optimization**, **transaction management**, **security**, and **scalability** .
- Some of the **applications** of IDBS are:
  - **Business intelligence**: IDBS can help businesses to extract valuable insights from large and complex data sets, and to support decision making, planning, and forecasting .
  - **Personalization**: IDBS can help to tailor the content and services to the individual user's preferences, behavior, and context, and to provide personalized recommendations, suggestions, and feedback .
  - **Knowledge management**: IDBS can help to capture, store, organize, and share the knowledge and expertise of an organization, and to facilitate learning, collaboration, and innovation .
  - **Semantic web**: IDBS can help to create and use **ontologies** to represent the meaning and relationships of the data on the web, and to enable **semantic interoperability** and **reasoning** across different sources and domains .



# Temporal Data Models

- Temporal data models are data models that capture the changes of data over time, as well as the time references of the data.
- Temporal data models can be classified into three levels of abstraction: conceptual, logical, and physical.
- Conceptual level: the data models are generally extensions of the Entity-Relationship Model, which represent the entities, attributes, and relationships of a domain.
- Logical level: the data models are generally extensions of the relational data model or of an object-oriented data model, which define the schema, constraints, and operations of a database.
- Physical level: the data models detail how the data are to be stored, indexed, and accessed by the database system.
- Temporal data models can also be classified into three types of time references: valid time, transaction time, and decision time.
- Valid time: the time when the data is valid with respect to the real world, such as the birth date of a person, the duration of a contract, or the expiration date of a product.
- Transaction time: the time when the data is recorded in the database, such as the insertion, update, or deletion of a record.
- Decision time: the time when the data is used for decision making, such as the analysis, reporting, or querying of the data.
- Temporal data models can be uni-temporal, bi-temporal, or tri-temporal, depending on how many types of time references they capture.
- Uni-temporal: the data model captures only one type of time reference, either valid time or transaction time.
- Bi-temporal: the data model captures both valid time and transaction time, allowing to track the history and the current state of the data.
- Tri-temporal: the data model captures valid time, transaction time, and decision time, allowing to track the history, the current state, and the future projections of the data.



# Temporal Query Languages

- A temporal query language is a database query language that offers some form of built-in support for the querying and modification of time-referenced data, as well as enabling the specification of assertions and constraints on such data.
- Time-referenced data is data that has temporal attributes, such as valid time, transaction time, or event time, that indicate when the data is valid, stored, or occurred.
- Temporal query languages can be classified into two main categories: temporal extensions of existing query languages, such as SQL, and novel query languages designed specifically for temporal data.
- Temporal extensions of existing query languages aim to preserve the syntax and semantics of the original query language, while adding new temporal features, such as temporal data types, temporal predicates, temporal operators, and temporal modifiers .
- Novel query languages for temporal data are based on different data models and paradigms, such as logic programming, functional programming, or stream processing .
- Some examples of temporal extensions of SQL are TSQL2, ATSQL2, IXSQL, ATSQL, and SQL/TP . TSQL2 represents an effort to design a consensus data model and query language, and it includes many of the concepts that were proposed by earlier temporal data models and query languages.
- Some examples of novel query languages for temporal data are Tempura, TQuel, TLP, and Trill . Trill is an open source .NET library designed to process one trillion events a day, and it provides a temporal query language enabling you to embed real-time analytics in your own application.
- Temporal query languages can support different types of temporal semantics, such as snapshot semantics, sequenced semantics, or nonsequenced semantics . Snapshot semantics treats temporal data as if it were nontemporal, and applies the query to a single time point or interval. Sequenced semantics applies the query to each time point or interval in the temporal data, and returns a temporal result. Nonsequenced semantics applies the query to the entire temporal data, and returns a nontemporal result.
- Temporal query languages can also support different types of temporal operators, such as temporal selection, temporal projection, temporal join, temporal aggregation, temporal grouping, temporal coalescing, temporal slicing, temporal interpolation, and temporal extrapolation . Temporal operators can manipulate temporal data in various ways, such as filtering, transforming, combining, summarizing, merging, splitting, filling, and extending.
- Temporal query languages are useful for applications that deal with historical, current, and future data, such as business intelligence, data warehousing, data mining, event processing, stream processing, and temporal reasoning  . Temporal query languages can help to answer complex temporal queries, such as finding trends, patterns, anomalies, correlations, and causations in temporal data .



# Ontologies for the notes of the Unit 5 - Applications in IDBS in the subject of INTELLIGENT DATABASE SYSTEM

- Ontologies are formal systems for modeling concepts and their relationships in a given domain .
- Ontologies can be used to express data in which the relationships between objects are important, and to store the information in a graph database or triplestore.
- Ontologies can also be used to improve the effectiveness of the human-computer communication, by allowing users to pose queries based on terms from the ontology, and get answers that incorporate the term hierarchy or other logical features of the ontology .
- Ontologies can be implemented using several semantic languages, such as Resource Description Framework (RDF), Web Ontology Language (OWL), or Simple Knowledge Organization System (SKOS) .
- Ontologies can be applied to various domains and tasks, such as data mining, machine learning, social networks, recommendation systems, web services, cloud computing, security, intelligent internet systems, knowledge management, language processing, image, video, motion analysis and recognition, and more.



# Ontology Theoretical Foundations

Ontology is the philosophical study of being, as well as related concepts such as existence, becoming, and reality. Ontology addresses questions like how entities are grouped into categories and which of these entities exist on the most fundamental level.

Ontology is also a branch of knowledge engineering, artificial intelligence and computer science, that deals with the representation and reasoning of concepts, relations, and properties of a domain of interest. Ontology can be used for knowledge management, natural language processing, e-commerce, intelligent information integration, and information retrieval.

Ontology development can be done in a top-down or a bottom-up approach. A top-down approach starts from a high-level and general categorization of the domain, and then refines and specifies the concepts and relations according to the requirements and the data sources. A bottom-up approach starts from the data sources and the requirements, and then abstracts and generalizes the concepts and relations to form a coherent and consistent ontology.

A foundational ontology is a type of top-down ontology that provides a high-level and domain-independent categorization of the kinds of things that exist in the world, such as objects, events, processes, qualities, relations, etc. A foundational ontology can be used as a basis for developing more specific and domain-dependent ontologies, by reusing and extending the concepts and relations defined in the foundational ontology .

Some examples of foundational ontologies are:

- Basic Formal Ontology (BFO): a minimalist and realist ontology that distinguishes between continuants (things that persist through time) and occurrents (things that happen in time), and defines various relations such as parthood, dependence, and participation.
- Descriptive Ontology for Linguistic and Cognitive Engineering (DOLCE): a cognitivist and descriptive ontology that focuses on the human perspective and common sense, and distinguishes between endurants (things that endure in time) and perdurants (things that perdure in time), and defines various relations such as constitution, quality, and quale.
- General Formal Ontology (GFO): a hybrid and modular ontology that combines aspects of BFO and DOLCE, and distinguishes between categories (things that are independent of time) and chronoids (things that are dependent on time), and defines various relations such as instantiation, inherence, and predication.

The choice of a foundational ontology depends on the purpose and scope of the ontology development, as well as the ontological commitments and assumptions of the ontology developers. Different foundational ontologies may have different advantages and disadvantages, such as expressiveness, clarity, consistency, compatibility, and applicability .



# Environments for building ontologies

- An ontology is a formal representation of the concepts and relationships in a domain of interest.
- Ontology engineering is the process of developing and maintaining ontologies.
- Ontology engineering environments are tools that support the ontology engineering process by providing functionalities such as editing, browsing, querying, reasoning, and sharing ontologies.
- There are different types of ontology engineering environments, depending on the purpose, scope, and methodology of ontology development.
- Some of the factors that can be used to evaluate ontology engineering environments are:

  - The expressiveness and standardization of the ontology language
  - The usability and functionality of the ontology editor
  - The availability and integration of ontology libraries and resources
  - The support for ontology reuse and alignment
  - The support for ontology evaluation and validation
  - The support for ontology evolution and maintenance
  - The support for ontology collaboration and dissemination

- Some of the examples of ontology engineering environments are:

  - OntoEdit: A graphical ontology editor that supports multiple ontology languages and formats, such as RDF(S), OWL, and XML. It also provides features such as ontology visualization, modularization, merging, and mapping.
  - WebODE: A web-based ontology engineering platform that supports ontology development, management, and reuse. It also provides features such as ontology import and export, ontology annotation, ontology query and inference, and ontology publication.
  - Protege: An open-source ontology editor and framework that supports various ontology languages and formats, such as RDF(S), OWL, and XML Schema. It also provides features such as ontology import and export, ontology annotation, ontology query and inference, and ontology plugins.
  - Hozo: An ontology engineering environment that focuses on the role and relationship concepts in ontology modeling. It also provides features such as ontology editor, ontology studio, and ontology server .



# Structured, semi-structured and unstructured data

- Structured data is data with a high degree of organization, typically stored in a spreadsheet-like manner. It has a predefined schema and follows a rigid format. Examples of structured data are relational databases, CSV files, XML files, etc. Structured data is easy to query, analyze and manipulate using SQL or other programming languages. Structured data is used in machine learning and drives its algorithms   .
- Semi-structured data is data with some degree of organization, but not as much as structured data. It does not follow a tabular data structure, but it has some elements that can be used to group or categorize the data, such as tags, labels, keys, etc. Examples of semi-structured data are JSON files, HTML files, log files, etc. Semi-structured data is more flexible than structured data, but still requires some processing to extract useful information. Semi-structured data is the “bridge” between structured and unstructured data    .
- Unstructured data is data with no predefined organizational form and no specific format. It is a collection of many varied data types that are stored in their native formats. Examples of unstructured data are text documents, images, videos, audio files, social media posts, etc. Unstructured data is the most complex and abundant type of data, but also the most difficult to analyze and process. It requires advanced techniques such as natural language processing and text mining to extract meaningful insights. Unstructured data is used in natural language processing and text mining     .

: https://www.indeed.com/career-advice/career-development/structured-vs-unstructured-vs-semi-structured-data
: https://www.michael-gramlich.com/what-is-structured-semi-structured-and-unstructured-data/
: https://k21academy.com/microsoft-azure/dp-900/structured-data-vs-unstructured-data-vs-semi-structured-data/
: https://www.geeksforgeeks.org/difference-between-structured-semi-structured-and-unstructured-data/
: https://www.ibm.com/cloud/blog/structured-vs-unstructured-data
: https://www.forbes.com/sites/bernardmarr/2019/10/18/whats-the-difference-between-structured-semi-structured-and-unstructured-data/



# Multimedia Database

A multimedia database (MMDB) is a database that hosts one or more multimedia data types, such as text, images, graphics, audio, video, and animation. Multimedia data types are broadly categorized into three classes:

- Static media: time-independent data, such as images and graphics.
- Dynamic media: time-dependent data, such as audio, video, and animation.
- Dimensional media: data that have spatial or temporal dimensions, such as 3D models and virtual reality.

Multimedia databases have some unique characteristics and challenges compared to traditional databases, such as:

- Large size and variety of data formats and types.
- Complex and diverse queries and retrieval methods.
- High bandwidth and performance requirements.
- Need for integration and synchronization of different media types.
- Need for content-based analysis and indexing of multimedia data.

Multimedia databases have many applications in various domains, such as:

- Documents and records management: industries and businesses that keep detailed records and documents, such as legal, medical, and financial sectors.
- Knowledge dissemination: multimedia databases are effective tools for knowledge dissemination, such as e-learning, online courses, and tutorials.
- Education and entertainment: multimedia databases are widely used for education and entertainment purposes, such as games, movies, music, and art.
- Scientific and engineering research: multimedia databases are useful for scientific and engineering research, such as computer vision, image processing, and computer graphics.



# Semi-structured data

- Semi-structured data is a form of structured data that does not obey the tabular structure of data models associated with relational databases or other forms of data tables   .
- Semi-structured data can include data that is quantitative, or numerical, as well as data that is qualitative, or textual.
- Semi-structured data can also include data that has an organizational structure understandable to both machines and humans, such as tags, metadata, or hierarchies   .
- Examples of semi-structured data are:
  - Email: Email is a type of semi-structured data that many employees and businesses use regularly. The written content of the email is unstructured, but the email header, sender, recipient, subject, and date are structured.
  - HTML: Webpages you can create through Hypertext Markup Language (HTML) use semi-structured data. HTML refers to a set of tags that define the structure and content of a webpage. The tags are structured, but the content within the tags can be unstructured.
  - Online images and videos: Online images and videos can have semi-structured data associated with them, such as captions, descriptions, tags, ratings, comments, and metadata. The images and videos themselves are unstructured, but the data that describes them is structured.
  - JSON: JavaScript Object Notation (JSON) is a popular format for exchanging data on the web. JSON uses a syntax that resembles JavaScript objects, with key-value pairs and arrays. JSON data is semi-structured, as it can contain nested and complex data structures, but it also follows a consistent and predictable format.
  - XML: Extensible Markup Language (XML) is another common format for exchanging data on the web. XML uses a syntax that resembles HTML, with tags and attributes. XML data is semi-structured, as it can contain nested and complex data structures, but it also follows a set of rules and standards.
- Benefits of semi-structured data are:
  - Flexibility: Semi-structured data can accommodate changes in the data schema or structure without requiring extensive modifications or migrations. Semi-structured data can also handle data that is heterogeneous, incomplete, or inconsistent .
  - Scalability: Semi-structured data can be stored and processed in distributed systems, such as cloud platforms or big data frameworks, that can handle large volumes and varieties of data. Semi-structured data can also be compressed and optimized for faster and more efficient processing .
  - Interoperability: Semi-structured data can be easily converted or transformed into other formats, such as CSV, XML, or JSON, depending on the needs and preferences of the users or applications. Semi-structured data can also be integrated or combined with other types of data, such as structured or unstructured data, to provide a more comprehensive and holistic view of the data .



# Mediators for the notes of the Unit 5 - Applications in IDBS in the subject of INTELLIGENT DATABASE SYSTEM

- A mediator is a software component that provides a uniform interface to heterogeneous data sources, such as databases, legacy systems, web services, etc. 
- A mediator can perform various tasks, such as data integration, query processing, data transformation, data analysis, etc. 
- A mediator can be classified into two types: wrapper mediators and integrator mediators. 
  - A wrapper mediator is a mediator that encapsulates a single data source and provides a common data model and query language for accessing it. 
  - An integrator mediator is a mediator that combines data from multiple wrapper mediators and provides a global view of the integrated data. 
- A mediator can be used for various applications in intelligent database systems (IDBSs), such as:
  - Providing convenient access to heterogeneous and distributed data sources. 
  - Enhancing the functionality and performance of existing data sources. 
  - Supporting complex and intelligent queries over integrated data. 
  - Enabling interoperability and collaboration among different data sources and users. 
  - Incorporating domain knowledge and inference mechanisms into data processing. 
  - Facilitating the development and maintenance of IDBSs.



# Motivation for the notes of the Unit 5 - Applications in IDBS in the subject of INTELLIGENT DATABASE SYSTEM

- Intelligent database systems (IDBS) are systems that integrate database management and artificial intelligence techniques to support various tasks such as data analysis, decision making, knowledge discovery, and problem solving.
- IDBS have many potential applications in various domains, such as business, science, engineering, medicine, education, and social media.
- In this unit, we will explore some of the applications of IDBS in different areas, such as:
  - Data mining and knowledge discovery: how IDBS can extract useful patterns and insights from large and complex data sets.
  - Recommender systems: how IDBS can provide personalized and relevant suggestions to users based on their preferences and behavior.
  - Natural language processing: how IDBS can understand and generate natural language texts and queries.
  - Image processing and computer vision: how IDBS can process and analyze images and videos for various purposes, such as face recognition, object detection, and scene understanding.
  - Bioinformatics and health informatics: how IDBS can help in analyzing and interpreting biological and medical data, such as DNA sequences, protein structures, and electronic health records.
- The main objectives of this unit are to:
  - Introduce the concepts and techniques of IDBS in different application domains.
  - Illustrate the benefits and challenges of IDBS in real-world scenarios.
  - Provide examples and case studies of IDBS applications in various fields.
  - Encourage students to explore and evaluate IDBS applications in their own areas of interest.



# Architecture for the notes of the Unit 5 - Applications in IDBS

- An intelligent database system (IDBS) is a system that combines the capabilities of a database management system (DBMS) with artificial intelligence (AI) techniques to provide efficient and effective access, processing and analysis of data.
- An IDBS can be applied to various domains and scenarios, such as banking, education, health care, e-commerce, social media, etc. Some of the benefits and challenges of IDBS applications are:

  - Banking: An IDBS can help banks to manage transactions, customer data, fraud detection, risk analysis, etc. An IDBS can also provide personalized services and recommendations to customers based on their preferences and behavior. However, an IDBS also faces challenges such as security, privacy, scalability, and compliance with regulations.
  - Education: An IDBS can help educational institutions to conduct online examinations, evaluate student performance, provide feedback, and design adaptive learning systems. An IDBS can also help students to access relevant information, learn at their own pace, and collaborate with peers. However, an IDBS also faces challenges such as quality, reliability, fairness, and ethics of the educational data and processes.
  - Health care: An IDBS can help health care providers to store and retrieve medical records, diagnose diseases, prescribe treatments, and monitor patients. An IDBS can also help patients to access health information, manage their health conditions, and communicate with doctors. However, an IDBS also faces challenges such as accuracy, privacy, security, and trust of the health data and decisions.
  - E-commerce: An IDBS can help e-commerce platforms to manage inventory, transactions, customer data, and marketing. An IDBS can also help customers to find products, compare prices, and get recommendations based on their preferences and behavior. However, an IDBS also faces challenges such as competition, fraud, customer satisfaction, and loyalty.
  - Social media: An IDBS can help social media platforms to manage user data, content, and interactions. An IDBS can also help users to discover, share, and consume information, express opinions, and connect with others. However, an IDBS also faces challenges such as privacy, security, misinformation, and polarization.

- An IDBS can be designed and implemented using different architectures and components, such as:

  - Intelligent database interfaces: These are cache-based systems that can efficiently access one or more DBMSs, remote or not, and provide flexible options for conducting queries. They can also interact with users to ensure that they are supplied with all relevant information.
  - Intelligent data platforms: These are comprehensive data platforms that can integrate data from various sources, such as operational databases, business applications, cloud services, etc., and provide data integration, transformation, analysis, and visualization capabilities. They can also leverage AI techniques such as machine learning, natural language processing, computer vision, etc., to enable data-driven innovation and agility.
  - Intelligent data mining tools: These are high-level tools that can manage data quality and automatically discover relevant patterns in the data, such as associations, clusters, classifications, predictions, etc., using AI techniques such as machine learning, neural networks, genetic algorithms, etc. They can also provide explanations, interpretations, and evaluations of the data mining results.



# Application of mediators to heterogeneous systems for the notes of the Unit 5 - Applications in IDBS in the subject of INTELLIGENT DATABASE SYSTEM

- A mediator is a software component that provides a uniform interface to access heterogeneous data sources, such as relational databases, XML files, web services, etc. 
- A mediator can perform various tasks, such as data transformation, query processing, data integration, data analysis, etc.   
- A mediator can be useful for intelligent database systems, which aim to provide intelligent services to users, such as data mining, knowledge discovery, decision support, etc. 
- A mediator can enable intelligent database systems to access and integrate data from multiple and diverse sources, which can enhance the quality and quantity of the available information.  
- A mediator can also support intelligent database systems to monitor and update the data sources, which can improve the timeliness and accuracy of the information. 
- A mediator can also facilitate intelligent database systems to perform complex and distributed queries over the data sources, which can increase the efficiency and scalability of the system. 
- Some examples of applications of mediators to heterogeneous systems for intelligent database systems are:
  - An XML Mediator (XMed) that can access and process data from different XML sources, such as web services, XML databases, etc. 
  - An Intelligent Software Agents (ISA) system that can create and execute standing requests for information (SRIs) that monitor multiple heterogeneous data sources for changes critical to the predicted success of a plan. 
  - A mediation-based integration system that can integrate incomplete and uncertain information from heterogeneous relational databases, such as customer data, product data, etc. 
  - A semantic integration system that can integrate heterogeneous proteomic data from different sources, such as protein annotation, protein-protein interaction, protein structure, etc. 

: An Intelligent Mediator for Heterogeneous Data Sources
: Intelligent Monitoring of Distributed, Heterogeneous Data Sources
: Intelligent data integration from heterogeneous relational databases containing incomplete and uncertain information
: A Mediator Approach for a Semantic Integration of Heterogeneous Proteomic Data Sources



# Proposals for the notes of the Unit 5 - Applications in IDBS in the subject of INTELLIGENT DATABASE SYSTEM

- An intelligent database is a full-text database with artificial intelligence (AI) components that interact with users to ensure that users are supplied all relevant information.
- An intelligent database system (IDBS) is a system that manages information (rather than data) in a way that appears natural to users and which goes beyond simple record keeping.
- An IDBS has three levels of intelligence: high level tools, the user interface and the database engine.
- High level tools manage data quality and automatically discover relevant patterns in the data with a process called data mining.
- The user interface provides natural language processing, speech recognition, graphical visualization and multimedia capabilities to facilitate user interaction with the system.
- The database engine supports advanced data models, query languages, inference mechanisms, rules, triggers and constraints to enable efficient and flexible data manipulation and reasoning.
- Some of the applications of IDBS are:
  - Business intelligence: IDBS can help businesses analyze their data and gain insights into their performance, customers, competitors and market trends.
  - Knowledge management: IDBS can help organizations capture, store, share and reuse their knowledge assets, such as documents, reports, best practices and lessons learned.
  - Decision support: IDBS can help decision makers access and evaluate relevant information, generate and compare alternatives, and choose the best course of action.
  - Personalization: IDBS can help customize the content and services delivered to users based on their preferences, behavior and feedback.
  - Recommendation: IDBS can help suggest products, services, information or actions to users based on their needs, interests and goals.
  - Fraud detection: IDBS can help detect and prevent fraudulent activities, such as credit card fraud, insurance fraud and identity theft, by analyzing patterns and anomalies in the data.
  - Security: IDBS can help protect the data and the system from unauthorized access, modification or deletion, by enforcing policies, rules and encryption.
- Some of the challenges of IDBS are:
  - Data quality: IDBS need to ensure that the data they use and produce are accurate, complete, consistent and timely.
  - Data integration: IDBS need to integrate data from multiple sources, formats and domains, and resolve any conflicts or inconsistencies.
  - Data privacy: IDBS need to respect the privacy and confidentiality of the data and the users, and comply with any ethical or legal regulations.
  - Scalability: IDBS need to handle large volumes of data and users, and provide fast and reliable performance.
  - Explainability: IDBS need to provide transparent and understandable explanations for their results and recommendations, and allow users to provide feedback and corrections.
  - Trust: IDBS need to build and maintain the trust and confidence of the users, and ensure that they are not biased, manipulated or deceived.



# Multi-Agent Systems for the Notes of the Unit 5 - Applications in IDBS in the Subject of Intelligent Database Systems

- A multi-agent system (MAS) is a computerized system composed of multiple interacting intelligent agents that can solve problems that are difficult or impossible for an individual agent or a monolithic system to solve.
- An intelligent agent is an entity that can perceive its environment, reason, learn, and act autonomously or semi-autonomously to achieve its goals.
- A multi-agent system can be seen as a distributed artificial intelligence (DAI) system that involves cooperation, coordination, or competition among agents in a shared environment.
- Multi-agent systems can be applied to various domains that require distributed control, such as online trading, disaster response, target surveillance, and social structure modelling .
- Some examples of multi-agent systems applications in intelligent database systems are:
  - Ambient intelligence: a vision of human-centric computing that aims to provide intelligent and personalized services to users in a natural and unobtrusive way. Multi-agent systems can provide a paradigm to design ambient intelligent applications that can adapt to the user's preferences, context, and needs.
  - Data mining: a process of discovering useful patterns and knowledge from large and complex data sets. Multi-agent systems can enhance data mining by enabling distributed, parallel, and collaborative analysis of data, as well as providing intelligent decision support to the users.
  - Semantic web: an extension of the current web that aims to make the data more understandable and interoperable by machines. Multi-agent systems can facilitate the semantic web by providing mechanisms for ontology creation, alignment, and reasoning, as well as for information retrieval, integration, and exchange.



# Main issues in designing a multi-agent system

A multi-agent system (MAS) is a system composed of multiple autonomous and interacting agents that can cooperate, coordinate, or compete to achieve common or individual goals. MAS can be applied to various domains, such as intelligent databases, distributed problem solving, e-commerce, social simulation, and robotics.

However, designing a MAS is not a trivial task, as it involves many challenges and issues, such as:

- **Interoperability**: How to ensure that the agents can communicate and exchange information with each other and with other systems, regardless of their heterogeneity, diversity, and complexity. This requires standard protocols, languages, ontologies, and architectures for agent communication and interaction .
- **Coordination**: How to manage the dependencies and interactions among the agents and their tasks, such as task allocation, resource sharing, synchronization, negotiation, and collaboration. This requires effective mechanisms and strategies for agent coordination, such as contracts, auctions, coalitions, and norms .
- **Conflict**: How to deal with the potential conflicts and inconsistencies that may arise among the agents and their goals, beliefs, and actions, such as competition, disagreement, deception, and violation. This requires robust methods and techniques for conflict resolution, such as argumentation, voting, mediation, and trust .
- **Ethics**: How to ensure that the agents behave in a moral and responsible way, respecting the values, norms, and laws of the society and the environment in which they operate. This requires ethical principles, frameworks, and guidelines for agent design, evaluation, and governance .



# Open problems for the notes of the Unit 5 - Applications in IDBS in the subject of INTELLIGENT DATABASE SYSTEM

- Intelligent database systems (IDBS) are databases that integrate artificial intelligence techniques, such as machine learning, natural language processing, and knowledge representation, to provide advanced functionalities and services to users and applications.
- IDBS have many applications in various domains, such as business intelligence, e-commerce, health care, education, and social media.
- However, IDBS also face many open problems and challenges, such as:

  - **Data quality and integration**: IDBS need to deal with heterogeneous, incomplete, inconsistent, and noisy data from various sources, and ensure that the data is accurate, reliable, and up-to-date. Data quality and integration techniques, such as data cleaning, data fusion, data lineage, and data provenance, are essential for IDBS to maintain data quality and integrity.
  - **Data security and privacy**: IDBS need to protect the data and the users from unauthorized access, modification, or disclosure, and respect the users' preferences and rights regarding their data. Data security and privacy techniques, such as encryption, authentication, authorization, anonymization, and differential privacy, are important for IDBS to ensure data confidentiality and compliance.
  - **Data scalability and performance**: IDBS need to handle large volumes of data and support high concurrency and availability of the data and the services. Data scalability and performance techniques, such as distributed computing, parallel processing, caching, indexing, and query optimization, are crucial for IDBS to achieve data efficiency and effectiveness.
  - **Data analysis and mining**: IDBS need to extract useful information and knowledge from the data and provide insights and recommendations to the users and the applications. Data analysis and mining techniques, such as classification, clustering, association, regression, and anomaly detection, are key for IDBS to enable data discovery and exploration.
  - **Data interaction and presentation**: IDBS need to communicate with the users and the applications in natural and intuitive ways and provide them with relevant and personalized data and services. Data interaction and presentation techniques, such as natural language processing, speech recognition, dialogue systems, visualization, and recommendation systems, are vital for IDBS to enhance data usability and user experience.



# Internet indexing and retrieval

- Internet indexing and retrieval is the process of collecting, parsing, storing, and searching data from the Internet to provide fast and accurate information to users.
- Internet indexing and retrieval involves the following steps:
  - Crawling: Scouring the Internet for content, looking over the code/content for each URL they find.
  - Indexing: Storing and organizing the content found during the crawling process. Once a page is in the index, it’s in the running to be displayed as a result to relevant queries.
  - Ranking: Sorting the indexed pages by relevance and popularity for each query.
  - Retrieving: Displaying the ranked pages to the user in a user-friendly format.
- Internet indexing and retrieval is an application of intelligent database systems (IDBS) because it uses techniques such as natural language processing, information extraction, data mining, machine learning, and artificial intelligence to improve the quality and efficiency of information retrieval .
- Internet indexing and retrieval faces many challenges, such as:
  - Handling the large and dynamic nature of the Internet data .
  - Dealing with the heterogeneity and ambiguity of the data formats, languages, and semantics .
  - Providing relevant and personalized results to the user's needs and preferences .
  - Ensuring the security, privacy, and trustworthiness of the data and the system .
- Internet indexing and retrieval can benefit from the subject approach, which is the application of subject analysis and representation to the Internet data to enhance the retrieval performance and user satisfaction.
- The subject approach involves the following aspects:
  - Subject identification: Determining the main topics and concepts of the data.
  - Subject representation: Assigning appropriate terms, codes, or symbols to represent the subjects of the data.
  - Subject organization: Establishing relationships and structures among the subject terms, such as hierarchies, networks, or facets.
  - Subject access: Providing tools and interfaces for the user to browse, search, and navigate the subject terms and the data.



# Basic indexing methods for the notes of the Unit 5 - Applications in IDBS in the subject of INTELLIGENT DATABASE SYSTEM

- Indexing is a way to optimize the performance of a database by minimizing the number of disk accesses required when a query is processed.
- Indexing is a data structure technique which is used to quickly locate and access the data in a database.
- Indexes are created using a few database columns.
- Indexing in Database is defined based on its indexing attributes.
- Two main types of indexing methods are:
  - Primary Indexing
  - Secondary Indexing
- Primary Indexing
  - Primary Index is an ordered file which is fixed length size with two fields.
  - The first field is the same as a primary key and the second field is a pointer to that specific data block.
  - Primary Index is defined on an ordered data file. The data file is ordered on a key field.
  - Primary Indexing is also further divided into two types:
    - Dense Index
    - Sparse Index
  - Dense Index
    - In a dense index, a record is created for every search key value in the database.
    - The index file size is large and requires more disk space.
    - The index file is updated frequently when new records are inserted or deleted.
  - Sparse Index
    - In a sparse index, a record is created for only some of the search key values in the database.
    - The index file size is small and requires less disk space.
    - The index file is updated less frequently when new records are inserted or deleted.
- Secondary Indexing
  - Secondary Index may be generated from a field which is a candidate key and has a unique value in every record, or a non-key with duplicate values.
  - Secondary Index is an ordered file with two fields.
  - The first field is the same as the secondary key and the second field is a pointer to the primary index record.
  - Secondary Index is defined on an unordered data file.
  - Secondary Indexing is useful for queries that do not involve the primary key.
- Other indexing techniques for advanced database systems
  - Traditional indexing techniques such as the B-tree and its variants do not efficiently support some applications, such as spatial, temporal, multimedia, or text databases.
  - As a result of the demand for database support for new applications, there has been a proliferation of new indexing techniques.
  - Some examples of new indexing techniques are:
    - R-tree and its variants for spatial databases
    - B+-tree and its variants for temporal databases
    - Signature file and inverted file for text databases
    - Bitmap index and join index for data warehousing
    - Grid file and hash-based index for multidimensional databases



# Search engines or meta-searchers for the notes of the Unit 5 - Applications in IDBS in the subject of INTELLIGENT DATABASE SYSTEM

- A search engine is a software system that allows users to find information on the web by using keywords or queries. A search engine typically consists of three components: a crawler, an indexer, and a query processor. The crawler scans the web and collects documents that match certain criteria. The indexer organizes the documents into a data structure called an index, which facilitates fast and accurate retrieval. The query processor interprets the user's query and returns a ranked list of relevant documents from the index.
- A meta-search engine is a type of search engine that does not have its own index, but instead aggregates the results from multiple other search engines. A meta-search engine may apply its own ranking algorithm or filter to the results, or simply display them as they are. A meta-search engine can offer some advantages over a single search engine, such as broader coverage, diversity, and redundancy.
- Some examples of search engines are Google, Bing, and Yahoo. Some examples of meta-search engines are Dogpile, Metacrawler, and WebCrawler.
- Search engines and meta-search engines can be used for various applications in intelligent database systems (IDBS), such as information retrieval, data integration, data mining, and knowledge discovery. IDBS are database systems that incorporate artificial intelligence techniques to provide intelligent services to users, such as natural language processing, reasoning, learning, and adaptation.
- Some of the topics that can be covered in the notes of the Unit 5 - Applications in IDBS are:

  - Information retrieval: the process of finding relevant information from a large collection of documents, such as the web. Information retrieval involves indexing, querying, ranking, and evaluation of the results. Some of the challenges and techniques in information retrieval are: handling unstructured data, dealing with synonyms and ambiguity, relevance feedback, query expansion, and personalization.
  - Data integration: the process of combining data from multiple sources into a unified view, such as a data warehouse. Data integration involves schema matching, data cleaning, data transformation, and data fusion. Some of the challenges and techniques in data integration are: handling heterogeneity, inconsistency, incompleteness, and uncertainty of the data, entity resolution, record linkage, and data provenance.
  - Data mining: the process of discovering patterns, trends, and associations from large and complex data sets, such as transactional, spatial, temporal, and multimedia data. Data mining involves classification, clustering, association rule mining, anomaly detection, and prediction. Some of the challenges and techniques in data mining are: handling high dimensionality, scalability, noise, and outliers, feature selection, feature extraction, and dimensionality reduction.
  - Knowledge discovery: the process of extracting useful and actionable knowledge from data, such as rules, models, and insights. Knowledge discovery involves data preprocessing, data mining, and postprocessing. Some of the challenges and techniques in knowledge discovery are: handling uncertainty, incompleteness, and inconsistency of the knowledge, knowledge representation, knowledge validation, and knowledge visualization.

: https://www.makeuseof.com/tag/technology-explained-what-is-a-meta-search-engine/
: https://www.makeuseof.com/tag/technology-explained-what-is-a-meta-search-engine/
: https://www.lifewire.com/best-search-engines-2483352
: https://paperpile.com/g/academic-search-engines/



# Internet spiders

- An Internet spider is a program designed to "crawl" over the World Wide Web, the portion of the Internet most familiar to general users, and retrieve locations of Web pages .
- It is sometimes referred to as a webcrawler, a search bot or simply a bot .
- Many search engines use webcrawlers to obtain links, which are filed away in an index .
- Webcrawlers copy pages for processing by a search engine, which indexes the downloaded pages so that users can search more efficiently.
- Webcrawlers can also perform other tasks, such as validating HTML code, checking for broken links, extracting data, or monitoring website changes.
- Webcrawlers follow a set of rules or policies to determine which pages to visit and how often.
- Some of these rules are specified by the website owners using a file called robots.txt, which can allow or disallow certain webcrawlers from accessing parts of the website.
- Other rules are based on the webcrawler's own algorithms, such as prioritizing popular or frequently updated pages, or avoiding duplicate or irrelevant content.
- Webcrawlers can also cooperate or compete with each other, depending on their goals and strategies.
- Webcrawlers are essential for the functioning of the Internet, as they enable search engines to provide relevant and up-to-date information to users.
- Webcrawlers also pose some challenges and limitations, such as consuming bandwidth and resources, respecting privacy and security, and dealing with dynamic or complex web content.



# Data mining for the notes of the Unit 5 - Applications in IDBS in the subject of INTELLIGENT DATABASE SYSTEM

- Data mining is a process of discovering patterns in a large set of data and data warehouses using various techniques such as regression analysis, association, and clustering, classification, and outlier analysis.
- Data mining is a crucial component of successful analytics initiatives in organizations, as it can generate useful information for business intelligence (BI) and advanced analytics applications.
- Data mining can also be applied to real-time analytics applications that examine streaming data as it is created or collected.
- Data mining has many applications in different domains and industries, such as:
  - Sales and marketing: Data mining can help companies collect and analyze data about their customers and prospects, such as their preferences, behavior, and feedback. This can help them segment their market, target their campaigns, personalize their offers, and improve their customer satisfaction and loyalty.
  - Banking and finance: Data mining can help banks and financial institutions detect fraud, assess credit risk, optimize portfolio management, and improve customer service.
  - Healthcare and biomedicine: Data mining can help healthcare providers and researchers diagnose diseases, predict outcomes, identify risk factors, and discover new drugs and treatments.
  - Manufacturing and engineering: Data mining can help manufacturers and engineers optimize production processes, improve product quality, reduce costs, and enhance safety.
  - Education and e-learning: Data mining can help educators and learners analyze learning data, such as test scores, assignments, and feedback. This can help them improve teaching methods, personalize learning paths, and evaluate learning outcomes.
- Data mining techniques and applications can be integrated with intelligent database systems (IDBS), which are database systems that incorporate artificial intelligence (AI) methods, such as machine learning, natural language processing, and knowledge representation, to support data management and analysis.
- IDBS can provide the following benefits for data mining:
  - Data preprocessing: IDBS can help clean, transform, and integrate data from different sources and formats, and handle missing, noisy, and inconsistent data.
  - Data storage and retrieval: IDBS can help store and access large and complex data sets efficiently and securely, and support various data models and query languages.
  - Data analysis and mining: IDBS can help apply various data mining techniques, such as classification, clustering, association, and outlier analysis, to extract useful patterns and knowledge from data.
  - Data visualization and presentation: IDBS can help present and communicate the results of data mining in an understandable and interactive way, using various graphical and textual tools.
  - Data feedback and refinement: IDBS can help evaluate and improve the quality and relevance of data mining results, and incorporate user feedback and domain knowledge to refine the data mining process.
- Some examples of IDBS that support data mining are:
  - Intelligent Data Mining (IDM): A series of books that present various data mining techniques and applications in different domains, such as economics, management, industrial engineering, and bioinformatics.
  - Intelligent Data Analysis (IDA): A journal that publishes original research papers on data analysis and mining, with a focus on AI methods and applications.
  - Intelligent Data Engineering and Automated Learning (IDEAL): A conference that covers topics on data engineering, data mining, machine learning, and computational intelligence.
  - Intelligent Data Analysis and Applications (IDAA): A workshop that aims to provide a platform for researchers and practitioners to exchange ideas and experiences on data analysis and applications.



# Data mining tasks

Data mining is a computer-assisted technique used in analytics to process and explore large data sets. With data mining tools and methods, organizations can discover hidden patterns and relationships in their data. Data mining transforms raw data into practical knowledge.

Data mining tasks are designed to be semi-automatic or fully automatic and on large data sets to uncover patterns such as groups or clusters, unusual or over the top data called anomaly detection and dependencies such as association and sequential pattern.

Data mining tasks can be classified into two types: descriptive and predictive.

- Descriptive mining tasks define the common features of the data in the database, such as summarization, visualization, clustering, etc.
- Predictive mining tasks act in inference on the current information to develop predictions, such as classification, regression, time-series analysis, etc.

A data mining system can execute one or more of the above specified tasks as part of data mining.

Some of the applications of data mining in IDBS are:

- Customer relationship management: Data mining can help identify customer segments, predict customer behavior, optimize marketing campaigns, etc.
- Fraud detection: Data mining can help detect anomalous transactions, identify fraud patterns, prevent losses, etc.
- Bioinformatics: Data mining can help analyze biological data, such as DNA sequences, gene expression, protein structures, etc.
- Web mining: Data mining can help extract useful information from web data, such as web content, web structure, web usage, etc.
- Text mining: Data mining can help extract meaningful information from unstructured text data, such as documents, emails, social media, etc.



# Data mining tools for the notes of the Unit 5 - Applications in IDBS in the subject of INTELLIGENT DATABASE SYSTEM

- Data mining is the process of discovering patterns, trends, and relationships in large and complex data sets to support informed decision-making and planning .
- Data mining tools are software applications that enable data analysts and data scientists to apply various data mining techniques, such as clustering, classification, regression, association, anomaly detection, and text mining, to extract valuable insights from data  .
- Data mining tools can be integrated with various data sources, such as relational databases, data warehouses, data lakes, multidimensional cubes, web data, social media data, sensor data, and unstructured data  .
- Data mining tools can also provide features for data preparation, data visualization, data modeling, data evaluation, and data deployment  .
- Some examples of data mining tools are Oracle Data Mining, IBM SPSS Modeler, RapidMiner, KNIME, SAS Enterprise Miner, and Weka.
- Data mining tools can be used for various applications in intelligent database systems, such as:
  - Customer segmentation and profiling: Data mining tools can help identify and group customers based on their characteristics, preferences, and behaviors, and provide personalized recommendations and offers .
  - Fraud detection and prevention: Data mining tools can help detect and prevent fraudulent transactions, claims, and activities by analyzing patterns and anomalies in data .
  - Market basket analysis: Data mining tools can help analyze the associations and co-occurrences of items purchased by customers, and generate rules for cross-selling and up-selling .
  - Text mining and sentiment analysis: Data mining tools can help extract and analyze information from textual data, such as documents, emails, reviews, and social media posts, and identify topics, keywords, sentiments, and opinions .
  - Predictive analytics and forecasting: Data mining tools can help build and evaluate predictive models based on historical and current data, and forecast future outcomes and trends  .
  - Time series analysis: Data mining tools can help analyze and model data that changes over time, such as sales, stock prices, and weather data, and identify patterns, cycles, and seasonality  .



# Medical and Legal Information Systems

- Medical information systems are systems that collect, store, process, and communicate health-related data for various purposes, such as diagnosis, treatment, research, and public health.
- Legal information systems are systems that collect, store, process, and communicate legal-related data for various purposes, such as litigation, compliance, regulation, and education.
- Both types of systems have some common characteristics, such as:
  - They deal with sensitive and confidential information that requires protection from unauthorized access, use, or disclosure.
  - They have to comply with various laws and regulations that govern the collection, storage, processing, and communication of information, such as the Health Insurance Portability and Accountability Act (HIPAA) and the Family Educational Rights and Privacy Act (FERPA) in the US.
  - They have to ensure the quality, accuracy, completeness, and timeliness of the information they provide, as it may have significant impacts on the outcomes of health or legal decisions.
  - They have to cope with the complexity, diversity, and dynamism of the information they handle, as it may come from various sources, formats, languages, and domains.
  - They have to support the needs and preferences of various users and stakeholders, such as patients, providers, lawyers, judges, regulators, researchers, and educators.
- Some examples of medical information systems are:
  - Electronic medical records (EMRs), which are digital versions of paper-based medical charts that contain information about a patient's medical history, diagnoses, treatments, medications, allergies, and other relevant data.
  - Electronic health records (EHRs), which are interoperable and integrated versions of EMRs that can be shared across different health care settings and organizations, and can include information from other sources, such as laboratory tests, imaging studies, and wearable devices.
  - Personal health records (PHRs), which are patient-controlled and patient-centered versions of EHRs that allow patients to access, manage, and share their own health information with their providers and others.
  - Health information exchanges (HIEs), which are networks or platforms that facilitate the secure and standardized exchange of health information among different health care entities, such as hospitals, clinics, pharmacies, and public health agencies.
  - Clinical decision support systems (CDSSs), which are systems that provide guidance, recommendations, or alerts to health care providers based on the analysis of patient data and evidence-based knowledge.
  - Telemedicine or telehealth systems, which are systems that enable the delivery of health care services remotely, using information and communication technologies, such as videoconferencing, mobile apps, and sensors.
- Some examples of legal information systems are:
  - Legal databases or repositories, which are systems that store and provide access to various types of legal information, such as statutes, regulations, case law, contracts, patents, and trademarks.
  - Legal search engines or portals, which are systems that allow users to search, browse, and retrieve relevant legal information from various sources, using natural language queries, keywords, or filters.
  - Legal analytics or intelligence systems, which are systems that use data mining, machine learning, or artificial intelligence techniques to extract, analyze, and visualize patterns, trends, or insights from large and complex legal data sets, such as court opinions, litigation records, or legal documents.
  - Legal document automation or generation systems, which are systems that use natural language processing, knowledge representation, or logic programming techniques to create, edit, or fill out legal documents, such as contracts, forms, or letters, based on predefined templates, rules, or user inputs.
  - Legal expert systems or chatbots, which are systems that use rule-based or case-based reasoning, natural language understanding, or natural language generation techniques to provide legal advice, guidance, or assistance to users, based on their questions, problems, or scenarios.



# Medical Information Systems

Medical information systems are computer-based systems that store, process, and communicate health-related data for various purposes, such as clinical care, research, education, and administration. Medical information systems can be classified into different types, such as:

- **Electronic medical records (EMRs)**: These are digital versions of the paper charts that contain the medical history, diagnoses, treatments, medications, and other information of a patient within a single health care provider's organization. EMRs can improve the quality, safety, and efficiency of patient care by facilitating access, sharing, and analysis of health data.
- **Electronic health records (EHRs)**: These are similar to EMRs, but they contain more comprehensive and longitudinal health information of a patient across multiple health care providers and settings. EHRs can enable interoperability, coordination, and integration of health care services among different providers and organizations.
- **Personal health records (PHRs)**: These are electronic tools that allow patients to access, manage, and share their own health information, such as medical history, medications, allergies, immunizations, test results, and preferences. PHRs can empower patients to participate in their own health care and improve communication and collaboration with their providers.
- **Medical informatics**: This is a sub-discipline of health informatics that applies computer science and information technology to improve health care and patient outcomes. Medical informatics involves the design, development, evaluation, and implementation of medical information systems, as well as the analysis and interpretation of health data for clinical decision support, knowledge discovery, and evidence-based practice.
- **Health information exchange (HIE)**: This is the process of electronically transmitting and receiving health information among different health care entities, such as providers, hospitals, laboratories, pharmacies, and public health agencies. HIE can facilitate the delivery of timely, accurate, and complete health information to support patient care, quality improvement, population health, and public health.
- **Telemedicine**: This is the use of information and communication technologies to provide health care services remotely, such as diagnosis, consultation, treatment, monitoring, and education. Telemedicine can improve access, quality, and cost-effectiveness of health care, especially for rural and underserved populations, as well as for chronic and emergency conditions.
- **Digital health**: This is the convergence of digital technologies with health, health care, and society, such as mobile health, wearable devices, artificial intelligence, big data, cloud computing, and blockchain. Digital health can transform health care delivery, research, and innovation, as well as empower patients and consumers to take control of their own health and wellness.

: https://onlinemasters.ohio.edu/blog/health-information-systems/

: https://www.usfhealthonline.com/resources/health-informatics/what-is-medical-informatics/

: https://www.sciencedirect.com/topics/medicine-and-dentistry/medical-information-systems

: https://www.fda.gov/medical-devices/digital-health-center-excellence/digital-health-reports

: https://www.scvmc.org/patients-visitors/services/requesting-medical-records



# Legal information systems

Legal information systems are systems that store, process, and retrieve legal information, such as legislation, case law, and scholarly works. Legal information systems are important for providing access to the law to laymen and legal professionals, as well as for supporting various tasks related to legal reasoning, argumentation, and decision making.

Some of the applications of legal information systems in intelligent database systems are:

- **Legal information retrieval**: This is the science of information retrieval applied to legal text, using techniques such as natural language processing, information extraction, text classification, and text summarization. Legal information retrieval systems aim to help users find relevant and reliable legal information from large and complex collections of legal documents. Examples of legal information retrieval systems are  :

  - **Search engines**: These are systems that allow users to enter queries and receive ranked lists of documents that match the queries. Search engines may use different ranking algorithms, such as keyword matching, vector space model, or probabilistic model, to measure the relevance of documents to queries. Search engines may also use different indexing methods, such as inverted index, suffix tree, or signature file, to store and access the documents efficiently. Search engines may also provide advanced features, such as query expansion, query reformulation, query suggestion, or query refinement, to help users formulate effective queries. Examples of search engines for legal information are Google Scholar, LexisNexis, and Westlaw.

  - **Question answering systems**: These are systems that allow users to enter natural language questions and receive direct answers, rather than lists of documents. Question answering systems may use different techniques, such as named entity recognition, relation extraction, semantic parsing, or inference, to analyze the questions and the documents, and to generate the answers. Question answering systems may also use different sources of knowledge, such as ontologies, databases, or knowledge graphs, to enrich the answers with additional information. Examples of question answering systems for legal information are IBM Watson, ROSS Intelligence, and LIA.

  - **Summarization systems**: These are systems that generate concise and coherent summaries of legal documents, such as cases, statutes, or contracts. Summarization systems may use different techniques, such as extraction, abstraction, or compression, to select and generate the most important information from the documents. Summarization systems may also use different strategies, such as generic, query-focused, or user-oriented, to tailor the summaries to different purposes and preferences. Examples of summarization systems for legal information are SummarizeBot, LegalSifter, and LexNLP.

- **Legal information management**: This is the process of organizing, storing, updating, and sharing legal information, such as litigation matters, court proceedings, or legal opinions. Legal information management systems aim to help users manage and monitor the legal data efficiently and effectively. Examples of legal information management systems are  :

  - **Database systems**: These are systems that store and manipulate legal data in structured and organized formats, such as tables, records, or fields. Database systems may use different models, such as relational, hierarchical, or network, to represent the data and the relationships among them. Database systems may also use different languages, such as SQL, XQuery, or SPARQL, to query and update the data. Examples of database systems for legal information are WorldLII, EUR-Lex, and CanLII.

  - **Document management systems**: These are systems that store and manipulate legal documents in unstructured or semi-structured formats, such as text, images, or audio. Document management systems may use different techniques, such as metadata, annotation, or indexing, to describe and categorize the documents. Document management systems may also use different features, such as version control, access control, or collaboration, to manage and share the documents. Examples of document management systems for legal information are Dropbox, Google Drive, and OneDrive.

  - **Workflow management systems**: These are systems that model and execute the business processes and tasks related to legal information, such as filing, reviewing, or approving. Workflow management systems may use different techniques, such as flowchart, Petri net, or state machine, to represent the workflow models. Workflow management systems may also use different features, such as automation, notification, or escalation, to execute and monitor the workflow instances. Examples of workflow management systems for legal information are Legal Information Management and Briefing System (LIMBS), LegalServer, and Clio.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some possible conclusions for the notes of the Unit 5 - Applications in IDBS in the subject of Intelligent Database System:

# Conclusions

- Intelligent database systems (IDBS) are systems that integrate database management systems (DBMS) with artificial intelligence (AI) techniques to provide enhanced functionality, such as reasoning, learning, natural language processing, and knowledge representation.
- IDBS can be classified into three categories based on the degree of integration between DBMS and AI: loosely coupled, tightly coupled, and fully integrated. Each category has its own advantages and disadvantages in terms of performance, flexibility, and compatibility.
- IDBS can be applied to various domains, such as expert systems, decision support systems, data mining, information retrieval, multimedia databases, and spatial databases. Each domain has its own requirements and challenges for IDBS, such as knowledge representation, inference mechanisms, query processing, and user interfaces.
- IDBS can benefit from the use of ontologies, which are formal and explicit specifications of the concepts and relationships in a domain. Ontologies can provide a common vocabulary and a semantic framework for IDBS, enabling interoperability, consistency, and reuse of knowledge.
- IDBS can also benefit from the use of machine learning, which is the ability of a system to learn from data and improve its performance. Machine learning can help IDBS to discover patterns, rules, and associations from large and complex data sets, as well as to adapt to changing environments and user preferences.

