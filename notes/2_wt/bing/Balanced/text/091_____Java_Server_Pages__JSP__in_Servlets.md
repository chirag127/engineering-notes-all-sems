### Java Server Pages (JSP) in Servlets

- Java Server Pages (JSP) are a technology that allows web developers to create dynamic web pages using Java code embedded in HTML or XML documents.
- JSP are compiled into servlets by a JSP compiler, which is part of a web container or application server that supports the Java Servlet API.
- JSP can access Java objects, such as beans, servlets, or Java classes, and use them to generate dynamic content or perform business logic.
- JSP can also use custom tags, which are reusable components that encapsulate Java code or other JSP elements, and can be defined by the developer or provided by a tag library.
- JSP have a life cycle that consists of the following phases:
  - Translation: The JSP compiler translates the JSP file into a Java servlet class.
  - Compilation: The Java compiler compiles the servlet class into a bytecode file.
  - Loading: The web container loads the servlet class into memory.
  - Initialization: The web container invokes the init() method of the servlet to perform any initialization tasks.
  - Execution: The web container invokes the service() method of the servlet to process each request from the client and generate a response.
  - Destruction: The web container invokes the destroy() method of the servlet to perform any cleanup tasks before removing it from memory.
- JSP have some advantages over servlets, such as:
  - Ease of development: JSP allow web developers to write Java code and HTML/XML code in the same file, without the need to use print statements or string concatenation to generate the output.
  - Separation of concerns: JSP enable web developers to separate the presentation layer from the business logic layer, by using Java objects or custom tags to perform the latter.
  - Reusability: JSP can reuse Java objects or custom tags across multiple pages, reducing code duplication and improving maintainability.
  - Extensibility: JSP can be extended by using custom tags or tag libraries, which can provide additional functionality or simplify the development process.