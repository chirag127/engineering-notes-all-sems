### Domain Constraints

Domain constraints specify that within each tuple, the value of each attribute must be an atomic value from the domain of that attribute. In other words, the domain constraint specifies the set of permissible values that each attribute can take.

- Domain constraints are the most elementary form of integrity constraint.
- They are tested easily by the system whenever a new data item is entered into the database.
- The domain of an attribute is the set of values that the attribute can legitimately take.
- The domain is usually specified when the attribute is first defined, and it is enforced by the system whenever a new value is entered for that attribute.
- The domain can be any data type, such as integer, character, date, etc.
- The domain can also be specified using a range of values, a set of values, or a combination of both.
- The domain can also be specified using a validation rule, which is a logical expression that returns true if the data is valid and false otherwise.