Session tracking is a mechanism that servlets use to maintain state about a series of requests from the same user across some period of time. Sessions are shared among the servlets accessed by a client. There are four techniques used in session tracking: cookies, hidden form fields, URL rewriting and HttpSession. HttpSession is an interface that provides a way to identify a user across more than one page request or visit to a website and to store information about that user.

The following diagram illustrates the basic architecture of a session tracking using HttpSession in servlets:

### Session Tracking in Servlets

```
+----------------+            +----------------+            +----------------+
|                |            |                |            |                |
|     Client     |            |     Server     |            |     Servlet    |
|                |            |                |            |                |
+----------------+            +----------------+            +----------------+
       |                            |                            |
       |  Request with no session   |                            |
       |--------------------------->|                            |
       |                            |                            |
       |                            |  Create new session object |
       |                            |--------------------------->|
       |                            |                            |
       |                            |  Return session object     |
       |                            |<---------------------------|
       |                            |                            |
       |  Response with session ID  |                            |
       |<---------------------------|                            |
       |                            |                            |
       |  Request with session ID   |                            |
       |--------------------------->|                            |
       |                            |                            |
       |                            |  Retrieve session object   |
       |                            |--------------------------->|
       |                            |                            |
       |                            |  Perform business logic    |
       |                            |<--------------------------->|
       |                            |                            |
       |  Response with session ID  |                            |
       |<---------------------------|                            |
       |                            |                            |
       |  Request with session ID   |                            |
       |--------------------------->|                            |
       |                            |                            |
       |                            |  Retrieve session object   |
       |                            |--------------------------->|
       |                            |                            |
       |                            |  Perform business logic    |
       |                            |<--------------------------->|
       |                            |                            |
       |  Response with session ID  |                            |
       |<---------------------------|                            |
       |                            |                            |
```

: https://www.cs.fsu.edu/~jtbauer/cis3931/tutorial/servlets/client-state/session-tracking.html
: https://www.javatpoint.com/session-tracking-in-servlets
: https://www.c-sharpcorner.com/article/session-tracking-using-the-httpsession-interface-in-servlets/