### Cookies in Servlets

- Cookies are small pieces of information that are stored in the client's browser and sent to the server with every request .
- Cookies are used for state management and session tracking, as the server treats every client request as a new one by default.
- Cookies are created using the `Cookie` class in the `javax.servlet.http` package .
- To create a cookie, we need to pass the name and value of the cookie to the constructor of the `Cookie` class, for example:

```java
Cookie cookie = new Cookie("username", "John");
```

- To send a cookie to the client, we need to add it to the response object using the `addCookie()` method, for example:

```java
response.addCookie(cookie);
```

- To retrieve a cookie from the client, we need to get the array of cookies from the request object using the `getCookies()` method, and then loop through the array to find the cookie by name, for example:

```java
Cookie[] cookies = request.getCookies();
if (cookies != null) {
  for (Cookie c : cookies) {
    if (c.getName().equals("username")) {
      String username = c.getValue();
      // do something with username
    }
  }
}
```

- Cookies have optional attributes such as `comment`, `path`, `domain`, `maxAge`, and `version` that can be set or get using the corresponding methods of the `Cookie` class.
- For example, to set the expiration date of a cookie, we can use the `setMaxAge()` method, which takes the number of seconds as a parameter, for example:

```java
cookie.setMaxAge(60 * 60 * 24); // expires in one day
```

- Cookies are not very secure, as they can be easily modified or deleted by the client, or intercepted by a third party. Therefore, sensitive information should not be stored in cookies.