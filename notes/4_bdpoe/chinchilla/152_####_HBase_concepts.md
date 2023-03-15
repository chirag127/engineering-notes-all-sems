#### HBase Concepts

HBase is a distributed NoSQL database that runs on top of the Hadoop Distributed File System (HDFS). It provides real-time access to large amounts of structured and semi-structured data stored in HDFS. Here are some of the key concepts related to HBase:

1. **Column Families**: A column family is a group of related columns that are stored together. Each column family must be defined when a table is created in HBase. All columns in a column family have the same prefix, which is used as a qualifier to distinguish them from other columns in the same table.

2. **Rows and Cells**: HBase stores data in rows and cells, just like a traditional relational database. Each row in a table is identified by a unique row key, which is used to retrieve data from that row. Each row can contain multiple cells, which are identified by a column name (including the column family prefix) and a timestamp.

3. **Regions**: HBase tables are divided into regions, which are contiguous ranges of rows. Each region is served by a region server, which is responsible for handling read and write requests for that region. When a table grows too large to be stored on a single region server, HBase automatically splits it into multiple regions, which can be served by different region servers.

4. **ZooKeeper**: ZooKeeper is a distributed coordination service that is used by HBase to manage cluster membership and to store metadata about the state of the cluster. HBase uses ZooKeeper to coordinate region assignments, track the location of region servers, and perform other administrative tasks.

5. **Master Server**: The master server is a special node in the HBase cluster that is responsible for managing the deployment of regions across the region servers. It also manages other administrative tasks, such as schema changes and cluster configuration.

6. **WAL (Write-Ahead Log)**: The WAL is a file on each region server that records all write operations before they are applied to the underlying HDFS files. The WAL is used to ensure data durability in case of a region server failure or crash.

7. **Compaction**: HBase periodically compacts data to optimize storage and improve performance. During compaction, HBase merges smaller HDFS files into larger ones, discards deleted or expired data, and creates new index files.

8. **Snapshots**: HBase supports snapshots, which are read-only copies of a table or a region at a point in time. Snapshots can be used for backup, recovery, and data analysis purposes.

9. **Filters**: HBase supports filters, which allow users to selectively retrieve data based on certain criteria. Filters can be applied to row keys, column families, column qualifiers, and timestamps.

Mnemonic: "Column Families Row Regions ZooKeeper Master WAL Compaction Snapshots Filters" (C-F-R-R-Z-M-W-C-S-F)