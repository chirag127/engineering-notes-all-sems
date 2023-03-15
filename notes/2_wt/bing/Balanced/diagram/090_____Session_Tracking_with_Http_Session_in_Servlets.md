Session tracking is a way to maintain state (data) of an user across multiple requests to the server. Session tracking can be done by the server using the HttpSession interface in servlets. The server assigns a unique session ID to each client and creates a session object to store the session data. The session ID is sent to the client as a cookie or as a part of the URL. The client sends the session ID back to the server in each request. The server uses the session ID to retrieve the session object and access the session data.

Here is a diagram to illustrate the session tracking with Http Session in servlets:

### Session Tracking with Http Session in Servlets

```
    +----------------+            +----------------+            +----------------+
    |                |            |                |            |                |
    |     Client     |            |     Server     |            |   Servlet      |
    |                |            |                |            |                |
    +----------------+            +----------------+            +----------------+
          |                             |                             |
          |  Request                    |                             |
          |---------------------------> |                             |
          |                             |  Create session object     |
          |                             |---------------------------> |
          |                             |  Generate session ID       |
          |                             |<--------------------------- |
          |                             |  Send response with        |
          |                             |  session ID as cookie      |
          |  Response with cookie      |  or URL parameter          |
          |<-------------------------- |                             |
          |                             |                             |
          |  Request with cookie       |                             |
          |---------------------------> |                             |
          |                             |  Retrieve session object   |
          |                             |---------------------------> |
          |                             |  Access session data       |
          |                             |<--------------------------- |
          |                             |  Send response             |
          |  Response                   |                             |
          |<-------------------------- |                             |
          |                             |                             |
          |  Request with cookie       |                             |
          |---------------------------> |                             |
          |                             |  Retrieve session object   |
          |                             |---------------------------> |
          |                             |  Access session data       |
          |                             |<--------------------------- |
          |                             |  Send response             |
          |  Response                   |                             |
          |<-------------------------- |                             |
          |                             |                             |
          |                             |  Invalidate session object |
          |                             |---------------------------> |
          |                             |                             |
          |                             |                             |
```