### Cookies

Cookies are small text files that are stored on a user's computer by a web server. They are used to store information about the user's preferences and activities on a website. Cookies can be used to track user behavior, personalize content, and provide a better browsing experience.

#### Types of Cookies

There are two types of cookies:

1. Session Cookies: These cookies are stored in the browser's memory and are deleted when the user closes the browser. They are used to maintain session information, such as login credentials, during a user's visit to a website.

2. Persistent Cookies: These cookies are stored on the user's computer and remain there even after the user closes the browser. They are used to remember user preferences, such as language or theme, and to track user behavior over time.

#### Cookie Attributes

Cookies have several attributes that can be set by the web server:

1. Name: The name of the cookie.
2. Value: The value of the cookie.
3. Domain: The domain of the website that the cookie belongs to.
4. Path: The directory path on the website that the cookie belongs to.
5. Expires: The expiration date of the cookie.
6. Secure: Indicates whether the cookie should only be sent over a secure connection (HTTPS).
7. HttpOnly: Indicates whether the cookie can be accessed by JavaScript.

#### Working with Cookies in Servlets

Servlets can use the `javax.servlet.http.Cookie` class to work with cookies. The following methods are available:

1. `Cookie(String name, String value)`: Creates a new cookie with the specified name and value.
2. `void setDomain(String domain)`: Sets the domain of the cookie.
3. `void setPath(String path)`: Sets the path of the cookie.
4. `void setMaxAge(int maxAge)`: Sets the expiration time of the cookie in seconds.
5. `void setSecure(boolean secure)`: Sets the secure flag of the cookie.
6. `void setHttpOnly(boolean httpOnly)`: Sets the HttpOnly flag of the cookie.
7. `String getName()`: Returns the name of the cookie.
8. `String getValue()`: Returns the value of the cookie.
9. `String getDomain()`: Returns the domain of the cookie.
10. `String getPath()`: Returns the path of the cookie.
11. `int getMaxAge()`: Returns the expiration time of the cookie in seconds.
12. `boolean getSecure()`: Returns the secure flag of the cookie.
13. `boolean isHttpOnly()`: Returns the HttpOnly flag of the cookie.

To set a cookie in a servlet, use the `javax.servlet.http.HttpServletResponse` object's `addCookie` method:

```java
Cookie cookie = new Cookie("name", "value");
response.addCookie(cookie);
```

To retrieve a cookie in a servlet, use the `javax.servlet.http.HttpServletRequest` object's `getCookies` method:

```java
Cookie[] cookies = request.getCookies();
if (cookies != null) {
    for (Cookie cookie : cookies) {
        if (cookie.getName().equals("name")) {
            String value = cookie.getValue();
            // do something with the value
        }
    }
}
```

#### Conclusion

Cookies are an important part of web development and are used to store user preferences and track user behavior. Servlets can use the `javax.servlet.http.Cookie` class to work with cookies and set and retrieve cookie attributes. Understanding how cookies work and how to work with them in servlets is an essential skill for web developers.