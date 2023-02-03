### Schema – Star and Snowflake Schemas for the notes of the Unit 2 - BI – DATA MINING & WAREHOUSING in the subject of BUSINESS INTELLIGENCE AND ANALYTICS KCS

Schema: A schema is a blueprint or structure that defines the organization of data in a database.

Star Schema: A star schema is a type of data modeling technique used in data warehousing where data is organized into a central fact table and multiple dimension tables. The fact table contains the measures (e.g. sales, quantity) and the dimension tables contain the descriptive attributes (e.g. time, product, location). The relationship between the fact table and dimension tables is represented by a series of connections that resemble the shape of a star.

Snowflake Schema: A snowflake schema is a type of data modeling technique used in data warehousing where data is organized into a central fact table and multiple dimension tables. The difference between a snowflake schema and a star schema is that in a snowflake schema, the dimension tables are normalized, meaning that the data is split into multiple related tables to reduce data redundancy. This results in a more complex structure compared to the star schema, hence the name snowflake.

In Business Intelligence and Analytics, both star and snowflake schemas are used to model and organize data in a data warehouse. The choice between the two depends on the specific requirements of the data and the desired level of complexity. Star schema is preferred for its simplicity and ease of use, while snowflake schema is preferred for its ability to handle complex relationships and reduce data redundancy.
