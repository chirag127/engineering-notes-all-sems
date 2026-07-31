 Here is the content written in markdown format with formal tone and without any emojis or external links:

#### Implicit Objects in Servlets

-   `request`: It is an object of `HttpServletRequest` class and contains information about the HTTP request sent by the client. Data such as request parameters, headers, request URI, etc. can be obtained using this object.
-   `response`: It is an object of `HttpServletResponse` class and is used to create HTTP response to be sent to the client. We can specify response status code, add headers, get output stream, etc. using this object.
-   `out`: It is a `PrintWriter` object used to write the response to the client. It basically wraps the `getWriter()` method of the `response` object.
-   `application`: It is an object of `ServletContext` interface and refers to the servlet context of the web application deployed on the server. It can be used to store attributes at application level and obtain MIME types, resource paths, etc.
-   `session`: It is an object of `HttpSession` interface and represents the user session. Attributes can be stored and retrieved using session for a particular user. Session tracking is enabled using this object.
-   `pageContext`: It is an object of `PageContext` class and is available only to JSP pages, not servlets. It encapsulates different implicit objects and provides additional functionality like inclusion of other resources.

The above implicit objects can be directly used in servlets and JSP pages without explicitly declaring them. They provide information regarding the request, response, application, session, etc. which reduces the amount of boilerplate code required to be written.