Session tracking is a mechanism that servlets use to maintain state about a series of requests from the same user across some period of time. There are four techniques used in session tracking: cookies, hidden form fields, URL rewriting and HttpSession. HttpSession is an interface that provides a way to identify a user across more than one page request or visit to a website and to store information about that user.

Here is a detailed ASCII diagram for session tracking in servlets using HttpSession:

### Session Tracking in Servlets

```
  +-----------------+            +-----------------+            +-----------------+
  |                 |            |                 |            |                 |
  |  Web Browser    |            |  Web Server     |            |  Servlet        |
  |                 |            |                 |            |                 |
  +-----------------+            +-----------------+            +-----------------+
        |                             |                             |
        |  Request a servlet         |                             |
        |--------------------------->|                             |
        |                             |                             |
        |                             |  Forward request to servlet |
        |                             |---------------------------> |
        |                             |                             |
        |                             |                             |  Create a new session
        |                             |                             |  object and assign a
        |                             |                             |  unique session ID
        |                             |                             |
        |                             |                             |  Store session ID in
        |                             |                             |  a cookie or URL
        |                             |                             |
        |                             |  Return response with       |
        |                             |  session ID                 |
        |                             |<--------------------------- |
        |                             |                             |
        |  Receive response with     |                             |
        |  session ID                 |                             |
        |<--------------------------- |                             |
        |                             |                             |
        |  Send another request with |                             |
        |  session ID                 |                             |
        |--------------------------->|                             |
        |                             |                             |
        |                             |  Forward request to servlet |
        |                             |---------------------------> |
        |                             |                             |
        |                             |                             |  Retrieve the session
        |                             |                             |  object using the
        |                             |                             |  session ID
        |                             |                             |
        |                             |                             |  Perform some actions
        |                             |                             |  on the session object
        |                             |                             |
        |                             |  Return response            |
        |                             |<--------------------------- |
        |                             |                             |
        |  Receive response          |                             |
        |<--------------------------- |                             |
        |                             |                             |
        |                             |                             |
```