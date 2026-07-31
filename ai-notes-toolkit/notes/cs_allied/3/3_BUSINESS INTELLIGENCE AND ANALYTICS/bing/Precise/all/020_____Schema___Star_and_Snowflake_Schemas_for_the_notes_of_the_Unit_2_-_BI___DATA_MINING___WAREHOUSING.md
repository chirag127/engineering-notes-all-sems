# Schema – Star and Snowflake Schemas

## Star Schema
- A star schema is a type of data warehouse design.
- It is called a star schema because the diagram resembles a star, with points radiating from a central table.
- The central table is the fact table and the points of the star are the dimension tables.
- The fact table contains the measures or facts, and the dimension tables contain the descriptive information about the facts.
- The fact table is connected to the dimension tables through foreign keys.
- The star schema is simple and easy to understand.
- It is also easy to write queries against a star schema.

## Snowflake Schema
- A snowflake schema is a variation of the star schema.
- It is called a snowflake schema because the diagram resembles a snowflake.
- The main difference between a star schema and a snowflake schema is that the dimension tables in a snowflake schema are normalized.
- This means that the dimension tables are split into multiple related tables.
- The snowflake schema is more complex than the star schema.
- It can be more difficult to write queries against a snowflake schema.
- However, the snowflake schema can be more efficient in terms of storage space and query performance.
