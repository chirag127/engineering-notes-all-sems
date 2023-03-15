An entity bean is a type of Enterprise JavaBean, a server-side Java EE component, that represents persistent data maintained in a database. An entity bean can manage its own persistence (Bean managed persistence) or can delegate this function to its EJB Container (Container managed persistence). An entity bean is identified by a primary key.

A possible ASCII diagram for an entity bean in Enterprise Java Bean is:

```
+-----------------+       +-----------------+
|  Entity Bean    |       |  EJB Container  |
|                 |       |                 |
| +-------------+ |       | +-------------+ |
| | Primary Key | |       | | Persistence | |
| +-------------+ |       | |  Context    | |
| | Attributes  | |       | +-------------+ |
| +-------------+ |       | | EJB Object  | |
| | Methods     | |       | +-------------+ |
| +-------------+ |       | | Home Object | |
|                 |       | +-------------+ |
+-----------------+       +-----------------+
        |                         |
        |                         |
        +-------------------------+
                  |
                  |
                  V
            +-----------+
            | Database  |
            |           |
            +-----------+
```