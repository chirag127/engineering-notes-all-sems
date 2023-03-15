### Reduction of an ER Diagrams to Tables

1. **Entity Sets to Tables**: Each entity set is converted into a table. Each attribute of the entity set becomes a column in the table, and each instance of the entity set becomes a row in the table.

2. **Relationship Sets to Tables**: Each relationship set is also converted into a table. The primary key of this table is a combination of the primary keys of the participating entity sets. Attributes of the relationship set become columns in the table.

3. **Representing Weak Entity Sets**: Weak entity sets are represented as tables with the addition of columns for the primary key of the identifying strong entity set. The primary key of the weak entity set table is a combination of the primary key of the identifying strong entity set and the partial key of the weak entity set.

4. **Representing ISA Hierarchies**: There are three main approaches to representing ISA hierarchies: using a separate table for each entity set in the hierarchy, using a single table with a type attribute, and using a single table with multiple type attributes.

5. **Representing Multi-valued Attributes**: Multi-valued attributes are represented by creating a new table for the attribute. The primary key of this table is a combination of the primary key of the entity set and the multi-valued attribute.

6. **Representing N-ary Relationship Sets**: N-ary relationship sets are represented as tables with columns for the primary keys of the participating entity sets and any attributes of the relationship set. The primary key of this table is a combination of the primary keys of the participating entity sets.