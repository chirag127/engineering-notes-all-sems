 Here are the notes for Unit 2 - Relational data Model and Language in the subject of Database Management System:

### Relational Model

- Data is organized into one or more tables (relations) of columns and rows.
- Each column has a name and contains values of a particular kind, like integers, floats, strings, etc.
- Each row contains a record (tuple) with a unique primary key.
- Tables are related to each other using common attributes (foreign keys).
- Advantages: Structured, efficient storage, powerful query language (SQL), data independence.

### Relational Algebra

- Set of operators to manipulate relations.
- Selection (σ) - Removes unwanted rows.
- Projection (π) - Removes unwanted columns.
- Union (U), Intersection (⋂), Difference (-) - Combine rows of two relations.
- Join (⋈) - Combine rows from two relations based on a common attribute.
- Divide (÷), Aggregate (Λ) - Advanced operators.
- Results of operators are relations.
- Basis for relational calculus and SQL.

### Relational Calculus

- Declarative language to specify what to retrieve without specifying how to retrieve it.
- Tuple relational calculus - Specifies rows to retrieve based on constraint.
- Domain relational calculus - Specifies column values to retrieve based on constraint.
- Calculus has variable ranging over domain of discourse. Query evaluator uses algorithms to determine efficient evaluation strategy.
- Basis for SQL SELECT queries.

The notes are written in a formal tone with points and without any emojis or external links as requested. The content is written inside header markup and in Markdown format. Please let me know if you would like me to modify or add anything.