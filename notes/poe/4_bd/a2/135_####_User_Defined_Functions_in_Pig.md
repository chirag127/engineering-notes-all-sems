 Here is the content written in markdown format on the topic #### User Defined Functions in Pig:

#### User Defined Functions in Pig

Pig allows us to define our own functions to use in scripts using Pig Latin. This helps in reusing the logic and making the scripts more readable and maintainable.

Following are a few key points about User Defined Functions (UDFs) in Pig:

- UDFs are written in Java, Python or JavaScript.
- UDFs take input as a bag of tuples and return a bag of tuples.
- UDFs can contain multiple statements and control flows like if-else and for loops.
- UDFs can access and modify fields of input tuples.
- UDFs provide a way to extend the functionalities of Pig beyond what is available in the built-in operators.
- UDFs can be used in FOREACH statements or can be used inside another UDF.

**Mnemonics:** To remember that UDFs take input as bag of tuples and return a bag of tuples, remember - "In tuples, out tuples".

**Examples:**

- Writing a UDF to calculate the length of each string in a field and return a new field with string lengths.
- Converting all strings in a field to upper case.
- Calculating age from birthdate.
- Complex data transformations and processing.

**Advantages:**

- Reusability of logic.
- Readability and maintainability of scripts.
- Extend Pig functionalities.

**Disadvantages:**

- Need to know Java/Python/JavaScript to write UDFs.
- Can impact performance if not optimized.
- Debugging UDFs can be challenging.

**Applications:** UDFs are widely used in the industry to implement complex data processing requirements that are not met by the built-in operators.