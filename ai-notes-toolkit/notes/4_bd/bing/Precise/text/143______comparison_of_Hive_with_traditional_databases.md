#### Comparison of Hive with traditional databases

Hive is a data warehouse software system that provides data query and analysis. It gives an interface like SQL to query data stored in various databases and file systems that integrate with Hadoop. Hive helps with querying and managing large datasets real fast .

- **Schema on Read**: Hive enforces schema on read time, meaning it does not verify the schema until the data is read .
- **Scalability**: Hive is very easily scalable at low cost .
- **Based on Hadoop**: Hive is based on Hadoop notation that is Write once Read many times .
- **Record level updates**: Record level updates are not possible in Hive .
- **Data Analysis**: Hive is majorly used to do analysis on a huge amount of data which traditional databases cannot process using MapReduce .

On the other hand, traditional databases enforce schema on write time, meaning the table schema is enforced when the data is written . They are not as easily scalable and can be costly to scale up . Record level updates, insertions, and deletions are possible in traditional databases .

In summary, Hive is similar to traditional databases by supporting the SQL interface but it is not a full database. Instead of calling Hive a database, it can also be called a data warehouse . It is better suited for querying and managing large datasets, while traditional databases are better suited for record level updates and transactions.