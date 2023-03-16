## Installation of Hive along with practice examples

Hive is a data warehouse software that facilitates querying and managing large datasets residing in distributed storage. Hive provides a SQL-like interface to data stored in Hadoop. To install Hive on Ubuntu, you can follow these steps:

- Step 1: Download and untar Hive. Visit the Apache Hive official download page and determine which Hive version is best suited for your Hadoop edition. Once you establish which version you need, select the Download a Release Now! option. The mirror link on the subsequent page leads to the directories containing available Hive tar packages. You can download the package using the `wget` command in the terminal, for example:

  `wget http://archive.apache.org/dist/hive/hive-2.1.0/apache-hive-2.1.0-bin.tar.gz`

  Then, you can extract the package using the `tar` command, for example:

  `tar -xvzf apache-hive-2.1.0-bin.tar.gz`

  This will create a directory named `apache-hive-2.1.0-bin` in your current working directory.

- Step 2: Configure Hive environment variables. The `$HIVE_HOME` environment variable needs to direct the client to the location of the Hive installation. You can set this variable in the `.bashrc` file in your home directory, for example:

  `echo "export HIVE_HOME=/home/user/apache-hive-2.1.0-bin" >> ~/.bashrc`

  You also need to add the Hive bin directory to the `$PATH` variable, for example:

  `echo "export PATH=$PATH:$HIVE_HOME/bin" >> ~/.bashrc`

  Then, you need to source the `.bashrc` file to apply the changes, for example:

  `source ~/.bashrc`

- Step 3: Edit `hive-config.sh` file. This file is located in the `conf` directory of the Hive installation. You need to edit this file to specify the Hadoop installation directory and the Java installation directory, for example:

  `export HADOOP_HOME=/home/user/hadoop-2.7.3`

  `export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64`

- Step 4: Start Hive shell. You can start the Hive shell by typing `hive` in the terminal. This will launch the Hive command-line interface, where you can execute Hive queries and commands.

To practice Hive, you can use some sample data sets and queries provided by Hive. For example, you can use the following steps to create a table and load some data from a file:

- Step 1: Create a directory in HDFS to store the data file, for example:

  `hdfs dfs -mkdir /user/hive/data`

- Step 2: Download a sample data file from the Hive website, for example:

  `wget https://cwiki.apache.org/confluence/download/attachments/27362075/NASDAQ_daily_prices_subset.csv`

- Step 3: Copy the data file to the HDFS directory, for example:

  `hdfs dfs -put NASDAQ_daily_prices_subset.csv /user/hive/data`

- Step 4: Create a table in Hive using the `CREATE TABLE` statement, for example:

  `CREATE TABLE nasdaq (exchange STRING, stock_symbol STRING, date STRING, stock_price_open FLOAT, stock_price_high FLOAT, stock_price_low FLOAT, stock_price_close FLOAT, stock_volume INT, stock_price_adj_close FLOAT) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';`

- Step 5: Load the data from the file into the table using the `LOAD DATA` statement, for example:

  `LOAD DATA INPATH '/user/hive/data/NASDAQ_daily_prices_subset.csv' OVERWRITE INTO TABLE nasdaq;`

- Step 6: Query the table using the `SELECT` statement, for example:

  `SELECT * FROM nasdaq LIMIT 10;`

  This will display the first 10 rows of the table.

You can also use other Hive features, such as partitioning, bucketing, views, functions, and joins, to practice more complex queries and operations on the data. You can refer to the Hive documentation for more details and examples.