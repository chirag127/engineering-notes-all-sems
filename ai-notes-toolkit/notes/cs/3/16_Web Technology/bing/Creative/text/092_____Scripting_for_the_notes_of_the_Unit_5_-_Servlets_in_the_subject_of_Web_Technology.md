### Scripting for Servlets

- Servlets are Java programs that run on a web server and handle requests from web clients (such as browsers).
- Servlets can generate dynamic web pages, process form data, interact with databases, and perform other server-side tasks.
- Servlets are robust and scalable because of the Java language and the servlet API.
- Servlets are managed by a servlet container, which is a component of a web server that provides the runtime environment and services for servlets.
- The servlet API consists of two packages: javax.servlet and javax.servlet.http. These packages contain the classes and interfaces that define the servlet model, the request and response objects, the servlet context and configuration, the session management, the filters, the listeners, and the annotations.
- Scripts are a special type of servlets that are written in a scripting language (such as JSP, Groovy, Ruby, etc.) and are executed by a scripting engine.
- Scripts are useful for creating dynamic web pages with less code and more flexibility than servlets.
- Scripts are also servlets, and they implement the SlingScript interface, which extends the javax.servlet.Servlet interface.
- Scripts are either stored in the resource repository (such as JCR) or provided inside a bundle (such as OSGi) without being installed into the repository.
- Scripts have a resource path, which is either the location in the repository, the resource type in a servlet component configuration, or the virtual bundle resource path.
- Scripts are resolved and selected by the servlet resolver, which is a service that maps a request to a servlet or a script based on the resource path, the request method, the selectors, the extension, and the suffix.
- Scripts can access the request and response objects, the servlet context and configuration, the session, and other servlet API features through the scripting bindings, which are objects that are injected into the script by the scripting engine.
- Scripts can also use the Sling API features, such as the resource resolver, the resource, the value map, the adaptable, the adapter factory, the sling settings service, and the sling models.
- Scripts can be written in various scripting languages, such as JSP, Groovy, Ruby, JavaScript, etc. Each scripting language has its own scripting engine, which is a service that implements the SlingScriptEngine interface and provides the methods for evaluating and compiling scripts.
- Scripts can also be written in Java, which is the default scripting language for Sling. Java scripts are compiled into servlet classes by the Java compiler service, which implements the SlingScriptEngine interface and uses the Java compiler API.
- Scripts can be cached by the script cache, which is a service that stores the compiled scripts in memory and reduces the overhead of script evaluation and compilation. The script cache can be configured by the script cache configuration, which defines the cache size, the cache strategy, and the cache invalidation policy.