#### Java Server Pages Overview in Servlets

JavaServer Pages (JSP) is a technology that allows developers to create dynamic web pages using Java and Java Servlets. JSP pages are compiled into Java servlets and run on the server. JSP uses a special syntax that embeds snippets of Java code within HTML, and these pages are stored as regular HTML files with a .jsp extension.

A servlet is a Java class that extends the javax.servlet.http.HttpServlet class and handles HTTP requests and responses. Servlets are under the control of another Java application called a Servlet Container, which is responsible for managing the servlet lifecycle and dispatching requests to the appropriate servlets.

The following diagram illustrates the basic architecture of a JSP and servlet application:

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   Web Browser   | <--> |   Web Server    | <--> |   Servlet       |
|                 |      |                 |      |   Container     |
+-----------------+      +-----------------+      +-----------------+
                                    |                     |
                                    |                     |
                                    v                     v
                              +-----------------+      +-----------------+
                              |                 |      |                 |
                              |   Static HTML   |      |   JSP Pages    |
                              |   Files         |      |                 |
                              +-----------------+      +-----------------+
```

The web browser sends an HTTP request to the web server, which forwards it to the servlet container. The servlet container checks if the request is for a static HTML file or a JSP page. If it is for a static HTML file, the web server serves the file directly to the browser. If it is for a JSP page, the servlet container invokes the corresponding servlet that was generated from the JSP page. The servlet executes the Java code embedded in the JSP page, generates the dynamic HTML content, and sends it back to the web server, which delivers it to the browser.