### Cookies in Servlets

- A cookie is a small piece of information that is persisted between the multiple client requests.
- A cookie has a name, a single value, and optional attributes such as a comment, path and domain qualifiers, a maximum age, and a version number.
- Cookies are used for state management and session tracking in servlets, as the server treats every client request as a new one.
- The Cookie class in the javax.servlet.http package is used to create and manipulate cookies.
- To send a cookie to the client, we need to create a Cookie object and add it to the response object using the addCookie() method.
- For example:

```java
Cookie uiColorCookie = new Cookie("color", "red"); // create a cookie with name "color" and value "red"
response.addCookie(uiColorCookie); // add the cookie to the response
```

- To receive a cookie from the client, we need to get an array of Cookie objects from the request object using the getCookies() method.
- For example:

```java
Cookie[] cookies = request.getCookies(); // get an array of cookies from the request
if (cookies != null) {
  for (Cookie cookie : cookies) {
    // do something with each cookie
  }
}
```

- To delete a cookie, we need to set its maximum age to zero and add it to the response object.
- For example:

```java
Cookie uiColorCookie = new Cookie("color", "red"); // create a cookie with name "color" and value "red"
uiColorCookie.setMaxAge(0); // set its maximum age to zero
response.addCookie(uiColorCookie); // add the cookie to the response
```

- Some of the advantages of cookies are:
  - They are easy to use and implement.
  - They do not require any server-side resources or storage.
  - They can store user preferences and personalization data.
- Some of the disadvantages of cookies are:
  - They have a limited size and number per domain.
  - They can be disabled or deleted by the user or browser settings.
  - They can pose security and privacy risks if they contain sensitive information.
- Some of the applications of cookies are:
  - To store user credentials and authentication tokens.
  - To store shopping cart items and order details.
  - To store user language and theme preferences.
- A possible mnemonic to remember the attributes of a cookie is:

```
Name Value Comment Path Domain MaxAge Version
Never Venture Carelessly Past Dangerous Mountains Very
```