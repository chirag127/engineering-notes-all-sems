### Create a Cookie and add these four user id’s and passwords to this Cookie

Cookies are small text files that are stored on a user's computer by a web server. They are used to store information about the user's activity on the website, such as login information, preferences, and browsing history. Here are the steps to create a cookie and add four user id’s and passwords to it:

1. **Create a cookie object:** To create a cookie, you need to create an instance of the `javax.servlet.http.Cookie` class. This can be done by calling the `Cookie` constructor with two arguments: the name of the cookie and its value.

```java
Cookie cookie = new Cookie("users", "user1:password1,user2:password2,user3:password3,user4:password4");
```

2. **Set the maximum age of the cookie:** The maximum age of the cookie determines how long the cookie will be stored on the user's computer. This can be set by calling the `setMaxAge` method on the cookie object. The value is specified in seconds.

```java
cookie.setMaxAge(60 * 60 * 24 * 365); // 1 year
```

3. **Add the cookie to the response:** To send the cookie to the user's browser, you need to add it to the response object. This can be done by calling the `addCookie` method on the response object and passing the cookie as an argument.

```java
response.addCookie(cookie);
```

After these steps, the cookie will be stored on the user's computer and can be accessed by the server on subsequent requests. The server can retrieve the cookie by calling the `getCookies` method on the request object and searching for the cookie with the specified name.