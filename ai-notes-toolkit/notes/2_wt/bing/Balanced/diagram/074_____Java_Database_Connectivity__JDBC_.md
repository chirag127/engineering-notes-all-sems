Java Database Connectivity (JDBC) is a standard Java API that allows Java programs to access various types of databases. JDBC supports both two-tier and three-tier models for database access. In the two-tier model, a Java application or applet communicates directly with the database using a JDBC driver. In the three-tier model, a Java application or applet communicates with a middle-tier server that handles the database access using a JDBC driver. The JDBC API consists of two layers: the JDBC API layer and the JDBC Driver layer. The JDBC API layer defines the interfaces and classes that Java applications use to connect to a database, execute SQL statements, and process the results. The JDBC Driver layer implements the JDBC API for a specific database vendor or type. The JDBC Driver Manager is a class that manages the loading and registration of JDBC drivers and provides a connection to a database.

The following diagram shows the basic JDBC architecture in the two-tier model:

```
+----------------+      +-----------------+      +-----------------+
| Java Application |<--->| JDBC API Layer  |<--->| JDBC Driver Layer |
+----------------+      +-----------------+      +-----------------+
                                    |                       |
                                    |                       |
                                    |                       |
                                    v                       v
                              +-----------------+      +-----------------+
                              | JDBC Driver Manager |<--->| Database-specific |
                              +-----------------+      | JDBC Driver       |
                                                      +-----------------+
                                                                |
                                                                |
                                                                |
                                                                v
                                                      +-----------------+
                                                      | Database Server |
                                                      +-----------------+
```