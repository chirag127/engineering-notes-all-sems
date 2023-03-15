### Domain Constraints

- Domain constraints specify that within each tuple, the value of each attribute must be an element of the attribute's domain.
- The domain of an attribute is the set of all possible values that the attribute can take.
- Domain constraints are the most elementary form of integrity constraint.
- They are checked whenever a tuple is inserted or modified.
- If a tuple being inserted or modified violates a domain constraint, the operation is rolled back and an error is reported.
- Domain constraints can be specified using the `CHECK` clause of the `CREATE TABLE` or `ALTER TABLE` statements in SQL.
- For example, to specify that the value of the `age` attribute must be between 0 and 150, the following `CHECK` constraint can be used: `CHECK (age >= 0 AND age <= 150)`.
- Domain constraints can also be enforced by defining a custom data type using the `CREATE DOMAIN` statement in SQL.
- For example, to define a custom data type for age that only allows values between 0 and 150, the following `CREATE DOMAIN` statement can be used: `CREATE DOMAIN age_type AS INTEGER CHECK (VALUE >= 0 AND VALUE <= 150)`.
- Once a custom data type has been defined, it can be used as the data type of an attribute in a table definition.
- For example, to use the `age_type` data type defined above as the data type of the `age` attribute in the `person` table, the following `CREATE TABLE` statement can be used: `CREATE TABLE person (name VARCHAR(20), age age_type)`.