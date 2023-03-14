#### Java Server Pages Overview in Servlets

JavaServer Pages (JSP) is a technology that allows dynamic content injection into static HTML pages using Java and Java Servlets. JSP pages are compiled into Java servlets and run on the server. JSP uses a special syntax that embeds snippets of Java code within HTML, and these pages are stored as regular HTML files with a .jsp extension.

The basic architecture of a JSP page is as follows:

```
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|   Web Browser  |    |   Web Server   |    |   Servlet      |
|                |    |                |    |   Container    |
+----------------+    +----------------+    +----------------+
       |                     |                     |
       |  HTTP Request      |                     |
       |-------------------->|                     |
       |                     |                     |
       |                     |  JSP Page Request  |
       |                     |-------------------->|
       |                     |                     |
       |                     |  JSP Page          |
       |                     |<--------------------|
       |                     |                     |
       |                     |  Servlet           |
       |                     |<--------------------|
       |                     |                     |
       |                     |  HTML Response     |
       |  HTML Response      |-------------------->|
       |<--------------------|                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
```

The diagram illustrates the following steps:

- The web browser sends an HTTP request to the web server for a JSP page.
- The web server forwards the request to the servlet container, which is responsible for managing and executing servlets and JSP pages.
- The servlet container checks if the JSP page has been compiled into a servlet. If not, it compiles the JSP page into a servlet class and loads it into memory.
- The servlet container invokes the servlet, which executes the Java code embedded in the JSP page and generates the HTML output.
- The servlet container sends the HTML output back to the web server, which in turn sends it to the web browser.