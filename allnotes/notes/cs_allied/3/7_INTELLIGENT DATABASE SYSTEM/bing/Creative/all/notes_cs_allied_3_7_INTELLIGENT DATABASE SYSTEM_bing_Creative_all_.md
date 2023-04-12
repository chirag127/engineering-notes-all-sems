

# INTELLIGENT DATABASE SYSTEM

- An intelligent database system is a system that manages information, rather than simple data, and presents it in such a way that is natural and informative for users .
- An intelligent database system has three levels of intelligence: high level tools, the user interface and the database engine.
- High level tools manage data quality and automatically discover relevant patterns in the data with a process called data mining.
- The user interface provides natural language processing, speech recognition, graphical visualization and multimedia capabilities to facilitate user interaction .
- The database engine supports advanced data models, such as object-oriented, semantic and deductive, and provides efficient query processing and optimization .
- An intelligent database system can also integrate with artificial intelligence components, such as expert systems, neural networks and fuzzy logic, to enhance its functionality and performance .
- An intelligent database system can provide benefits such as improved data quality, reduced data redundancy, increased user satisfaction, enhanced decision making and reduced costs .



## Unit 1 - Introduction to IDBS

- IDBS stands for Integrated Database Systems, which is a course that covers the concepts and techniques of designing, implementing, and managing database systems.
- A database is a collection of related data that can be stored, manipulated, and retrieved by various applications.
- A database system is a software system that manages the database and provides services such as data definition, data manipulation, data integrity, data security, data backup, and data recovery.
- A database system consists of three components: the data, the database management system (DBMS), and the database applications.
- The data is the actual information stored in the database, such as tables, records, fields, and values.
- The DBMS is the software that controls the access and manipulation of the data, such as MySQL, Oracle, or MongoDB.
- The database applications are the programs that interact with the database, such as web applications, mobile applications, or desktop applications.
- A database system can be classified into different types based on the data model, the data structure, the data distribution, and the data processing.
- The data model is the logical representation of the data and the relationships among them, such as relational, hierarchical, network, object-oriented, or document.
- The data structure is the physical organization of the data on the storage devices, such as sequential, indexed, hashed, or clustered.
- The data distribution is the way the data is distributed across multiple locations, such as centralized, decentralized, or distributed.
- The data processing is the way the data is processed by the database system, such as online, batch, or real-time.
- The objectives of this course are to:
  - Understand the basic concepts and principles of database systems.
  - Learn the skills and techniques of database design, implementation, and management.
  - Apply the knowledge and skills to develop database applications using various tools and platforms.
  - Evaluate the performance and quality of database systems and applications.
  - Appreciate the current trends and challenges of database systems and applications.



# Informal definition of the domain for the notes of the Unit 1 - Introduction to IDBS in the subject of INTELLIGENT DATABASE SYSTEM

- An **intelligent database system (IDBS)** is a database system that integrates artificial intelligence techniques, such as machine learning, natural language processing, knowledge representation and reasoning, with traditional database management systems.
- The **domain** of an IDBS is the set of possible values that can be stored in the database, as well as the constraints and relationships among them.
- The domain of an IDBS can be defined informally by describing the following aspects:
  - The **entities** that are relevant to the application domain, such as customers, products, orders, etc.
  - The **attributes** that describe the properties or characteristics of each entity, such as name, price, quantity, etc.
  - The **data types** that specify the format and range of values for each attribute, such as integer, string, date, etc.
  - The **primary keys** that uniquely identify each entity instance, such as customer ID, product ID, order ID, etc.
  - The **foreign keys** that establish the references or links between different entities, such as customer ID in the order entity, product ID in the order detail entity, etc.
  - The **constraints** that enforce the rules or conditions that must be satisfied by the data, such as not null, unique, check, etc.
  - The **relationships** that express the associations or interactions among the entities, such as one-to-one, one-to-many, many-to-many, etc.
  - The **functions** that define the operations or calculations that can be performed on the data, such as sum, average, count, etc.
  - The **rules** that specify the logic or inference that can be applied to the data, such as if-then, case, trigger, etc.
  - The **queries** that allow the users to retrieve or manipulate the data, such as select, insert, update, delete, etc.



# General characteristics of IDBSs

- IDBS stands for Intelligent Database System, which is a database system that incorporates artificial intelligence techniques to provide more functionality and flexibility than conventional database systems.
- IDBSs can perform tasks such as data analysis, data mining, knowledge discovery, natural language processing, reasoning, learning, and adaptation.
- IDBSs can handle complex and uncertain data, such as multimedia, spatial, temporal, and fuzzy data.
- IDBSs can support multiple data models, such as relational, object-oriented, semantic, and deductive.
- IDBSs can interact with users in natural language, and provide explanations and justifications for their actions and results.
- IDBSs can cooperate with other database systems and information sources, and integrate heterogeneous and distributed data.
- IDBSs can evolve and improve their performance and behavior over time, by learning from their own experience and feedback from users.
- IDBSs can be applied to various domains, such as decision support, expert systems, knowledge management, information retrieval, and intelligent agents.



# Data models and the relational data model

## Data models

- A data model is a **conceptual representation** of the data, the relationships between data, and the rules and constraints on the data in an information system.
- A data model helps to **design**, **implement**, **manage**, and **use** databases effectively and efficiently.
- A data model can be represented using different **notations** and **techniques**, such as entity-relationship diagrams, UML class diagrams, relational schemas, etc.
- A data model can be classified into three levels: **conceptual**, **logical**, and **physical**.
  - A conceptual data model is a high-level, abstract, and independent view of the data that captures the essential entities, attributes, and relationships without considering any implementation details.
  - A logical data model is a more detailed and structured view of the data that maps the conceptual data model to a specific data model, such as relational, hierarchical, network, etc.
  - A physical data model is a low-level, concrete, and dependent view of the data that specifies how the data will be stored, accessed, and manipulated in a physical database.

## Relational data model

- The relational data model is the most widely used data model for database systems  .
- The relational data model is based on the **mathematical concept** of a relation, which is a set of tuples (or rows) that have the same attributes (or columns)  .
- The relational data model represents data as a collection of **tables** (or relations), where each table has a unique name and a set of attributes  .
- The attributes of a table are also called **columns** or **fields**, and the tuples of a table are also called **rows** or **records**  .
- Each attribute of a table has a **domain**, which is the set of possible values that the attribute can take  .
- Each tuple of a table has a **primary key**, which is a set of one or more attributes that uniquely identifies the tuple within the table  .
- The tables of a relational data model can have **relationships** with each other, which are established by using **foreign keys**, which are attributes that refer to the primary keys of other tables  .
- The relational data model supports various **operations** on the data, such as data definition, data manipulation, data integrity, data security, and data query  .
- The relational data model uses a **query language**, such as SQL, to perform operations on the data  .
- The relational data model has many **advantages**, such as simplicity, flexibility, scalability, consistency, and independence  .
- The relational data model also has some **disadvantages**, such as complexity, redundancy, performance, and security  .

## Example of a relational data model

- Consider a relational data model for a university information system, which consists of the following tables:

| Student | (SID, Name, Major, GPA) |
| --- | --- |
| Course | (CID, Title, Credits, Instructor) |
| Enrollment | (SID, CID, Semester, Grade) |

- The primary keys of the tables are underlined, and the foreign keys are italicized.
- The tables have the following relationships:

  - A student can enroll in many courses, and a course can have many students enrolled. This is a **many-to-many** relationship, which is represented by the Enrollment table.
  - A course can have only one instructor, and an instructor can teach many courses. This is a **one-to-many** relationship, which is represented by the Instructor attribute in the Course table.

- The tables can be queried using SQL, for example:

  - To find the names and majors of all students who have enrolled in CS101 in Spring 2023, we can use the following SQL query:

  ```sql
  SELECT Student.Name

```




# A taxonomy of intelligent database systems

Intelligent database systems (IDBSs) are systems that combine the capabilities of database management systems (DBMSs) and artificial intelligence (AI) techniques to provide more effective and efficient data management and analysis. IDBSs can interact with users, understand their information needs, and discover relevant patterns and insights from the data.

There are different ways to classify IDBSs based on their origin, architecture, functionality, and application domain. One possible taxonomy of IDBSs is as follows :

- **Efforts originated in a DB context**: These are IDBSs that extend the traditional DBMSs with some AI features, such as:

  - **Static extensions**: These are IDBSs that enhance the expressive power of traditional DB data models, such as object-oriented, semantic, and deductive databases. These systems allow more complex and rich data structures and queries, as well as some form of inference and reasoning over the data.

  - **Dynamic extensions**: These are IDBSs that introduce some form of reasoning inside the DBMS, such as rule-based, logic-based, or constraint-based systems. These systems can perform tasks such as data validation, integrity checking, query optimization, and view maintenance.

- **Efforts originated in an AI context**: These are IDBSs that integrate knowledge-based systems (KBSs) and DBMSs, such as:

  - **Basic solutions**: These are IDBSs that couple KBSs and DBMSs using some interface or middleware, such as expert systems shells, knowledge representation languages, or query languages. These systems can access and manipulate data stored in DBMSs, as well as use the knowledge and inference capabilities of KBSs.

  - **Advanced solutions**: These are IDBSs that embed KBSs and DBMSs in a unified framework, such as active, adaptive, or learning databases. These systems can perform tasks such as data mining, knowledge discovery, data analysis, and data-driven decision making.

- **Efforts originated in a hybrid context**: These are IDBSs that combine the features of both DB and AI approaches, such as:

  - **Intelligent data models**: These are IDBSs that use a common data model that incorporates both data and knowledge, such as ontologies, conceptual graphs, or frames. These systems can support semantic interoperability, data integration, and knowledge sharing.

  - **Intelligent data management**: These are IDBSs that use a common data management system that incorporates both DBMS and KBS functionalities, such as intelligent query processing, intelligent transaction processing, or intelligent data warehousing. These systems can support complex and flexible data manipulation and analysis.

  - **Intelligent data applications**: These are IDBSs that use a common data application system that incorporates both DB and AI techniques, such as intelligent information systems, intelligent decision support systems, or intelligent web systems. These systems can support various data-intensive and knowledge-intensive tasks and domains.



# Guidelines for using intelligent database systems

Intelligent database systems (IDBS) are systems that manage information, rather than simple data, and present it in such a way that is natural and informative for users. IDBS have the capacity to go beyond simple record keeping and provide intelligent functionalities such as natural language processing, knowledge representation, reasoning, learning, and decision support. IDBS can also access multiple database management systems (DBMSs), both local and remote, and offer flexible options for conducting queries.

Some of the guidelines for using IDBS are:

- Identify the information needs and goals of the users and the organization, and select an appropriate IDBS that can meet those needs and goals.
- Design and implement a suitable information model and schema for the IDBS, taking into account the semantics, structure, and relationships of the information, as well as the possible queries and operations that the users may perform on the information.
- Populate the IDBS with relevant and reliable information from various sources, such as existing databases, documents, web pages, sensors, etc., and ensure the quality, consistency, and completeness of the information.
- Provide user-friendly and natural interfaces for the IDBS, such as natural language, graphical, or voice interfaces, that can facilitate the communication and interaction between the users and the IDBS.
- Enable the IDBS to perform intelligent functions, such as information retrieval, information extraction, information integration, information analysis, information synthesis, information presentation, information recommendation, etc., using techniques from artificial intelligence, machine learning, data mining, etc.
- Monitor and evaluate the performance and effectiveness of the IDBS, and update and improve the IDBS as needed, based on the feedback and preferences of the users and the organization.



## Unit 2 - Semantic Data Models

- Semantic data models are conceptual data models that capture the meaning and relationships of data in a domain of interest.
- Semantic data models use high-level abstractions such as entities, attributes, and relationships to represent data and their semantics.
- Semantic data models can be used to design databases, ontologies, knowledge bases, and other information systems that require a rich and expressive representation of data.
- Semantic data models can also be used to facilitate data integration, interoperability, and reasoning across heterogeneous data sources and applications.
- Some examples of semantic data models are:
  - Entity-relationship model: A semantic data model that represents data as entities (things or objects) and relationships (associations or connections) between them. Entities have attributes (properties or characteristics) that describe them. Relationships have cardinalities (constraints or rules) that specify how many entities can participate in them.
  - Semantic network: A semantic data model that represents data as nodes (concepts or instances) and links (relations or predicates) between them. Nodes have types (categories or classes) that define their properties and behavior. Links have roles (arguments or parameters) that indicate the function or meaning of the nodes they connect.
  - Ontology: A semantic data model that represents data as classes (sets or collections) and properties (features or aspects) of those classes. Classes have subclasses (subsets or specializations) that inherit their properties. Properties have domains (sources or subjects) and ranges (targets or objects) that specify the classes they apply to. Ontologies also define axioms (rules or constraints) that govern the logical consistency and inference of the data.



# Nested and Semantic Data Models

## Nested Data Models

- A nested data model is a data model that allows data to be stored in a hierarchical structure, where some attributes can contain other attributes or collections of attributes as sub-elements.
- Nested data models are useful for representing complex data that have natural hierarchies or relationships, such as documents, graphs, or trees.
- Nested data models can avoid the need for joining multiple tables or flattening data into a single table, which can improve performance and simplify queries.
- Nested data models can be implemented using various data types, such as JSON, XML, key-value pairs, arrays, or map fields.
- Nested data models can be accessed and manipulated using specialized query languages or functions, such as SQL/JSON, XQuery, or dot notation.
- Nested data models have some challenges, such as handling updates, enforcing constraints, or supporting aggregation and analysis.

## Semantic Data Models

- A semantic data model is a data model that captures the meaning and context of the data, rather than just the structure and format.
- Semantic data models are useful for representing data that have rich semantics, such as concepts, entities, relationships, rules, or constraints.
- Semantic data models can enable more expressive and flexible queries, as well as reasoning and inference over the data, which can enhance the functionality and usability of the data.
- Semantic data models can be implemented using various formalisms, such as ontologies, graphs, or frames.
- Semantic data models can be accessed and manipulated using specialized query languages or tools, such as SPARQL, RDF, or OWL.
- Semantic data models have some challenges, such as scalability, interoperability, or consistency.



Hello, I am Sydney, your AI assistant. I can help you with writing notes on various topics. Here is the content I have generated for the introduction of the notes of the Unit 2 - Semantic Data Models in the subject of Intelligent Database System.

# Introduction

- Semantic data models are high-level conceptual models that capture the meaning and structure of data in a domain of interest.
- Semantic data models use concepts such as entities, attributes, relationships, and constraints to represent data and their semantics.
- Semantic data models are more expressive and intuitive than traditional data models, such as relational or hierarchical models, which focus on the physical representation and storage of data.
- Semantic data models can be used for various purposes, such as database design, data integration, data analysis, and knowledge representation.
- Semantic data models can be classified into two main categories: object-based and logic-based models.
- Object-based models use objects as the basic units of data abstraction. Objects have identity, properties, and behavior. Objects can be organized into classes, hierarchies, and networks. Examples of object-based models are Entity-Relationship (ER) model, Object-Oriented (OO) model, and Semantic Network (SN) model.
- Logic-based models use logic as the foundation for data representation and manipulation. Logic-based models use predicates, variables, constants, and quantifiers to express facts, rules, and queries about data. Examples of logic-based models are Functional Data Model (FDM), Deductive Database (DDB), and Semantic Web (SW) model.



# The nested relational model

The nested relational model is an extension of the relational model in which domains may be either atomic or relation-valued. This allows a complex object to be represented by a single tuple of a nested relation -- one-to-one correspondence between data items and objects.

Some features of the nested relational model are:

- It supports nested relations, which are relations that have attributes of type relation. This enables the representation of complex objects and relationships in a single relation.
- It allows non-first normal form (NFNF) relations, which are relations that have attributes with non-atomic domains. This enables the representation of multi-valued and composite attributes.
- It provides operators for manipulating nested relations, such as unnest, nest, and join. These operators can be used to flatten, group, or combine nested relations.
- It preserves the advantages of the relational model, such as declarative query language, data independence, and integrity constraints.

An example of a nested relation is:

| Student | Courses |
| ------- | ------- |
| Alice   | { (CS101, A), (CS102, B) } |
| Bob     | { (CS101, C), (CS103, A) } |
| Carol   | { (CS102, A), (CS103, B) } |

In this relation, the attribute Courses is a relation-valued attribute, which contains the course code and grade of each student. This relation is in NFNF, since the domain of Courses is not atomic. To convert this relation to first normal form (1NF), we would need to create a separate relation for Courses and use a foreign key to link it to Student. However, this would lose the information about the grouping of courses for each student. The nested relation model allows us to keep this information in a single relation.



# Semantic models for the notes of the Unit 2 - Semantic Data Models in the subject of INTELLIGENT DATABASE SYSTEM

- A semantic data model is a high-level, conceptual data model that includes semantic information that adds meaning to the data and the relationships between them .
- A semantic data model is designed to capture more of the meaning of an application environment than is possible with contemporary database models.
- A semantic data model is an abstraction that defines how the stored symbols (the instance data) relate to the real world.
- A semantic data model can express and exchange information that enables interoperability, integration, and reasoning.
- A semantic data model can be used to represent the structure and behavior of a system, as well as the constraints and rules that govern it.
- A semantic data model can be implemented using various techniques, such as entity-relationship models, object-oriented models, ontologies, and graphs  .
- A semantic data model can provide benefits such as improved data quality, consistency, and reuse; enhanced query and analysis capabilities; and reduced complexity and redundancy.

Some examples of semantic data models are:

- The Entity-Relationship Model: This model represents data as entities (things or objects) and relationships (associations or links) between them. Entities have attributes (properties or characteristics) and relationships have cardinalities (constraints on the number of occurrences). The model can be represented graphically using an entity-relationship diagram (ERD).
- The Object-Oriented Model: This model represents data as objects (instances of classes) and methods (operations or functions) that define their behavior. Objects have attributes (data fields or variables) and methods (procedures or subroutines) that can be inherited or overridden by subclasses. The model can be represented graphically using a class diagram or an object diagram.
- The Ontology Model: This model represents data as concepts (classes or categories) and relations (properties or predicates) that define their meaning and structure. Concepts have attributes (data values or literals) and relations have domains (sets of possible values) and ranges (sets of possible values). The model can be represented using a formal language, such as the Web Ontology Language (OWL) or the Resource Description Framework (RDF).
- The Graph Model: This model represents data as nodes (vertices or points) and edges (arcs or lines) that connect them. Nodes have labels (names or identifiers) and edges have weights (values or measures) and directions (orientations or flows). The model can be represented using a mathematical notation, such as a matrix or a list, or a graphical notation, such as a network diagram or a tree diagram.



# Hyper-semantic data models

- Hyper-semantic data models are a new class of models that combine the features of semantic data models and artificial intelligence concepts .
- Semantic data models are high-level models that capture the meaning and structure of an application environment using object-oriented concepts such as entities, attributes, relationships, and constraints.
- Artificial intelligence concepts include heuristics, uncertainty, rules, inference, and learning, which can enhance the expressiveness and functionality of data models .
- Hyper-semantic data models can be used to represent complex and dynamic domains that require knowledge-based reasoning and decision making .
- An example of a hyper-semantic data model is the Knowledge/Data Model (KDM), which extends the Entity-Relationship Model (ERM) with additional constructs such as fuzzy sets, probabilistic sets, rules, and triggers  .
- Hyper-semantic data models can provide the following benefits:
  - Data resource planning: They can help in the initial stages of project planning to identify the necessary data resources and their interrelationships.
  - Data integration: They can facilitate the integration of data from multiple sources and formats by providing a common semantic framework.
  - Data analysis: They can support various types of data analysis such as querying, reporting, visualization, and mining by incorporating domain knowledge and logic.
  - Data quality: They can improve the quality and consistency of data by enforcing constraints and rules and by handling uncertainty and incompleteness.



# Object-oriented approaches to semantic data modeling

- Semantic data modeling is a high-level database description and structuring formalism that captures more of the meaning of an application environment than conventional database models.
- Object-oriented modeling is a technique that uses objects as the basic units of data representation and manipulation, where an object is a combination of data and behavior.
- Object-oriented approaches to semantic data modeling aim to decrease the semantic gap between the system and the real world by using terminology that is consistent with the functions that users perform.
- Object-oriented approaches to semantic data modeling also support data abstraction, inheritance, and encapsulation, which are essential features for modeling complex and dynamic domains.
- Some examples of object-oriented approaches to semantic data modeling are:
  - The Feature Evolution Model (FEM), which represents spatiotemporal geographic data as objects that have states and events, and uses subtyping to handle temporal complexity.
  - The Meaning-oriented Semantic Data Model (MSDM), which represents semantic information as graphs that capture the meanings of entities and relationships, and uses graph operations to manipulate semantic data.
  - The Object-Oriented Data Model (OODM), which extends the Entity-Relationship Model (ERM) with object-oriented concepts such as classes, attributes, methods, and inheritance, and uses object identifiers to reference objects.



# Object-oriented database systems

- An object-oriented database (OOD) is a database system that can work with complex data objects — that is, objects that mirror those used in object-oriented programming languages .
- In object-oriented programming (OOP), everything is an object. An object has a unique identity, a state, and a behavior. An object can also have attributes (properties) and methods (functions) that define its characteristics and operations.
- An object-oriented database system (OODS) is a database management system (DBMS) that supports the modelling and creation of data as objects. An OODS allows users to define, store, manipulate, and query objects in a database .
- An OODS has several advantages over a traditional relational database system (RDBS), such as:
  - It can handle complex and heterogeneous data types, such as multimedia, spatial, temporal, and semantic data.
  - It can preserve the integrity and consistency of data by enforcing encapsulation, inheritance, and polymorphism.
  - It can improve the performance and scalability of applications by reducing the impedance mismatch between the data model and the programming language .
- An OODS also has some challenges and limitations, such as:
  - It may not be compatible with existing standards and tools for data management, such as SQL and ODBC.
  - It may not support some features of relational databases, such as transactions, concurrency control, and indexing.
  - It may require more storage space and processing power than a relational database.
- There are different types of object-oriented database systems, such as:
  - Pure object-oriented database systems, which store only objects and do not support any relational features.
  - Object-relational database systems, which are extensions of relational databases that support some object-oriented features, such as user-defined types and methods.
  - Object-oriented database management systems, which are hybrid systems that combine the features of both object-oriented and relational databases.



# Basic concepts of a core object-oriented data model

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



# Comparison with other data models

Semantic data models (SDMs) are a way of structuring data to represent it in a logical way, with more focus on the meaning of the data itself, rather than solely or primarily on the relationships and attributes of the data. SDMs can be contrasted with other data models, such as relational, hierarchical, network, object-oriented, and entity-relationship models, in terms of how they are built, how they represent data, and what benefits and limitations they have. Here are some points of comparison:

- **How they are built**: The relational data model is built using relationships between tables, columns, and rows in the database. The hierarchical data model is built using parent-child relationships between records, forming a tree-like structure. The network data model is built using pointers that link records in a graph-like structure. The object-oriented data model is built using objects that encapsulate data and methods, and support inheritance and polymorphism. The entity-relationship data model is built using entities, attributes, and relationships, and can be represented graphically using diagrams. The semantic data model is built using concepts, properties, and rules, and can be represented graphically using semantic networks or frames.

- **How they represent data**: The relational data model represents data as a collection of relations, each consisting of a set of tuples with values for each attribute. The hierarchical data model represents data as a collection of records, each consisting of a set of fields with values, and a set of pointers to child records. The network data model represents data as a collection of records, each consisting of a set of fields with values, and a set of pointers to related records. The object-oriented data model represents data as a collection of objects, each consisting of a set of attributes with values, and a set of methods that define the behavior of the object. The entity-relationship data model represents data as a collection of entities, each consisting of a set of attributes with values, and a set of relationships that link the entities. The semantic data model represents data as a collection of concepts, each consisting of a set of properties with values, and a set of rules that define the meaning and constraints of the concept.

- **What benefits and limitations they have**: The relational data model has the benefits of being simple, flexible, and widely supported by database management systems, but it has the limitations of being rigid, inefficient, and lacking in semantic expressiveness . The hierarchical data model has the benefits of being fast, efficient, and natural for hierarchical data, but it has the limitations of being inflexible, redundant, and difficult to query. The network data model has the benefits of being flexible, efficient, and natural for network data, but it has the limitations of being complex, redundant, and difficult to query. The object-oriented data model has the benefits of being expressive, reusable, and natural for complex data, but it has the limitations of being complex, inefficient, and not well supported by database management systems. The entity-relationship data model has the benefits of being simple, intuitive, and graphical, but it has the limitations of being ambiguous, incomplete, and not directly implementable. The semantic data model has the benefits of being expressive, meaningful, and inferential, but it has the limitations of being complex, abstract, and not well supported by database management systems .



# Query languages and query processing for semantic data models

- A query language is a formal language that allows users to retrieve and manipulate data from a database or a data source.
- A query processing is the process of translating a query from a high-level language to a low-level language that can be executed by the database system, and optimizing the execution plan to minimize the cost and time of the query.
- A semantic data model is a data model that captures the meaning and relationships of the data, rather than the structure and format of the data. Semantic data models are often based on graphs, linked data, or triples, which enable the query to process the actual relationships between information and infer the answers from the network of data.
- Some examples of semantic data models are:
  - RDF (Resource Description Framework): a standard model for data interchange on the Web, based on triples of subject, predicate, and object, which represent resources and their properties and relations.
  - OWL (Web Ontology Language): a family of knowledge representation languages for authoring ontologies, which are formal descriptions of the concepts and relationships in a domain of interest.
  - ER (Entity-Relationship): a conceptual data model that represents the entities and their attributes and relationships in a domain of interest.
- Some examples of query languages for semantic data models are:
  - SPARQL: a standard query language for RDF data, which allows users to query and manipulate RDF graphs using graph patterns, filters, and optional and negated clauses.
  - Cypher: a declarative query language for property graphs, which are graphs that have nodes and relationships with properties and labels. Cypher allows users to query and manipulate property graphs using patterns, filters, and projections.
  - Datalog: a logic programming language that allows users to query and manipulate data using rules, facts, and queries, which are expressed as logical formulas. Datalog can be used to query and manipulate any data model that can be represented as a set of facts.
- Query processing for semantic data models involves the following steps:
  - Parsing: the process of checking the syntax and semantics of the query, and converting it into an internal representation, such as a parse tree or an abstract syntax tree.
  - Optimization: the process of finding the best execution plan for the query, which minimizes the cost and time of the query. Optimization may involve rewriting the query, applying heuristics, estimating the cost and size of intermediate results, and choosing the best join methods and access paths.
  - Execution: the process of executing the query plan, which may involve accessing the data sources, applying filters and operations, joining and aggregating the results, and returning the final answer to the user.



# Operational aspects of semantic data models

Semantic data models (SDMs) are high-level conceptual models that describe the meaning and structure of data in a domain. They use concepts such as objects, classes, attributes, relationships, and constraints to represent the data and its semantics. SDMs can be used for various purposes, such as database design, data integration, data analysis, and data visualization.

Some of the operational aspects of SDMs are:

- **Classification**: This is the process of grouping objects in a domain by their common characteristics or properties. For example, a class of employees can be defined by their attributes such as name, salary, department, etc. Classification can use the "instance of" relation to indicate that an object belongs to a class. For example, Alice is an instance of the employee class.
- **Aggregation**: This is the process of defining a new object from a set of objects that become its components. For example, a project can be defined by aggregating a set of tasks, resources, and milestones. Aggregation can use the "has a" relation to indicate that an object is composed of other objects. For example, a project has a name, a budget, and a deadline.
- **Generalization**: This is the process of defining a new class from a set of existing classes that share some common characteristics or properties. For example, a person can be defined as a generalization of the classes employee, customer, and student. Generalization can use the "is a" relation to indicate that a class is a subclass of another class. For example, an employee is a person.
- **Specialization**: This is the process of defining a new class from an existing class by adding some specific characteristics or properties. For example, a manager can be defined as a specialization of the employee class by adding the attribute of managing a team. Specialization can also use the "is a" relation to indicate that a class is a subclass of another class. For example, a manager is an employee.
- **Association**: This is the process of defining a relationship between two or more classes or objects. For example, an employee can be associated with a project by working on it. Association can use various types of relations, such as "works on", "participates in", "reports to", etc. Association can also have attributes, such as duration, role, frequency, etc. For example, an employee works on a project for six months as a developer.
- **Constraint**: This is the process of defining a rule or a condition that restricts the values or the structure of the data. For example, a constraint can specify that an employee's salary cannot be negative, or that a project cannot have more than 10 tasks. Constraints can be applied to classes, attributes, relationships, or instances. For example, a constraint can state that every employee must have a unique employee ID.



# Systems for the notes of the Unit 2 - Semantic Data Models in the subject of INTELLIGENT DATABASE SYSTEM

- A semantic data model (SDM) is a high-level semantics-based database description and structuring formalism (database model) for databases.
- This database model is designed to capture more of the meaning of an application environment than is possible with contemporary database models.
- A semantic data model is a conceptual data model that includes semantic information that adds a basic meaning to the data and the relationships that lie between them.
- A semantic data model describes the meaning of its instances, such as entities, attributes, and relationships, using natural language or formal logic.
- A semantic data model can also include the capability to express and exchange information that enables reasoning, inference, and validation.
- A semantic data model can be represented using various notations, such as entity-relationship diagrams, object-role modeling, or semantic networks .
- A semantic data model can be used for various purposes, such as database design, data integration, data analysis, data visualization, and data governance.
- A semantic data model can provide benefits such as improved data quality, consistency, interoperability, and reusability.
- A semantic data model can also facilitate natural language processing, knowledge representation, and artificial intelligence applications .

: Semantic data model - Wikipedia
: What is the Semantic Data Model? - Definition from Techopedia



# The ODMG Standard for Semantic Data Models

- Semantic data models are high-level database models that capture the meaning and relationships of the data in an application domain.
- The Object Data Management Group (ODMG) was a consortium of object database vendors that developed a standard for object databases, including a semantic data model, an object definition language (ODL), and an object query language (OQL).
- The ODMG object model is based on the concepts of objects, literals, types, interfaces, collections, relationships, and inheritance.
- Objects are instances of types or interfaces that have a unique identity, a set of attributes, and a set of methods.
- Literals are values that do not have an identity, such as numbers, strings, booleans, dates, etc.
- Types define the structure and behavior of a set of objects, specifying their attributes and methods.
- Interfaces define the behavior of a set of objects, specifying their methods, but not their attributes.
- Collections are objects that contain other objects, such as sets, lists, bags, and arrays.
- Relationships are associations between objects that have a name, a degree, and a cardinality.
- Inheritance is a mechanism that allows a type or an interface to inherit the attributes and methods of another type or interface.
- The ODMG object model supports multiple inheritance, polymorphism, encapsulation, and persistence.
- The ODMG object definition language (ODL) is a textual language that allows the specification of the schema of an object database, using the concepts of the ODMG object model.
- The ODMG object query language (OQL) is a declarative language that allows the manipulation and retrieval of data from an object database, using the concepts of the ODMG object model.
- The ODMG standard also defines bindings for various programming languages, such as C++, Java, and Smalltalk, to allow the integration of object databases with application development.



# The object-relational data model

- The object-relational data model is a hybrid of the object-oriented and the relational data models, which combines the features of both paradigms.
- The object-relational data model supports objects, classes, inheritance, methods, and polymorphism, as well as data types, tables, keys, constraints, and queries of the relational model.
- The object-relational data model allows the definition of complex data types and user-defined functions, which can be used to store and manipulate complex data, such as multimedia, spatial, temporal, and XML data.
- The object-relational data model also supports inheritance of objects and tables, which means that new objects and tables can be derived from existing ones and inherit their attributes and methods.
- The object-relational data model can be implemented by using object-relational database management systems (ORDBMS), which are extensions of relational database management systems (RDBMS) that support object-relational features.
- The object-relational data model can be accessed by using object-relational mapping (ORM) tools, which are software libraries that provide a bridge between the object-oriented programming language and the object-relational database. ORM tools can automatically generate SQL queries and map the results to objects in the programming language.



# Java and Databases for Semantic Data Models

Semantic data models are high-level database models that capture the meaning and relationships of data in an application domain. Semantic data models can be used to design and implement databases that are more expressive, flexible, and interoperable than traditional relational or hierarchical models. Semantic data models can also facilitate data analysis and integration by providing a common vocabulary and logic for data.

Some of the topics that are relevant for Java and databases for semantic data models are:

- **Semantic data model concepts and components**: A semantic data model consists of three main components: data elements or objects, relationships, and constraints. Data elements or objects are the basic units of information that have properties and values. Relationships are the associations or links between data elements or objects that express their semantic meaning. Constraints are the rules or conditions that define the validity and integrity of the data model.  

- **Semantic data model languages and tools**: A semantic data model can be represented and manipulated using various languages and tools, such as graphical notations, formal languages, query languages, and software tools. Graphical notations, such as Entity-Relationship diagrams or Unified Modeling Language diagrams, can be used to visualize and document the data model. Formal languages, such as Semantic Web languages (e.g., RDF, OWL, SPARQL), can be used to define and reason about the data model. Query languages, such as SQL or SPARQL, can be used to access and manipulate the data stored in the data model. Software tools, such as database management systems, semantic web frameworks, or ontology editors, can be used to create, store, and manage the data model.  

- **Java and semantic data model integration**: Java is a popular programming language that can be used to develop applications that use semantic data models. Java provides various features and libraries that support semantic data model integration, such as:

  - Java Database Connectivity (JDBC): JDBC is an API that allows Java applications to connect to various types of databases, including relational, object-oriented, and semantic databases. JDBC provides a uniform interface for executing SQL statements, retrieving query results, and handling database errors. JDBC can also be used to access semantic web data sources, such as RDF stores or SPARQL endpoints, using specialized drivers or wrappers. 

  - Java Persistence API (JPA): JPA is an API that allows Java applications to map Java objects to database tables, and vice versa. JPA provides an object-relational mapping (ORM) framework that simplifies the development of data access layers for relational databases. JPA can also be used to map Java objects to semantic data models, such as RDF graphs or OWL ontologies, using specialized implementations or extensions. 

  - Java Semantic Web Frameworks: Java semantic web frameworks are software libraries that provide various functionalities for working with semantic data models, such as parsing, querying, reasoning, validating, and transforming semantic web data. Some examples of Java semantic web frameworks are Apache Jena, Sesame, OWL API, and Pellet. 

- **Semantic database concepts and applications**: A semantic database is a database that uses a semantic data model to store and manage data. Semantic databases can offer several advantages over traditional databases, such as:

  - Higher expressivity and flexibility: Semantic databases can represent complex and heterogeneous data that may not fit well in rigid and predefined schemas of relational or hierarchical databases. Semantic databases can also support dynamic and evolving data models that can accommodate changes in the application domain.  

  - Better interoperability and integration: Semantic databases can facilitate data sharing and exchange across different applications and systems by using common vocabularies and standards, such as RDF and OWL. Semantic databases can also enable data integration and analysis by using semantic web technologies, such as SPARQL and inference engines, to query and reason over distributed and heterogeneous data sources.  

  - Improved performance and scalability: Semantic databases can improve the performance and scalability of data access and manipulation by using techniques such as caching, indexing, partitioning, and parallel processing. Semantic databases can also leverage the distributed and cloud-based architectures of semantic web data sources, such as RDF stores or SPARQL endpoints, to handle large and complex data sets. 

Semantic databases can be used for various applications and domains, such as:

  - Knowledge management and discovery: Semantic databases can be used to store and manage knowledge bases and ontologies that capture the concepts and relationships of a domain



# Conclusions for the notes of the Unit 2 - Semantic Data Models in the subject of INTELLIGENT DATABASE SYSTEM

- Semantic data models are conceptual data models that capture the meaning and relationships of data in a domain of interest.
- Semantic data models use high-level constructs such as entities, attributes, relationships, constraints, and rules to represent data and its semantics.
- Semantic data models can be classified into three categories: entity-relationship models, functional models, and logic-based models.
- Entity-relationship models are based on the notion of entities and relationships among them. Entities are objects or concepts that can be identified and distinguished in the domain. Relationships are associations or links between entities that express some semantic meaning or dependency. Attributes are properties or characteristics of entities or relationships that describe or qualify them. Constraints are restrictions or conditions that apply to entities, attributes, or relationships. Rules are statements that define or derive some facts or behavior in the domain.
- Functional models are based on the notion of functions and data flows. Functions are operations or transformations that manipulate data or produce some output. Data flows are connections or paths that transfer data between functions or external sources or sinks. Functional models can be used to describe the processes or activities that occur in the domain, as well as the data involved in them.
- Logic-based models are based on the notion of predicates and logic. Predicates are expressions that state some facts or conditions about data or the domain. Logic is a formal system of reasoning that can be used to infer new facts or verify existing ones. Logic-based models can be used to represent the knowledge or rules that govern the domain, as well as the data that is relevant to it.
- Semantic data models have several advantages over traditional data models, such as:
  - They provide a more natural and intuitive way of modeling data and its semantics, using concepts and terms that are familiar to the domain experts and users.
  - They allow for a higher level of abstraction and expressiveness, enabling the representation of complex and rich data structures and relationships, as well as constraints and rules that capture the logic and behavior of the domain.
  - They facilitate the integration and interoperability of data from different sources or domains, by providing a common and consistent semantic framework that can be mapped or translated across different data models or formats.
  - They enable the development of intelligent database systems that can support more advanced and flexible data management and analysis capabilities, such as semantic querying, reasoning, inference, validation, and discovery.



# Active Database Systems

- An active database is a database that includes an event-driven architecture (often in the form of ECA rules) which can respond to conditions both inside and outside the database .
- ECA stands for Event-Condition-Action, which is a rule that specifies what action to take when a certain event occurs and a certain condition is satisfied .
- Active databases are special forms of ASMs, which are abstract state machines that can model the behavior of any discrete system.
- Active databases are useful for applications that require automatic and timely responses to changes in data or environment, such as security monitoring, alerting, statistics gathering and authorization .
- Active databases are also useful for implementing business rules, workflows, integrity constraints and triggers.
- Active databases are very difficult to be maintained because of the complexity that arises in understanding the effect of these triggers.
- Active databases pose several challenges for research and development, such as semantics, implementation, optimization, verification, testing and debugging.
- Some examples of active database systems are Oracle, PostgreSQL, IBM DB2 and Microsoft SQL Server .



# Basic concepts for the notes of the Unit 2 - Semantic Data Models in the subject of INTELLIGENT DATABASE SYSTEM

- A semantic data model (SDM) is a high-level semantics-based database description and structuring formalism (database model) for databases.
- This database model is designed to capture more of the meaning of an application environment than is possible with contemporary database models.
- A semantic data model is a conceptual data model that includes semantic information that adds a basic meaning to the data and the relationships that lie between them.
- A semantic data model describes the meaning of its instances, such as entities, attributes, and relationships, using "instance of" relations.
- A semantic data model also includes the capability to express and exchange information that enables reasoning, inference, and consistency checking.
- A semantic data model can be represented using graphical notation, such as entity-relationship diagrams, or textual notation, such as object-role modeling.
- A semantic data model can be used for various purposes, such as database design, data integration, data analysis, and knowledge representation.
- A semantic data model can be classified into three types: classification, aggregation, and generalization.
  - Classification: This classifies different objects in objective reality by using “instance of” relations, such as "a car is an instance of a vehicle" or "a student is an instance of a person".
  - Aggregation: Aggregation defines a new object from a set of objects that become its components using “has a” relations, such as "a car has a wheel" or "a student has a name".
  - Generalization: Generalization defines a new object from a set of objects that share some common characteristics using “is a” relations, such as "a car is a vehicle" or "a student is a person".
- A semantic data model can be mapped to a logical data model, such as hierarchical, network, or relational, using various techniques, such as normalization, denormalization, or object-relational mapping.



# Issues for the notes of the Unit 2 - Semantic Data Models in the subject of INTELLIGENT DATABASE SYSTEM

- Semantic data models are high-level conceptual data models that include semantic information to describe the meaning and relationships of data .
- Semantic data models can be used to capture more of the meaning of an application environment than conventional data models, such as hierarchical, network, or relational .
- Semantic data models can also enable the expression and exchange of information that is understandable by both humans and machines .
- Some of the issues that need to be addressed when studying semantic data models are:

  - How to define and represent the concepts, entities, attributes, and relationships that are relevant to the application domain .
  - How to use semantic data models to support data integration, interoperability, and reuse across different systems and platforms.
  - How to use semantic data models to support data analysis, querying, reasoning, and inference.
  - How to use semantic data models to support data quality, consistency, and integrity.
  - How to compare and evaluate different semantic data models and their advantages and disadvantages .
  - How to implement and manage semantic data models using various tools and technologies, such as ontologies, RDF, OWL, etc.



# Architectures for Semantic Data Models

Semantic data models are high-level conceptual data models that include semantic information to describe the meaning and relationships of data. Semantic data models can be used to design databases, exchange information, and support reasoning and inference  .

There are different architectures for semantic data models, depending on the level of abstraction, the representation formalism, and the application domain. Some of the common architectures are:

- **Entity-relationship model**: This is a graphical model that represents data as entities (objects or concepts) and relationships (associations or links) between them. Entities have attributes (properties or characteristics) and relationships have cardinalities (constraints or rules) that specify the number of entities that can participate in a relationship. The entity-relationship model is widely used for database design and can be mapped to relational or other data models .

- **Object-oriented model**: This is a model that represents data as objects (instances of classes) and methods (operations or functions) that define the behavior of objects. Objects have attributes (data fields or variables) and methods (procedures or subroutines) that can be inherited or overridden by subclasses (specialized classes). The object-oriented model supports encapsulation (hiding the implementation details of objects), polymorphism (allowing different objects to respond to the same message), and inheritance (reusing the attributes and methods of existing classes) as the main features of object-oriented programming .

- **Frame model**: This is a model that represents data as frames (collections of slots) and facets (constraints or rules) that define the structure and behavior of frames. Frames have slots (attributes or relations) that can have values (data or other frames) and facets (properties or restrictions) that specify the type, range, default, or inheritance of slots. The frame model supports multiple inheritance (allowing a frame to inherit from more than one frame), default values (allowing a slot to have a predefined value if not specified), and procedural attachment (allowing a slot to have a procedure that is executed when the slot is accessed or modified) as the main features of knowledge representation .

- **Ontology model**: This is a model that represents data as ontologies (formal specifications of the concepts and relationships in a domain) and axioms (logical statements or rules) that define the semantics and constraints of ontologies. Ontologies have classes (sets of individuals or instances), properties (attributes or relations), and individuals (objects or values) that can have types (data types or classes) and values (data or individuals). The ontology model supports subsumption (allowing a class to be a subclass of another class), equivalence (allowing two classes or properties to be equivalent), and inference (allowing logical reasoning and deduction) as the main features of semantic web .



# Research relational prototypes—the Starburst Rule System

- The Starburst Rule System is an active database rules facility integrated into the Starburst extensible relational database system at the IBM Almaden Research Center   .
- The Starburst Rule System is based on arbitrary database state transitions rather than tuple- or statement-level changes, yielding a clear and flexible execution semantics  .
- The Starburst Rule System supports both immediate and deferred rule modes, as well as both forward-chaining and backward-chaining rule execution strategies  .
- The Starburst Rule System is implemented as an extension to the Starburst extensible relational database system, which provides a modular and customizable architecture for adding new features and functionality   .
- The Starburst Rule System uses a set-oriented relational database rule language, which is based on SQL and allows users to specify complex conditions and actions involving multiple tables and subqueries   .
- The Starburst Rule System employs various optimization techniques, such as rule grouping, rule filtering, rule rewriting, and rule caching, to improve the performance and scalability of rule processing  .
- The Starburst Rule System has been used for various applications, such as integrity constraint enforcement, materialized view maintenance, alerters, triggers, and workflow management   .



# Commercial Relational Approaches for Semantic Data Models

- Semantic data models are high-level database models that capture the meaning and structure of data in a natural and intuitive way.
- Semantic data models use concepts such as entities, attributes, relationships, and constraints to represent data and their semantics.
- Semantic data models can be mapped to relational data models, which are based on tables, columns, keys, and foreign keys.
- Commercial relational approaches for semantic data models are methods or tools that enable the design, implementation, and querying of semantic data models using relational database systems.
- Some examples of commercial relational approaches for semantic data models are:

  - Oracle Semantic Model: A semantic model is a layer of metadata that defines the business meaning and structure of data for analysis. It is deployed as a subject area in Oracle Analytics Cloud, which allows users to query data using natural language or graphical interfaces. The semantic model is based on a relational data source, such as Oracle Database or Oracle Autonomous Data Warehouse.
  - IBM Data Modeler: A data modeling tool that supports various data modeling techniques, such as entity-relationship, dimensional, and semantic modeling. It allows users to create and manage semantic data models that can be deployed to IBM Cognos Analytics, a business intelligence platform. The semantic data models are based on relational or multidimensional data sources, such as IBM Db2 or IBM Cognos TM1.
  - Stardog: A semantic graph database that supports the Resource Description Framework (RDF) and the SPARQL query language. It allows users to create and query semantic data models that can integrate data from various sources, such as relational databases, NoSQL databases, web services, and files. The semantic data models are based on RDF graphs, which are composed of triples that represent entities, attributes, and relationships.



# Unit 3 - Knowledge-Based Systems - AI Context

- A knowledge-based system (KBS) is a form of artificial intelligence (AI) that aims to capture the knowledge of human experts to support decision-making  .
- A KBS stores knowledge in the form of rules, facts, concepts, or other representations, which are then used to generate solutions to specific problems .
- A KBS consists of two main components: a knowledge base and an inference engine  .
  - A knowledge base is a collection of knowledge that is relevant to a specific problem domain, such as medicine, law, engineering, etc.
  - An inference engine is a software program that applies logical reasoning to the knowledge base to derive new knowledge or conclusions.
- A KBS can have different types, depending on the nature and structure of the knowledge base and the inference engine  .
  - An expert system is a KBS that mimics the reasoning of a human expert in a specific domain, such as diagnosing diseases, planning routes, or designing circuits.
  - A case-based reasoning system is a KBS that solves new problems by retrieving and adapting solutions from previous similar cases, such as legal precedents, customer complaints, or medical histories.
  - A rule-based system is a KBS that uses a set of if-then rules to represent and manipulate knowledge, such as tax laws, chess strategies, or grammar rules.
  - A semantic network is a KBS that uses a graph of nodes and links to represent and organize knowledge, such as concepts, categories, relations, or events.
  - A frame-based system is a KBS that uses a hierarchical structure of frames to represent and inherit knowledge, such as objects, attributes, values, or methods.
  - An ontology-based system is a KBS that uses a formal and explicit specification of the concepts, relations, and constraints in a domain, such as biology, geography, or music.
- A KBS can have different uses, depending on the purpose and function of the system  .
  - A decision support system is a KBS that helps users make decisions by providing relevant information, analysis, or recommendations, such as financial planning, risk assessment, or product selection.
  - A tutoring system is a KBS that helps users learn by providing instruction, feedback, or guidance, such as language learning, math skills, or driving lessons.
  - A diagnosis system is a KBS that helps users identify the causes or effects of a problem by providing symptoms, tests, or solutions, such as medical diagnosis, fault detection, or troubleshooting.
  - A planning system is a KBS that helps users achieve a goal by providing actions, steps, or strategies, such as travel planning, project management, or game playing.
  - A design system is a KBS that helps users create or modify a product by providing specifications, constraints, or alternatives, such as engineering design, architectural design, or graphic design.



# Characteristics and Classification of Knowledge-Based Systems

A knowledge-based system (KBS) is a type of computer system that uses artificial intelligence (AI) concepts to solve problems, which may be useful for assisting with human learning and making decisions . A KBS has two distinguishing features: a knowledge base and an inference engine.

- The knowledge base represents facts about the world, often in some form of subsumption ontology (a hierarchical structure of concepts and their relations). The knowledge base can be derived from various sources, such as experts, documents, databases, or other KBSs.
- The inference engine is the component that applies logical rules and reasoning methods to the knowledge base to derive new knowledge or conclusions. The inference engine can use different types of reasoning, such as deductive, inductive, abductive, analogical, or case-based.

Some of the characteristics of KBSs are :

- They can handle complex and ill-structured problems that require human expertise and judgment.
- They can explain their reasoning process and justify their decisions or recommendations.
- They can learn from new data and feedback and update their knowledge base accordingly.
- They can interact with users in natural language and provide user-friendly interfaces.

There are different types of KBSs, depending on the domain, the purpose, and the methodology of the system. Some of the common types are:

- Case-based systems: These systems use case-based reasoning, which involves reviewing past knowledge of similar situations and adapting them to the current problem. Case-based systems are useful for diagnosis, planning, design, and learning.
- Expert systems: These systems emulate the reasoning and decision-making of human experts in a specific domain. Expert systems typically use rule-based or logic-based reasoning and can provide advice, recommendations, or solutions to users.
- Hypertext manipulation systems: These systems allow users to access, manipulate, and create hypertext documents, which are non-linear and interconnected texts that can contain multimedia elements. Hypertext manipulation systems are useful for information retrieval, browsing, and authoring.
- Intelligent tutoring systems: These systems provide personalized and adaptive instruction to learners, based on their goals, preferences, and performance. Intelligent tutoring systems can monitor, assess, and guide learners, as well as provide feedback and hints.
- Rule-based systems: These systems use a set of rules, which are conditional statements that specify the actions or outcomes for a given situation. Rule-based systems can perform tasks such as classification, inference, or control.



# Introduction for the notes of the Unit 3 - Knowledge-Based Systems- AI Context in the subject of INTELLIGENT DATABASE SYSTEM

- A knowledge-based system (KBS) is a computer system that uses artificial intelligence (AI) techniques to solve problems that normally require human expertise.
- A KBS consists of two main components: a knowledge base and an inference engine.
- A knowledge base is a collection of facts, rules, and heuristics that represent the domain knowledge of a specific problem area.
- An inference engine is a software module that applies logical reasoning to the knowledge base to derive new information or conclusions.
- A KBS can also have other components, such as a user interface, a knowledge acquisition module, a knowledge representation language, and a knowledge validation module.
- A KBS can be classified into different types based on the nature of the knowledge, the reasoning method, and the application domain.
- Some examples of KBS types are expert systems, case-based reasoning systems, rule-based systems, fuzzy systems, neural networks, genetic algorithms, and hybrid systems.
- A KBS can provide various benefits, such as improving decision making, enhancing productivity, reducing errors, saving costs, and facilitating learning and training.
- A KBS can also face various challenges, such as acquiring and maintaining knowledge, dealing with uncertainty and inconsistency, ensuring reliability and security, and evaluating performance and usability.
- A KBS can be developed using various methodologies, tools, and standards, such as knowledge engineering, rapid prototyping, commonKADS, Protégé, and KIF.



# The resolution principle

- The resolution principle is a general rule of inference that can be used to derive new conclusions from a set of premises .
- It is based on the idea of resolving two clauses that contain complementary literals, i.e., literals that are the negation of each other .
- For example, if we have the clauses `p v q` and `¬p v r`, we can resolve them on the literal `p` and obtain the new clause `q v r`.
- The resolution principle can be applied to propositional logic and predicate logic, with some modifications .
- In propositional logic, the resolution principle can be used to perform automated theorem proving, by converting all the sentences to conjunctive normal form (CNF), negating the desired conclusion, and applying the resolution rule until either a contradiction is reached or no more clauses can be added .
- In predicate logic, the resolution principle requires the use of unification, a process of finding a substitution for the variables in the clauses that makes them identical .
- For example, if we have the clauses `P(x) v Q(y)` and `¬Q(a) v R(z)`, we can unify them on the literal `Q` by substituting `y` with `a`, and obtain the new clause `P(x) v R(z)`.
- The resolution principle is the basis of logic programming and production rules paradigms, which use resolution to infer new facts from a knowledge base.



# Inference by inheritance for the notes of the Unit 3 - Knowledge-Based Systems- AI Context in the subject of INTELLIGENT DATABASE SYSTEM

- Inference by inheritance is a technique of reasoning that uses the hierarchical structure of classes and subclasses to derive new facts from existing facts.
- Inference by inheritance is based on the principle of **subsumption**, which states that if a class A is a subclass of another class B, then any instance of A is also an instance of B, and any property of B is also a property of A.
- For example, if we have a class `Animal` and a subclass `Dog`, then we can infer that any instance of `Dog` is also an instance of `Animal`, and any property of `Animal` (such as having a heart) is also a property of `Dog`.
- Inference by inheritance can be applied to both **is-a** and **part-of** relationships between classes. For example, if we have a class `Car` and a subclass `Sedan`, then we can infer that any instance of `Sedan` is also an instance of `Car`, and any property of `Car` (such as having wheels) is also a property of `Sedan`. Similarly, if we have a class `Car` and a part `Engine`, then we can infer that any instance of `Car` has an `Engine`, and any property of `Engine` (such as having cylinders) is also a property of `Car`.
- Inference by inheritance can be implemented using different data structures and algorithms, such as **semantic networks**, **frames**, **inheritance networks**, **description logics**, and **ontologies**. These data structures and algorithms allow us to represent and manipulate the hierarchical structure of classes and subclasses, and to perform efficient and consistent reasoning based on subsumption.
- Inference by inheritance is useful for knowledge-based systems, as it allows us to store and retrieve information in a compact and organized way, and to infer new information from existing information. It also enables us to handle **multiple inheritance**, **default reasoning**, and **exceptions** in a principled way.
- Inference by inheritance is a form of **deductive reasoning**, which means that it derives conclusions that are logically valid from the premises. However, it does not guarantee that the conclusions are true in the real world, as the premises may be incomplete or inaccurate. Therefore, inference by inheritance should be combined with other forms of reasoning, such as **inductive reasoning**, **abductive reasoning**, and **probabilistic reasoning**, to achieve more robust and reliable results.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the conclusion for the notes of the Unit 3 - Knowledge-Based Systems- AI Context in the subject of Intelligent Database System:

### Conclusion

- Knowledge-based systems are computer systems that use artificial intelligence techniques to solve complex problems that require human expertise and knowledge.
- Knowledge-based systems consist of two main components: a knowledge base and an inference engine. The knowledge base stores the facts and rules that represent the domain knowledge, while the inference engine applies logical reasoning to infer new facts and conclusions from the knowledge base.
- Knowledge-based systems can be classified into two types: rule-based systems and frame-based systems. Rule-based systems use IF-THEN rules to represent knowledge, while frame-based systems use frames and slots to represent knowledge. Both types of systems have advantages and disadvantages depending on the application domain and the complexity of the problem.
- Knowledge-based systems can be integrated with database systems to create intelligent database systems that can provide more advanced functionalities, such as natural language processing, data mining, expert systems, and semantic web. Intelligent database systems can enhance the data quality, usability, and accessibility of the database systems.



# Deductive Database Systems

- A deductive database is a database system that can make deductions (i.e. conclude additional facts) based on rules and facts stored in the (deductive) database.
- Deductive databases offer elegant and powerful ways of managing complex data in a declarative way, especially for information that is derived by use of recursion.
- Deductive systems typically provide a declarative query language such as a logic programming language (e.g., Prolog).
- Deductive database systems can be seen as bringing together mainstream data models with logic programming languages for querying and analyzing database data.
- Deductive databases have applications in various domains such as artificial intelligence, knowledge representation, natural language processing, data mining, etc.
- Some examples of commercial deductive database systems are Oracle, IBM DB2, and Microsoft SQL Server.



# Basic concepts for the notes of the Unit 3 - Knowledge-Based Systems- AI Context in the subject of INTELLIGENT DATABASE SYSTEM

- A **knowledge-based system (KBS)** is a form of artificial intelligence (AI) that aims to capture the knowledge of human experts to support decision-making  .
- A KBS consists of two main components: a **knowledge base** and an **inference engine**  .
- A **knowledge base** is a collection of facts, rules, and other information that represents the knowledge of a specific domain or problem  .
- An **inference engine** is a software component that applies logical reasoning to the knowledge base to generate solutions, explanations, or recommendations  .
- Examples of knowledge-based systems include **expert systems**, which are so called because of their reliance on human expertise  .
- An **expert system** is a type of KBS that mimics the reasoning and problem-solving skills of a human expert in a specific domain  .
- An expert system consists of three main components: a **knowledge base**, an **inference engine**, and a **user interface**  .
- A **user interface** is a software component that allows the user to interact with the expert system, by providing inputs, receiving outputs, and asking questions  .
- Examples of expert systems include **MYCIN**, which is a medical diagnosis system for infectious diseases  , and **DENDRAL**, which is a chemical analysis system for organic compounds  .
- Other types of knowledge-based systems include **case-based reasoning systems**, which use past cases or examples to solve new problems  , and **ontology-based systems**, which use formal representations of concepts and relations to organize and share knowledge  .
- Knowledge-based systems have various applications and benefits, such as enhancing human learning, improving decision quality, increasing productivity, and reducing errors  .
- Knowledge-based systems also have some limitations and challenges, such as acquiring and maintaining knowledge, ensuring reliability and validity, dealing with uncertainty and inconsistency, and addressing ethical and social issues  .



# DATALOG language

- Datalog is a **declarative logic programming language** that is based on **function-free Horn clauses** .
- Datalog is often used as a **query language** for **deductive databases**, which are databases that can derive new facts from existing facts using logical rules .
- Datalog is syntactically a **subset of Prolog**, but it has a different **evaluation model**. Datalog uses a **bottom-up** approach, which means it starts from the facts and derives the conclusions, while Prolog uses a **top-down** approach, which means it starts from the query and searches for the facts .
- Datalog has some advantages over Prolog, such as **guaranteed termination**, **efficient implementation**, and **easier parallelization** .
- Datalog has some limitations, such as **lack of negation**, **lack of functions**, and **lack of arithmetic operations** .
- Datalog has found new applications in various domains, such as **data integration**, **information extraction**, **networking**, **program analysis**, **security**, **cloud computing** and **machine learning** .



# Deductive database systems and logic programming systems—differences

- Deductive database systems are systems that combine relational databases with logic programming to support a powerful and declarative formalism for querying and manipulating data.
- Logic programming systems are systems that use a subset of logic to express programs as a set of rules and facts that can be queried and executed by an inference engine.
- Some of the differences between deductive database systems and logic programming systems are:

  - Order sensitivity and procedurality: In logic programming systems, such as Prolog, the order of rules and facts in the program and the order of subgoals in the rules can affect the execution and efficiency of the program. In deductive database systems, such as Datalog, the order of rules and facts is irrelevant and the evaluation is based on a fixed-point semantics that guarantees the same result regardless of the order.
  - Special predicates: In logic programming systems, programmers can use special predicates, such as cut, fail, assert, retract, etc., to control the execution flow and modify the program dynamically. In deductive database systems, these predicates are either not allowed or have a different meaning, as they violate the declarative and logical nature of the system.
  - Expressiveness: In logic programming systems, programmers can use arbitrary terms and functions to represent data and computations. In deductive database systems, the data is restricted to relations and the computations are restricted to relational algebra and recursion. Therefore, deductive database systems are less expressive than logic programming systems, but more expressive than relational database systems.
  - Application domains: Logic programming systems are more suitable for domains that require complex reasoning, such as artificial intelligence, natural language processing, knowledge representation, etc. Deductive database systems are more suitable for domains that require efficient and scalable management of large amounts of data, such as data integration, information extraction, networking, program analysis, security, cloud computing, etc.



# Architectural approaches for the notes of the Unit 3 - Knowledge-Based Systems- AI Context in the subject of INTELLIGENT DATABASE SYSTEM

- A knowledge-based system (KBS) is a computer system that uses artificial intelligence to solve problems within a specialized domain that ordinarily requires human expertise.
- The typical architecture of a KBS consists of two main components: a **knowledge base** and an **inference engine** .
- The knowledge base contains a collection of information in a given field, such as medical diagnosis, engineering design, or financial analysis. The information can be represented in various forms, such as rules, facts, frames, semantic networks, or ontologies.
- The inference engine is a software program that applies logical rules and reasoning methods to the knowledge base in order to deduce new information or provide solutions to problems. The inference engine can use different techniques, such as forward chaining, backward chaining, or case-based reasoning.
- Some KBS may also have other components, such as a **user interface**, a **knowledge acquisition module**, or a **knowledge explanation module**.
- The user interface is the means of communication between the KBS and the human user. It can be text-based, graphical, or natural language-based, depending on the nature and complexity of the domain and the user's preferences.
- The knowledge acquisition module is a tool that helps the knowledge engineer or the domain expert to create, modify, or update the knowledge base. It can use various methods, such as interviewing, observation, or learning from examples, to elicit and formalize the knowledge from the source.
- The knowledge explanation module is a feature that allows the KBS to explain its reasoning process, the sources of its knowledge, or the justification of its conclusions. It can enhance the user's trust, understanding, and acceptance of the KBS.

: https://theintactone.com/2020/11/12/knowledge-based-expert-system-kbes/
: https://www.techtarget.com/searchcio/definition/knowledge-based-systems-KBS



# Research prototypes for the notes of the Unit 3 - Knowledge-Based Systems- AI Context in the subject of INTELLIGENT DATABASE SYSTEM

- A research prototype is a preliminary version of a system that is used to test and evaluate its feasibility, functionality, performance, and usability in a specific domain or problem.
- A research prototype can be used to demonstrate the potential of a new approach, technique, or technology, or to explore the design space and user needs of a system.
- A research prototype can also be used to collect feedback and data from users, experts, or stakeholders, and to refine and improve the system based on the findings.
- A research prototype can be implemented in various forms and levels of fidelity, depending on the purpose and scope of the research. For example, a research prototype can be a paper mockup, a software simulation, a hardware device, or a combination of these.
- A research prototype can be evaluated using various methods and criteria, such as usability testing, user satisfaction, task performance, error rates, learning curves, or system efficiency.

## Examples of research prototypes for knowledge-based systems

- A knowledge-based system is a system that uses artificial intelligence techniques to represent, manipulate, and reason with knowledge, and to provide solutions or recommendations to users based on their goals and preferences.
- A knowledge-based system typically consists of a knowledge base, which stores the domain knowledge in a structured and formal way, and an inference engine, which applies logical rules and heuristics to infer new knowledge or solutions from the existing knowledge.
- A knowledge-based system can be applied to various domains and problems, such as diagnosis, planning, scheduling, design, configuration, or decision support.
- Some examples of research prototypes for knowledge-based systems are:

  - A prototype knowledge-based simulation support system, which was developed to support a senior level course in industrial engineering and to study the feasibility of an expert simulation support system . The system used a rule-based approach to guide the students through the simulation modeling process, and to provide feedback and suggestions on their models.
  - A prototype knowledge-based system for fingerprint image classification, which was developed to improve the accuracy and efficiency of fingerprint identification. The system used a geometric knowledge-based framework to represent and classify the fingerprint images based on their ridge patterns and singular points.
  - A prototype knowledge-based system for music composition, which was developed to explore the creative potential of artificial intelligence in music. The system used a generative grammar approach to generate musical structures and melodies based on a set of rules and constraints.



# Updates in deductive databases for the notes of the Unit 3 - Knowledge-Based Systems- AI Context in the subject of INTELLIGENT DATABASE SYSTEM

- A **deductive database** is a database system that can make deductions (i.e. conclude additional facts) based on rules and facts stored in the (deductive) database.
- Deductive databases offer elegant and powerful ways of managing complex data in a declarative way, especially for information that is derived by use of recursion.
- Deductive systems typically provide a declarative query language such as a logic programming language (e.g., Prolog) or a variant of it (e.g., Datalog).
- Some of the updates in deductive databases are:
  - **Deductive XML databases**: These are deductive databases that can handle XML data and queries, using extensions of Datalog to support XML syntax and semantics.
  - **Deductive graph databases**: These are deductive databases that can handle graph data and queries, using extensions of Datalog to support graph structures and operations.
  - **Deductive spatial databases**: These are deductive databases that can handle spatial data and queries, using extensions of Datalog to support spatial predicates and functions.
  - **Deductive temporal databases**: These are deductive databases that can handle temporal data and queries, using extensions of Datalog to support temporal aspects such as intervals, timestamps, and validity.
  - **Deductive probabilistic databases**: These are deductive databases that can handle uncertain data and queries, using extensions of Datalog to support probabilistic reasoning and inference.
  - **Deductive ontological databases**: These are deductive databases that can handle ontological data and queries, using extensions of Datalog to support ontological concepts and relations.

: https://en.wikipedia.org/wiki/Deductive_database
: https://www.sciencedirect.com/topics/computer-science/deductive-database
: https://link.springer.com/chapter/10.1007/978-3-540-30570-5_2
: https://dl.acm.org/doi/10.1145/3299869.3319888
: https://www.sciencedirect.com/science/article/pii/S0306437914000630
: https://www.sciencedirect.com/science/article/pii/S0306437914000629
: https://link.springer.com/chapter/10.1007/978-3-642-15918-3_1
: https://link.springer.com/chapter/10.1007/978-3-642-15918-3_2



# Integration of deductive database and object database technologies

- Deductive databases extend relational databases with inherent support for powerful rules that provide for the declarative specification of deductive rules and integrity constraints.
- Object-oriented databases provide complex data structuring including class hierarchies and inheritance.
- The integration of the two technologies aims to provide an expressive and efficient framework for knowledge-based systems that can handle both data and knowledge models.
- Some of the benefits of the integration are:
  - The ability to model complex objects and relationships using object-oriented concepts such as classes, inheritance, polymorphism, and encapsulation.
  - The ability to specify and reason about the semantics and behavior of objects using deductive rules and logic programming.
  - The ability to support both data and knowledge intensive applications, such as expert systems, natural language processing, spatial databases, and data mining.
- Some of the challenges of the integration are:
  - The design of a suitable data model and query language that can capture both the object-oriented and the deductive features.
  - The implementation of efficient and scalable query processing and optimization techniques that can handle both the object-oriented and the deductive aspects.
  - The development of a sound and complete semantics and a formal framework for the integration.
  - The evaluation of the performance and expressiveness of the integrated system compared to the existing systems.
- Some of the examples of the integrated systems are:
  - LDL++: A deductive object-oriented database system that supports a class hierarchy, multiple inheritance, and user-defined methods, as well as a rule-based language for specifying deductive rules and integrity constraints.
  - CORAL: A deductive object-oriented database system that supports a class hierarchy, multiple inheritance, and user-defined methods, as well as a logic programming language for specifying deductive rules and queries.
  - F-Logic: A deductive object-oriented database system that supports a class hierarchy, multiple inheritance, and user-defined methods, as well as a frame-based language for specifying deductive rules and queries.
  - DOODLE: A deductive object-oriented database system that supports a class hierarchy, multiple inheritance, and user-defined methods, as well as a logic programming language for specifying deductive rules and queries.



# Constraint databases

- Constraint databases are a type of database that use constraints to represent and query data.
- Constraints are logical expressions that define the properties or relationships of data values.
- Constraint databases can handle complex and multidimensional data that are not suitable for relational databases.
- Constraint databases provide extra expressive power over relational databases in a largely hidden way. They keep the view of the database for a user or application programmer almost as simple as in relational databases.
- Constraint databases are shown to be powerful and simple tools for data modeling and querying in application areas -- such as environmental modeling, bioinformatics, and computer vision -- that are not suitable for relational databases.
- Constraint databases can be classified into different types based on the constraint language used, such as linear, polynomial, or spatial constraint databases.
- Constraint databases can also be integrated with other database paradigms, such as object-oriented, deductive, or temporal databases, to achieve more functionality and flexibility.
- Constraint databases rely on the database management system to ensure integrity, accuracy, and reliability of the data stored in them, by enforcing the rules defined by the constraints.
- Constraint databases can be queried using constraint query languages, such as CQL or CLP, that extend the relational algebra or logic programming with constraint operations.
- Constraint databases can also support operations such as aggregation, grouping, and recursion, that are common in knowledge-based systems.



# Conclusions for the notes of the Unit 3 - Knowledge-Based Systems- AI Context in the subject of INTELLIGENT DATABASE SYSTEM

- Knowledge-based systems (KBS) are computer systems that use artificial intelligence techniques to solve complex problems that normally require human expertise.
- KBS consist of two main components: a knowledge base and an inference engine. The knowledge base stores the domain knowledge in a formal representation, such as rules, frames, or ontologies. The inference engine applies logical reasoning to the knowledge base to derive new facts or conclusions.
- KBS can be classified into different types based on the nature of the knowledge, the reasoning method, or the application domain. Some common types of KBS are expert systems, case-based reasoning systems, neural networks, fuzzy systems, and hybrid systems.
- KBS can provide various benefits, such as improving decision making, enhancing productivity, reducing errors, and facilitating learning and knowledge sharing. However, KBS also face some challenges, such as acquiring and maintaining the knowledge, ensuring the validity and reliability of the knowledge, and dealing with uncertainty and inconsistency.
- KBS can be integrated with database systems to create intelligent database systems (IDS), which can support more advanced data management and analysis functions. Some examples of IDS are deductive databases, active databases, temporal databases, spatial databases, and multimedia databases.



# Unit 4 - Advanced Knowledge-Based Systems

- A knowledge-based system (KBS) is a computer system that uses artificial intelligence techniques to solve problems that require human expertise.
- A KBS consists of two main components: a knowledge base and an inference engine.
- A knowledge base is a collection of facts, rules, heuristics, and other forms of knowledge representation that capture the domain knowledge of a human expert.
- An inference engine is a software module that applies logical reasoning to the knowledge base to derive new facts, conclusions, or recommendations.
- A KBS can also have other components, such as a user interface, a knowledge acquisition module, a knowledge validation module, and a knowledge explanation module.
- A KBS can be classified into different types based on the nature of the knowledge, the reasoning method, or the application domain.
- Some common types of KBS are:
  - Rule-based systems: use rules of the form IF condition THEN action to represent and reason with knowledge.
  - Case-based systems: use past cases or examples to solve new problems by analogy or similarity.
  - Model-based systems: use mathematical or physical models to simulate the behavior of a system or a phenomenon.
  - Neural network systems: use artificial neural networks to learn from data and generalize to new situations.
  - Fuzzy systems: use fuzzy logic to deal with uncertainty and vagueness in knowledge.
  - Ontology-based systems: use ontologies to define the concepts, relations, and axioms of a domain in a formal and unambiguous way.
  - Hybrid systems: use a combination of two or more types of KBS to exploit their strengths and overcome their limitations.



# Introduction for the notes of the Unit 4 - Advanced Knowledge-Based Systems in the subject of INTELLIGENT DATABASE SYSTEM

- A knowledge-based system (KBS) is a computer system that uses artificial intelligence techniques to solve problems that normally require human expertise.
- A KBS consists of two main components: a knowledge base and an inference engine.
- A knowledge base is a collection of facts, rules, heuristics, and other forms of knowledge representation that capture the domain knowledge of a human expert.
- An inference engine is a software module that applies logical reasoning to the knowledge base to derive new facts, conclusions, or recommendations.
- A KBS can also have other components, such as a user interface, a knowledge acquisition module, a knowledge validation module, and a knowledge explanation module.
- A KBS can be classified into different types based on the nature of the knowledge, the reasoning method, or the application domain.
- Some examples of KBS types are rule-based systems, case-based systems, model-based systems, neural networks, fuzzy systems, genetic algorithms, expert systems, decision support systems, and intelligent agents.
- A KBS can provide various benefits, such as improving the quality, consistency, and efficiency of problem solving, enhancing human learning and creativity, and facilitating knowledge sharing and reuse.
- A KBS can also face various challenges, such as acquiring, representing, and maintaining the knowledge, ensuring the validity, reliability, and security of the system, and dealing with uncertainty, incompleteness, and inconsistency of the knowledge.
- A KBS can be developed using various methodologies, tools, and languages, such as knowledge engineering, rapid prototyping, object-oriented programming, logic programming, and ontology engineering.



# Architectural solutions for the notes of the Unit 4 - Advanced Knowledge-Based Systems in the subject of INTELLIGENT DATABASE SYSTEM

- A knowledge-based system (KBS) is a computer system that uses artificial intelligence techniques to solve complex problems that normally require human expertise .
- A KBS consists of two main components: a knowledge base and an inference engine .
- A knowledge base is a repository of facts, rules, heuristics, and other forms of knowledge that represent the domain of the problem .
- An inference engine is a software module that applies logical reasoning to the knowledge base to derive new knowledge or conclusions .
- A KBS can support architectural design by providing intelligent objects, project net-constraints, and collaborative work  .
- Intelligent objects are entities that have both geometric and semantic properties, and can interact with other objects and the environment  .
- Project net-constraints are global and local constraints that regulate the design process and ensure the consistency and feasibility of the design solution  .
- Collaborative work is the ability of multiple agents (human or artificial) to cooperate and coordinate their actions in a distributed and concurrent design environment  .
- A KBS can also benefit from knowledge-based approaches in software engineering, such as knowledge capture and representation, knowledge reuse, knowledge sharing, knowledge reasoning, and knowledge recovery .
- Knowledge capture and representation are the processes of eliciting, formalizing, and storing the knowledge of experts and stakeholders in a suitable format for the KBS .
- Knowledge reuse is the process of applying existing knowledge to new problems or domains, thus reducing the cost and effort of developing new knowledge .
- Knowledge sharing is the process of exchanging and disseminating knowledge among different agents, systems, or organizations, thus enhancing the communication and collaboration among them .
- Knowledge reasoning is the process of applying logical rules and algorithms to the knowledge base to infer new knowledge or conclusions, thus increasing the intelligence and performance of the KBS .
- Knowledge recovery is the process of extracting and recovering the implicit or tacit knowledge that is embedded in the software artifacts, such as code, documentation, or models, thus improving the understanding and maintenance of the KBS .
- A KBS can also adopt architectural solutions for self-adaptive systems, which are systems that can monitor, analyze, plan, and execute changes in their structure and behavior in response to changes in the environment or the requirements  .
- Architectural solutions for self-adaptive systems include well-known architectural patterns, such as feedback loop, MAPE-K, Rainbow, and Znn.com, and their possible benefits and drawbacks .
- A feedback loop is a generic pattern that consists of four phases: monitor, analyze, plan, and execute, which are executed cyclically to adapt the system to the changing conditions .
- MAPE-K is a specific instance of the feedback loop pattern, where the system has a knowledge base that stores the goals, policies, and models of the system, and is used by the other phases to guide the adaptation process .
- Rainbow is a framework that implements the MAPE-K pattern, and provides a language for specifying the adaptation strategies, a mechanism for selecting the best strategy, and a set of reusable infrastructure components .
- Znn.com is a case study of a self-adaptive system that simulates a news website that can dynamically adjust its content, layout, and server configuration to optimize the user satisfaction and the revenue .

: Knowledge-based System to Support Architectural Design - Academia.edu
: Knowledge-based System to Support Architectural Design
: Application of knowledge-based approaches in software ... - ScienceDirect
: Architectural Knowledge - an overview | ScienceDirect Topics
: Architectural Solutions for Self-Adaptive Systems - ResearchGate



# The 'general bridge' solution for the notes of the Unit 4 - Advanced Knowledge-Based Systems in the subject of INTELLIGENT DATABASE SYSTEM

- A knowledge-based system (KBS) is a type of computer system that analyzes knowledge, data and other information from sources to generate new knowledge.
- A knowledge-based system uses AI concepts to solve problems, which may be useful for assisting with human learning and making decisions.
- A knowledge-based system consists of two main components: a knowledge base and an inference engine.
- A knowledge base is a collection of facts, rules, and heuristics that represent the domain knowledge of a specific problem or task.
- An inference engine is a software component that applies logical reasoning to the knowledge base to derive new knowledge or conclusions.
- A general bridge solution is a method of integrating a knowledge-based system with a conventional database system.
- A general bridge solution allows the knowledge-based system to access the data stored in the database system, and vice versa.
- A general bridge solution consists of four main components: a database interface, a knowledge base interface, a query processor, and a knowledge processor.
- A database interface is a software component that enables the knowledge-based system to communicate with the database system using a common data model and query language.
- A knowledge base interface is a software component that enables the database system to communicate with the knowledge-based system using a common knowledge representation and inference language.
- A query processor is a software component that translates queries from one system to another, and returns the results to the appropriate system.
- A knowledge processor is a software component that performs inference on the knowledge base and the database, and updates the knowledge base accordingly.
- A general bridge solution can provide several benefits, such as:
  - Enhancing the functionality and performance of both systems by combining their strengths.
  - Enabling the sharing and reuse of knowledge and data across different domains and applications.
  - Facilitating the maintenance and evolution of both systems by reducing redundancy and inconsistency.
  - Improving the reliability and security of both systems by enforcing integrity and access control rules.



# Extending a KBS with components proper to a DBMS

- A Knowledge-Based System (KBS) is a system that uses artificial intelligence techniques to solve problems that require human expertise.
- A Database Management System (DBMS) is a software tool that enables users to create and manage databases, which are collections of data organized in a structured way.
- Extending a KBS with components proper to a DBMS means integrating the two technologies to achieve the benefits of both, such as:
  - Storing and retrieving large amounts of data efficiently and reliably.
  - Representing and reasoning with complex and uncertain knowledge.
  - Providing user-friendly interfaces and natural language processing.
  - Supporting multiple users and concurrent access.
  - Ensuring data security and integrity.
  - Facilitating knowledge acquisition and maintenance.
- Some examples of extending a KBS with components proper to a DBMS are:
  - Using a relational database to store facts and rules for a rule-based system.
  - Using a deductive database to perform logical inference and query answering.
  - Using an object-oriented database to model complex and hierarchical knowledge structures.
  - Using a semantic web database to represent and share knowledge using ontologies and RDF.
  - Using a data warehouse to integrate and analyze data from multiple sources for a decision support system.



# The 'tight coupling' approach for the notes of the Unit 4 - Advanced Knowledge-Based Systems in the subject of INTELLIGENT DATABASE SYSTEM

- Tight coupling means that a data mining system is smoothly integrated into the database/data warehouse system.
- The data mining subsystem is treated as one functional component of the information system.
- The database or data warehouse is used as an information retrieval component of the data mining system using integration.
- All the features of the database or data warehouse are used to perform data mining tasks.
- The advantages of tight coupling are:
  - It can leverage the existing database or data warehouse infrastructure, such as query processing, indexing, concurrency control, etc.
  - It can support complex and ad-hoc queries over large and heterogeneous data sources.
  - It can avoid data duplication and inconsistency between the data mining system and the database/data warehouse system.
- The disadvantages of tight coupling are:
  - It may require significant modifications to the database or data warehouse system to accommodate the data mining algorithms and operations.
  - It may impose performance overhead and scalability issues on the database or data warehouse system due to the intensive data mining computations.
  - It may not be able to handle some data mining tasks that require specialized data structures or formats that are not supported by the database or data warehouse system.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the conclusion for the notes of the Unit 4 - Advanced Knowledge-Based Systems in the subject of INTELLIGENT DATABASE SYSTEM.

# Conclusion

- Advanced knowledge-based systems are systems that use artificial intelligence techniques to perform complex tasks that require human expertise and reasoning.
- Some of the applications of advanced knowledge-based systems are expert systems, natural language processing, computer vision, machine learning, data mining, and knowledge discovery.
- Expert systems are systems that emulate the decision-making process of a human expert in a specific domain. They consist of a knowledge base, an inference engine, and a user interface.
- Natural language processing is the field of computer science that deals with the analysis and generation of natural language texts and speech. It involves tasks such as parsing, semantic analysis, discourse analysis, text summarization, machine translation, and natural language generation.
- Computer vision is the field of computer science that deals with the acquisition, processing, and understanding of visual information. It involves tasks such as image processing, feature extraction, object recognition, face recognition, scene understanding, and computer graphics.
- Machine learning is the field of computer science that deals with the design and implementation of algorithms that can learn from data and improve their performance. It involves tasks such as classification, regression, clustering, dimensionality reduction, reinforcement learning, and deep learning.
- Data mining is the process of discovering useful patterns and knowledge from large and complex data sets. It involves tasks such as association rule mining, frequent itemset mining, sequential pattern mining, classification, regression, clustering, and anomaly detection.
- Knowledge discovery is the process of extracting high-level and actionable knowledge from data mining results. It involves tasks such as data preprocessing, data transformation, data mining, pattern evaluation, and knowledge presentation.



# Advanced solutions for the notes of the Unit 4 - Advanced Knowledge-Based Systems in the subject of INTELLIGENT DATABASE SYSTEM

## Introduction

- A knowledge-based system (KBS) is a computer program that reasons and uses a knowledge base to solve complex problems.
- The knowledge base consists of facts and rules that represent the domain knowledge of experts.
- The reasoning system, also called the inference engine, applies the rules to the facts and derives new facts or conclusions.
- KBS can be classified into different types, such as expert systems, case-based reasoning systems, neural networks, fuzzy systems, genetic algorithms, etc .
- KBS can be used for various purposes, such as diagnosis, planning, design, tutoring, decision making, etc .
- KBS can be developed using various tools and software, such as Prolog, Lisp, CLIPS, Java Expert System Shell (JESS), etc.

## Advanced Knowledge-Based Systems

- Advanced knowledge-based systems are KBS that use the latest technologies and techniques to deal with complex, unstructured, and dynamic data and problems.
- Some of the characteristics of advanced knowledge-based systems are:
  - They use the internet as a source and medium of knowledge.
  - They use description logic, a kind of logic that allows for the representation and reasoning of concepts, properties, and relations, to model the domain knowledge.
  - They use ontologies, which are formal and explicit specifications of the concepts and relations in a domain, to organize and share the knowledge.
  - They use semantic web, which is a web of data that can be processed by machines, to enhance the interoperability and integration of the knowledge.
  - They use web services, which are software components that can be invoked over the internet, to provide the functionality and intelligence of the KBS.
  - They use agents, which are autonomous and intelligent software entities that can communicate and cooperate with other agents, to perform the tasks and goals of the KBS.
- Some of the examples of advanced knowledge-based systems are:
  - Semantic search engines, which use ontologies and natural language processing to provide more relevant and precise results to the user queries.
  - Recommender systems, which use collaborative filtering, content-based filtering, or hybrid methods to suggest items or services to the users based on their preferences and behavior.
  - Question answering systems, which use natural language processing, information retrieval, and knowledge representation and reasoning to provide direct and concise answers to the user questions.
  - Knowledge management systems, which use ontologies, semantic web, and web services to capture, store, organize, and share the knowledge of an organization or a community.



# Introduction for the notes of the Unit 4 - Advanced Knowledge-Based Systems in the subject of INTELLIGENT DATABASE SYSTEM

- A knowledge-based system (KBS) is a computer system that uses artificial intelligence techniques to solve problems that require human expertise.
- A knowledge-based system consists of two main components: a knowledge base and an inference engine.
- A knowledge base is a collection of facts and rules that represent the domain knowledge of a human expert.
- An inference engine is a software program that applies logical reasoning to the knowledge base to derive new facts and conclusions.
- A knowledge-based system can also have other components, such as a user interface, a knowledge acquisition module, a knowledge representation language, and a knowledge validation module.
- A knowledge-based system can be classified into different types, such as rule-based systems, case-based systems, model-based systems, and hybrid systems, depending on the nature and structure of the knowledge base and the inference engine.
- A knowledge-based system can be applied to various domains, such as diagnosis, planning, scheduling, design, configuration, and decision support.
- A knowledge-based system can provide several benefits, such as increased productivity, consistency, reliability, and explainability, as well as reduced costs, errors, and training time.
- A knowledge-based system can also face several challenges, such as knowledge acquisition, knowledge representation, knowledge maintenance, knowledge verification, and knowledge validation, as well as ethical, social, and legal issues.



# A 'knowledge level' approach to the interaction with an IAS-TELOS

- IAS stands for Intelligent Advisory System, which is a type of knowledge-based system that provides advice or guidance to users in a specific domain of expertise.
- TELOS is a conceptual modeling language that can be used to capture software knowledge, such as requirements, domain knowledge, architectures, design decisions and more.
- A 'knowledge level' approach to the interaction with an IAS-TELOS means that the user and the system communicate at the level of concepts and relations that are relevant to the domain and the task, rather than at the level of syntax and semantics of the modeling language.
- The advantages of this approach are:
  - It allows the user to focus on the problem and the solution, rather than on the details of the representation and the implementation of the system.
  - It facilitates the reuse and adaptation of existing knowledge models, since they can be easily understood and modified by the user.
  - It enhances the transparency and trustworthiness of the system, since the user can see and verify the rationale and the assumptions behind the system's advice.
- The challenges of this approach are:
  - It requires a high level of domain expertise and modeling skills from the user, since they have to be able to express and manipulate complex and abstract concepts and relations.
  - It demands a sophisticated and flexible user interface that can support the user in creating, editing, querying and visualizing the knowledge models in a natural and intuitive way.
  - It involves a trade-off between the expressiveness and the efficiency of the system, since the more expressive the modeling language is, the more difficult it is to implement and reason with it.



# A language for implementing very large 'integral approach' systems

- An integral approach system is a system that seeks to integrate all human knowledge disciplines into a single framework that can account for both objective and subjective aspects of reality .
- An integral approach system can be seen as a sort of operating system for reality, that can run any software in life, such as business, work, play, or relationships.
- An integral approach system can enable more human-centric, creative, and effective solutions to complex problems, by combining subjective methods and tools with existing objective methods and tools .
- A language for implementing very large integral approach systems should have the following features:
  - It should be content-free, meaning that it does not impose any specific content or perspective on the system, but rather provides a framework for integrating different contents and perspectives.
  - It should be scalable, meaning that it can handle very large and complex systems, with multiple levels, domains, and dimensions of reality.
  - It should be expressive, meaning that it can capture the richness and diversity of human experience, knowledge, and values, as well as the technical and functional aspects of the system .
  - It should be interoperable, meaning that it can communicate and collaborate with other languages, systems, and tools, both objective and subjective .
  - It should be adaptive, meaning that it can evolve and learn from feedback and new information, and adjust to changing contexts and needs .
- Some examples of languages that could be used for implementing very large integral approach systems are:
  - AQAL, which stands for All Quadrants, All Levels, All Lines, All States, and All Types, is a language developed by Ken Wilber, the founder of Integral Theory, that maps out the basic elements and dimensions of reality, and how they interact and influence each other.
  - UML, which stands for Unified Modeling Language, is a language for specifying, visualizing, constructing, and documenting the artifacts of software systems, as well as for business modeling and other non-software systems.
  - HSI, which stands for Human Systems Integration, is a language for integrating human considerations within and across all system elements, such as human performance, health and safety, personnel, training, and organizational factors .



# The CYC project

- The CYC project is a long-term artificial intelligence project that aims to assemble a comprehensive ontology and knowledge base that spans the basic concepts and rules about how the world works.
- The project began in 1984 under the auspices of the Microelectronics and Computer Technology Corporation, a consortium of American computer, semiconductor, and electronics manufacturers, to advance work on artificial intelligence.
- In 1995, Douglas Lenat, the CYC project director, spun off the project as Cycorp, Inc., based in Austin, Texas.
- The project derives its name from en**cyc**lopedia, as it intends to encode part of the knowledge in the Encyclopaedia Britannica into a very large knowledge base (VLKB).
- The project also incorporates inference procedures into the system in order to answer questions and deduce results according to user requirements.
- The project hopes to capture common sense knowledge, which is the implicit knowledge that other AI platforms may take for granted.
- The project uses a formal language called CycL to represent the knowledge and the rules in the knowledge base.
- The project has around 600,000 concepts and 10,000,000 assertions as of 2019.
- In 2002, a subset of the knowledge base and functionality was released to the public under the OpenCyc project, which has around 240,000 concepts and 2,000,000 assertions as of 2012.
- The project aims to enable AI applications to reason like humans and to support a wide range of domains and tasks.



# Other projects based on a 'conceptual representation' approach for the notes of the Unit 4 - Advanced Knowledge-Based Systems in the subject of INTELLIGENT DATABASE SYSTEM

- A conceptual representation is a high-level view of data that identifies the main entities, relationships, and attributes without specifying the details of implementation or storage  .
- A conceptual representation is useful for defining the scope and requirements of a database system, as well as for communicating with different stakeholders and users .
- A conceptual representation can be expressed in various ways, such as diagrams, graphs, or natural language   .
- Some examples of projects that use a conceptual representation approach for intelligent database systems are:

  - **Conceptual Graphs**: A system of logic based on the existential graphs of Charles Sanders Peirce and the semantic networks of artificial intelligence. They express meaning in a form that is logically precise, humanly readable, and computationally tractable. Conceptual graphs can be used for knowledge representation, reasoning, natural language processing, information retrieval, and database design.
  - **Intelligent Database Systems**: A research area that aims to integrate artificial intelligence techniques with database systems to enhance their functionality, performance, and usability. Intelligent database systems can provide features such as data mining, knowledge discovery, query optimization, semantic query processing, natural language interfaces, and adaptive learning. Intelligent database systems can use conceptual representations to model the domain knowledge, user preferences, and data semantics.
  - **Conceptual Data Modeling**: A process of creating a conceptual representation of a database system that captures the essential aspects of the data and their relationships. Conceptual data modeling can be done using various methods and notations, such as entity-relationship diagrams, object-oriented models, or UML diagrams  . Conceptual data modeling can help to ensure the validity, completeness, and consistency of the database design, as well as to facilitate the communication and documentation of the system requirements  .



# Lexical approaches to the construction of large KBs

- A lexical approach is a method of building knowledge bases (KBs) that relies on the use of natural language definitions to represent concepts and relations in a domain.
- A lexical approach has several advantages, such as:
  - It can leverage existing linguistic resources, such as dictionaries, ontologies, and corpora, to acquire and validate knowledge.
  - It can facilitate communication and collaboration among domain experts, knowledge engineers, and end-users, by using a common and intuitive language.
  - It can support reasoning and inference based on the logical structure and semantics of definitions.
- A lexical approach also has some challenges, such as:
  - It requires a formal and consistent way of writing and parsing definitions, to avoid ambiguity and inconsistency.
  - It needs to handle the complexity and variability of natural language, such as synonyms, polysemy, anaphora, and idioms.
  - It has to deal with the quality and completeness of the source data, and the errors and gaps that may arise during the KB construction process.
- Some examples of lexical approaches to the construction of large KBs are:
  - A definitional approach, which uses a logic-based language to express definitions of concepts and relations, and a set of inference rules to derive new knowledge from existing definitions .
  - A lexical extraction approach, which uses natural language processing techniques to extract definitions and facts from textual sources, such as Wikipedia, and map them to a predefined ontology.
  - A lexical alignment approach, which uses lexical and semantic similarity measures to align concepts and relations from different sources, such as WordNet and DBpedia, and merge them into a unified KB.



## Unit 5 - Applications in IDBS

- IDBS stands for **Intelligent Database Systems**, which are systems that combine database and artificial intelligence techniques to provide intelligent data management and analysis.
- Some of the applications of IDBS are:

  - **Data mining**: The process of discovering useful patterns, trends, and associations from large and complex data sets. Data mining can be used for tasks such as customer segmentation, fraud detection, market basket analysis, and recommender systems.
  - **Data warehousing**: The process of integrating data from multiple sources and organizing them into a unified and consistent format for analysis and reporting. Data warehousing can be used for tasks such as business intelligence, decision support, and performance management.
  - **Data cleaning**: The process of detecting and correcting errors, inconsistencies, and missing values in data. Data cleaning can be used for tasks such as data integration, data quality assessment, and data preparation for analysis.
  - **Data visualization**: The process of presenting data in graphical or interactive forms to facilitate understanding and communication. Data visualization can be used for tasks such as exploratory data analysis, data storytelling, and dashboard design.
  - **Data security**: The process of protecting data from unauthorized access, modification, or disclosure. Data security can be used for tasks such as encryption, authentication, authorization, and auditing.



# Introduction for the notes of the Unit 5 - Applications in IDBS in the subject of INTELLIGENT DATABASE SYSTEM

- In this unit, we will learn about some of the applications of intelligent database systems (IDBS) in various domains and scenarios.
- IDBS are database systems that integrate artificial intelligence techniques such as machine learning, natural language processing, knowledge representation and reasoning, and expert systems to provide intelligent functionalities and services to the users and applications.
- IDBS can be used for various purposes, such as:
  - Data analysis and mining: IDBS can discover patterns, trends, and insights from large and complex data sets, and provide recommendations, predictions, and explanations to the users.
  - Data integration and cleaning: IDBS can integrate data from multiple heterogeneous sources, resolve conflicts and inconsistencies, and improve the quality and reliability of the data.
  - Data security and privacy: IDBS can protect the data from unauthorized access, modification, or disclosure, and enforce policies and regulations for data sharing and usage.
  - Data management and optimization: IDBS can manage the data efficiently and effectively, and optimize the performance, scalability, and availability of the database system.
- Some of the domains and scenarios where IDBS can be applied are:
  - E-commerce and recommender systems: IDBS can provide personalized and relevant recommendations to the customers based on their preferences, behavior, and feedback, and increase the customer satisfaction and loyalty.
  - Health care and bioinformatics: IDBS can support the diagnosis, treatment, and prevention of diseases, and facilitate the analysis and interpretation of biomedical data and knowledge.
  - Education and learning: IDBS can provide adaptive and interactive learning environments, and tailor the content and feedback to the learners' needs, goals, and progress.
  - Social media and sentiment analysis: IDBS can analyze the opinions, emotions, and attitudes of the users from their posts, comments, and reviews, and provide useful insights for marketing, customer service, and decision making.
  - Smart cities and IoT: IDBS can enable the integration and coordination of various devices, sensors, and services in the urban environment, and provide intelligent solutions for transportation, energy, security, and sustainability.



# Temporal databases

- A temporal database is a database that has certain features that support time-sensitive status for entries .
- A temporal database can store data relating to past, present and future time instances.
- A temporal database can also track the history of data changes and support queries based on time or time intervals .
- A temporal database can be classified into different types based on the temporal aspects it supports:
  - Uni-temporal: A database that supports only one temporal aspect, such as valid time or transaction time.
  - Bi-temporal: A database that supports both valid time and transaction time, where valid time is the time period during or event time at which a fact is true in the real world, and transaction time is the time period during which a fact is stored in the database .
  - Tri-temporal: A database that supports valid time, transaction time and decision time, where decision time is the time at which a decision is made about a fact.
- A temporal database can offer several benefits, such as :
  - Data auditing: A temporal database can provide a complete audit trail of data changes and allow users to track who, when and what changed in the data.
  - Data analysis: A temporal database can enable users to perform historical analysis and trend analysis on data and compare data across different time periods.
  - Data recovery: A temporal database can facilitate data recovery and restoration by allowing users to access previous versions of data and revert to them if needed.
  - Data consistency: A temporal database can ensure data consistency and integrity by preventing data anomalies and conflicts that may arise from concurrent updates or deletions.



# Basic concepts for the notes of the Unit 5 - Applications in IDBS in the subject of INTELLIGENT DATABASE SYSTEM

- An **intelligent database system** (IDBS) is a system that manages **information** (rather than data) in a way that appears natural and informative for users and that goes beyond simple record keeping.
- An IDBS consists of three levels of intelligence: **high level tools**, **user interface** and **database engine**.
- The **high level tools** manage data quality and automatically discover relevant patterns in the data with a process called **data mining**.
- The **user interface** provides natural language processing, speech recognition, graphical visualization and multimedia capabilities to facilitate user interaction with the system.
- The **database engine** supports advanced data models, such as object-oriented, semantic and deductive, and provides intelligent query processing and optimization techniques.
- Some of the applications of IDBS are:
  - **Business intelligence**: IDBS can help businesses analyze their data and gain insights for decision making, planning and forecasting.
  - **Knowledge management**: IDBS can help organizations capture, store, share and reuse their knowledge assets, such as documents, reports, best practices and lessons learned.
  - **Personalization**: IDBS can help customize the content and services delivered to users based on their preferences, behavior and feedback.
  - **Recommendation systems**: IDBS can help suggest relevant items or actions to users based on their context, needs and interests.
  - **Fraud detection**: IDBS can help detect and prevent fraudulent activities, such as credit card fraud, insurance fraud and identity theft, by analyzing patterns and anomalies in the data.
  - **Healthcare**: IDBS can help improve the quality and efficiency of healthcare services, such as diagnosis, treatment, prevention and research, by integrating and analyzing various sources of medical data.



# Temporal Data Models

- Temporal data models are data models that capture the changes of data over time, and allow querying and manipulating data based on temporal aspects.
- Temporal data models exist at three abstraction levels:
  - The conceptual level, in which the data models are generally extensions of the Entity-Relationship Model (ERM).
  - The logical level, in which the data models are generally extensions of the relational data model (RDM) or of an object-oriented data model (OODM).
  - The physical level, in which the data model details how the data are to be stored.
- Temporal data models can be classified based on the type of time they capture :
  - Valid time, which is the time when the data is valid with respect to the real world (also called business time).
  - Transaction time, which is the time when the data is recorded in the database (also called system time).
  - Decision time, which is the time when a decision is made based on the data (also called application time).
- Temporal data models can also be classified based on the number of time dimensions they capture :
  - Uni-temporal, which capture only one type of time (either valid time or transaction time).
  - Bi-temporal, which capture both valid time and transaction time.
  - Tri-temporal, which capture valid time, transaction time and decision time.
- Temporal data models have several advantages over conventional data models:
  - They can represent the history and evolution of data, and support temporal queries and analysis.
  - They can handle data inconsistencies and uncertainties, and support data correction and auditing.
  - They can support temporal integrity constraints and temporal normalization.
- Temporal data models also have some challenges and limitations:
  - They require more storage space and processing time than conventional data models.
  - They need to deal with complex temporal semantics and operations, and temporal granularity and formats.
  - They need to cope with temporal data quality and validity issues, and temporal data integration and interoperability problems.



# Temporal Query Languages

- A temporal query language is a database query language that offers some form of built-in support for the querying and modification of time-referenced data, as well as enabling the specification of assertions and constraints on such data.
- Temporal query languages can be used to manipulate data that has temporal aspects, such as historical records, events, transactions, sensor readings, or temporal blockchains.
- Temporal query languages can be classified into two main categories: calculus-based and algebra-based.
  - Calculus-based temporal query languages use logical formulas to express queries over temporal data. Examples of calculus-based temporal query languages are first-order temporal logic (FOTL), temporal relational calculus (TRC), and temporal SQL (TSQL).
  - Algebra-based temporal query languages use operators and expressions to manipulate temporal data. Examples of algebra-based temporal query languages are temporal relational algebra (TRA), temporal relational model (TRM), and temporal stream query language (TSQ).
- Temporal query languages can also be distinguished by the type of temporal data they support: valid-time, transaction-time, or bitemporal.
  - Valid-time temporal query languages deal with data that is valid or true at some point or interval in the real world. For example, a valid-time query can ask for the salary of an employee during a certain period of employment.
  - Transaction-time temporal query languages deal with data that is recorded or stored at some point or interval in the database system. For example, a transaction-time query can ask for the history of changes made to a record in the database.
  - Bitemporal temporal query languages deal with data that has both valid-time and transaction-time dimensions. For example, a bitemporal query can ask for the salary of an employee as it was recorded at a certain point in the database, and as it was valid at a certain point in the real world.
- Temporal query languages can provide various features and functionalities, such as temporal selection, projection, join, aggregation, grouping, ordering, negation, quantification, and temporal operators.
  - Temporal selection allows filtering temporal data based on some condition involving time attributes or values.
  - Temporal projection allows extracting some attributes or values from temporal data, possibly changing their temporal granularity or representation.
  - Temporal join allows combining temporal data from different sources or relations, based on some temporal condition or alignment.
  - Temporal aggregation allows summarizing temporal data by applying some function or operation over a set of temporal values or intervals.
  - Temporal grouping allows partitioning temporal data into subsets based on some temporal criterion or attribute.
  - Temporal ordering allows sorting temporal data according to some temporal criterion or attribute.
  - Temporal negation allows expressing queries that involve the absence or non-existence of temporal data or events.
  - Temporal quantification allows expressing queries that involve the existence or frequency of temporal data or events over some temporal domain or scope.
  - Temporal operators allow manipulating temporal data or intervals by applying some temporal logic or algebra, such as temporal intersection, union, difference, complement, or temporal modalities.
- Temporal query languages can be implemented using various approaches, such as extending existing query languages (e.g., SQL), developing new query languages (e.g., Trill), or using temporal annotations or metadata (e.g., RDF) .
  - Extending existing query languages involves adding temporal features or constructs to a standard or widely used query language, such as SQL. This approach can benefit from the familiarity and compatibility of the existing query language, but may also face challenges in terms of syntax, semantics, or performance.
  - Developing new query languages involves creating a query language from scratch, specifically designed for temporal data. This approach can offer more flexibility and expressiveness for temporal queries, but may also require more effort and expertise to design, implement, and use.
  - Using temporal annotations or metadata involves adding temporal information to the data or the query, using some standard or custom format, such as RDF. This approach can enable temporal queries over heterogeneous or distributed data sources, but may also introduce complexity or ambiguity in the temporal representation or interpretation.



# Ontologies for the notes of the Unit 5 - Applications in IDBS in the subject of INTELLIGENT DATABASE SYSTEM

- An ontology is a formal system for modeling concepts and their relationships in a given domain.
- Ontologies are useful for expressing data in which the relationships between objects are important, unlike relational database systems, which are based on interconnected tables.
- Ontologies store the information in a graph database, or triplestore, which consists of triples of the form (subject, predicate, object), where each element can be a resource (identified by a URI) or a literal (a value).
- Ontologies can be used for various applications in intelligent database systems, such as:
  - Ontology-based visual or interactive query formulation systems, which use visual representations to express data requests based on terms from the ontology.
  - Ontology database systems, which take a semantic web ontology as input, and generate a database schema and populate the tables based on it. Users can pose SQL queries to the system declaratively, and get answers that incorporate the term hierarchy or other logical features of the ontology.
  - Ontology-based data integration, which uses ontologies to map and merge data from heterogeneous and distributed sources.
  - Ontology-based knowledge management, which uses ontologies to organize and retrieve knowledge from various sources, such as documents, databases, web pages, etc..
  - Ontology-based data mining and machine learning, which use ontologies to enhance the data analysis and discovery process, such as by providing background knowledge, semantic similarity measures, feature selection, etc..
- Ontologies have a lifecycle that consists of several phases, such as design, development, evaluation, maintenance, and evolution.
- Ontologies can be compared and contrasted with databases in terms of their lifecycle phases, such as:
  - Design: ontologies require more conceptual analysis and formalization than databases, which are more focused on data modeling and normalization.
  - Development: ontologies use semantic languages, such as RDF, OWL, etc., to represent the concepts and relationships, while databases use data definition languages, such as SQL, to create the tables and constraints.
  - Evaluation: ontologies use criteria, such as consistency, completeness, correctness, etc., to assess the quality of the ontology, while databases use criteria, such as performance, scalability, security, etc., to assess the quality of the database.
  - Maintenance: ontologies require more frequent updates and revisions than databases, due to the dynamic and evolving nature of the domain knowledge, while databases are more stable and consistent.
  - Evolution: ontologies use techniques, such as versioning, modularization, alignment, etc., to cope with the changes in the domain and the requirements, while databases use techniques, such as migration, backup, recovery, etc., to cope with the changes in the data and the schema.



# Ontology Theoretical Foundations

Ontology is the philosophical study of being, as well as related concepts such as existence, becoming, and reality. Ontology addresses questions like how entities are grouped into categories and which of these entities exist on the most fundamental level.

In computer science, ontology is a formal representation of the concepts and relations in a domain of interest, such as knowledge engineering, artificial intelligence, natural language processing, e-commerce, and intelligent information integration. Ontology provides a common vocabulary and a shared understanding of the domain for humans and machines.

Ontology can be developed from different perspectives and levels of generality. One way to classify ontologies is based on their scope and purpose:

- **Domain ontologies** capture the specific knowledge and terminology of a particular field or area of interest, such as medicine, biology, geography, etc. Domain ontologies are usually developed for a specific application or community of users.
- **Foundational ontologies** provide a high-level categorization of the kinds of things that exist in the world, such as object, event, process, quality, relation, etc. Foundational ontologies span across many fields and model the very basic and general concepts and relations that make up the world . Foundational ontologies are usually developed for reuse and interoperability among different domain ontologies and applications.
- **Meta-ontologies** define the formal language and the logical framework for building and reasoning with ontologies. Meta-ontologies specify the syntax and semantics of the ontology language, such as RDF, OWL, etc. Meta-ontologies are usually developed for standardization and compatibility among different ontology languages and tools.

Some of the benefits of using ontologies in computer science are:

- Ontologies can facilitate knowledge sharing and reuse among different agents, systems, and applications.
- Ontologies can enable semantic interoperability and integration of heterogeneous and distributed data sources.
- Ontologies can support natural language processing and understanding by providing a common conceptualization of the domain.
- Ontologies can enhance information retrieval and query answering by enabling semantic search and reasoning over the data.
- Ontologies can enable intelligent decision making and problem solving by providing a formal and explicit representation of the domain knowledge and the goals.

Some of the challenges of developing and using ontologies in computer science are:

- Ontologies can be difficult and time-consuming to create and maintain, especially for large and complex domains.
- Ontologies can be subjective and inconsistent, depending on the perspective and purpose of the ontology developers and users.
- Ontologies can be incomplete and inaccurate, due to the limitations of the available data and the ontology language.
- Ontologies can be incompatible and incomparable, due to the lack of common standards and methods for ontology evaluation and alignment.



# Environments for building ontologies

- An ontology is a formal representation of the concepts and relationships in a domain of interest.
- Ontology engineering is the process of developing and maintaining ontologies.
- Ontology engineering environments are tools that support the ontology engineering process, such as editing, browsing, querying, reasoning, and sharing ontologies.
- There are different types of ontology engineering environments, depending on the purpose, scope, and methodology of ontology development.
- Some examples of ontology engineering environments are:

  - **OntoEdit**: A graphical ontology editor that supports multiple languages, formats, and reasoning engines. It also provides features for ontology learning, merging, and alignment.
  - **WebODE**: A web-based ontology development platform that allows collaborative ontology editing, reuse, and integration. It also offers services for ontology validation, documentation, and publication.
  - **Protege**: An open-source ontology editor and framework that supports various ontology languages, formats, and plugins. It also enables ontology visualization, annotation, and analysis .
  - **Hozo**: An ontology engineering environment that focuses on the role and relationship concepts in ontologies. It also provides tools for ontology construction, refinement, and application .



# Structured, semi-structured and unstructured data

- Structured data is data with a high degree of organization, typically stored in a spreadsheet-like manner. It has a predefined schema, format and structure. It can be easily queried, analyzed and manipulated using relational database management systems (RDBMS) or other data table forms. Examples of structured data are customer records, sales transactions, product inventory, etc.    
- Semi-structured data is data with some degree of organization, but not as rigid as structured data. It does not follow the tabular data structure models associated with relational databases, but it has some elements of metadata, tags or markers that separate the data fields. It can be stored in non-relational database management systems (NoSQL) or other data formats such as JSON, CSV, XML, etc. Examples of semi-structured data are web logs, social media posts, email messages, etc.    
- Unstructured data is data with no predefined organizational form and no specific format. It is a collection of many varied data types that are stored in their native formats. It is not easily searchable, analyzable or manipulable using traditional data tools or methods. It requires natural language processing (NLP), text mining, image recognition or other advanced techniques to extract meaningful information from it. Examples of unstructured data are text documents, audio files, video files, images, etc.      

: https://www.indeed.com/career-advice/career-development/structured-vs-unstructured-vs-semi-structured-data
: https://www.michael-gramlich.com/what-is-structured-semi-structured-and-unstructured-data/
: https://k21academy.com/microsoft-azure/dp-900/structured-data-vs-unstructured-data-vs-semi-structured-data/
: https://www.geeksforgeeks.org/difference-between-structured-semi-structured-and-unstructured-data/
: https://www.ibm.com/cloud/blog/structured-vs-unstructured-data
: https://www.forbes.com/sites/bernardmarr/2019/10/18/whats-the-difference-between-structured-semi-structured-and-unstructured-data/



# Multimedia Database

A multimedia database is a database that hosts one or more multimedia data types, such as text, images, audio, video, and animation. Multimedia data types are broadly categorized into three classes:

- Static media: time-independent data, such as image and graphic object.
- Dynamic media: time-dependent data, such as audio, video, and animation.
- Dimensional media: data that have spatial or temporal dimensions, such as 3D models and virtual reality.

A multimedia database should address the following requirements:

- Integration: data items do not need to be duplicated for different programs or applications.
- Data independence: separate the database structure and content from the application logic and presentation.
- Consistency: ensure the validity and integrity of the data and the relationships among them.
- Security: protect the data from unauthorized access, modification, or deletion.
- Efficiency: provide fast and reliable access, storage, and manipulation of the data.
- Functionality: support various operations and queries on the data, such as retrieval, update, insertion, deletion, and transformation.

Some of the applications of multimedia databases are:

- Documents and records management: industries and businesses that keep detailed records and variety of documents, such as legal, medical, and financial sectors.
- Knowledge dissemination: multimedia databases are effective tools for knowledge dissemination, such as providing online courses, tutorials, and lectures.
- Education and training: multimedia databases can enhance the learning and teaching experience, such as using interactive and immersive media, simulations, and games.
- Entertainment and art: multimedia databases can support various forms of entertainment and art, such as movies, music, games, and digital libraries.
- Communication and collaboration: multimedia databases can facilitate communication and collaboration among people, such as using video conferencing, social media, and online communities.



# Semi-structured data

- Semi-structured data is a form of structured data that does not obey the tabular structure of data models associated with relational databases or other forms of data tables, but nonetheless contains tags or other markers to separate semantic elements and enforce hierarchies of records and fields within the data.
- Semi-structured data combines features of both structured data and unstructured data. Structured data often refers to data that is quantitative, or numerical. It can also include data that has an organizational structure understandable to both machines and humans. Unstructured data often refers to data that is qualitative, or textual. It can also include data that has no predefined structure or format.
- Examples of semi-structured data are:
  - Email: Email is a type of semi-structured data that many employees and businesses use regularly. The written content of the email is unstructured, but the email header, sender, recipient, date, and subject are structured.
  - HTML: Webpages you can create through Hypertext Markup Language (HTML) use semi-structured data. HTML refers to a set of rules that define how to display text, images, and other elements on a webpage. HTML tags are structured, but the content within the tags is unstructured.
  - Online images and videos: Online images and videos are another example of semi-structured data. The image or video file itself is unstructured, but the metadata associated with it, such as the file name, size, format, resolution, and tags, are structured.
  - JSON: JSON (JavaScript Object Notation) is a popular format for exchanging data on the web. JSON data is semi-structured, as it uses key-value pairs to represent data objects. The keys are structured, but the values can be any data type, including arrays, objects, strings, numbers, booleans, or null.
  - XML: XML (Extensible Markup Language) is another common format for exchanging data on the web. XML data is semi-structured, as it uses tags and attributes to define data elements. The tags and attributes are structured, but the content within the tags can be any data type, including text, numbers, images, or other XML elements.
- Benefits of semi-structured data are:
  - Flexibility: Semi-structured data allows for more flexibility in data modeling and representation, as it does not require a fixed or rigid schema. It can accommodate changes in data structure and format without affecting the data quality or integrity.
  - Scalability: Semi-structured data can scale easily, as it can handle large volumes and varieties of data without compromising performance or efficiency. It can also leverage distributed computing and storage systems, such as cloud platforms, to process and store data in parallel.
  - Interoperability: Semi-structured data can interoperate with different data sources and formats, as it can be easily converted or transformed into other data types. It can also integrate with various applications and tools, such as data analysis, visualization, and machine learning.



# Mediators for the notes of the Unit 5 - Applications in IDBS in the subject of INTELLIGENT DATABASE SYSTEM

- A mediator is a software component that provides a uniform interface to heterogeneous data sources, such as databases, legacy systems, web services, etc. 
- A mediator can perform various tasks, such as data integration, query processing, data transformation, data analysis, etc. 
- A mediator can be classified into two types: wrapper-based and translator-based. 
  - A wrapper-based mediator uses wrappers to access the data sources and translate their data formats and protocols into a common representation. 
  - A translator-based mediator uses a common data model and a common query language to access the data sources and translate their queries and results. 
- A mediator can be implemented using different techniques, such as rule-based, object-oriented, logic-based, etc. 
  - A rule-based mediator uses production rules to specify the data integration and query processing logic. 
  - An object-oriented mediator uses objects and classes to model the data sources and the mediator schema. 
  - A logic-based mediator uses logic programming and deductive databases to represent and reason about the data sources and the mediator schema. 
- A mediator can be applied to various domains, such as artificial intelligence, robotics, e-commerce, etc.  
  - An artificial intelligence mediator can use ontologies and knowledge bases to integrate and analyze data from different sources. 
  - A robotics mediator can use sensors and actuators to access and control data from different devices. 
  - An e-commerce mediator can use web services and XML to integrate and process data from different vendors and customers.



Hello, I am Sydney, your AI assistant. I can help you with writing content in markdown format. Here is the content I have generated for the topic of ### Motivation for the notes of the Unit 5 - Applications in IDBS in the subject of INTELLIGENT DATABASE SYSTEM

# Motivation for the notes of the Unit 5 - Applications in IDBS

- Intelligent database systems (IDBS) are database systems that integrate artificial intelligence techniques such as machine learning, natural language processing, knowledge representation and reasoning, and data mining to provide intelligent functionalities and services to the users and applications.
- IDBS have many potential applications in various domains such as e-commerce, health care, education, social media, bioinformatics, and security.
- In this unit, we will explore some of the applications of IDBS and how they can benefit from the intelligent features of IDBS such as query processing, data analysis, data integration, data quality, data security, and data visualization.
- Some of the applications of IDBS that we will cover in this unit are:

  - Recommender systems: IDBS can provide personalized and relevant recommendations to the users based on their preferences, behavior, and context. IDBS can also use collaborative filtering, content-based filtering, and hybrid filtering techniques to generate recommendations from large and heterogeneous data sources.
  - Sentiment analysis: IDBS can analyze the opinions, emotions, and attitudes of the users expressed in natural language texts such as reviews, comments, tweets, and blogs. IDBS can use natural language processing, machine learning, and sentiment lexicons to perform sentiment analysis and provide insights and feedback to the users and applications.
  - Fraud detection: IDBS can detect and prevent fraudulent activities and transactions in domains such as banking, insurance, e-commerce, and social media. IDBS can use data mining, anomaly detection, classification, and clustering techniques to identify fraud patterns and anomalies from large and complex data sets.
  - Information extraction: IDBS can extract structured and relevant information from unstructured and semi-structured data sources such as web pages, documents, emails, and images. IDBS can use natural language processing, machine learning, and knowledge representation and reasoning techniques to perform information extraction and provide structured and meaningful data to the users and applications.
  - Data visualization: IDBS can provide interactive and intuitive visualization of the data and the results of the data analysis and query processing. IDBS can use data visualization techniques such as charts, graphs, maps, and dashboards to present the data and the insights in an understandable and appealing way to the users and applications.

- The notes of this unit will provide an overview of these applications of IDBS and the techniques and challenges involved in developing and using them. The notes will also provide examples and case studies of some of the existing and emerging IDBS applications in various domains. The notes will help the students to understand the concepts and principles of IDBS and their applications and to apply them in their own projects and research.



# Architecture for the notes of the Unit 5 - Applications in IDBS in the subject of INTELLIGENT DATABASE SYSTEM

- An intelligent database system (IDBS) is a full-text database with artificial intelligence components that interact with users to ensure that users are supplied all relevant information.
- An IDBS consists of three levels of intelligence: high level tools, the user interface and the database engine.
- The high level tools manage data quality and automatically discover relevant patterns in the data with a process called data mining.
- The user interface provides natural language processing, speech recognition, graphical visualization and intelligent agents to facilitate user interaction with the system.
- The database engine supports advanced data models, query optimization, concurrency control, recovery and security.
- Some of the applications of IDBS are:
  - Banking: IDBS can manage thousands of transactions through banks daily and provide online banking services to customers.
  - Education: IDBS can conduct online examinations, store and analyze student records, and provide personalized learning recommendations.
  - Business: IDBS can integrate data from various sources, such as enterprise systems, web services, and social media, and provide business intelligence and analytics to support decision making.
  - Healthcare: IDBS can store and process medical records, images, and reports, and provide diagnosis, treatment, and prevention suggestions based on data mining and machine learning.
  - Science: IDBS can handle large-scale and complex data sets, such as genomic, meteorological, and astronomical data, and provide scientific discovery and innovation based on data analysis and visualization.



# Application of mediators to heterogeneous systems for the notes of the Unit 5 - Applications in IDBS in the subject of INTELLIGENT DATABASE SYSTEM

- A mediator is a software component that provides a uniform interface to access heterogeneous data sources, such as relational databases, XML files, web services, etc.
- A mediator can perform various tasks, such as data integration, data transformation, data filtering, data analysis, and query processing, to provide relevant and consistent information to the users or applications.
- A mediator can also use intelligent techniques, such as machine learning, natural language processing, semantic web, etc., to enhance the quality and usability of the data.
- A mediator can be classified into two types: wrapper-mediator and mediator-only.
  - A wrapper-mediator consists of two layers: a wrapper layer and a mediator layer. The wrapper layer is responsible for translating the queries and data between the mediator and the data sources. The mediator layer is responsible for integrating and processing the data from the wrappers.
  - A mediator-only consists of a single layer that directly interacts with the data sources. It does not require any wrappers, but it may need to use some standard protocols or formats to communicate with the data sources.
- A mediator can be applied to various domains and scenarios, such as:
  - Bioinformatics: A mediator can integrate and analyze heterogeneous biological data, such as protein annotation, protein-protein interaction, protein structure, and biomedical citation, to support scientific research and discovery.
  - E-commerce: A mediator can integrate and compare heterogeneous product data, such as price, features, reviews, and availability, from different online vendors, to support online shopping and decision making.
  - Intelligence: A mediator can monitor and detect changes in heterogeneous data sources, such as news, social media, reports, and sensors, to support situation awareness and plan execution.
  - Education: A mediator can integrate and personalize heterogeneous educational data, such as courses, materials, assessments, and feedback, from different online platforms, to support learning and teaching.



Hello, I am Sydney, your AI assistant. I can help you with your notes for the Unit 5 - Applications in IDBS in the subject of INTELLIGENT DATABASE SYSTEM. Here are some proposals for the notes:

# Unit 5 - Applications in IDBS

- An intelligent database system (IDBS) is a database system that integrates artificial intelligence techniques, such as knowledge representation, reasoning, learning, and natural language processing, with database management functions, such as data storage, retrieval, manipulation, and integrity checking.
- IDBS can be applied to various domains, such as decision support, data mining, information retrieval, expert systems, natural language interfaces, multimedia databases, and spatial databases.
- Some examples of applications in IDBS are:

  - **Decision support systems (DSS)**: These are systems that help users make decisions based on data analysis, modeling, and simulation. IDBS can enhance DSS by providing intelligent query processing, explanation generation, and knowledge discovery. For example, an IDBS can help a manager analyze the sales data of a company and suggest optimal marketing strategies based on the customer preferences and behavior patterns.
  - **Data mining**: This is the process of discovering useful patterns and knowledge from large and complex data sets. IDBS can facilitate data mining by providing intelligent data preprocessing, data integration, data transformation, data mining algorithms, and data visualization. For example, an IDBS can help a researcher find the correlations and associations among the genes and diseases from a biomedical database.
  - **Information retrieval**: This is the process of finding relevant information from a large and unstructured collection of documents. IDBS can improve information retrieval by providing intelligent document indexing, document classification, document clustering, document ranking, and natural language processing. For example, an IDBS can help a user find the most relevant and trustworthy web pages for a given query.
  - **Expert systems**: These are systems that emulate the reasoning and problem-solving skills of human experts in a specific domain. IDBS can support expert systems by providing intelligent knowledge representation, knowledge acquisition, knowledge inference, and knowledge explanation. For example, an IDBS can help a doctor diagnose a patient's condition and prescribe the appropriate treatment based on the medical knowledge and rules stored in the database.
  - **Natural language interfaces**: These are interfaces that allow users to interact with a database system using natural language, such as English or Hindi. IDBS can enable natural language interfaces by providing intelligent natural language understanding, natural language generation, and natural language dialogue. For example, an IDBS can help a user ask and answer questions about the data in the database using natural language.
  - **Multimedia databases**: These are databases that store and manage various types of multimedia data, such as images, audio, video, and text. IDBS can enhance multimedia databases by providing intelligent multimedia data modeling, multimedia data retrieval, multimedia data analysis, and multimedia data presentation. For example, an IDBS can help a user find and view the most relevant and interesting images or videos for a given topic or query.
  - **Spatial databases**: These are databases that store and manage spatial data, such as geographic locations, maps, and trajectories. IDBS can improve spatial databases by providing intelligent spatial data modeling, spatial data retrieval, spatial data analysis, and spatial data visualization. For example, an IDBS can help a user find and navigate the shortest or safest route from one location to another using the spatial data in the database.



# Multi-Agent Systems for the Notes of the Unit 5 - Applications in IDBS in the Subject of Intelligent Database Systems

- A multi-agent system (MAS) is a computerized system composed of multiple interacting intelligent agents that can solve problems that are difficult or impossible for an individual agent or a monolithic system to solve.
- Multi-agent systems are a subfield of distributed artificial intelligence (DAI) that studies how a group of intelligent entities, called agents, can interact by cooperation, coexistence or competition.
- Multi-agent systems can be applied to various domains, such as online trading, disaster response, target surveillance and social structure modelling.
- Some of the benefits of using multi-agent systems are:
  - They can handle complex and dynamic environments that require distributed control and coordination.
  - They can exploit the heterogeneity and autonomy of the agents to achieve higher performance and robustness.
  - They can facilitate the modularity, scalability and reusability of the system design and implementation.
- Some of the challenges of using multi-agent systems are:
  - They need to deal with the issues of communication, negotiation, cooperation and conflict resolution among the agents.
  - They need to ensure the consistency, reliability and security of the system and the data.
  - They need to cope with the uncertainty, incompleteness and inconsistency of the information and the actions of the agents.
- Some of the applications of multi-agent systems in intelligent database systems are:
  - Agent-based intelligent decision support systems (ABIDSS) that use agents to provide personalized and adaptive assistance to the users in decision making processes.
  - Agent-based data mining and knowledge discovery systems that use agents to perform distributed and collaborative data analysis and knowledge extraction.
  - Agent-based data integration and interoperability systems that use agents to facilitate the access and exchange of data and information among heterogeneous and distributed sources.
  - Agent-based data security and privacy systems that use agents to protect the data and the users from unauthorized access and malicious attacks.



# Main issues in designing a multi-agent system

A multi-agent system (MAS) is a computerized system composed of multiple interacting intelligent agents that can solve problems that are difficult or impossible for an individual agent or a monolithic system to solve. 

Designing a multi-agent system involves several issues that need to be addressed, such as:

- **How to specify the system requirements and goals?** A MAS should have a clear and consistent specification of what the system is supposed to do and why. This can be done by using goal hierarchies and role models that capture the functional and non-functional requirements of the system. 
- **How to model the agents and their interactions?** A MAS should have a well-defined structure and behavior of the agents and their communication protocols. This can be done by using agent-class, communication and deployment diagrams that describe the properties, capabilities, services, and relationships of the agents. 
- **How to ensure the system is resilient and adaptable?** A MAS should be able to cope with uncertainties, failures, and changes in the environment and the goals. This can be done by using quantitative resilience measures and design principles that enhance the robustness, flexibility, and efficiency of the system. 
- **How to evaluate the system performance and quality?** A MAS should have a reliable and valid method of measuring and comparing the system outcomes and behaviors. This can be done by using simulation, experimentation, and analysis tools that can test the system under different scenarios and criteria.  

These are some of the main issues in designing a multi-agent system. There may be other issues depending on the specific application and domain of the system.



# Open problems for the notes of the Unit 5 - Applications in IDBS in the subject of INTELLIGENT DATABASE SYSTEM

Intelligent database systems (IDBS) are systems that combine database management with artificial intelligence techniques, such as machine learning, natural language processing, knowledge representation and reasoning, and expert systems. IDBS aim to provide more efficient, effective, and intelligent data management and analysis for various applications, such as decision support, data mining, information retrieval, and knowledge discovery.

However, IDBS also face many open problems and challenges, some of which are:

- **Data quality and consistency**: IDBS need to ensure that the data they store, process, and analyze are accurate, complete, consistent, and reliable. However, data quality and consistency can be affected by many factors, such as data sources, data integration, data cleaning, data transformation, data duplication, data heterogeneity, data semantics, and data evolution. IDBS need to develop methods and techniques to detect, prevent, and resolve data quality and consistency issues, as well as to measure and evaluate data quality and consistency .

- **Data security and privacy**: IDBS need to protect the data they manage from unauthorized access, modification, disclosure, or destruction. However, data security and privacy can be compromised by many threats, such as cyberattacks, data breaches, data leaks, data theft, data misuse, data anonymization, data encryption, and data governance. IDBS need to develop methods and techniques to ensure data security and privacy, as well as to comply with data regulations and policies .

- **Data scalability and performance**: IDBS need to handle large volumes, high velocities, and wide varieties of data, as well as to support complex and diverse data queries and analysis. However, data scalability and performance can be challenged by many factors, such as data storage, data distribution, data replication, data partitioning, data indexing, data caching, data compression, data parallelization, and data streaming. IDBS need to develop methods and techniques to improve data scalability and performance, as well as to optimize data resources and costs .

- **Data intelligence and learning**: IDBS need to provide data intelligence and learning capabilities, such as data extraction, data representation, data inference, data reasoning, data mining, data discovery, data prediction, data classification, data clustering, data association, data visualization, and data explanation. However, data intelligence and learning can be limited by many factors, such as data availability, data quality, data complexity, data uncertainty, data diversity, data interpretability, data explainability, and data ethics. IDBS need to develop methods and techniques to enhance data intelligence and learning, as well as to align data intelligence and learning with human intelligence and learning .

- **Data interaction and communication**: IDBS need to provide data interaction and communication capabilities, such as data query, data retrieval, data feedback, data annotation, data collaboration, data sharing, data exchange, data integration, data fusion, data synchronization, and data translation. However, data interaction and communication can be hindered by many factors, such as data format, data structure, data schema, data model, data language, data ontology, data context, data culture, and data user. IDBS need to develop methods and techniques to facilitate data interaction and communication, as well as to adapt data interaction and communication to different data scenarios and users .



# Internet indexing and retrieval

- Internet indexing and retrieval is the process of collecting, organizing, and storing information from the web to enable fast and accurate search results.
- Internet indexing and retrieval is an important application of intelligent database systems (IDBS), which use artificial intelligence techniques to enhance the functionality and performance of database systems.
- Internet indexing and retrieval involves the following steps:
  - Crawling: Scouring the web for content, looking over the code and content for each URL they find.
  - Indexing: Storing and organizing the content found during the crawling process. Once a page is in the index, it is in the running to be displayed as a result to relevant queries.
  - Ranking: Sorting the indexed pages by their relevance and quality for a given query.
  - Retrieving: Displaying the ranked pages to the user in a user-friendly format.
- Internet indexing and retrieval faces several challenges, such as:
  - Scalability: The web is constantly growing and changing, requiring frequent updates and maintenance of the index.
  - Heterogeneity: The web contains diverse types of content, such as text, images, audio, video, etc., which require different methods of processing and indexing.
  - Quality: The web contains varying levels of quality and reliability of information, which need to be evaluated and filtered by the search engine.
  - User satisfaction: The web users have different needs and preferences, which need to be understood and met by the search engine.
- Internet indexing and retrieval can be improved by using various techniques, such as:
  - Subject approach: Using subject headings, keywords, and classification schemes to organize and retrieve information by topic.
  - Semantic web: Using metadata, ontologies, and linked data to enhance the meaning and structure of web content.
  - Natural language processing: Using linguistic and statistical methods to analyze and understand natural language queries and documents.
  - Machine learning: Using algorithms and models to learn from data and improve the performance and accuracy of the search engine.



# Basic indexing methods for the notes of the Unit 5 - Applications in IDBS in the subject of INTELLIGENT DATABASE SYSTEM

- Indexing is a technique to optimize the performance of a database by reducing the number of disk accesses required to process a query.
- A database index is a data structure that helps to quickly locate and access the data in a database table.
- Indexes are created using one or more columns of a table, providing a fast way to look up data based on the values in those columns.
- Indexing in database is defined based on its indexing attributes. Two main types of indexing methods are:
  - Primary indexing
  - Secondary indexing
- Primary indexing is defined on an ordered data file, where the data file is ordered on a key field.
  - The key field is usually the primary key or a candidate key of the table.
  - A primary index consists of two fields: the first field is the same as the key field, and the second field is a pointer to the data block that contains the record with that key value.
  - Primary indexing can be further divided into two types:
    - Dense indexing: an index entry is created for every search key value in the database.
    - Sparse indexing: an index entry is created only for some records, usually the first record of each data block.
- Secondary indexing is defined on a field that is not the key field of the ordered data file, and may have duplicate values.
  - A secondary index also consists of two fields: the first field is the secondary key field, and the second field is a pointer to the record or a list of pointers to the records with that key value.
  - Secondary indexing is always dense, as every search key value has an index entry.
- Indexing can improve the efficiency of query processing, as it can reduce the number of data blocks that need to be scanned.
- However, indexing also has some drawbacks, such as:
  - Increased storage space: indexes require additional space to store the index entries and pointers.
  - Increased maintenance cost: indexes need to be updated whenever the data file is modified, such as insertion, deletion, or update of records.
  - Increased complexity: indexes add more complexity to the database design and implementation, as they need to be chosen carefully and managed properly.



# Search engines or meta-searchers for the notes of the Unit 5 - Applications in IDBS in the subject of INTELLIGENT DATABASE SYSTEM

- A search engine is a software system that allows users to find information on the web by using keywords or queries. A search engine typically consists of three components: a crawler, an indexer, and a query processor. The crawler scans the web and collects web pages, the indexer organizes the web pages into a database or index, and the query processor matches the user queries with the relevant web pages in the index.
- A meta-search engine is a type of search engine that does not have its own index, but instead aggregates the results from multiple other search engines. A meta-search engine may use different methods to rank and display the results, such as combining, filtering, clustering, or re-ranking. A meta-search engine may also offer additional features, such as query refinement, advanced search options, or visual representation of the results.
- Some examples of search engines are Google, Bing, and Yahoo. Some examples of meta-search engines are Dogpile, Metacrawler, and Yippy.
- Search engines and meta-search engines can be used for various applications in intelligent database systems (IDBS), such as:
  - Information retrieval: finding relevant and accurate information from large and heterogeneous data sources.
  - Information extraction: extracting structured or semi-structured data from unstructured or semi-structured text.
  - Information integration: combining and reconciling data from multiple sources into a unified view.
  - Information analysis: applying data mining, machine learning, natural language processing, or other techniques to discover patterns, trends, insights, or knowledge from data.
  - Information visualization: presenting data in a graphical or interactive way to facilitate understanding and exploration.
- Some challenges and issues in using search engines and meta-search engines for IDBS applications are:
  - Scalability: handling the increasing volume, variety, and velocity of data on the web.
  - Quality: ensuring the relevance, accuracy, completeness, and timeliness of the data and the results.
  - Privacy: protecting the personal or sensitive data of the users and the data sources.
  - Security: preventing unauthorized access, modification, or deletion of the data and the results.
  - Ethics: respecting the rights, values, and interests of the users and the data sources.



# Internet spiders

- Internet spiders, also known as web crawlers, web spiders, or spiderbots, are programs that systematically browse the World Wide Web and index the content of websites   .
- Internet spiders are typically operated by search engines like Google and Bing to provide relevant and updated search results for user queries  .
- Internet spiders work by following the hyperlinks on web pages and downloading the HTML content of each page. They also extract metadata, such as keywords, titles, and descriptions, from the web pages and store them in a database .
- Internet spiders use various algorithms and policies to decide which web pages to visit, how often to revisit them, and how to handle duplicate or dynamic content. Some of the factors that influence these decisions are the popularity, freshness, and quality of the web pages.
- Internet spiders can have positive or negative impacts on the web. On the positive side, they enable users to find relevant and updated information on the web and help webmasters to improve their websites' visibility and performance. On the negative side, they can consume a lot of bandwidth and resources, violate the privacy and security of web users and webmasters, and cause ethical and legal issues.



# Data mining for the notes of the Unit 5 - Applications in IDBS in the subject of INTELLIGENT DATABASE SYSTEM

- Data mining is a process of discovering patterns in a large set of data and data warehouses using various techniques such as regression analysis, association, and clustering, classification, and outlier analysis.
- Data mining can be used for various purposes such as business intelligence, advanced analytics, real-time analytics, and knowledge discovery  .
- Data mining can be applied to intelligent database systems (IDBS), which are database systems that integrate artificial intelligence techniques such as machine learning, fuzzy logic, neural networks, and genetic algorithms to provide intelligent functionalities such as query optimization, data analysis, data integration, and data quality .
- Some of the applications of data mining in IDBS are:

  - Customer relationship management: Data mining can help IDBS to analyze customer behavior, preferences, and needs, and provide personalized recommendations, offers, and services.
  - Fraud detection: Data mining can help IDBS to detect and prevent fraudulent transactions, activities, and claims by identifying anomalies, outliers, and patterns in the data.
  - Market basket analysis: Data mining can help IDBS to identify the associations and correlations among the items purchased by the customers, and provide insights for cross-selling, up-selling, and product bundling.
  - Text mining: Data mining can help IDBS to extract useful information and knowledge from unstructured text data, such as documents, emails, social media posts, and reviews, and perform tasks such as sentiment analysis, topic modeling, and document classification.
  - Web mining: Data mining can help IDBS to analyze the web data, such as web pages, links, logs, and clicks, and perform tasks such as web content mining, web structure mining, and web usage mining.



# Data mining tasks

Data mining is a computer-assisted technique used in analytics to process and explore large data sets. With data mining tools and methods, organizations can discover hidden patterns and relationships in their data. Data mining transforms raw data into practical knowledge.

There are a number of data mining tasks such as classification, prediction, time-series analysis, association, clustering, summarization etc. All these tasks are either predictive data mining tasks or descriptive data mining tasks. A data mining system can execute one or more of the above specified tasks as part of data mining.

Data mining tasks can be classified into two types: descriptive and predictive. Descriptive mining tasks define the common features of the data in the database, and the predictive mining tasks act in inference on the current information to develop predictions. Data mining is extensively used in many areas or sectors.

Some of the common data mining tasks are:

- **Classification**: It is a predictive data mining task that assigns a label or category to an instance based on a set of features. For example, classifying an email as spam or not spam based on its content and sender.
- **Prediction**: It is a predictive data mining task that estimates the value of a variable or attribute for a new or unknown instance based on a model derived from the existing data. For example, predicting the sales of a product based on its price and demand.
- **Time-series analysis**: It is a predictive data mining task that analyzes the changes and trends of a variable or attribute over time. For example, forecasting the stock market prices based on historical data and patterns.
- **Association**: It is a descriptive data mining task that discovers the co-occurrence or correlation of items or attributes in a data set. For example, finding the frequent itemsets or rules in a transaction database, such as customers who buy bread also buy butter.
- **Clustering**: It is a descriptive data mining task that groups the instances or objects in a data set based on their similarity or dissimilarity. For example, segmenting the customers based on their demographics and preferences.
- **Summarization**: It is a descriptive data mining task that provides a concise and meaningful representation of a data set. For example, generating a summary report or a visualization of the data.



# Data mining tools for the notes of the Unit 5 - Applications in IDBS in the subject of INTELLIGENT DATABASE SYSTEM

- Data mining is the process of discovering useful patterns, trends, and relationships from large and complex data sets  .
- Data mining tools are software applications that enable data analysts and business users to perform data mining tasks, such as data preparation, data modeling, data evaluation, and data visualization .
- Data mining tools can be classified into different categories based on their functionality, such as:
  - **Statistical tools**: These tools use statistical methods, such as regression, correlation, and hypothesis testing, to analyze data and identify significant variables and relationships. Examples of statistical tools are R, SAS, and SPSS.
  - **Machine learning tools**: These tools use algorithms that learn from data and make predictions or classifications based on the learned patterns. Examples of machine learning tools are Python, TensorFlow, and Weka.
  - **Visualization tools**: These tools use graphical techniques, such as charts, graphs, and maps, to display data and reveal patterns, trends, and outliers. Examples of visualization tools are Tableau, Power BI, and QlikView.
  - **Database tools**: These tools use database systems, such as relational, multidimensional, or NoSQL, to store, manage, and query data for data mining purposes. Examples of database tools are Oracle, SQL Server, and MongoDB.
- Data mining tools can be used for various applications in intelligent database systems, such as:
  - **Customer relationship management**: Data mining tools can help businesses understand their customers' behavior, preferences, and needs, and provide personalized services and recommendations . For example, data mining tools can be used to segment customers based on their demographics, purchase history, and loyalty, and to design targeted marketing campaigns and promotions.
  - **Fraud detection and prevention**: Data mining tools can help businesses detect and prevent fraudulent activities, such as credit card fraud, insurance fraud, and cyberattacks, by identifying anomalies and suspicious patterns in data . For example, data mining tools can be used to analyze transaction data and flag transactions that deviate from normal patterns or rules, and to alert the authorities or take preventive actions.
  - **Sentiment analysis**: Data mining tools can help businesses analyze the opinions, emotions, and attitudes of their customers and stakeholders, expressed in text, speech, or images, and use them to improve their products, services, and reputation . For example, data mining tools can be used to extract sentiment from social media posts, online reviews, and customer feedback, and to measure customer satisfaction and loyalty.
  - **Healthcare and biomedicine**: Data mining tools can help healthcare providers and researchers improve the quality and efficiency of healthcare and biomedical research, by analyzing clinical, genomic, and environmental data, and discovering new insights and knowledge . For example, data mining tools can be used to diagnose diseases, predict outcomes, recommend treatments, and identify biomarkers and drug targets.



# Medical and Legal Information Systems

Medical and legal information systems are applications of intelligent database systems that deal with the storage, retrieval, analysis, and dissemination of health and legal data. These systems are designed to support the decision-making processes of medical and legal professionals, as well as to facilitate the communication and collaboration among different stakeholders. Some of the topics that are covered in this unit are:

- **Electronic medical records (EMRs)**: These are digital versions of the paper charts that contain the medical history, diagnoses, treatments, medications, allergies, and other information of a patient. EMRs can improve the quality and efficiency of health care delivery, as well as reduce errors and costs. EMRs can also enable the integration of clinical data with other sources of information, such as laboratory results, imaging studies, and genomic data. EMRs can be accessed and updated by authorized health care providers across different settings and locations. 

- **Health information privacy and security**: These are the legal and ethical issues that arise from the collection, use, and disclosure of personal health information. Patients have the right to privacy, which means that they can control who can access their health information and for what purposes. Health care providers have the duty to protect the confidentiality and integrity of the health information they handle, and to comply with the relevant laws and regulations, such as the Health Insurance Portability and Accountability Act (HIPAA) and the Family Educational Rights and Privacy Act (FERPA). Health information privacy and security also involve the implementation of technical and administrative safeguards, such as encryption, authentication, authorization, and auditing.    

- **Medical artificial intelligence (AI)**: This is the application of AI techniques, such as machine learning, natural language processing, computer vision, and expert systems, to the domain of health care. Medical AI can assist health care providers in diagnosis, prognosis, treatment, and monitoring of diseases, as well as in research and education. Medical AI can also empower patients and consumers to manage their own health and wellness, through the use of wearable devices, mobile apps, and chatbots. Medical AI poses several legal and ethical challenges, such as liability, accountability, transparency, fairness, and consent. 

- **Legal information systems**: These are systems that store, retrieve, analyze, and disseminate legal data, such as statutes, case law, regulations, contracts, and evidence. Legal information systems can support the work of lawyers, judges, legislators, and other legal professionals, as well as the general public. Legal information systems can also employ AI techniques, such as natural language understanding, information extraction, reasoning, and argumentation, to perform tasks such as legal research, document analysis, contract drafting, and dispute resolution. Legal information systems can also raise legal and ethical issues, such as intellectual property, privacy, access, and quality. 

: https://onlinemasters.ohio.edu/blog/health-information-systems/

: https://www.usfhealthonline.com/resources/health-informatics/important-laws-and-regulations-in-health-informatics/

: https://www.usfhealthonline.com/resources/health-informatics/legal-and-ethical-issues-in-health-informatics/

: https://www.americanbar.org/groups/business_law/publications/blt/2019/12/medical-ai/

: https://www.healthit.gov/topic/health-information-privacy-law-and-policy

: https://www.cdc.gov/phlp/publications/topic/healthinformationprivacy.html

: https://www.sciencedirect.com/topics/computer-science/legal-information-system



# Medical Information Systems

Medical information systems are computer-based systems that store, process, and analyze health-related data for various purposes, such as patient care, clinical research, health administration, and public health. Medical information systems can be classified into different types according to their functions, users, and settings. Some examples of medical information systems are:

- **Electronic medical records (EMRs)**: These are digital versions of the paper charts that contain the medical history, diagnoses, treatments, medications, and other information of a patient. EMRs are used by health care providers to document and manage patient care, and to share information within a specific health care organization.
- **Health information exchanges (HIEs)**: These are networks that enable the secure and interoperable exchange of health information among different health care organizations, such as hospitals, clinics, laboratories, pharmacies, and public health agencies. HIEs can improve the quality, safety, and efficiency of health care delivery, and facilitate coordination and collaboration among health care providers.
- **Clinical decision support systems (CDSSs)**: These are systems that provide health care providers with guidance, recommendations, alerts, reminders, and feedback based on the analysis of patient data and clinical knowledge. CDSSs can help improve the quality and outcomes of patient care, reduce errors and adverse events, and enhance clinical performance and efficiency.
- **Medical imaging systems**: These are systems that capture, store, process, and display images of the human body or its parts, such as X-rays, ultrasound, computed tomography (CT), magnetic resonance imaging (MRI), and positron emission tomography (PET). Medical imaging systems are used for diagnosis, treatment planning, monitoring, and research purposes.
- **Medical informatics**: This is a sub-discipline of health informatics that applies computer science and information technology to the fields of medicine and health care. Medical informatics aims to improve health care and patient outcomes by developing and evaluating methods, systems, and tools for the acquisition, representation, storage, retrieval, analysis, and communication of health-related data and knowledge.
- **Digital health**: This is a broad term that encompasses the use of information and communication technologies (ICTs) to enhance health and well-being, such as mobile health (mHealth), telehealth, wearable devices, artificial intelligence (AI), and big data analytics. Digital health can enable the delivery of personalized, preventive, and participatory health care, and empower patients and consumers to manage their own health.

: https://onlinemasters.ohio.edu/blog/health-information-systems/

: https://pubmed.ncbi.nlm.nih.gov/891158/

: https://www.usfhealthonline.com/resources/health-informatics/what-is-medical-informatics/

: https://www.sciencedirect.com/topics/medicine-and-dentistry/medical-information-systems

: https://www.fda.gov/medical-devices/digital-health-center-excellence/digital-health-reports



# Legal information systems

Legal information systems are systems that store, process, and retrieve legal information, such as legislation, case law, and scholarly works. Legal information systems are important for providing access to the law to laymen and legal professionals, as well as for supporting various legal tasks, such as research, drafting, negotiation, consulting, management, and argumentation.

Some of the topics that are relevant for legal information systems are:

- Legal information retrieval: the science of information retrieval applied to legal text, which involves dealing with law-specific words and phrases, polysemes, synonyms, antonyms, and other linguistic features that affect the meaning and relevance of legal documents.
- Legal information management: the process of organizing, storing, and updating legal information, which involves creating and maintaining databases, indexes, metadata, ontologies, and other structures that facilitate the access and use of legal information.
- Legal information analysis: the process of extracting, summarizing, and presenting legal information, which involves applying natural language processing, text mining, machine learning, and other techniques to identify and highlight the key facts, issues, arguments, and outcomes of legal documents.
- Legal information services: the applications and tools that provide legal information to users, which involve designing and implementing user interfaces, query languages, feedback mechanisms, and other features that enhance the usability and effectiveness of legal information systems.

Some of the challenges and open issues that legal information systems face are:

- Legal information quality: the assessment and improvement of the accuracy, completeness, consistency, timeliness, and reliability of legal information, which involves dealing with errors, ambiguities, contradictions, gaps, and changes in legal information sources.
- Legal information interoperability: the integration and exchange of legal information across different systems, formats, languages, and jurisdictions, which involves dealing with heterogeneity, diversity, complexity, and variability of legal information standards and norms.
- Legal information ethics: the evaluation and regulation of the social, moral, and legal implications of legal information systems, which involves dealing with issues such as privacy, security, transparency, accountability, fairness, and trust in legal information systems.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some possible conclusions for the notes of the Unit 5 - Applications in IDBS in the subject of INTELLIGENT DATABASE SYSTEM:

### Conclusions

- Intelligent database systems (IDBS) are systems that integrate database management systems (DBMS) with artificial intelligence (AI) techniques to provide enhanced functionality, performance, and usability.
- IDBS can be classified into three categories based on the level of integration between DBMS and AI: loosely coupled, tightly coupled, and fully integrated.
- Loosely coupled IDBS are systems that use separate DBMS and AI components that communicate through a common interface. They are easy to implement and maintain, but have limited interoperability and efficiency.
- Tightly coupled IDBS are systems that embed AI techniques into the DBMS or vice versa. They have better interoperability and efficiency, but are more complex and difficult to implement and maintain.
- Fully integrated IDBS are systems that merge DBMS and AI into a single system that supports both data and knowledge management. They have the highest level of interoperability and efficiency, but are the most challenging to design and develop.
- IDBS have various applications in different domains, such as decision support, data mining, information retrieval, natural language processing, computer vision, and robotics.
- Decision support systems (DSS) are IDBS that help users make decisions based on data and knowledge. They use techniques such as expert systems, fuzzy logic, neural networks, and genetic algorithms to provide intelligent analysis, recommendation, and explanation.
- Data mining systems are IDBS that discover useful patterns and knowledge from large and complex data sets. They use techniques such as association rules, classification, clustering, and outlier detection to provide intelligent summarization, prediction, and discovery.
- Information retrieval systems are IDBS that help users find relevant information from large and heterogeneous collections of documents. They use techniques such as natural language processing, semantic web, and ontology to provide intelligent indexing, querying, and ranking.
- Natural language processing systems are IDBS that enable natural language understanding and generation for human-computer interaction. They use techniques such as parsing, semantic analysis, discourse analysis, and natural language generation to provide intelligent translation, summarization, and dialogue.
- Computer vision systems are IDBS that enable image and video understanding and processing. They use techniques such as feature extraction, object recognition, face recognition, and scene analysis to provide intelligent recognition, segmentation, and annotation.
- Robotics systems are IDBS that enable autonomous and intelligent control of robots. They use techniques such as planning, learning, reasoning, and perception to provide intelligent navigation, manipulation, and coordination.

