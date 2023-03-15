# Create a Cookie and add these four user id’s and passwords to this Cookie for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- A cookie is a small piece of data that is stored by the browser and sent to the server with every request. Cookies can be used to store user preferences, authentication information, session tracking, etc.
- To create a cookie in Java, we can use the `Cookie` class from the `javax.servlet.http` package. The constructor of this class takes two parameters: the name and the value of the cookie. For example:

```java
Cookie cookie = new Cookie("username", "Alice");
```

- To add a cookie to the response, we can use the `addCookie` method of the `HttpServletResponse` interface. This method takes a `Cookie` object as an argument and adds it to the `Set-Cookie` header of the response. For example:

```java
response.addCookie(cookie);
```

- To read a cookie from the request, we can use the `getCookies` method of the `HttpServletRequest` interface. This method returns an array of `Cookie` objects that represent all the cookies sent by the browser. We can loop through this array and find the cookie we want by its name. For example:

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

- To add four user ids and passwords to a cookie, we can either create four separate cookies, one for each pair of user id and password, or we can create one cookie that contains all four pairs of user id and password, separated by some delimiter. For example, using the first approach:

```java
Cookie cookie1 = new Cookie("user1", "password1");
Cookie cookie2 = new Cookie("user2", "password2");
Cookie cookie3 = new Cookie("user3", "password3");
Cookie cookie4 = new Cookie("user4", "password4");
response.addCookie(cookie1);
response.addCookie(cookie2);
response.addCookie(cookie3);
response.addCookie(cookie4);
```

Using the second approach:

```java
Cookie cookie = new Cookie("users", "user1:password1;user2:password2;user3:password3;user4:password4");
response.addCookie(cookie);
```

- Note that storing passwords in plain text in cookies is not a secure practice and should be avoided. A better way to handle authentication is to use a session id or a token that is stored in a cookie and verified by the server.