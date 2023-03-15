### Cookies in Servlets

1. Cookies are small text files that are stored on the client's computer by the server.
2. They are used to maintain session information between the client and the server.
3. Cookies are sent by the server to the client in the HTTP response header.
4. The client stores the cookies and sends them back to the server in the HTTP request header in subsequent requests.
5. Cookies can be used to store information such as user preferences, login information, and shopping cart contents.
6. In servlets, cookies can be created using the `javax.servlet.http.Cookie` class.
7. The `addCookie()` method of the `HttpServletResponse` interface is used to send a cookie to the client.
8. The `getCookies()` method of the `HttpServletRequest` interface is used to retrieve cookies from the client.
9. Cookies have a limited lifespan, which can be set using the `setMaxAge()` method of the `Cookie` class.
10. Cookies can also be deleted by setting their maximum age to zero.