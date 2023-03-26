 Here is the formal notes on the given topic:

## Patrice importing and exporting data from various data bases

Notes for BIG DATA AND ANALYTICS LAB

1. Import data from databases
- Connect to the database using connection strings/ODBC drivers
- Write SQL queries to extract data from tables
- Read data from queries into dataframes/datasets in Python/R
- Handle errors and missing data

2. Export data to databases
- Connect to the database using connection strings/ODBC drivers
- Create tables to store data (if not existing already)
- Convert dataframes/datasets into SQL insert queries
- Execute queries to insert data into tables
- Handle errors and edge cases

3. Different types of databases
- Relational databases - MySQL, PostgreSQL, SQL Server, Oracle
- NoSQL databases - MongoDB, Cassandra, HBase
- Data warehouses - Snowflake, Redshift, BigQuery
- Time series databases - InfluxDB, TimescaleDB

4. Data extraction techniques
- Full extracts vs incremental extracts
- Partitioned extracts (extracting only recent data)
- Usage of timestamp/incremental columns to identify new/modified records
- Usage of primary keys to avoid duplicate records in incremental extracts

The notes cover the key steps and concepts involved in importing and exporting data from various databases for data analysis and processing. The different types of databases and data extraction techniques are also outlined.