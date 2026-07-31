#### Schema Design in HBase

- HBase schema design is very different compared to the relation database schema design .
- HBase does not support any kind of joins, but it provides the single-indexing strategy on the row key .
- Each table in HBase is indexed on the row key. Data is sorted lexicographically by this row key .
- HBase schema design supports denormalization with nested entities. These nested entities are nothing but a column whose name is the unique identifier for the nested entity and whose value is the entire record mashed together. Since HBase allows dynamic column definition, there's no problem .
