 Here is the content in markdown format for the given topic:

### MVD (Multi-valued Dependency) for Unit 3 - Data Base Design & Normalization

- MVD is a type of dependency between attributes in a relation where a attribute can have multiple values for a single value of another attribute.
- For example, in a relation containing employee details - An employee can have multiple skills. Here 'Employee_ID' is the determinant and 'Skills' is the dependent attribute exhibiting MVD.
- MVD leads to insertion, deletion and update anomalies if the relation is not normalized.
- To remove MVD, the relation can be split into two relations - one containing the determinant attribute and the other containing the dependent multi-valued attribute.
- For example, the employee relation can be split into two relations - 'Employee_Details' containing 'Employee_ID' and other attributes, and 'Employee_Skills' containing 'Employee_ID' and 'Skills'.
- This split eliminates the MVD and the relation is said to be in 3NF (Normal Form), i.e. free of MVDs.
- Hence, removal of MVDs by splitting relations is important to achieve higher normal forms and improve data integrity.

[Detailed diagrams and examples can be added here to explain MVD and split of relations in a better way for learning.]

[Advantages and disadvantages of MVD and ways to handle MVD can also be included for complete study material.]

[Application of concepts of MVD to real-world database design problems can be discussed to relate theory with practical scenarios.]