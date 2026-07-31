### Candidate Key

- A candidate key is a specific type of field in a relational database that can identify each unique record independently of any other data.
- A candidate key is a minimal superkey. In other words, it is any set of columns that have a unique combination of values in each row (which makes it a superkey), with the additional constraint that removing any column could produce duplicate combinations of values (which makes it a minimal superkey).
- A candidate key can be a single column or a combination of columns, as long as it satisfies the uniqueness and minimality properties.
- A table can have more than one candidate key, but only one of them can be chosen as the primary key, which is the candidate key selected by the database administrator to uniquely identify tuples in a table.
- To find the candidate keys of a table, we can use the following algorithm:
  - List all the possible superkeys of the table, i.e., all the sets of columns that have unique values in each row.
  - Eliminate any superkey that contains another superkey, i.e., any set of columns that has a subset of columns that is also a superkey.
  - The remaining superkeys are the candidate keys of the table.