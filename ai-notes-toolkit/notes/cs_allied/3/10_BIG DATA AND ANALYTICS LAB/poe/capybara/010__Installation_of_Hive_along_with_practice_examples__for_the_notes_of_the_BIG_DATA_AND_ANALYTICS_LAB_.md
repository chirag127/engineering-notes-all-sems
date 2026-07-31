## Installation of Hive along with practice examples

In this section, we will discuss the installation of Hive and provide some practice examples to help you understand the process better. 

### Installation

To install Hive, follow these steps:

1. Download the latest version of Apache Hive from the official website.
2. Extract the downloaded package to a preferred directory.
3. Set the `HIVE_HOME` and `PATH` environment variables.
4. Start the Hive server by executing the command `hive --service hiveserver2` in the terminal.

### Practice Examples

Now that we have installed Hive, let's dive into some practice examples.

#### Example 1: Creating a Table

To create a table in Hive, run the following command:

```
CREATE TABLE employee (
  id INT,
  name STRING,
  age INT,
  salary FLOAT
);
```

#### Example 2: Loading Data into a Table

To load data into a table, run the following command:

```
LOAD DATA INPATH '/path/to/data' INTO TABLE employee;
```

#### Example 3: Querying Data from a Table

To query data from a table, run the following command:

```
SELECT * FROM employee;
```

#### Example 4: Creating a Partitioned Table

To create a partitioned table in Hive, run the following command:

```
CREATE TABLE employee_partitioned (
  id INT,
  name STRING,
  age INT,
  salary FLOAT
) PARTITIONED BY (dept STRING);
```

#### Example 5: Inserting Data into a Partitioned Table

To insert data into a partitioned table, run the following command:

```
INSERT INTO TABLE employee_partitioned PARTITION (dept='IT')
VALUES (1, 'John', 25, 5000.00);
```

These are just a few examples to get you started with Hive. We encourage you to explore more and experiment with different commands to gain a better understanding of the tool.