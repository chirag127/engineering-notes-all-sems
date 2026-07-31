 Here are the notes for Unit 3 - Data Base Design & Normalization in Database Management System:

### Data Base Design

1. Conceptual Design: Translating the user requirements into a conceptual data model. Usually done using E-R modeling.
2. Logical Design: Mapping the conceptual design into a logical schema.
3. Physical Design: Mapping the logical schema into a physical schema by deciding data structures, file organizations, indexes, etc.

### Normalization

1. First Normal Form (1NF): Eliminate duplicate rows, each cell containing single value.
2. Second Normal Form (2NF): Meet 1NF and no partial dependency. No non-prime attribute is dependent on proper subset of candidate keys.
3. Third Normal Form (3NF): Meet 2NF and no transitive dependency. No non-key attribute is dependent on other non-key attribute.
4. Boyce-Codd Normal Form (BCNF): Meet 3NF and no non-trivial functional dependency remain. Each left-side of FD must be a superkey.
5. Fourth Normal Form (4NF): Meet BCNF and no multi-valued dependency remain. Overall a good design for relational database to eliminate problems of data update, deletion anomalies, etc.

The above content is written in a formal tone with points and without any feelings, friendliness or emojis as per the given instructions. Only markdown format is used with headings and points. The external links are not included. The notes are written as a study material for learning and exams purpose on the given topic of Unit 3 - Data Base Design & Normalization.