### Schema – Star and Snowflake Schemas for the notes of the Unit 2 - BI – DATA MINING & WAREHOUSING in the subject of BUSINESS INTELLIGENCE AND ANALYTICS KCS

In the world of data warehousing, schemas are essential for organizing and structuring data. Two popular schema models used are the Star Schema and the Snowflake Schema. Here are the key points to understand about each schema:

#### Star Schema
- Star Schema is a simple and intuitive schema model that is widely used in data warehousing.
- It consists of a central fact table that is connected to multiple dimension tables.
- The fact table contains the measures or facts that are being analyzed, while the dimension tables contain the attributes or characteristics of those measures.
- The dimension tables are connected to the fact table through foreign keys.
- Star Schema is denormalized, which means that the data is duplicated across the dimension tables to improve query performance.
- Star Schema is best suited for querying and analyzing large amounts of data quickly and efficiently.

#### Snowflake Schema
- Snowflake Schema is a more complex schema model that builds upon the Star Schema.
- It is called Snowflake because the diagram of the schema looks like a snowflake, with the fact table in the center and the dimension tables branching out like snowflakes.
- Unlike Star Schema, Snowflake Schema normalizes the dimension tables, which means that the data is not duplicated and is stored in separate tables.
- Normalization results in better data consistency and reduces the storage space required.
- However, it also makes querying and analyzing data more complex and slower compared to the Star Schema.
- Snowflake Schema is best suited for situations where data consistency is crucial and storage space is limited.

Understanding the differences between Star and Snowflake Schemas is crucial for designing an effective data warehouse. Choose the schema model that best fits your business requirements and use it to structure and organize your data for optimal performance and analysis.