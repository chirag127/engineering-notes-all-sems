### Concepts of Super Key

- A super key is a set of one or more attributes that can uniquely identify each record or tuple in a table  .
- A super key may have additional attributes that are not needed for unique identification .
- A super key is a superset of a candidate key, which is a minimal set of attributes that can uniquely identify each record or tuple in a table .
- A super key can also be NULL, which means that the attribute value is unknown or missing.
- A table can have more than one super key, but only one primary key, which is a chosen candidate key  .
- A super key can be used to enforce referential integrity, which means that the values of a foreign key in one table must match the values of a primary key in another table.

#### Example of Super Key

Consider the following table of students:

| Student_ID | Name | Email | Phone |
|------------|------|-------|-------|
| 101        | Alice | alice@gmail.com | 1234567890 |
| 102        | Bob   | bob@yahoo.com   | 2345678901 |
| 103        | Carol | carol@hotmail.com | 3456789012 |

Some possible super keys for this table are:

- {Student_ID}
- {Email}
- {Student_ID, Name}
- {Email, Phone}
- {Student_ID, Name, Email, Phone}

The first two super keys are also candidate keys, as they are minimal sets of attributes that can uniquely identify each record. The last three super keys are not candidate keys, as they have additional attributes that are not needed for unique identification. The primary key can be chosen from any of the candidate keys, such as {Student_ID} or {Email}.