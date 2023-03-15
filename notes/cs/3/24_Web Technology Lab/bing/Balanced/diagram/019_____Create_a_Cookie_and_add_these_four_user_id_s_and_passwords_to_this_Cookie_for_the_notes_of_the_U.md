### Create a Cookie and add these four user id’s and passwords to this Cookie for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- A cookie is a small piece of data that is stored by the browser and sent to the server with every request. Cookies can be used to store user preferences, session information, authentication tokens, etc.
- To create a cookie in Java, we can use the `Cookie` class from the `javax.servlet.http` package. We can also use the `document.cookie` property in JavaScript .
- To create a cookie, we need to specify a name and a value for the cookie. Optionally, we can also set some attributes, such as the expiration date, the domain, the path, the secure flag, etc.
- To add a cookie to the response, we can use the `addCookie(Cookie)` method of the `HttpServletResponse` interface  . This will send the cookie to the browser along with the response headers.
- To read a cookie from the request, we can use the `getCookies()` method of the `HttpServletRequest` interface . This will return an array of `Cookie` objects that represent the cookies sent by the browser.
- To update or delete a cookie, we can modify its value or attributes and send it back to the browser using the `addCookie(Cookie)` method. To delete a cookie, we can set its expiration date to a past time.
- To add the user id's and passwords to a cookie, we can use the following steps:

  - Create a `Cookie` object for each user id and password pair, using the user id as the name and the password as the value. For example:

    ```java
    Cookie user1 = new Cookie("user1", "pass1");
    Cookie user2 = new Cookie("user2", "pass2");
    Cookie user3 = new Cookie("user3", "pass3");
    Cookie user4 = new Cookie("user4", "pass4");
    ```

  - Set the expiration date for each cookie to a future time, using the `setMaxAge(int)` method. For example, to set the cookie to expire in one hour:

    ```java
    user1.setMaxAge(60 * 60); // 60 seconds * 60 minutes
    user2.setMaxAge(60 * 60);
    user3.setMaxAge(60 * 60);
    user4.setMaxAge(60 * 60);
    ```

  - Optionally, set other attributes for the cookies, such as the domain, the path, the secure flag, etc. using the corresponding methods of the `Cookie` class. For example, to set the domain to `example.com` and the path to `/webtech`:

    ```java
    user1.setDomain("example.com");
    user1.setPath("/webtech");
    user2.setDomain("example.com");
    user2.setPath("/webtech");
    user3.setDomain("example.com");
    user3.setPath("/webtech");
    user4.setDomain("example.com");
    user4.setPath("/webtech");
    ```

  - Add the cookies to the response, using the `addCookie(Cookie)` method of the `HttpServletResponse` interface. For example:

    ```java
    response.addCookie(user1);
    response.addCookie(user2);
    response.addCookie(user3);
    response.addCookie(user4);
    ```

- To read the user id's and passwords from the cookie, we can use the following steps:

  - Get the array of `Cookie` objects from the request, using the `getCookies()` method of the `HttpServletRequest` interface. For example:

    ```java
    Cookie[] cookies = request.getCookies();
    ```

  - Loop through the array and check the name of each cookie. If the name matches the user id, get the value of the cookie, which is the password. For example:

    ```java
    for (Cookie cookie : cookies) {
      String name = cookie.getName();
      String value = cookie.getValue();
      if (name.equals("user1")) {
        // value is the password for user1
      } else if (name.equals("user2")) {
        // value is the password for user2
      } else if (name.equals("user3")) {
        // value is the password for