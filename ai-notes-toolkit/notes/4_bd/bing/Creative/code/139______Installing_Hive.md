#### Installing Hive

- Hive is a data warehouse system that runs on top of Hadoop, a distributed file system that stores large amounts of data.
- Hive provides a SQL-like interface to query and analyze data stored in Hadoop.
- To install Hive, you need to have Java, Hadoop and MySQL installed on your system.
- The steps to install Hive are as follows:

  1. Download the latest version of Hive from https://hive.apache.org/downloads.html and extract it to a desired location.
  2. Set the environment variables `HIVE_HOME` and `PATH` to point to the Hive directory and its bin subdirectory, respectively.
  3. Create a MySQL database and user for Hive metastore, which stores the metadata of Hive tables and partitions.
  4. Copy the MySQL JDBC driver jar file to the Hive lib directory.
  5. Edit the `hive-site.xml` file in the Hive conf directory and configure the following properties:

     - `javax.jdo.option.ConnectionURL` : the JDBC connection URL to the MySQL database
     - `javax.jdo.option.ConnectionDriverName` : the JDBC driver class name for MySQL
     - `javax.jdo.option.ConnectionUserName` : the MySQL user name for Hive metastore
     - `javax.jdo.option.ConnectionPassword` : the MySQL password for Hive metastore
     - `hive.metastore.warehouse.dir` : the HDFS directory where Hive stores the data of its tables
     - `hive.exec.scratchdir` : the HDFS directory where Hive stores the intermediate results of its queries

  6. Initialize the Hive metastore schema by running the `schematool` command with the `-initSchema` option and the `-dbType` option set to `mysql`.
  7. Start the Hive shell by running the `hive` command and verify that you can create and query tables.