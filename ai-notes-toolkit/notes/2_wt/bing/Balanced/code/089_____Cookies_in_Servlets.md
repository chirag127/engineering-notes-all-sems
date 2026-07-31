### Cookies in Servlets

Cookies are small pieces of data that are stored by a web browser on the client side. They can be used to store information about the user's preferences, session state, or other data that can be accessed by the server.

To create a cookie in a servlet, you can use the Cookie class from the javax.servlet.http package. The constructor of the Cookie class takes two parameters: the name and the value of the cookie. For example:

```java
Cookie cookie = new Cookie("username", "John");
```

To send a cookie to the client, you can use the addCookie method of the HttpServletResponse object. For example:

```java
response.addCookie(cookie);
```

To read a cookie from the client, you can use the getCookies method of the HttpServletRequest object. This method returns an array of Cookie objects that represent all the cookies sent by the client. You can loop through the array and find the cookie by its name. For example:

```java
Cookie[] cookies = request.getCookies();
if (cookies != null) {
  for (Cookie c : cookies) {
    if (c.getName().equals("username")) {
      String username = c.getValue();
      // do something with the username
    }
  }
}
```

To delete a cookie from the client, you can set its maximum age to zero and send it back to the client. For example:

```java
Cookie cookie = new Cookie("username", "");
cookie.setMaxAge(0);
response.addCookie(cookie);
```