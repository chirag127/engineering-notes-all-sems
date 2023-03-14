A Java Server Page (JSP) is a web page that contains small snippets of Java code that are executed on the server side and generate dynamic content for the client. A servlet is a Java class that extends the functionality of a web server by handling requests and responses from clients. A servlet can also forward requests to other servlets or JSPs.

The following diagram illustrates the basic architecture of a JSP and servlet example:

```
    +-----------------+       +-----------------+       +-----------------+
    |                 |       |                 |       |                 |
    |    Web Browser  |  <--> |    Web Server   |  <--> |    Database     |
    |                 |       |                 |       |                 |
    +-----------------+       +-----------------+       +-----------------+
                                |             ^
                                v             |
                            +-----------------+
                            |                 |
                            |    Servlet      |
                            |                 |
                            +-----------------+
                                |             ^
                                v             |
                            +-----------------+
                            |                 |
                            |    JSP Page     |
                            |                 |
                            +-----------------+
```

The web browser sends a request to the web server, which invokes the servlet. The servlet performs some logic, such as querying the database or validating user input, and then forwards the request to the JSP page. The JSP page contains HTML code and Java code that are combined to generate the dynamic content for the response. The JSP page sends the response back to the servlet, which sends it back to the web server, which sends it back to the web browser.