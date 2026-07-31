### Cookies in Servlets

- A cookie is a small piece of information that is persisted between the multiple client requests.
- A cookie has a name, a single value, and optional attributes such as a comment, path and domain qualifiers, a maximum age, and a version number.
- Cookies are used for state management and session tracking, as the server treats every client request as a new one by default.
- Cookies are stored in the user's browser and sent back to the server for all the subsequent requests until the cookie is valid.
- The Cookie class in the javax.servlet.http package is used to create cookies.
- To send a cookie to the client, we need to create one and add it to the response object:

```java
Cookie uiColorCookie = new Cookie("color", "red"); // create a cookie with name "color" and value "red"
response.addCookie(uiColorCookie); // add the cookie to the response
```

- To get a cookie from the client, we need to get the array of cookies from the request object and loop through it to find the desired cookie:

```java
Cookie[] cookies = request.getCookies(); // get the array of cookies from the request
if (cookies != null) { // check if the array is not null
  for (Cookie cookie : cookies) { // loop through the array
    if (cookie.getName().equals("color")) { // check if the cookie name is "color"
      String color = cookie.getValue(); // get the cookie value
      // do something with the color
    }
  }
}
```

- To set the cookie expiration date, we need to use the setMaxAge() method of the Cookie class:

```java
Cookie uiColorCookie = new Cookie("color", "red"); // create a cookie with name "color" and value "red"
uiColorCookie.setMaxAge(60 * 60 * 24); // set the cookie to expire after one day (in seconds)
response.addCookie(uiColorCookie); // add the cookie to the response
```

- To delete a cookie, we need to set its max age to zero and add it to the response:

```java
Cookie uiColorCookie = new Cookie("color", "red"); // create a cookie with name "color" and value "red"
uiColorCookie.setMaxAge(0); // set the cookie to expire immediately
response.addCookie(uiColorCookie); // add the cookie to the response
```

- To modify a cookie, we need to create a new cookie with the same name and a different value and add it to the response:

```java
Cookie uiColorCookie = new Cookie("color", "blue"); // create a new cookie with name "color" and value "blue"
response.addCookie(uiColorCookie); // add the new cookie to the response
```

- Some advantages of cookies are:
  - They are easy to use and implement.
  - They do not require any server-side resources or storage.
  - They can store user preferences and personalization data.
- Some disadvantages of cookies are:
  - They are limited in size and number (usually 4 KB and 20 cookies per domain).
  - They are not secure and can be tampered with or stolen by malicious users or programs.
  - They can be disabled or deleted by the user or the browser.
  - They can cause privacy issues if they store sensitive or personal information.

- A possible mnemonic to remember the attributes of a cookie is:

**C**omment, **P**ath, **D**omain, **M**axAge, **V**ersion

- A possible learning trick to remember the difference between a cookie and a session is:

A cookie is like a **label** that the server attaches to the client, while a session is like a **locker** that the server allocates to the client. The label can be read by anyone, but the locker can only be accessed by the owner. The label can be removed or changed by the client, but the locker can only be deleted or modified by the server. The label can store a small amount of information, but the locker can store a large amount of information.