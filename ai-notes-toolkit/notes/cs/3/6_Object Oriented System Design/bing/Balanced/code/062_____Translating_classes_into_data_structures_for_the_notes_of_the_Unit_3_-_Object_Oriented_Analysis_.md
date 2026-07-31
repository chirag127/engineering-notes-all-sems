### Translating classes into data structures

- Translating classes into data structures is the process of implementing each class as a single contiguous block of attributes, also known as a record structure.
- Each attribute has a declared type, which can be a primitive type, such as integer, real or character, or a structured type, such as an embedded record structure or a fixed-length array.
- Each class in the design becomes a C struct, and each attribute defined in the class becomes a field of the C struct.
- Translating classes into data structures is necessary when using a non-object oriented language, such as C, to implement an object-oriented concept.
- Translating classes into data structures is different from translating classes into relational database tables, which requires mapping the object model to the relational model.