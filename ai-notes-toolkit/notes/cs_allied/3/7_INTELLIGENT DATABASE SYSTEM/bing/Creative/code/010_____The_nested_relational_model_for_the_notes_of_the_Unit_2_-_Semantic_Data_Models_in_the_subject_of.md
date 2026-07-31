# The nested relational model

- The nested relational model is an extension of the relational model in which domains may be either atomic or relation-valued .
- This allows a complex object to be represented by a single tuple of a nested relation, which has a one-to-one correspondence between data items and objects.
- A nested relation can be seen as a relation of relations, where each tuple may contain one or more sub-relations as attribute values.
- A nested relation schema can be defined recursively as follows:
  - A nested relation schema is a set of attributes, each of which has a name and a type.
  - A type can be either atomic or a nested relation schema.
  - An atomic type is a predefined data type, such as integer, string, or boolean.
  - A nested relation schema can be denoted by R(A1:T1, A2:T2, ..., An:Tn), where R is the name of the relation, Ai is the name of the ith attribute, and Ti is the type of the ith attribute.
- A nested relation instance can be defined recursively as follows:
  - A nested relation instance is a set of tuples, each of which conforms to a nested relation schema.
  - A tuple conforms to a nested relation schema if it has the same number of attribute values as the schema, and each attribute value is of the same type as the corresponding attribute in the schema.
  - An attribute value is of an atomic type if it is a constant of that type, such as 42, "hello", or true.
  - An attribute value is of a nested relation schema type if it is a nested relation instance that conforms to that schema.
  - A nested relation instance can be denoted by {t1, t2, ..., tm}, where ti is the ith tuple of the instance.
- An example of a nested relation schema and instance is shown below:

| Name | Address | Phone | Courses |
| --- | --- | --- | --- |
| string | R(Street:string, City:string, Zip:string) | string | R(CourseId:string, Grade:string) |

| Name | Address | Phone | Courses |
| --- | --- | --- | --- |
| Alice | {("123 Main St.", "New York", "10001")} | "555-1111" | {("CS101", "A"), ("CS102", "B")} |
| Bob | {("456 Elm St.", "Boston", "02115")} | "555-2222" | {("CS101", "B"), ("CS103", "C")} |
| Carol | {("789 Pine St.", "Seattle", "98101")} | "555-3333" | {("CS102", "A"), ("CS103", "B")} |

- The nested relational model has some advantages over the flat relational model, such as :
  - It can represent complex objects and relationships more naturally and compactly, without requiring normalization or decomposition.
  - It can support more expressive queries and operations, such as nested aggregation, grouping, and projection.
  - It can preserve the semantics and integrity of the data, by avoiding null values, dangling references, and redundancy.
- The nested relational model also has some challenges and limitations, such as :
  - It requires extensions to the relational algebra and calculus, and the SQL language, to manipulate nested relations.
  - It may incur higher storage and processing costs, due to the increased complexity and size of the data.
  - It may lose some of the desirable properties of the flat relational model, such as closure, independence, and normalization.