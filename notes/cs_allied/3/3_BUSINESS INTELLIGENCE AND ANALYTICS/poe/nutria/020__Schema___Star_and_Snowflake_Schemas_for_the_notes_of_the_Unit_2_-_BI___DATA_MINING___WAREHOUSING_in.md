
### Schema - Star and Snowflake Schemas

* A **star schema** is a type of database schema where data is organized into facts and dimensions. Facts are the numerical values that are used to measure a particular event or activity, while dimensions are the characteristics of the facts. 
* The star schema consists of a single fact table, which is surrounded by multiple dimension tables. The fact table contains the primary keys of the dimension tables, allowing the data to be linked together. 
* A **snowflake schema** is a type of database schema that is similar to a star schema, but with additional layers of normalized dimensions. The snowflake schema consists of a single fact table surrounded by multiple dimension tables, which are further broken down into sub-dimension tables. 
* The snowflake schema is more complex than the star schema, but it offers more flexibility when it comes to querying the data. The normalized structure of the snowflake schema also reduces the amount of redundant data stored in the database. 
* Both the star and snowflake schemas are used in business intelligence and data warehousing applications to store and analyze large amounts of data. They both offer advantages and disadvantages depending on the type of data being stored and the type of analysis being performed.