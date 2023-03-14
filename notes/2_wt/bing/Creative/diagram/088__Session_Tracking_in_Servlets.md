Session tracking is a way to maintain state (data) of an user across multiple requests. It is also known as session management in servlets. HTTP protocol is stateless, which means that each request is treated as a new one and the server does not remember the previous requests from the same client. Session tracking is important for applications that need to recognize the user and store information about them, such as online shopping, mailing, or banking applications.

There are four techniques used in session tracking: cookies, hidden form fields, URL rewriting, and HttpSession. Cookies are small pieces of data sent by the server and stored by the browser. Hidden form fields are input elements in HTML forms that are not visible to the user but can carry information to the server. URL rewriting is a technique of appending the session ID to the URL of the request. HttpSession is an interface that provides methods to store and retrieve attributes associated with a session.

The following diagram illustrates the basic architecture of session tracking in servlets using HttpSession:

```
    +----------------+             +----------------+             +----------------+
    |                |             |                |             |                |
    |   Web Browser  |             |   Web Server   |             |   Servlet      |
    |                |             |                |             |                |
    +----------------+             +----------------+             +----------------+
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |----Request with no SID-->|   |                          |   |
          |   |                          |   |----Request with no SID-->|   |
          |   |                          |   |                          |   |----Create new session object and assign SID---->
          |   |                          |   |<---Response with SID-----|   |
          |   |<---Response with SID-----|   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |----Request with SID----->|   |                          |   |
          |   |                          |   |----Request with SID----->|   |
          |   |                          |   |                          |   |----Retrieve session object using SID---->
          |   |                          |   |<---Response-------------|   |
          |   |<---Response--------------|   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |

```

SID stands for session ID, which is a unique identifier for each session. The session ID can be sent and received using cookies, hidden form fields, or URL rewriting. The servlet container creates a new session object and assigns a session ID when it receives a request with no session ID. The servlet container retrieves the session object using the session ID when it receives a request with a session ID. The session object can store and retrieve attributes that are associated with the user's session. The session object can also be invalidated or timed out when the user logs out or the session is inactive for a long time.