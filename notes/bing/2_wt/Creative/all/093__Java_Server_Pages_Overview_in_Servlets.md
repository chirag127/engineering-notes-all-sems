#### Java Server Pages Overview in Servlets

- JavaServer Pages (JSP) is a technology that allows developers to create dynamic web pages using Java and Java Servlets .
- JSP pages are stored as regular HTML files with a .jsp extension and can contain HTML, XML, JavaScript, CSS, and Java code snippets.
- JSP pages are compiled into Java servlets and run on the server-side by a servlet container, such as Tomcat or Jetty  .
- JSP pages use a special syntax that embeds Java code within HTML tags, such as `<% ... %>` for scriptlets, `<%= ... %>` for expressions, and `<%@ ... %>` for directives .
- JSP pages can also use custom tags, which are reusable components that encapsulate Java logic and can be invoked by a simple tag name, such as `<my:hello />`.
- JSP pages follow a life cycle that consists of the following phases :
  - Translation: The JSP page is translated into a Java servlet class by the servlet container.
  - Compilation: The servlet class is compiled into a bytecode file by the Java compiler.
  - Loading: The bytecode file is loaded into the servlet container's memory by the class loader.
  - Initialization: The servlet container invokes the `init()` method of the servlet class to perform any initialization tasks.
  - Execution: The servlet container invokes the `service()` method of the servlet class to process the request and generate the response.
  - Destruction: The servlet container invokes the `destroy()` method of the servlet class to perform any cleanup tasks and release any resources.

- JSP pages have some advantages over servlets, such as :
  - Ease of development: JSP pages are easier to write and maintain than servlets, as they separate the presentation logic from the business logic and allow the use of HTML editors and tag libraries.
  - Performance: JSP pages are compiled into servlets only once, and then cached and reused for subsequent requests, which improves the performance and scalability of the web application.
  - Extensibility: JSP pages can be extended with custom tags, JavaBeans, and other Java components, which enhance the functionality and reusability of the web application.

- JSP pages also have some disadvantages, such as:
  - Debugging: JSP pages are harder to debug than servlets, as they are translated into servlets at runtime and may generate complex Java code that is not easy to understand or trace.
  - Security: JSP pages may expose sensitive information, such as database credentials or business logic, if they are not properly protected or encrypted, as they are stored as plain text files on the server.
  - Testing: JSP pages may require more testing than servlets, as they may have different behaviors depending on the browser, the server, and the servlet container.

- A possible mnemonic to remember the JSP life cycle phases is: **T**om **C**an **L**earn **I**talian **E**asily **D**aily. (Translation, Compilation, Loading, Initialization, Execution, Destruction).