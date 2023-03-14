#### Data Processing operators in Pig

- Data processing operators in Pig are the commands that are used to manipulate and transform data in Pig Latin, a high-level scripting language for Apache Pig.
- Pig Latin operators can be classified into four categories: load/store operators, relational operators, diagnostic operators, and evaluation operators.
- Load/store operators are used to read data from and write data to the file system. The most common load/store operators are LOAD and STORE.
- Relational operators are used to perform operations on relations, such as filtering, grouping, joining, sorting, and projecting. The most common relational operators are FILTER, FOREACH, GROUP, JOIN, ORDER BY, and DISTINCT.
- Diagnostic operators are used to display information about the data or the execution plan, such as the schema, the data type, the number of records, and the physical plan. The most common diagnostic operators are DESCRIBE, DUMP, EXPLAIN, and ILLUSTRATE.
- Evaluation operators are used to evaluate expressions or functions on the data, such as arithmetic, logical, comparison, string, and user-defined functions. The most common evaluation operators are +, -, *, /, %, AND, OR, NOT, ==, !=, <, >, <=, >=, CONCAT, SUBSTRING, and UDFs.

- A mnemonic to remember the four categories of Pig Latin operators is **LORD** (Load/store, Relational, Diagnostic, Evaluation).
- A mnemonic to remember the most common load/store operators is **LS** (Load, Store).
- A mnemonic to remember the most common relational operators is **FFGJOD** (Filter, Foreach, Group, Join, Order by, Distinct).
- A mnemonic to remember the most common diagnostic operators is **DDIE** (Describe, Dump, Explain, Illustrate).
- A mnemonic to remember the most common evaluation operators is **ALCSU** (Arithmetic, Logical, Comparison, String, UDFs).

- An example of using Pig Latin operators to process data is:

```
-- Load data from a file
A = LOAD 'data.txt' USING PigStorage(',') AS (name:chararray, age:int, salary:float);

-- Filter data by age
B = FILTER A BY age > 30;

-- Group data by name and calculate average salary
C = FOREACH (GROUP B BY name) GENERATE group AS name, AVG(B.salary) AS avg_salary;

-- Sort data by average salary in descending order
D = ORDER C BY avg_salary DESC;

-- Store data to a file
STORE D INTO 'output.txt' USING PigStorage(',');
```

- An example of using diagnostic operators to display information about the data is:

```
-- Load data from a file
A = LOAD 'data.txt' USING PigStorage(',') AS (name:chararray, age:int, salary:float);

-- Describe the schema of A
DESCRIBE A;

-- Dump the first 10 records of A
DUMP LIMIT A 10;

-- Explain the execution plan of A
EXPLAIN A;

-- Illustrate the execution plan of A with sample data
ILLUSTRATE A;
```

- An example of using evaluation operators to perform calculations on the data is:

```
-- Load data from a file
A = LOAD 'data.txt' USING PigStorage(',') AS (name:chararray, age:int, salary:float);

-- Add a bonus column to A
B = FOREACH A GENERATE name, age, salary, salary * 0.1 AS bonus;

-- Filter data by bonus
C = FILTER B BY bonus > 1000;

-- Concatenate name and age
D = FOREACH C GENERATE CONCAT(name, '_', (chararray)age) AS name_age, bonus;
```