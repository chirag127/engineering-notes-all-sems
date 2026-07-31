### Schema – Star and Snowflake Schemas for the notes of the Unit 2 - BI – DATA MINING & WAREHOUSING in the subject of BUSINESS INTELLIGENCE AND ANALYTICS KCS

In the field of data warehousing, schema is the structure that defines how the data is organized and stored. There are two popular schema designs: Star Schema and Snowflake Schema. In this unit, we will learn about these schema designs and their differences.

#### Star Schema

Star Schema is a simple and intuitive schema design. It consists of one large fact table connected to a set of dimension tables. The fact table contains the measures or the quantitative data, and the dimension tables contain the descriptive data. The dimension tables are connected to the fact table through foreign keys.

Here are some key features of Star Schema:

- It is easy to understand and use.
- It is denormalized, which means it reduces the number of joins required to access the data.
- It is optimized for query performance, as it has fewer joins and less complex relationships.

#### Snowflake Schema

Snowflake Schema is an extension of the Star Schema. It is a more complex schema design. In Snowflake Schema, the dimension tables are normalized into multiple related tables, creating a snowflake-like structure.

Here are some key features of Snowflake Schema:

- It is normalized, which means it reduces data redundancy and saves storage space.
- It is more complex than Star Schema, and therefore more difficult to understand and use.
- It requires more joins to access the data, which can negatively impact query performance.

#### Differences between Star Schema and Snowflake Schema

Here are some of the key differences between Star Schema and Snowflake Schema:

- Star Schema is denormalized, while Snowflake Schema is normalized.
- Star Schema has fewer joins and less complex relationships, while Snowflake Schema has more joins and more complex relationships.
- Star Schema is easier to understand and use, while Snowflake Schema is more complex and difficult to understand.
- Star Schema is optimized for query performance, while Snowflake Schema can negatively impact query performance due to its complexity.

In conclusion, both Star Schema and Snowflake Schema have their advantages and disadvantages. The choice between the two schema designs depends on the specific requirements of the data warehouse and the preferences of the data analysts and developers.