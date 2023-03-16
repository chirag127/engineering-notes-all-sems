Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of Schema – Star and Snowflake Schemas for the notes of the Unit 2 - BI – DATA MINING & WAREHOUSING in the subject of BUSINESS INTELLIGENCE AND ANALYTICS KCS.

### Schema – Star and Snowflake Schemas

- A schema is a logical representation of the structure and organization of data in a data warehouse or data mart.
- A schema consists of fact tables and dimension tables that store the data and metadata of the data warehouse or data mart.
- A fact table contains the measures or metrics of the business processes, such as sales, revenue, profit, etc.
- A dimension table contains the attributes or characteristics of the business entities, such as product, customer, location, time, etc.
- A schema can be designed using different approaches, such as star schema, snowflake schema, or galaxy schema.
- A star schema and a snowflake schema are two popular approaches to organizing and structuring data in data warehousing and business intelligence projects.
- Each schema has its own unique characteristics and benefits, and the best fit for your specific needs will depend on the requirements of your project.

#### Star Schema

- A star schema is the simplest type of data warehouse schema.
- It is called a star schema because its structure resembles a star, with a central fact table and multiple dimension tables radiating from it.
- A star schema has the following features:
  - It has a single fact table that stores the measures of the business processes.
  - It has multiple dimension tables that store the attributes of the business entities.
  - Each dimension table has a primary key that is referenced by a foreign key in the fact table.
  - Each dimension table is denormalized, meaning that it contains all the relevant attributes in a single table, without any further sub-dimensions or hierarchies.
  - It has a simple and straightforward design that is easy to understand and query.
  - It has a high performance and fast query response time, as it involves a single join between the fact table and the dimension table.
  - It has a low maintenance and update cost, as it requires less tables and joins to be updated.
  - It has a high data redundancy and storage cost, as it duplicates the same attributes in multiple dimension tables.

#### Snowflake Schema

- A snowflake schema is an extension of a star schema, with some modifications and enhancements.
- It is called a snowflake schema because its structure resembles a snowflake, with multiple branches and sub-branches of dimension tables stemming from the fact table.
- A snowflake schema has the following features:
  - It has a single fact table that stores the measures of the business processes.
  - It has multiple dimension tables that store the attributes of the business entities.
  - Each dimension table has a primary key that is referenced by a foreign key in the fact table or another dimension table.
  - Each dimension table is normalized, meaning that it is split into multiple sub-dimension tables that store the hierarchies or levels of the attributes, such as country, state, city, etc.
  - It has a complex and sophisticated design that is difficult to understand and query.
  - It has a low performance and slow query response time, as it involves multiple joins between the fact table and the dimension tables, and between the dimension tables and the sub-dimension tables.
  - It has a high maintenance and update cost, as it requires more tables and joins to be updated.
  - It has a low data redundancy and storage cost, as it eliminates the duplication of the same attributes in multiple dimension tables.

#### Comparison of Star Schema and Snowflake Schema

- The star schema and the snowflake schema have some similarities and differences, as shown in the table below:

| Feature | Star Schema | Snowflake Schema |
| --- | --- | --- |
| Structure | Simple and flat | Complex and hierarchical |
| Design | Denormalized | Normalized |
| Number of tables | Fewer | More |
| Number of joins | Fewer | More |
| Query performance | Faster | Slower |
| Query complexity | Lower | Higher |
| Data redundancy | Higher | Lower |
| Data storage | Higher | Lower |
| Data quality | Lower | Higher |
| Data update | Easier | Harder |

- The choice of the schema depends on the trade-off between the query performance and the data quality, as well as the business requirements and the data characteristics.