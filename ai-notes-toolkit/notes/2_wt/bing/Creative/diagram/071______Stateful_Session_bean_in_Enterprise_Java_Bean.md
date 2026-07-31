A stateful session bean is a type of enterprise bean that preserves the conversational state with the client. It keeps the associated client state in its instance variables. The EJB container creates a separate stateful session bean for each client request .

A stateful session bean has a lifecycle that consists of four stages: does not exist, method-ready, passivated, and removed. The following diagram shows the lifecycle of a stateful session bean in ASCII art:

```
+----------------+   create()   +-----------------+   ejbCreate()   +-----------------+
| Does not exist | -----------> | Method-Ready    | -------------> | Method-Ready    |
|                |              | (No-EJB object) |                | (EJB object)    |
+----------------+              +-----------------+                +-----------------+
                                                                    |    |    |
                                                                    |    |    |
                                                                    |    |    |
                                                                    |    |    |
                                                                    |    |    |
                                                                    |    |    |
                                                                    |    |    |
                                                                    |    |    |
                                                                    |    |    |
                                                                    |    |    |
                                                                    |    |    |
                                                                    |    |    |
                                                                    |    |    |
+----------------+   remove()   +-----------------+   ejbRemove()   +-----------------+
| Does not exist | <----------- | Method-Ready    | <------------- | Method-Ready    |
|                |              | (No-EJB object) |                | (EJB object)    |
+----------------+              +-----------------+                +-----------------+
                                                                    |    |
                                                                    |    |
                                                                    |    |
                                                                    |    |
                                                                    |    |
                                                                    |    |
                                                                    |    |
                                                                    |    |
                                                                    |    |
                                                                    |    |
                                                                    |    |
                                                                    |    |
                                                                    |    |
+----------------+   passivate() +-----------------+   ejbPassivate() +-----------------+
| Does not exist | <------------ | Method-Ready    | <-------------- | Method-Ready    |
|                |               | (No-EJB object) |                 | (EJB object)    |
+----------------+               +-----------------+                 +-----------------+
                                 |    |
                                 |    |
                                 |    |
                                 |    |
                                 |    |
                                 |    |
                                 |    |
                                 |    |
                                 |    |
                                 |    |
                                 |    |
                                 |    |
                                 |    |
+----------------+   activate() +-----------------+   ejbActivate() +-----------------+
| Does not exist | -----------> | Method-Ready    | -------------> | Method-Ready    |
|                |              | (No-EJB object) |                | (EJB object)    |
+----------------+              +-----------------+                +-----------------+
```