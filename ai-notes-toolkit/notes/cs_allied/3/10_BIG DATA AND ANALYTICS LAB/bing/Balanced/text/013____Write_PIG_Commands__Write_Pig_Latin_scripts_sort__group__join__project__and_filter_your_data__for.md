## Write Pig Latin scripts to sort, group, join, project, and filter your data.

- Pig Latin is a dataflow scripting language for processing large datasets using Apache Hadoop. It allows users to write high-level commands that are translated into MapReduce jobs by the Pig engine  .
- Pig Latin scripts consist of a series of statements that define the data flow from the input sources to the output destinations. Each statement applies an operator to one or more relations (tables of data) and produces a new relation as a result.
- The following are some of the common Pig Latin operators and how to use them to sort, group, join, project, and filter your data  :

  - **ORDER BY**: This operator sorts a relation by one or more fields in ascending or descending order. The syntax is:

    `ordered_relation = ORDER relation BY field1 [ASC|DESC], field2 [ASC|DESC], ...;`

    For example, to sort the relation `a` by the first field in ascending order and the second field in descending order, you can write:

    `result = ORDER a BY c1 ASC, c2 DESC;`

  - **GROUP**: This operator groups a relation by one or more fields and creates a nested relation for each group. The syntax is:

    `grouped_relation = GROUP relation BY field1, field2, ...;`

    For example, to group the relation `a` by the first field and create a nested relation for each value of the first field, you can write:

    `result = GROUP a BY c1;`

  - **JOIN**: This operator joins two or more relations by one or more fields that have the same name and type in both relations. The syntax is:

    `joined_relation = JOIN relation1 BY field1, relation2 BY field1, ...;`

    For example, to join the relations `a` and `b` by the first field, you can write:

    `result = JOIN a BY c1, b BY c1;`

  - **FOREACH ... GENERATE**: This operator projects a relation by applying expressions to each record and generating new fields. The syntax is:

    `projected_relation = FOREACH relation GENERATE expression1 [AS alias1], expression2 [AS alias2], ...;`

    For example, to project the relation `a` by adding 1 to the first field and subtracting 1 from the second field, you can write:

    `result = FOREACH a GENERATE c1 + 1 AS c1_new, c2 - 1 AS c2_new, c3;`

  - **FILTER**: This operator filters a relation by applying a boolean expression to each record and keeping only those that evaluate to true. The syntax is:

    `filtered_relation = FILTER relation BY expression;`

    For example, to filter the relation `a` by keeping only those records where the first field is greater than 5, you can write:

    `result = FILTER a BY c1 > 5;`

- These are some of the basic Pig Latin commands to manipulate your data. You can also use other operators and functions to perform more complex tasks, such as aggregation, arithmetic, string manipulation, and user-defined functions.