# Schema – Star and Snowflake Schemas

- A schema is a logical representation of the structure and organization of data in a data warehouse or data mart.
- A schema defines the tables, columns, relationships, constraints, and other properties of the data.
- A schema can help to optimize the performance, usability, and scalability of the data warehouse or data mart.
- There are different types of schemas that can be used for data warehousing and business intelligence projects, such as star schema, snowflake schema, galaxy schema, etc.
- In this note, we will focus on the star schema and the snowflake schema, which are two of the most common and popular schemas.

## Star Schema

- A star schema is a type of schema that consists of a single fact table and one or more dimension tables.
- A fact table contains the measures or metrics of the business process, such as sales amount, order quantity, profit, etc.
- A dimension table contains the attributes or characteristics of the business process, such as product name, customer name, region, date, etc.
- A star schema is called so because its structure resembles a star, with the fact table at the center and the dimension tables radiating from it.
- A star schema has the following advantages:
  - It is simple and easy to understand and design.
  - It has a high query performance, as it involves fewer joins and less data redundancy.
  - It is flexible and adaptable to changes in business requirements and data sources.
- A star schema has the following disadvantages:
  - It may have data quality issues, such as inconsistency, incompleteness, or incorrectness, due to the denormalization of the data.
  - It may have data storage issues, such as increased disk space and memory usage, due to the duplication of the data.
  - It may have data maintenance issues, such as increased complexity and overhead, due to the update and delete operations on the data.

## Snowflake Schema

- A snowflake schema is a type of schema that is an extension of a star schema, where some or all of the dimension tables are further normalized into sub-dimension tables.
- A sub-dimension table contains the attributes or characteristics of a specific dimension, such as product category, product subcategory, product type, etc.
- A snowflake schema is called so because its structure resembles a snowflake, with the fact table at the center and the dimension tables and sub-dimension tables branching from it.
- A snowflake schema has the following advantages:
  - It has a high data quality, as it eliminates the data redundancy and inconsistency, and preserves the data integrity and accuracy.
  - It has a low data storage, as it reduces the disk space and memory usage, and optimizes the data compression and indexing.
  - It has a low data maintenance, as it simplifies the update and delete operations on the data, and minimizes the data anomalies and errors.
- A snowflake schema has the following disadvantages:
  - It is complex and difficult to understand and design.
  - It has a low query performance, as it involves more joins and more tables to access the data.
  - It is rigid and inflexible to changes in business requirements and data sources.