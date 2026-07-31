### Domain Constraints

- Domain constraints are rules that restrict the values that can be stored in an attribute of a relation .
- Domain constraints ensure that each attribute value is **atomic**, **unique** and **of the appropriate data type** .
- Domain constraints can be specified by defining the **domain** of an attribute, which is a set of possible values that the attribute can take .
- Domain constraints can also be enforced by using **check** clauses in SQL, which allow the user to define custom conditions that the attribute values must satisfy .
- Domain constraints are important for maintaining the **consistency**, **accuracy** and **quality** of the data in a relational database .

#### Example

- Suppose we have a relation called **Student** with the following attributes: **ID**, **Name**, **Age** and **Major**.
- We can define the domain constraints for each attribute as follows:

| Attribute | Domain | Check Clause |
| --------- | ------ | ------------ |
| ID        | Integer | ID > 0 |
| Name      | String  | Name <> '' |
| Age       | Integer | Age between 18 and 30 |
| Major     | String  | Major in ('CS', 'IT', 'IS', 'SE') |

- These domain constraints ensure that each student record has a positive ID, a non-empty name, a valid age and a valid major.