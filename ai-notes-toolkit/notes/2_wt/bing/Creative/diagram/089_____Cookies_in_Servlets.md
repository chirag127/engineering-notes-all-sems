A cookie is a small piece of information that is persisted between the multiple client requests. A cookie has a name, a single value, and optional attributes such as a comment, path and domain qualifiers, a maximum age, and a version number. Cookies are used to identify the user and maintain the state of the session.

### Cookies in Servlets

A servlet can create cookies and send them to the browser in the response header using the `addCookie()` method of the `HttpServletResponse` interface. The browser then stores the cookies on the local machine and sends them back to the server in the request header for all the subsequent requests until the cookie is valid. The servlet can retrieve the cookies from the request header using the `getCookies()` method of the `HttpServletRequest` interface. The servlet can also modify or delete the cookies by changing their attributes and sending them back to the browser.

The following diagram shows the basic flow of cookies in servlets:

```
    +----------------+              +----------------+              +----------------+
    |                |              |                |              |                |
    |   Web Browser  |              |   Web Server   |              |   Servlet      |
    |                |              |                |              |                |
    +----------------+              +----------------+              +----------------+
          |                                |                                |
          |                                |                                |
          |                                |                                |
          |                                |                                |
          |                                |                                |
          |                                |                                |
          |                                |                                |
          |                                |                                |
          |                                |                                |
          |                                |                                |
          |                                |                                |
          |                                |                                |
          |                                |                                |
          |  Request for a web page       |                                |
          |------------------------------> |                                |
          |                                |                                |
          |                                |  Forward the request to the    |
          |                                |  servlet                       |
          |                                |------------------------------> |
          |                                |                                |
          |                                |                                |
          |                                |                                |
          |                                |                                |
          |                                |                                |
          |                                |  Servlet creates a cookie      |
          |                                |  and adds it to the response   |
          |                                |  header                        |
          |                                |                                |
          |                                |                                |
          |                                |                                |
          |                                |  Response with the web page    |
          |                                |  and the cookie                |
          |                                |<------------------------------ |
          |                                |                                |
          |  Response with the web page   |                                |
          |  and the cookie                |                                |
          |<-------------------------------|                                |
          |                                |                                |
          |  Browser stores the cookie    |                                |
          |  on the local machine         |                                |
          |                                |                                |
          |                                |                                |
          |                                |                                |
          |                                |                                |
          |                                |                                |
          |  Request for another web page |                                |
          |  with the cookie              |                                |
          |------------------------------> |                                |
          |                                |                                |
          |                                |  Forward the request with the  |
          |                                |  cookie to the servlet         |
          |                                |------------------------------> |
          |                                |                                |
          |                                |  Servlet retrieves the cookie  |
          |                                |  from the request header       |
          |                                |                                |
          |                                |                                |
          |                                |  Servlet modifies or deletes   |
          |                                |  the cookie and adds it to the |
          |                                |  response header               |
          |                                |                                |
          |                                |                                |
          |                                |  Response with the web page    |
          |                                |  and the modified or deleted   |
          |                                |  cookie                        |
          |                                |<------------------------------ |
          |                                |                                |
          |  Response with the web page   |                                |
          |  and the modified or deleted  |                                |
          |  cookie                        |                                |
          |<-------------------------------|                                |
          |                                |                                |
          |  Browser updates or removes   |                                |
          |  the cookie                   |                                |
          |                                |                                |
          |                                |                                |
          |                                |                                |
          |                                |                                |
          |                                |                                |
          |                                |                                |
          |                                |                                |
          |                                |                                |
          |                                |                                |
          |                                |                                |
```