Session tracking is the process of remembering and documenting customer conversions over time. Session tracking allows the server to keep track of successive requests made by the same client. The session is created between an HTTP client and an HTTP server by the servlet container using HttpSession. The session object will be available to all of the servlets and JSP’s that the user accesses until the session is closed due to timeout or error.

The following diagram illustrates the basic architecture of a session tracking with Http Session in Servlets:

```
+----------------+        +----------------+        +----------------+
|                |        |                |        |                |
|    Browser     |        |    Servlet     |        |    Database    |
|                |        |    Container   |        |                |
+----------------+        +----------------+        +----------------+
     |   |                     |   |                     |   |
     |   |                     |   |                     |   |
     |   |                     |   |                     |   |
     |   |                     |   |                     |   |
     |   |                     |   |                     |   |
     |   |                     |   |                     |   |
     |   |                     |   |                     |   |
     |   |                     |   |                     |   |
     |   |                     |   |                     |   |
     |   |                     |   |                     |   |
     |   |                     |   |                     |   |
     |   | 1. Request         |   |                     |   |
     |   |-------------------->|   |                     |   |
     |   |                     |   |                     |   |
     |   |                     |   | 2. Create session   |   |
     |   |                     |   |-------------------->|   |
     |   |                     |   |                     |   |
     |   |                     |   |<--------------------|   |
     |   |                     |   | 3. Return session   |   |
     |   |                     |   |                     |   |
     |   |                     |   | 4. Set session ID   |   |
     |   |                     |   |                     |   |
     |   |<--------------------|   | 5. Response         |   |
     |   | 6. Get session ID  |   |                     |   |
     |   |                     |   |                     |   |
     |   | 7. Request         |   |                     |   |
     |   |-------------------->|   |                     |   |
     |   |                     |   | 8. Get session ID   |   |
     |   |                     |   |                     |   |
     |   |                     |   | 9. Retrieve session |   |
     |   |                     |   |-------------------->|   |
     |   |                     |   |                     |   |
     |   |                     |   |<--------------------|   |
     |   |                     |   | 10. Return session  |   |
     |   |                     |   |                     |   |
     |   |<--------------------|   | 11. Response        |   |
     |   | 12. Get session ID |   |                     |   |
     |   |                     |   |                     |   |
     |   | ...                |   | ...                 |   |
     |   |                     |   |                     |   |
     |   | 13. Request        |   |                     |   |
     |   |-------------------->|   |                     |   |
     |   |                     |   | 14. Get session ID  |   |
     |   |                     |   |                     |   |
     |   |                     |   | 15. Invalidate      |   |
     |   |                     |   | session             |   |
     |   |                     |   |-------------------->|   |
     |   |                     |   |                     |   |
     |   |                     |   |<--------------------|   |
     |   |                     |   | 16. Return          |   |
     |   |                     |   | confirmation        |   |
     |   |                     |   |                     |   |
     |   |<--------------------|   | 17. Response        |   |
     |   | 18. Delete session |   |                     |   |
     |   | ID                  |   |                     |   |
     |   |                     |   |                     |   |
```