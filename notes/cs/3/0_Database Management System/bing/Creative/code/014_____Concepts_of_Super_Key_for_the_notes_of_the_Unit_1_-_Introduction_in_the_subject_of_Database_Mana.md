Hello, I am Sydney, your AI assistant. I can help you with your study material for Database Management System. Here are some notes on the topic of Super Key.

### Concepts of Super Key

- A super key is a set of one or more attributes that can uniquely identify a tuple (or row) in a relation (or table) of a database.
- A super key may contain extra attributes that are not necessary for unique identification.
- A super key is a superset of a candidate key, which is a minimal set of attributes that can uniquely identify a tuple.
- A candidate key is also a super key, but not every super key is a candidate key.
- For example, in a relation STUDENT with attributes Roll_No, Name, Address, and Phone, the following are some possible super keys:

  - {Roll_No}
  - {Name, Phone}
  - {Roll_No, Name, Address, Phone}
  - {Roll_No, Name}
  - {Name, Address, Phone}

- Out of these, only {Roll_No} and {Name, Phone} are candidate keys, as they are minimal. The rest are super keys but not candidate keys, as they contain extra attributes.
- A super key can be used to enforce entity integrity, which means that no two tuples in a relation can have the same values for the super key attributes.
- A super key can also be used to define foreign key constraints, which means that the values of the super key attributes in one relation must match the values of the corresponding candidate key attributes in another relation.