Session tracking is a way to maintain state (data) of an user across multiple requests to the server. Session tracking can be done by the server using the HttpSession interface in servlets. The server assigns a unique session ID to each client and creates a session object to store the session data. The session ID is sent to the client as a cookie or as a part of the URL. The client sends the session ID back to the server in each request. The server uses the session ID to retrieve the session object and access the session data.

Here is a detailed ascii diagram for session tracking with Http session in servlets:

```
+--------+              +--------+              +--------+
| Client |              | Server |              | Servlet|
+--------+              +--------+              +--------+
    |                       |                       |
    |  Request              |                       |
    |---------------------> |                       |
    |                       |  Create session object|
    |                       |  Generate session ID  |
    |                       |  Store session data   |
    |                       |                       |
    |                       |  Response             |
    |                       |  Set-Cookie: JSESSIONID=1234
    |                       |---------------------> |
    |                       |                       |
    |                       |                       |
    |  Request              |                       |
    |  Cookie: JSESSIONID=1234                     |
    |---------------------> |                       |
    |                       |  Get session object   |
    |                       |  using session ID     |
    |                       |  Access session data  |
    |                       |                       |
    |                       |  Response             |
    |                       |---------------------> |
    |                       |                       |
    |                       |                       |
    |  Request              |                       |
    |  Cookie: JSESSIONID=1234                     |
    |---------------------> |                       |
    |                       |  Get session object   |
    |                       |  using session ID     |
    |                       |  Access session data  |
    |                       |                       |
    |                       |  Response             |
    |                       |---------------------> |
    |                       |                       |
    |                       |                       |
    |  Request              |                       |
    |  Cookie: JSESSIONID=1234                     |
    |---------------------> |                       |
    |                       |  Get session object   |
    |                       |  using session ID     |
    |                       |  Access session data  |
    |                       |                       |
    |                       |  Response             |
    |                       |---------------------> |
    |                       |                       |
    |                       |                       |
    |  Request              |                       |
    |  Cookie: JSESSIONID=1234                     |
    |---------------------> |                       |
    |                       |  Get session object   |
    |                       |  using session ID     |
    |                       |  Access session data  |
    |                       |                       |
    |                       |  Response             |
    |                       |---------------------> |
    |                       |                       |
    |                       |                       |
    |  Request              |                       |
    |  Cookie: JSESSIONID=1234                     |
    |---------------------> |                       |
    |                       |  Get session object   |
    |                       |  using session ID     |
    |                       |  Access session data  |
    |                       |                       |
    |                       |  Response             |
    |                       |---------------------> |
    |                       |                       |
    |                       |                       |
    |  Request              |                       |
    |  Cookie: JSESSIONID=1234                     |
    |---------------------> |                       |
    |                       |  Get session object   |
    |                       |  using session ID     |
    |                       |  Access session data  |
    |                       |                       |
    |                       |  Response             |
    |                       |---------------------> |
    |                       |                       |
    |                       |                       |
    |  Request              |                       |
    |  Cookie: JSESSIONID=1234                     |
    |---------------------> |                       |
    |                       |  Get session object   |
    |                       |  using session ID     |
    |                       |  Access session data  |
    |                       |                       |
    |                       |  Response             |
    |                       |---------------------> |
    |                       |                       |
    |                       |                       |
    |  Request              |                       |
    |  Cookie: JSESSIONID=1234                     |
    |---------------------> |                       |
    |                       |  Get session object   |
    |                       |  using session ID     |
    |                       |

```
