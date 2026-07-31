# Create a Cookie and add these four user id’s and passwords to this Cookie for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- A cookie is a small piece of data that is stored by the browser and sent to the server with every request. Cookies can be used to store user preferences, session information, authentication tokens, etc.
- To create a cookie in Java, we can use the `Cookie` class from the `javax.servlet.http` package. We can also use the `document.cookie` property in JavaScript .
- To add a cookie to the response, we can use the `addCookie(Cookie)` method of the `HttpServletResponse` interface. To read a cookie from the request, we can use the `getCookies()` method of the `HttpServletRequest` interface.
- To set the expiration date of a cookie, we can use the `setMaxAge(int)` method of the `Cookie` class. To delete a cookie, we can set its max age to zero.
- To store user id's and passwords in a cookie, we need to encode them using a suitable algorithm, such as Base64, to avoid exposing them in plain text. We also need to use a secure and http-only cookie to prevent unauthorized access or modification by malicious scripts.
- Here is an example of how to create a cookie and add four user id's and passwords to it in Java:

```java
// import the necessary packages
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.util.Base64;

// create a cookie object with a name and a value
Cookie cookie = new Cookie("users", "");

// encode the user id's and passwords using Base64
String user1 = Base64.getEncoder().encodeToString("user1:password1".getBytes());
String user2 = Base64.getEncoder().encodeToString("user2:password2".getBytes());
String user3 = Base64.getEncoder().encodeToString("user3:password3".getBytes());
String user4 = Base64.getEncoder().encodeToString("user4:password4".getBytes());

// concatenate the encoded user id's and passwords with a separator
String value = user1 + "|" + user2 + "|" + user3 + "|" + user4;

// set the value of the cookie
cookie.setValue(value);

// set the max age of the cookie to one day
cookie.setMaxAge(24 * 60 * 60);

// set the secure and http-only flags of the cookie
cookie.setSecure(true);
cookie.setHttpOnly(true);

// add the cookie to the response
response.addCookie(cookie);
```