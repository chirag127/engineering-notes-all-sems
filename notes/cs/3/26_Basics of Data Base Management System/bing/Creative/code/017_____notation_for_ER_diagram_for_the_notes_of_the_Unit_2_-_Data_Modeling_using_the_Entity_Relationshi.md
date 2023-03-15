# Notation for ER diagram

An ER diagram is a graphical representation of the entities and their relationships in a database. It helps to design and understand the logical structure of the data. There are different notations and symbols used to create an ER diagram, depending on the preference and convention of the modeler. Some of the common notations and symbols are:

- **Crow's foot notation**: This is the most intuitive and widely used notation for ER diagrams. It uses symbols to indicate the cardinality and optionality of the relationships between entities. The symbols are placed at the end of the relationship line, near the entity. The symbols are:

  - A single line indicates a **one** relationship, meaning that each instance of an entity can be related to only one instance of another entity.
  - A double line indicates a **one and only one** relationship, meaning that each instance of an entity must be related to exactly one instance of another entity.
  - A three-pronged fork (or crow's foot) indicates a **many** relationship, meaning that each instance of an entity can be related to many instances of another entity.
  - An open circle indicates a **zero or one** relationship, meaning that each instance of an entity can be related to zero or one instance of another entity.
  - A filled circle indicates a **zero and only one** relationship, meaning that each instance of an entity must be related to zero or one instance of another entity.
  - A half-open half-filled circle indicates a **one or many** relationship, meaning that each instance of an entity can be related to one or many instances of another entity.

  For example, the following ER diagram shows the relationship between students and courses using crow's foot notation:

  ![ER diagram using crow's foot notation](https://www.guru99.com/images/1/020819_0619_ERDiagramTu1.png)

  The diagram shows that:

  - A student can enroll in zero or many courses, and a course can have zero or many students enrolled in it. This is a **many-to-many** relationship, indicated by the crow's feet on both ends of the line.
  - A student can have zero or one advisor, and an advisor can advise one or many students. This is a **one-to-many** relationship, indicated by the single line and the crow's foot on opposite ends of the line.
  - A student must have one and only one department, and a department can have one or many students. This is a **one-to-many** relationship, indicated by the double line and the crow's foot on opposite ends of the line.

- **Chen notation**: This is another popular notation for ER diagrams, developed by Peter Chen in 1976. It uses rectangles to represent entities, diamonds to represent relationships, and ovals to represent attributes. The cardinality and optionality of the relationships are indicated by numbers or symbols inside the diamonds. The numbers or symbols are:

  - 1 indicates a **one** relationship, meaning that each instance of an entity can be related to only one instance of another entity.
  - N or M indicates a **many** relationship, meaning that each instance of an entity can be related to many instances of another entity.
  - 0 or O indicates a **zero** relationship, meaning that each instance of an entity can be related to zero instances of another entity.
  - 1,1 indicates a **one and only one** relationship, meaning that each instance of an entity must be related to exactly one instance of another entity.
  - 0,1 indicates a **zero or one** relationship, meaning that each instance of an entity can be related to zero or one instance of another entity.
  - 1,N or 1,M indicates a **one or many** relationship, meaning that each instance of an entity can be related to one or many instances of another entity.

  For example, the following ER diagram shows the relationship between students and courses using Chen notation:

  ![ER diagram using Chen notation](https://www.guru99.com/images/1/020819_0619_ERDiagramTu2.png)

  The diagram shows that:

  - A student can enroll in zero or many courses, and a course can have zero or many students enrolled in it. This is a **many-to-many** relationship, indicated by the N on both sides of the diamond.
  - A student can have zero or one advisor, and an advisor can advise one or many students. This is a **one-to-many** relationship, indicated by the 1 and N on opposite sides of the diamond.
  - A