 Here is the content in Markdown format without any emojis or external links and in a formal tone:

### Second Normal Form (2NF)

- Remove partial dependency: The relation is in 2NF if it is in 1NF and no non-prime attribute is dependent on a proper subset of any candidate key.
- A relation is in 2NF if it is in 1NF and every non-prime attribute is fully functionally dependent on the primary key.
- Using foreign keys to join tables and removing partial dependencies leads to second normal form.
- Benefits: Reduces data duplication and anomalies. Data is more consistent.

### Third Normal Form (3NF)

- Remove transitive dependency: The relation is in 3NF if it is in 2NF and no non-prime attribute is transitively dependent on the primary key.
- A relation is in 3NF if it is in 2NF and no non-prime attribute is dependent on other non-prime attributes.
- Removing transitive dependencies leads to third normal form.
- Benefits: Minimizes data duplication and anomalies. Maximizes data consistency.
- Most databases are designed upto 3NF as it achieves most normalization benefits. Going beyond 3NF leads to loss of data integrity and increase in database complexity.

The content summarizes the key points around Second Normal Form and Third Normal Form in Database Normalization. The points are written in a concise yet comprehensive manner with the relevant benefits highlighted. The tone is formal and free of emojis or external links as requested. Please let me know if you would like me to modify or expand the content in any way.