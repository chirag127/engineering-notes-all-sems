A stateless session bean is a type of enterprise bean, which is normally used to perform independent operations. A stateless session bean as per its name does not have any associated client state, but it may preserve its instance state .

The following diagram illustrates the basic architecture of a stateless session bean in enterprise java bean using ASCII art:

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|    Client      |     |    EJB Home    |     |    EJB Object  |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|    JNDI        |     |    EJB Pool    |     |    EJB Bean    |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
```

The steps involved in the diagram are:

- The client looks up the EJB home interface in the JNDI directory.
- The client invokes a method on the EJB home interface to create an EJB object.
- The EJB container selects an available EJB bean from the EJB pool and assigns it to the EJB object.
- The EJB object invokes the business method on the EJB bean.
- The EJB bean performs the business logic and returns the result to the EJB object.
- The EJB object returns the result to the client.
- The EJB bean is returned to the EJB pool for reuse by other EJB objects.