### Concepts of Super Key

- A super key is a set of one or more attributes that can uniquely identify each record or tuple in a table.  
- A super key may have additional attributes that are not necessary for unique identification.  
- A super key is a superset of a candidate key, which is a minimal set of attributes that can uniquely identify each record or tuple in a table. 
- There can be more than one super key for a table, and a super key can also be NULL. 
- For example, consider a table STUDENT with attributes Roll_No, Name, Address, and Phone_No. The possible super keys are:

  - {Roll_No}
  - {Name, Phone_No}
  - {Roll_No, Name}
  - {Roll_No, Address}
  - {Roll_No, Phone_No}
  - {Roll_No, Name, Address}
  - {Roll_No, Name, Phone_No}
  - {Roll_No, Address, Phone_No}
  - {Roll_No, Name, Address, Phone_No}
  - {Name, Address, Phone_No}

- Among these super keys, only {Roll_No} and {Name, Phone_No} are candidate keys, as they are minimal and cannot be reduced further. The rest of the super keys are not candidate keys, as they have redundant attributes.