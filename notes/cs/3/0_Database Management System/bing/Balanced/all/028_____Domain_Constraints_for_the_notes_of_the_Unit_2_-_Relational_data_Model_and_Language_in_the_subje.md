# Domain Constraints for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- Domain constraints are the rules that specify the allowed values for each attribute or column in a relation or table .
- Domain constraints are a type of integrity constraint that ensures the data quality and accuracy in a relational database .
- Domain constraints can be defined by the data type, format, range, or set of values for each attribute or column .
- Domain constraints can be enforced by the database management system (DBMS) or by the application program that manipulates the data .
- Domain constraints are important because they prevent the insertion of invalid or inconsistent data into the database, and they help to maintain the semantic meaning of the data .

Some examples of domain constraints are:

- The attribute `Student_ID` in the relation `Student` must be an integer value between 1000 and 9999.
- The attribute `Email` in the relation `Customer` must be a string value that follows the format of `name@domain.com`.
- The attribute `Gender` in the relation `Employee` must be a character value that belongs to the set of values `{'M', 'F', 'O'}`.