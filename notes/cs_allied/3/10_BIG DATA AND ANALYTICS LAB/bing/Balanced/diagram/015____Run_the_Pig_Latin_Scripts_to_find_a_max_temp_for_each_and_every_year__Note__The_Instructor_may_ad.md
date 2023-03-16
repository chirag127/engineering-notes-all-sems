## Run the Pig Latin Scripts to find a max temp for each and every year.

- Pig Latin is a high-level scripting language that allows users to write complex data transformations using a simple syntax. Pig Latin scripts can run on Apache Hadoop, a framework for distributed processing of large data sets.
- To find the maximum temperature for each year from a data set of weather records, we can use the following steps:

  1. Load the data from a file into a relation using the `LOAD` operator. Specify the schema of the data using the `AS` clause. For example:

     ```pig
     weather = LOAD 'weather.txt' USING PigStorage(',') AS (year:int, month:int, day:int, temp:float);
     ```

  2. Filter out the records that have invalid or missing temperature values using the `FILTER` operator. For example:

     ```pig
     valid = FILTER weather BY temp > -99.0;
     ```

  3. Group the records by year using the `GROUP` operator. This will create a nested relation where each group contains all the records for a given year. For example:

     ```pig
     by_year = GROUP valid BY year;
     ```

  4. Find the maximum temperature for each group using the `MAX` function and the `FOREACH` operator. The `MAX` function takes a bag of values and returns the maximum value. The `FOREACH` operator applies an expression to each group and generates a new relation. For example:

     ```pig
     max_temp = FOREACH by_year GENERATE group AS year, MAX(valid.temp) AS max_temp;
     ```

  5. Store the result into a file using the `STORE` operator. Specify the output format and the delimiter using the `USING` clause. For example:

     ```pig
     STORE max_temp INTO 'output' USING PigStorage(',');
     ```

  6. Run the Pig Latin script using the `pig` command. Specify the name of the script file as an argument. For example:

     ```bash
     pig max_temp.pig
     ```

  7. Check the output file for the maximum temperature for each year. For example:

     ```text
     1901,33.9
     1902,35.6
     1903,33.3
     ...
     ```