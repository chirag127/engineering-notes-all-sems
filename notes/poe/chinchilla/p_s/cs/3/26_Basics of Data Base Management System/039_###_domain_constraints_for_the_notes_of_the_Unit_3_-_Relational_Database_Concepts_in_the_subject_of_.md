### Domain Constraints for the notes of Unit 3 - Relational Database Concepts

Domain Constraints are the rules that define the permissible values for a given attribute in a table. These constraints are used to ensure the data in the table is valid and consistent with the domain of the attribute. In this unit, we will learn about the different types of domain constraints that can be applied to relational databases.

#### Data Types
Data types are used to define the type of data that can be stored in a table. The different data types include integer, float, character, date, and time. Each data type has a set of rules that define the acceptable values for the attribute.

#### Range Constraints
Range Constraints define the permissible range of values for a given attribute. For example, if an attribute defines the age of a person, the range constraint would specify the minimum and maximum age that can be stored in the database.

#### Default Constraints
Default Constraints define the default value for a given attribute in case no value is specified during insertion. For example, if an attribute defines the gender of a person, the default constraint could be set to “not specified” in case no gender is provided.

#### Null Constraints
Null Constraints define whether an attribute can have a null value or not. If a null constraint is set to “not null”, it means that the attribute must have a value for every record in the table.

#### Unique Constraints
Unique Constraints ensure that no two records have the same value for a given attribute. For example, in a table that stores email addresses, the unique constraint could be set to ensure that no two records have the same email address.

#### Check Constraints
Check Constraints define a Boolean expression that must be true for a given attribute. For example, if an attribute defines the age of a person, a check constraint could be set to ensure that the age is greater than or equal to 18.

#### Advantages of Domain Constraints
- Domain Constraints ensure the integrity and consistency of the data in the database.
- They help to prevent incorrect or invalid data from being inserted into the database.
- They make it easier to enforce business rules and constraints on the data.

#### Disadvantages of Domain Constraints
- Domain Constraints can be complex to implement and maintain.
- They can limit the flexibility of the database and make it difficult to make changes to the schema.
- They can slow down the performance of the database.

#### Examples of Domain Constraints
- An attribute that stores the date of birth of a person could have a range constraint that limits the range of dates to a certain period.
- An attribute that stores the phone number of a person could have a unique constraint to ensure that no two people have the same phone number.
- An attribute that stores the gender of a person could have a default constraint that sets the gender to “not specified” in case no gender is provided.

#### Applications of Domain Constraints
- Domain Constraints are used in all types of databases to ensure the integrity and consistency of the data.
- They are especially useful in financial and medical databases where accuracy and consistency are crucial.
- They are also used in e-commerce and online retail databases to ensure the accuracy of customer information.