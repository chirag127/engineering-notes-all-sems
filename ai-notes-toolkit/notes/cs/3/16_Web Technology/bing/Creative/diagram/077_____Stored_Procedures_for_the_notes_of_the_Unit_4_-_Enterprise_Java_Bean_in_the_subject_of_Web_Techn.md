### Stored Procedures

- Stored procedures are **Java methods** that are **published to SQL** and **stored in the database** for general use.
- Stored procedures can perform **database manipulation** and **business logic** tasks that are otherwise done by the application layer.
- Stored procedures can improve **performance**, **security**, and **maintainability** of the application.
- To create and use a stored procedure in Java DB, the following steps are required:
  - Create a **public static Java method** in a Java class that performs the required task of the stored procedure.
  - Create the **stored procedure** in the database that calls the Java method using a **call specification**. A call specification maps the Java method name, parameter types, and return types to their SQL counterparts.
  - Call the stored procedure from the application using a **CallableStatement** object. A CallableStatement object can execute a stored procedure and retrieve its output parameters and result sets.
- To call a stored procedure from JPA, the following steps are required:
  - Annotate the entity class with **@NamedStoredProcedureQuery** to define the stored procedure name, parameters, and result class.
  - Use the **EntityManager** to create a **StoredProcedureQuery** object with the stored procedure name.
  - Set the input parameters and execute the query using the **execute()** method.
  - Get the output parameters and result sets using the **getOutputParameterValue()** and **getResultList()** methods.