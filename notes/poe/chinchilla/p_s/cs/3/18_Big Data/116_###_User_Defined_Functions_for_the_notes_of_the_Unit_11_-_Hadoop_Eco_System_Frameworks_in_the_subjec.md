### User Defined Functions for the notes of the Unit 11 - Hadoop Eco System Frameworks in the subject of Big Data

User Defined Functions (UDFs) are custom functions that are developed by the user to perform specific operations on the data. In Hadoop Eco System Frameworks, UDFs are extensively used in Hive and Pig to process the data.

#### Advantages of using UDFs:
- Customized operations can be performed on the data to meet specific requirements.
- The performance of the data processing can be improved by using UDFs.
- The code reusability is increased as the same UDF can be used repeatedly in different queries.

#### Disadvantages of using UDFs:
- Writing UDFs require programming skills, which may not be available to all users.
- Poorly written UDFs can lead to performance issues and even failure of the data processing.

#### Types of UDFs:
There are three types of UDFs that can be used in Hadoop Eco System Frameworks:
1. Scalar UDFs - These UDFs take one or more input values and return a single output value. Examples include mathematical or string manipulation functions.
2. Aggregate UDFs - These UDFs take a set of input values and return a single output value. Examples include functions like SUM, COUNT, AVG, etc.
3. Table-generating UDFs - These UDFs take one or more input values and generate a table as output. Examples include functions that generate data for reporting purposes.

#### Example of using UDFs in Hive:
```
CREATE FUNCTION get_length AS 'org.apache.hadoop.hive.ql.udf.generic.GenericUDFLength';
SELECT get_length('Hello World');
```
In this example, a UDF is created using the class 'org.apache.hadoop.hive.ql.udf.generic.GenericUDFLength' to get the length of a string. The UDF is then called in a query to get the length of the string 'Hello World'.

#### Example of using UDFs in Pig:
```
DEFINE doubleNum org.apache.pig.piggybank.evaluation.math.DOUBLEMULTIPLY();
A = LOAD 'data' AS (num1:double, num2:double);
B = FOREACH A GENERATE doubleNum(num1, num2);
DUMP B;
```
In this example, a UDF named 'doubleNum' is defined using the class 'org.apache.pig.piggybank.evaluation.math.DOUBLEMULTIPLY()' to multiply two double values. The UDF is then used in a query to multiply two columns of a data set.

#### Applications of UDFs:
- Data transformation and manipulation
- Data cleaning and filtering
- Data aggregation and summarization
- Data visualization and reporting

UDFs play a crucial role in Hadoop Eco System Frameworks as they allow users to customize the data processing operations according to their requirements. By using UDFs, the performance of the data processing can be improved, and the code reusability can be increased.