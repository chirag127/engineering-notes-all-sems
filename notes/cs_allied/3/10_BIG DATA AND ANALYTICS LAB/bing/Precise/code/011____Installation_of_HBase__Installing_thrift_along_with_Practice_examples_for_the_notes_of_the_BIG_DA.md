## Installation of HBase, Installing thrift along with Practice examples for the notes of the BIG DATA AND ANALYTICS LAB in the subject of BIG DATA AND ANALYTICS LAB

1. **HBase Installation**
    - HBase is an open-source, non-relational, distributed database that runs on top of the Hadoop Distributed File System (HDFS).
    - To install HBase, first ensure that you have Java and Hadoop installed on your system.
    - Download the latest stable release of HBase from the Apache HBase website.
    - Extract the downloaded file to a directory of your choice.
    - Set the environment variables `HBASE_HOME` and `HBASE_CONF_DIR` to the HBase installation directory and the `conf` directory within the HBase installation directory, respectively.
    - Add the HBase `bin` directory to your `PATH` environment variable.
    - Edit the `hbase-site.xml` file in the `conf` directory to configure HBase to your needs.
    - Start HBase by running the `start-hbase.sh` script in the `bin` directory.

2. **Installing Thrift**
    - Thrift is a software framework for scalable cross-language services development.
    - To install Thrift, first ensure that you have the required dependencies installed, such as a C++ compiler, Boost, and libevent.
    - Download the latest stable release of Thrift from the Apache Thrift website.
    - Extract the downloaded file to a directory of your choice.
    - Change to the extracted directory and run the `./configure` script.
    - Run `make` to build Thrift.
    - Run `make install` to install Thrift.

3. **Practice Examples**
    - Example 1: Creating a table in HBase
        - Open the HBase shell by running the `hbase shell` command.
        - Create a table by running the `create` command, specifying the table name and column family names. For example: `create 'mytable', 'cf1', 'cf2'`.
        - Verify that the table was created by running the `list` command.
    - Example 2: Inserting data into an HBase table
        - Open the HBase shell by running the `hbase shell` command.
        - Insert data into a table by running the `put` command, specifying the table name, row key, column family, column qualifier, and value. For example: `put 'mytable', 'row1', 'cf1:col1', 'value1'`.
        - Verify that the data was inserted by running the `get` command, specifying the table name and row key. For example: `get 'mytable', 'row1'`.