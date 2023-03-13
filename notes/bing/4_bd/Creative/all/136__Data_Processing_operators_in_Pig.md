#### Data Processing operators in Pig

- Data processing operators in Pig are the commands that allow users to manipulate and transform data in Pig Latin, a high-level scripting language for Apache Pig.
- Pig Latin operators can be classified into four categories: load/store operators, relational operators, diagnostic operators, and evaluation operators.
- Load/store operators are used to read data from and write data to the file system. The most common load/store operators are LOAD and STORE.
  - LOAD reads data from a file or a directory and creates a relation (a bag of tuples) with a specified schema.
  - STORE writes a relation to a file or a directory in a specified format.
  - Example:

    ```
    -- Load data from a file named input.txt
    A = LOAD 'input.txt' AS (name:chararray, age:int, salary:float);

    -- Store the relation A to a directory named output
    STORE A INTO 'output';
    ```

- Relational operators are used to perform common relational operations on data, such as filtering, grouping, joining, sorting, etc. The most common relational operators are FILTER, FOREACH, GROUP, JOIN, ORDER, and DISTINCT.
  - FILTER selects tuples from a relation that satisfy a given condition.
  - FOREACH applies a set of expressions to each tuple in a relation and generates a new relation.
  - GROUP groups the tuples in a relation by one or more fields.
  - JOIN joins two or more relations by a common field or a set of fields.
  - ORDER sorts the tuples in a relation by one or more fields in ascending or descending order.
  - DISTINCT removes duplicate tuples from a relation.
  - Example:

    ```
    -- Filter the relation A by age
    B = FILTER A BY age > 25;

    -- Generate a new relation C with name and salary fields
    C = FOREACH B GENERATE name, salary;

    -- Group the relation C by name
    D = GROUP C BY name;

    -- Join the relation C with another relation E by name
    F = JOIN C BY name, E BY name;

    -- Sort the relation F by salary in descending order
    G = ORDER F BY salary DESC;

    -- Remove duplicate tuples from the relation G
    H = DISTINCT G;
    ```

- Diagnostic operators are used to display information about the data or the execution of Pig Latin scripts. The most common diagnostic operators are DUMP, DESCRIBE, EXPLAIN, and ILLUSTRATE.
  - DUMP prints the contents of a relation to the screen.
  - DESCRIBE prints the schema of a relation to the screen.
  - EXPLAIN prints the logical, physical, and map-reduce execution plans of a Pig Latin script to the screen or a file.
  - ILLUSTRATE shows an example of how a Pig Latin script operates on a small set of data.
  - Example:

    ```
    -- Dump the relation H to the screen
    DUMP H;

    -- Describe the schema of the relation H
    DESCRIBE H;

    -- Explain the execution plan of the script to a file named plan.txt
    EXPLAIN -out plan.txt;

    -- Illustrate how the script operates on a small set of data
    ILLUSTRATE;
    ```

- Evaluation operators are used to compute values from data, such as arithmetic operations, string manipulation, type conversion, etc. The most common evaluation operators are +, -, *, /, %, CONCAT, SUBSTRING, (int), (float), (chararray), etc.
  - +, -, *, /, and % perform arithmetic operations on numeric values.
  - CONCAT concatenates two or more strings.
  - SUBSTRING extracts a substring from a string.
  - (int), (float), and (chararray) convert values to different data types.
  - Example:

    ```
    -- Add 10% bonus to the salary field in the relation C
    I = FOREACH C GENERATE name, salary * 1.1 AS bonus;

    -- Concatenate the name and salary fields in the relation C
    J = FOREACH C GENERATE CONCAT(name, ':', (chararray)salary);

    -- Extract the first three characters of the name field in the relation C
    K = FOREACH C GENERATE SUBSTRING(name, 0, 3);

    -- Convert the salary field to integer in the relation C
    L = FOREACH C GENERATE name, (int)salary;
    ```