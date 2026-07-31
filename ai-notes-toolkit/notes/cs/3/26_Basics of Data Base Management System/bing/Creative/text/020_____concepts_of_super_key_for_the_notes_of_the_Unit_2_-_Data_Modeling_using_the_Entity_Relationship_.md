### Concepts of Super Key

- A super key is a set of one or more attributes that can uniquely identify each record or tuple in a table.  
- A super key may have additional attributes that are not needed for unique identification.  
- A super key is a superset of a candidate key, which is a minimal set of attributes that can uniquely identify each record or tuple in a table. 
- There can be more than one super key in a table, and it can also be NULL. 
- For example, in a table of students, the attributes {Student_ID}, {Student_Name, Phone_Number}, and {Student_ID, Student_Name, Phone_Number} are all super keys, but only {Student_ID} is a candidate key.