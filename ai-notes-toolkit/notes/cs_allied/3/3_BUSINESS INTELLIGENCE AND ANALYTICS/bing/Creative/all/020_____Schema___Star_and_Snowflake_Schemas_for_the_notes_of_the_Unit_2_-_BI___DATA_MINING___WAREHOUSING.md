# Schema – Star and Snowflake Schemas

- A schema is a logical representation of the structure and organization of data in a data warehouse or data mart.
- A schema consists of fact tables and dimension tables that are related by foreign keys.
- A fact table contains the quantitative or numerical data that are measured by the business process, such as sales, revenue, profit, etc.
- A dimension table contains the descriptive or categorical data that provide context and meaning to the fact data, such as product, customer, location, time, etc.
- A schema can be designed in different ways to optimize the performance, storage, and usability of the data warehouse or data mart.
- Two common types of schema design are star schema and snowflake schema.

## Star Schema

- A star schema is the simplest type of schema design that consists of a single fact table and multiple dimension tables.
- A star schema is called so because its structure resembles a star, with the fact table at the center and the dimension tables radiating from it.
- A star schema has the following characteristics:

  - The fact table has a composite primary key that is made up of the foreign keys from the dimension tables.
  - The dimension tables have a single primary key that uniquely identifies each row.
  - The dimension tables are denormalized, meaning that they contain all the relevant attributes for each dimension without any further sub-dimensions or hierarchies.
  - The dimension tables are usually small in size and have a low cardinality, meaning that they have a limited number of distinct values.
  - The fact table is usually large in size and has a high cardinality, meaning that it has a large number of distinct values.
  - The fact table contains the measures or metrics that are calculated using the dimension attributes, such as SUM, COUNT, AVERAGE, etc.
  - The star schema is easy to design, implement, and understand, as it has a simple and intuitive structure.
  - The star schema is efficient to query, as it requires fewer JOINs between tables and has a fast response time.

- An example of a star schema is shown below:

![star schema example](https://www.thoughtspot.com/sites/default/files/2020-10/star-schema-example.png)

## Snowflake Schema

- A snowflake schema is a variation of a star schema that consists of a single fact table and multiple dimension tables, with some of the dimension tables further normalized into sub-dimension tables.
- A snowflake schema is called so because its structure resembles a snowflake, with the fact table at the center and the dimension tables branching out into sub-dimension tables.
- A snowflake schema has the following characteristics:

  - The fact table has a composite primary key that is made up of the foreign keys from the dimension tables.
  - The dimension tables have a single primary key that uniquely identifies each row.
  - The dimension tables are normalized, meaning that they are split into sub-dimension tables based on the hierarchies or levels of each dimension, such as country, state, city, etc.
  - The sub-dimension tables have a foreign key that references the primary key of the parent dimension table.
  - The sub-dimension tables are usually small in size and have a low cardinality, meaning that they have a limited number of distinct values.
  - The fact table is usually large in size and has a high cardinality, meaning that it has a large number of distinct values.
  - The fact table contains the measures or metrics that are calculated using the dimension attributes, such as SUM, COUNT, AVERAGE, etc.
  - The snowflake schema is more complex to design, implement, and understand, as it has a nested and hierarchical structure.
  - The snowflake schema can be less efficient to query, as it requires more JOINs between tables and has a slower response time.

- An example of a snowflake schema is shown below:

![snowflake schema example](https://www.thoughtspot.com/sites/default/files/2020-10/snowflake-schema-example.png)

## Star Schema vs Snowflake Schema: Key Differences

- The main difference between star schema and snowflake schema is the level of normalization of the dimension tables.
- A star schema has denormalized dimension tables, while a snowflake schema has normalized dimension tables.
- A star schema is easier to design and implement than a snowflake schema.
- A star schema can be more efficient to query than a snowflake schema, because there are fewer JOINs between tables.
- A snowflake schema can reduce the data redundancy and duplication that may occur in a star schema, because the data