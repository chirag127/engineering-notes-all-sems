A cookie is a small piece of information that is persisted between the multiple client requests. A cookie has a name, a single value, and optional attributes such as a comment, path and domain qualifiers, a maximum age, and a version number.

Cookies are created using Cookie class present in Servlet API. Cookies are added to response object using the addCookie() method. This method sends cookie information over the HTTP response stream. getCookies() method is used to access the cookies that are added to response object.

The following diagram illustrates the basic architecture of a cookie in servlet:

### Cookies in Servlets

```
    +-----------------+                +-----------------+
    |                 |                |                 |
    |   Web Browser   |                |   Web Server    |
    |                 |                |                 |
    +-----------------+                +-----------------+
          |   |                              |   |
          |   |                              |   |
          |   |                              |   |
          |   |                              |   |
          |   |                              |   |
          |   |                              |   |
          |   |                              |   |
          |   |                              |   |
          |   |                              |   |
          |   |                              |   |
          |   |                              |   |
          |   |   HTTP Request               |   |
          |   |----------------------------->|   |
          |   |                              |   |
          |   |                              |   |
          |   |                              |   |
          |   |                              |   |
          |   |                              |   |
          |   |                              |   |   Create Cookie object
          |   |                              |   |   using Cookie class
          |   |                              |   |   and add it to response
          |   |                              |   |   object using addCookie()
          |   |                              |   |<--------------------------
          |   |                              |   |
          |   |                              |   |
          |   |                              |   |
          |   |   HTTP Response              |   |
          |   |   with Cookie                |   |
          |   |<-----------------------------|   |
          |   |                              |   |
          |   |                              |   |
          |   |                              |   |
          |   |   Store Cookie               |   |
          |   |   in Browser                 |   |
          |   |<-----------------------------|   |
          |   |                              |   |
          |   |                              |   |
          |   |                              |   |
          |   |   HTTP Request               |   |
          |   |   with Cookie                |   |
          |   |----------------------------->|   |
          |   |                              |   |
          |   |                              |   |
          |   |                              |   |
          |   |                              |   |   Retrieve Cookie object
          |   |                              |   |   from request object
          |   |                              |   |   using getCookies()
          |   |                              |   |-------------------------->
          |   |                              |   |
          |   |                              |   |
          |   |                              |   |
          |   |   HTTP Response              |   |
          |   |<-----------------------------|   |
          |   |                              |   |
          |   |                              |   |
          |   |                              |   |
          |   |                              |   |
          |   |                              |   |
          |   |                              |   |
          |   |                              |   |
          |   |                              |   |
          |   |                              |   |
          |   |                              |   |
          |   |                              |   |
          |   |                              |   |

```