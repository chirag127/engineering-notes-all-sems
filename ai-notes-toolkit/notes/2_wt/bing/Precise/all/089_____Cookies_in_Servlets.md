### Cookies in Servlets

- Cookies are small text files that are stored on the client's computer by the server.
- They are used to store information about the user's preferences and activities on the website.
- Cookies are sent by the server to the client's browser in the HTTP response header.
- The browser stores the cookies and sends them back to the server in the HTTP request header for subsequent requests.
- Cookies have a name-value pair format and can have additional attributes such as expiration date, domain, and path.
- Cookies can be created in Servlets using the `Cookie` class.
- To create a cookie, create an instance of the `Cookie` class and set its name and value using the constructor or the `setName` and `setValue` methods.
- To send a cookie to the client, add it to the response using the `addCookie` method of the `HttpServletResponse` object.
- To read cookies from the client, use the `getCookies` method of the `HttpServletRequest` object. This method returns an array of `Cookie` objects.
- Cookies have some limitations. They can only store a small amount of data (usually up to 4KB), and they can be disabled by the user in the browser settings.
- Cookies can be used for session management, personalization, and tracking user behavior on the website.

Here is an example of creating and sending a cookie in a Servlet:

```java
Cookie cookie = new Cookie("username", "JohnDoe");
cookie.setMaxAge(60*60*24); // 1 day
response.addCookie(cookie);
```

And here is an example of reading cookies in a Servlet:

```java
Cookie[] cookies = request.getCookies();
if (cookies != null) {
    for (Cookie cookie : cookies) {
        if (cookie.getName().equals("username")) {
            String username = cookie.getValue();
            // do something with the username
        }
    }
}
```

Mnemonic: **C**ookies **S**tore **S**mall **D**ata. (Cookies Store Small Data)