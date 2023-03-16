### Schema – Star and Snowflake Schemas

- A schema is a logical representation of the structure and organization of data in a data warehouse or data mart.
- A schema consists of fact tables and dimension tables that are related by foreign keys.
- A fact table contains the quantitative or numerical data that are measured by the business process, such as sales, revenue, profit, etc.
- A dimension table contains the descriptive or categorical data that provide context and meaning to the facts, such as product, customer, location, time, etc.
- A schema can be designed using different approaches, such as star schema and snowflake schema, depending on the level of normalization and denormalization of the dimension tables.

#### Star Schema

- A star schema is the simplest and most common type of schema in data warehousing and business intelligence projects.
- A star schema has one fact table and multiple dimension tables, each of which is directly connected to the fact table by a single foreign key.
- A star schema is called so because its structure resembles a star, with the fact table at the center and the dimension tables as the points.
- A star schema has the following characteristics and benefits:
  - It is easy to design and implement, as it requires minimal joins and relationships between tables.
  - It is efficient to query, as it allows fast and direct access to the facts and dimensions.
  - It is intuitive and user-friendly, as it provides a clear and simple view of the data and its dimensions.
  - It supports aggregation and summarization of data, as it enables slicing and dicing of data along multiple dimensions.
  - It has denormalized dimension tables, which means that each dimension table contains all the attributes and levels of hierarchy of that dimension, such as product name, category, subcategory, etc.
  - It has high data redundancy and duplication, which means that the same attribute or value may be repeated in multiple dimension tables, such as date, month, year, etc.
  - It consumes more storage space, as it stores redundant and duplicated data in the dimension tables.
  - It is less flexible and scalable, as it requires changes in the structure and data of the dimension tables whenever new attributes or levels of hierarchy are added or modified.

#### Snowflake Schema

- A snowflake schema is a variation or extension of the star schema, in which the dimension tables are further normalized into sub-dimension tables.
- A snowflake schema has one fact table and multiple dimension tables, each of which may be connected to one or more sub-dimension tables by foreign keys.
- A snowflake schema is called so because its structure resembles a snowflake, with the fact table at the center and the dimension tables and sub-dimension tables as the branches.
- A snowflake schema has the following characteristics and benefits:
  - It is more complex and difficult to design and implement, as it requires more joins and relationships between tables.
  - It is less efficient to query, as it involves more joins and traversals to access the facts and dimensions.
  - It is less intuitive and user-friendly, as it provides a more detailed and granular view of the data and its dimensions.
  - It supports normalization and integrity of data, as it eliminates redundancy and duplication of data in the dimension tables and sub-dimension tables.
  - It has normalized dimension tables, which means that each dimension table contains only the primary attributes and key of that dimension, and the other attributes and levels of hierarchy are stored in the sub-dimension tables, such as product key, product name, category key, subcategory key, etc.
  - It has low data redundancy and duplication, which means that the same attribute or value is stored only once in the appropriate sub-dimension table, such as date key, month key, year key, etc.
  - It consumes less storage space, as it stores only unique and non-redundant data in the dimension tables and sub-dimension tables.
  - It is more flexible and scalable, as it allows changes in the structure and data of the sub-dimension tables without affecting the dimension tables or the fact table.