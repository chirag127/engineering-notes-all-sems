 Here is the content in markdown format for the topic ### attributes for the notes of the Unit 3 - Relational Database Concepts in the subject of Basics of Data Base Management System:

# Attributes

- Attributes are the properties or characteristics of an entity. For example, for a STUDENT entity, attributes can be name, roll number, age, address, etc.
- Attributes have values. For example, the attribute name may have a value 'John' for a particular student.
- Each attribute has a data type associated with it which constrains the values that can be stored in it. For example, the attribute age may have an integer data type and thus can only store whole numbers.
- Attributes are defined by the data modeler (database designer) based on the requirements.
- Composite attributes can be created from multiple attributes. For example, name can be split into first_name and last_name.
- Derived attributes are attributes whose values can be calculated from other attributes. For example, age can be calculated if date_of_birth is given.
- Relationships are established between entities based on common attributes.
- Choose appropriate names for attributes which are descriptive and imply the semantic meaning.

**Diagrams:**

Here is an entity-relationship diagram showing some attributes for Student:

[A diagram showing Student entity with name, roll_number, age and address attributes]

**Examples:**

- For an EMPLOYEE entity: id, name, salary, department_id, etc.
- For a PRODUCT entity: id, name, price, quantity_in_stock, etc.

**Advantages:**

- Attributes provide meaning to data and make it useful.
- They enable establishing relationships between entities.
- They make it easy to understand and query the database.

**Disadvantages:**

- Too many attributes can make the design complex.
- If not chosen properly, attributes may not be descriptive enough or may be redundant.

**Applications:**

Attributes are fundamental components of any database design and are used in all database applications. They are essential to model the elements and aspects of the real-world scenario that the database is being designed for.