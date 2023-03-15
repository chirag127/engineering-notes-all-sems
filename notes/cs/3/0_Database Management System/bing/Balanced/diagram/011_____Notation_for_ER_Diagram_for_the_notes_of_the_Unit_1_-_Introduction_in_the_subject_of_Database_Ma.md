### Notation for ER Diagram

- ER diagram stands for Entity Relationship diagram, which is a graphical representation of the logical structure of a database.
- ER diagram shows the entities, attributes and relationships of a database schema.
- There are different notations and symbols used to draw ER diagrams, depending on the level of abstraction and the modeling methodology .
- Some of the common notations and symbols are:

  - **Arrow notation**: This notation uses arrows to indicate the cardinality and participation of entities in a relationship. For example, a single-headed arrow with an open circle means zero or one, a single-headed arrow with a solid circle means one and only one, a double-headed arrow means one or many, and a line without an arrow means many.
  - **Barker's notation**: This notation uses boxes for entities, ovals for attributes, and diamonds for relationships. The cardinality and participation are shown by placing a number or a letter inside the relationship diamond or on the line connecting the entities. For example, 1 means one and only one, M means many, N means none, and O means optional.
  - **Chen's notation**: This notation uses rectangles for entities, ovals for attributes, and diamonds for relationships. The cardinality and participation are shown by placing a number or a symbol on the line connecting the entities. For example, 1 means one and only one, N means many, (0,1) means zero or one, and (1,N) means one or many.
  - **Crow's foot notation**: This notation uses rectangles for entities, ovals for attributes, and lines for relationships. The cardinality and participation are shown by placing a symbol at the end of the line connecting the entities. For example, a single line means one and only one, a double line means one or more, a circle means zero or one, and a crow's foot means many.
  - **UML notation**: This notation uses rectangles for entities, ovals for attributes, and lines for relationships. The cardinality and participation are shown by placing a number or a symbol at the end of the line connecting the entities. For example, 1 means one and only one, * means many, 0..1 means zero or one, and 1..* means one or many.
  - **Min-Max notation**: This notation uses rectangles for entities, ovals for attributes, and lines for relationships. The cardinality and participation are shown by placing a pair of numbers in parentheses at the end of the line connecting the entities. For example, (1,1) means one and only one, (0,N) means zero or many, (0,1) means zero or one, and (1,N) means one or many.

- Here are some examples of ER diagrams using different notations and symbols:

  - Arrow notation:

    ```
    +----------+       +----------+
    | Employee |       |  Project |
    +----------+       +----------+
    | emp_id   |       | proj_id  |
    | name     |       | name     |
    | salary   |       | budget   |
    +----------+       +----------+
         |                  |
         |                  |
         |                  |
         |                  |
         |                  |
         |                  |
         |                  |
         |                  |
         |                  |
         |                  |
         |                  |
         |                  |
         |                  |
         |                  |
         |                  |
         |                  |
         |                  |
    +----|----+             |
    | WorksOn |<------------+
    +----|----+
    | hours  |
    +----|----+
    ```

    In this diagram, the relationship WorksOn has a single-headed arrow with a solid circle on the Employee side, meaning each employee works on one and only one project. The relationship WorksOn has a double-headed arrow on the Project side, meaning each project has one or many employees working on it. The attribute hours is shown inside the relationship WorksOn.

  - Barker's notation:

    ```
    +----------+       +----------+
    | Employee |       |  Project |
    +----------+       +----------+
    | emp_id   |       | proj_id  |
    | name     |       | name     |
    |