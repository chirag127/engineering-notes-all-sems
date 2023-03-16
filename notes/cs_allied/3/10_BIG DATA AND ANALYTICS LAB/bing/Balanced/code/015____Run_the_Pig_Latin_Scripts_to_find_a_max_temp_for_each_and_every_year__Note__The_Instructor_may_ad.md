Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is the content I have written in markdown format:

## Run the Pig Latin Scripts to find a max temp for each and every year.

Pig Latin is a high-level scripting language that can be used to process and analyze large-scale data sets using Apache Pig, a platform for parallel data processing. Pig Latin scripts can run on a single node or a cluster of nodes, and can interact with various data sources and formats, such as HDFS, Hive, JSON, CSV, etc.

To run the Pig Latin scripts to find the max temp for each and every year, we need to follow these steps:

- Load the data set that contains the temperature records for each day and each location. The data set can be in any format that Pig can read, such as a text file, a CSV file, a JSON file, etc. For example, we can load a CSV file from HDFS using the `LOAD` statement:

```
temp_data = LOAD 'hdfs://temp_data.csv' USING PigStorage(',') AS (date:chararray, location:chararray, temp:int);
```

- Filter the data set to remove any invalid or missing records, such as records with null values, negative temperatures, etc. We can use the `FILTER` statement to apply a condition on the data set and keep only the records that satisfy the condition. For example, we can filter out the records with null values using the `IS NOT NULL` operator:

```
temp_data = FILTER temp_data BY date IS NOT NULL AND location IS NOT NULL AND temp IS NOT NULL;
```

- Group the data set by the year, which is the first four characters of the date field. We can use the `GROUP` statement to create a relation that contains a group for each distinct value of the year field, and a bag of records that belong to that group. We can use the `SUBSTRING` function to extract the year from the date field. For example, we can group the data set by the year using the following statement:

```
temp_data_by_year = GROUP temp_data BY SUBSTRING(date, 0, 4);
```

- For each group, find the maximum temperature among all the records in that group. We can use the `FOREACH` statement to iterate over each group and apply a transformation on the records in that group. We can use the `MAX` function to find the maximum value of the temp field in each group. For example, we can find the maximum temperature for each year using the following statement:

```
max_temp_by_year = FOREACH temp_data_by_year GENERATE group AS year, MAX(temp_data.temp) AS max_temp;
```

- Store the result in a file or a table for further analysis or visualization. We can use the `STORE` statement to write the result to a file or a table in any format that Pig can write, such as a text file, a CSV file, a JSON file, etc. For example, we can store the result in a CSV file in HDFS using the following statement:

```
STORE max_temp_by_year INTO 'hdfs://max_temp_by_year.csv' USING PigStorage(',');
```

- Run the Pig Latin script using the `pig` command in the terminal or the Pig shell. We can specify the name of the script file as an argument to the `pig` command, or we can enter the Pig shell by typing `pig` without any arguments and then type or paste the script in the shell. For example, we can run the script file named `max_temp_by_year.pig` using the following command:

```
pig max_temp_by_year.pig
```

- Check the output file or table to see the result. We can use the `cat` command or the `hadoop fs -cat` command to view the content of the output file in the terminal, or we can use the `hive` command or the `beeline` command to query the output table in the Hive shell. For example, we can view the output file in HDFS using the following command:

```
hadoop fs -cat hdfs://max_temp_by_year.csv
```

The output file should contain the max temp for each and every year, such as:

```
2010,35
2011,38
2012,40
2013,37
2014,36
2015,39
```
