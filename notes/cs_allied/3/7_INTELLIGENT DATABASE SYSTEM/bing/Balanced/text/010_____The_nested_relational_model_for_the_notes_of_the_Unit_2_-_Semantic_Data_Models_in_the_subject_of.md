### The nested relational model

- The nested relational model is an extension of the relational model in which domains may be either atomic or relation-valued .
- This allows a complex object to be represented by a single tuple of a nested relation, which has a one-to-one correspondence between data items and objects.
- A nested relation can be seen as a relation of relations, where each tuple may contain other tuples as attribute values.
- A nested relation schema can be defined recursively as follows:

  - A nested relation schema is either an atomic type or a set of attribute-name/type pairs, where each type is a nested relation schema.
  - A nested relation instance is either an atomic value or a set of tuples, where each tuple is an instance of a nested relation schema.

- For example, consider the following nested relation schema and instance:

  - Schema: `EMPLOYEE(Name, Address, Phone, Projects)`
  - Type of `Name`: `String`
  - Type of `Address`: `String`
  - Type of `Phone`: `String`
  - Type of `Projects`: `PROJECT(Pname, Budget, Members)`
  - Type of `Pname`: `String`
  - Type of `Budget`: `Number`
  - Type of `Members`: `String`
  - Instance:

| Name | Address | Phone | Projects |
| --- | --- | --- | --- |
| Alice | 123 Main St. | 555-1234 | { (P1, 1000, {Bob, Carol}), (P2, 2000, {Dave, Eve}) } |
| Bob | 456 Maple Ave. | 555-2345 | { (P1, 1000, {Alice, Carol}), (P3, 3000, {Frank, Grace}) } |
| Carol | 789 Elm St. | 555-3456 | { (P1, 1000, {Alice, Bob}), (P4, 4000, {Harry, Irene}) } |

- The nested relational model supports various operations to manipulate nested relations, such as:

  - Projection: selecting a subset of attributes from a nested relation.
  - Restriction: selecting a subset of tuples from a nested relation based on a condition.
  - Join: combining two nested relations based on a common attribute.
  - Unnest: flattening a nested relation by removing one level of nesting.
  - Nest: creating a nested relation by grouping tuples based on a common attribute.
  - Aggregate: applying a function to a set of values in a nested relation.

- The nested relational model can be used to model complex and hierarchical data, such as:

  - Documents: a document can be seen as a nested relation of sections, paragraphs, sentences, words, etc.
  - XML: an XML document can be seen as a nested relation of elements, attributes, text, etc.
  - JSON: a JSON object can be seen as a nested relation of key-value pairs, where the values can be nested relations themselves.
  - Graphs: a graph can be seen as a nested relation of nodes, edges, labels, etc.