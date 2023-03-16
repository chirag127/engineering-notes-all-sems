## Run the Pig Latin Scripts to find a max temp for each and every year.

- Pig Latin is a high-level scripting language that allows users to write complex data transformations using a simple syntax. Pig Latin scripts can run on Apache Hadoop, a framework for distributed processing of large data sets.
- To find the maximum temperature for each year from a data set of weather records, we can use the following steps:

  1. Load the data set into a Pig relation using the `LOAD` operator. Specify the schema of the data, such as the fields and their types. For example, if the data set is stored in a file called `weather.txt` with the format `year,month,day,temp`, we can load it as follows:

  ```
  weather = LOAD 'weather.txt' USING PigStorage(',') AS (year:int, month:int, day:int, temp:float);
  ```

  2. Filter out any records that have missing or invalid temperature values using the `FILTER` operator. For example, we can filter out any records that have a temperature of -99, which is a common placeholder for missing data, as follows:

  ```
  weather = FILTER weather BY temp != -99;
  ```

  3. Group the records by year using the `GROUP` operator. This will create a nested relation, where each group contains a bag of records that belong to the same year. For example, we can group the records by year as follows:

  ```
  weather_by_year = GROUP weather BY year;
  ```

  4. Find the maximum temperature for each group using the `MAX` function and the `FOREACH` operator. The `MAX` function takes a bag of numeric values and returns the largest one. The `FOREACH` operator allows us to apply a transformation to each group. For example, we can find the maximum temperature for each year as follows:

  ```
  max_temp_by_year = FOREACH weather_by_year GENERATE group AS year, MAX(weather.temp) AS max_temp;
  ```

  5. Store the result into a file using the `STORE` operator. Specify the output format and the delimiter. For example, we can store the result as a comma-separated file called `max_temp_by_year.txt` as follows:

  ```
  STORE max_temp_by_year INTO 'max_temp_by_year.txt' USING PigStorage(',');
  ```

- To run the Pig Latin script, we can use the `pig` command in the terminal. For example, if the script is saved in a file called `max_temp.pig`, we can run it as follows:

  ```
  pig max_temp.pig
  ```

- Alternatively, we can use the Grunt shell, an interactive shell for Pig Latin, to run the script line by line. To enter the Grunt shell, we can use the `pig` command without any arguments. For example, we can enter the Grunt shell as follows:

  ```
  pig
  ```

  Then, we can type or paste the Pig Latin script in the shell and press enter to execute each line. To exit the Grunt shell, we can use the `quit` command. For example, we can exit the Grunt shell as follows:

  ```
  quit
  ```