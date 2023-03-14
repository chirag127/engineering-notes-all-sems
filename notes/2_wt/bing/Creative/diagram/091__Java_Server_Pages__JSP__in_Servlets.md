Java Server Pages (JSP) are web pages that contain Java code embedded in HTML or XML. They are compiled and executed by a JSP engine, which is a part of a web server that supports the JSP technology. JSP pages can access the Java Servlet API and other Java libraries to generate dynamic content.

The basic architecture of JSP in Servlets is as follows:

```
  +----------------+      +----------------+      +----------------+
  |                |      |                |      |                |
  |  Web Browser   | <--> |  Web Server    | <--> |  JSP Engine    |
  |                |      |                |      |                |
  +----------------+      +----------------+      +----------------+
                                    |                      |
                                    |                      |
                                    |                      |
                                    |                      |
                                    |                      |
                                    |                      |
                                    |                      |
                                    |                      |
                                    |                      |
                                    |                      |
                                    |                      |
                                    |                      |
                                    |                      |
                                    |                      |
                                    |                      |
                                    |                      |
                                    |                      |
                                    |                      |
                                    |                      |
                                    |                      |
                                    |                      |
                                    |                      |
                                    |                      |
                                    |                      |
                                    |                      |
                                    |                      |
                                    |                      |
                                    |                      |
                                    |                      |
                                    |                      |
                                    |                      |
                                    |                      |
                                    |                      |
                                    |                      |
                                    |                      |
                                    |                      |
                                    |                      |
                                    |                      |
                                    |                      |
                                    |                      |
                                    |                      |
                                    |                      |
                                    |                      |
                                    |                      |
                                    |                      |
                                    |                      |
                                    +----------------------+
                                    |                      |
                                    |  Java Servlet API    |
                                    |                      |
                                    +----------------------+
                                    |                      |
                                    |  Java Libraries      |
                                    |                      |
                                    +----------------------+
```

The diagram illustrates the following steps:

1. A web browser sends an HTTP request to a web server that supports JSP.
2. The web server forwards the request to the JSP engine, which is a servlet that handles JSP pages.
3. The JSP engine checks if the requested JSP page has been compiled into a servlet class. If not, it compiles the JSP page into a servlet class and loads it into memory.
4. The JSP engine invokes the servlet class, passing the request and response objects as parameters.
5. The servlet class executes the Java code embedded in the JSP page, which may access the Java Servlet API and other Java libraries to generate dynamic content.
6. The servlet class returns the response object, which contains the HTML or XML output, to the JSP engine.
7. The JSP engine sends the response back to the web server, which delivers it to the web browser.