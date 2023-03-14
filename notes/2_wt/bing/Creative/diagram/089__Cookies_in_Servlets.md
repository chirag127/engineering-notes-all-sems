Cookies in Servlets are small pieces of information that are stored in key-value pair format to the client’s browser during multiple requests. They are used to identify a client when sending a subsequent request or to pass some data from one servlet to another. The Cookie class in the javax.servlet.http package is used to create, manipulate and read cookies. The following diagram illustrates the basic architecture of cookies in servlets:

```
    +-----------------+             +-----------------+             +-----------------+
    |                 |             |                 |             |                 |
    |   Client        |             |   Servlet 1     |             |   Servlet 2     |
    |   Browser       |             |                 |             |                 |
    |                 |             |                 |             |                 |
    +-----------------+             +-----------------+             +-----------------+
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
          |   +-------------------------->   |                          |   |
          |   |   Request                 |   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   +-------------------------->   |
          |   |                          |   |   Forward request        |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |   Process request
          |   |                          |   |                          |   |   and create cookie
          |   |                          |   |                          |   |   with name and value
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |   Add cookie to response
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |   Send response
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   <--------------------------+   |
          |   |                          |   |   Response with cookie  |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   <--------------------------+   |                          |   |
          |   |   Response with cookie  |   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |                          |   |                          |   |
          |   |   Store cookie in       |   |                          |   |
          |   |   browser cache         |   |                          |   |
          |   |                          |   |                          |   |
          |   |