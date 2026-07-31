#### Cohesion Measures in Software Design

Cohesion refers to the degree to which the elements of a module belong together. In software design, it is considered desirable to have high cohesion. There are several measures of cohesion, including:

```
+----------------------+------------------------------------------------+
| Measure              | Description                                    |
+----------------------+------------------------------------------------+
| Coincidental         | Elements grouped together with no meaningful   |
|                      | relationship.                                  |
+----------------------+------------------------------------------------+
| Logical              | Elements grouped together because they are     |
|                      | logically related.                             |
+----------------------+------------------------------------------------+
| Temporal             | Elements grouped together because they are     |
|                      | related in time.                               |
+----------------------+------------------------------------------------+
| Procedural           | Elements grouped together because they are     |
|                      | part of a procedure.                           |
+----------------------+------------------------------------------------+
| Communicational      | Elements grouped together because they operate |
|                      | on the same data.                              |
+----------------------+------------------------------------------------+
| Sequential           | Elements grouped together because the output   |
|                      | of one is the input of another.                |
+----------------------+------------------------------------------------+
| Functional           | Elements grouped together because they         |
|                      | contribute to a single well-defined task.      |
+----------------------+------------------------------------------------+
```
