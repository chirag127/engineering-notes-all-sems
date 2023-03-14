#### Entity bean in Enterprise Java Bean

- An entity bean is a type of Enterprise Java Bean (EJB), a server-side Java EE component, that represents persistent data maintained in a database .
- An entity bean can manage its own persistence (Bean managed persistence) or can delegate this function to its EJB Container (Container managed persistence) .
- An entity bean is identified by a primary key, which is a unique identifier for each instance of the bean .
- Entity beans can be accessed by multiple clients concurrently and can participate in transactions.
- Entity beans were superseded by the Java Persistence API (JPA) in EJB 3.0 and are considered a deprecated technology as of Java EE 6 .
- Entity beans before EJB 2.0 had performance issues due to the use of RMI stubs and connections for each bean instance .
- Entity beans have a life cycle that consists of four states: does not exist, pooled, ready, and passive.