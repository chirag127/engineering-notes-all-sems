Session tracking is a mechanism that servlets use to maintain state about a series of requests from the same user across some period of time. Sessions are shared among the servlets accessed by a client. There are four techniques used in session tracking: cookies, hidden form fields, URL rewriting and HttpSession. HttpSession is an interface that provides a way to identify a user across more than one page request or visit to a website and to store information about that user.

A possible diagram for session tracking in servlets using HttpSession is:

### Session Tracking in Servlets

```
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|   Web Browser  |      |   Web Server   |      |   Servlet      |
|                |      |                |      |   Container    |
+----------------+      +----------------+      +----------------+
     |                       |                       |
     |  Request              |                       |
     |---------------------> |                       |
     |                       |  Create HttpSession   |
     |                       |---------------------> |
     |                       |  Return session ID    |
     |                       |<--------------------- |
     |  Response             |                       |
     |<--------------------- |                       |
     |                       |                       |
     |  Request              |                       |
     |  with session ID      |                       |
     |---------------------> |                       |
     |                       |  Lookup HttpSession   |
     |                       |---------------------> |
     |                       |  Return session data  |
     |                       |<--------------------- |
     |  Response             |                       |
     |<--------------------- |                       |
     |                       |                       |
     |  Request              |                       |
     |  with session ID      |                       |
     |---------------------> |                       |
     |                       |  Lookup HttpSession   |
     |                       |---------------------> |
     |                       |  Return session data  |
     |                       |<--------------------- |
     |  Response             |                       |
     |<--------------------- |                       |
     |                       |                       |
```