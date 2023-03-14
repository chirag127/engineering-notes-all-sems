### Session Tracking with Http Session in Servlets

Session tracking is the process of maintaining the state of a client-server interaction over multiple requests. Http Session is one of the techniques to implement session tracking in servlets. It uses a unique session ID to identify each client and store the session data on the server side. The session ID can be transmitted using cookies, URL rewriting, or hidden form fields.

The following ASCII diagram illustrates the basic architecture of session tracking with Http Session in servlets:

+----------------+            +----------------+            +----------------+
|                |            |                |            |                |
|     Client     |            |     Server     |            |     Servlet    |
|                |            |                |            |                |
+----------------+            +----------------+            +----------------+
      |                             |                             |
      |  Request with session ID    |                             |
      |---------------------------> |                             |
      |                             |  Lookup session data by ID  |
      |                             |---------------------------> |
      |                             |                             |  Process request
      |                             |                             |  and update session data
      |                             |                             |
      |                             |  Response with session ID   |
      |                             | <---------------------------|
      |  Store session ID in cookie |                             |
      | <---------------------------|                             |
      |                             |                             |
      |                             |                             |