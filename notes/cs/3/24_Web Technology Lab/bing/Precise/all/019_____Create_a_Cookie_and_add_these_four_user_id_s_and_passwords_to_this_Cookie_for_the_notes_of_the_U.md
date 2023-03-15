# Create a Cookie and add these four user id’s and passwords to this Cookie

In the context of web technology, a cookie is a small text file that is stored on the user's computer by the web server. This file contains information about the user, such as their preferences or login information. Cookies are used to track user activity and to personalize the user experience.

Here are the steps to create a cookie and add four user id’s and passwords to this cookie:

1. First, create a new cookie object by calling the `Cookie` constructor and passing in the name and value of the cookie as arguments. For example: `Cookie userCookie = new Cookie("user", "value");`

2. Set the maximum age of the cookie, in seconds, by calling the `setMaxAge` method on the cookie object. For example: `userCookie.setMaxAge(60*60*24);` This sets the cookie to expire after one day.

3. Add the cookie to the response by calling the `addCookie` method on the `HttpServletResponse` object. For example: `response.addCookie(userCookie);`

4. To add multiple user id’s and passwords to the cookie, you can create multiple cookie objects and add them to the response in the same way. For example:
```
Cookie user1Cookie = new Cookie("user1", "password1");
Cookie user2Cookie = new Cookie("user2", "password2");
Cookie user3Cookie = new Cookie("user3", "password3");
Cookie user4Cookie = new Cookie("user4", "password4");
response.addCookie(user1Cookie);
response.addCookie(user2Cookie);
response.addCookie(user3Cookie);
response.addCookie(user4Cookie);
```
