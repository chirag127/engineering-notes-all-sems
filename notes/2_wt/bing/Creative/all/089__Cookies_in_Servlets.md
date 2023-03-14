### Cookies in Servlets

- A cookie is a small piece of information that is stored on the client-side which servers use when communicating with clients.
- A cookie has a name, a single value, and optional attributes such as a comment, path and domain qualifiers, a maximum age, and a version number.
- Cookies are one of the state management techniques in session tracking. They are used to identify a client when sending a subsequent request or to pass some data from one servlet to another.
- To use cookies in Java, we need to use the Cookie class that is defined in the javax.servlet.http package.
- To create a cookie, we need to create an object of the Cookie class and pass a name and its value. For example:

```java
Cookie uiColorCookie = new Cookie("color", "red");
```

- To send a cookie to the client, we need to add it to the response object using the addCookie(Cookie) method of the HttpServletResponse interface. For example:

```java
response.addCookie(uiColorCookie);
```

- To read a cookie from the client, we need to get an array of cookies from the request object using the getCookies() method of the HttpServletRequest interface. For example:

```java
Cookie[] cookies = request.getCookies();
```

- We can iterate through this array and search for the cookie we need, e.g., by comparing their names. For example:

```java
public Optional<String> readCookie(String key) {
    return Arrays.stream(request.getCookies())
      .filter(c -> key.equals(c.getName()))
      .map(Cookie::getValue)
      .findAny();
}
```

- We can also set various attributes for a cookie using the methods of the Cookie class. For example:

```java
// Set the max age of the cookie to one hour
uiColorCookie.setMaxAge(60 * 60);

// Set the domain of the cookie to example.com and its subdomains
uiColorCookie.setDomain("example.com");

// Set the path of the cookie to /welcomeUser and its subdirectories
uiColorCookie.setPath("/welcomeUser");

// Set the secure flag of the cookie to true
uiColorCookie.setSecure(true);

// Set the comment of the cookie to "User's preferred color"
uiColorCookie.setComment("User's preferred color");

// Set the version of the cookie to 1
uiColorCookie.setVersion(1);
```

- Some advantages of using cookies are:
  - They are easy to use and implement
  - They can store small amounts of data on the client-side
  - They can reduce the load on the server by avoiding unnecessary requests
  - They can persist data across multiple requests and sessions

- Some disadvantages of using cookies are:
  - They are not secure and can be tampered with or stolen by malicious users
  - They are not reliable and can be disabled or deleted by the client
  - They have a limited size and number of cookies per domain
  - They can cause privacy issues by tracking user's browsing behavior

- Some examples of using cookies are:
  - To store user's preferences or settings such as language, theme, or layout
  - To store user's authentication or authorization information such as username, password, or role
  - To store user's shopping cart or wishlist items
  - To store user's browsing history or visited pages

- A mnemonic to remember the attributes of a cookie is:

```text
Name Value MaxAge Domain Path Secure Comment Version
NVM DPS CV
Never Violate My Data Privacy, Securely Communicate Values
```

- A learning trick to understand the difference between implicit and explicit domain and path of a cookie is:

```text
Implicit domain and path are set by the server that creates the cookie
Explicit domain and path are set by the programmer that creates the cookie
Implicit domain and path are more specific and restrictive
Explicit domain and path are more general and inclusive
```