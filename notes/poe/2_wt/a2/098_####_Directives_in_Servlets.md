 Here is the content in markdown format for the topic #### Directives in Servlets:

#### Directives in Servlets

- Servlet Directives are instructions specified in the servlet class file (using specific comment tags) that are used to provide information to the servlet container.
- They are processed by the servlet container before the servlet is loaded.
- The three common directives are:

#### @WebServlet
- Used to specify URL mapping, load-on-startup order, security roles, etc.
- Format: @WebServlet("/url-pattern", initParams)
- Examples:
@WebServlet("/Hello") //maps Hello servlet to "/Hello" URL
@WebServlet(urlPatterns = {"/Hello", "/Hi"}) //maps to multiple URLs
@WebServlet(loadOnStartup = 1) //specifies load-on-startup order

Mnemonics: Think WebServlet controls web-related attributes of servlet.

#### @WebInitParam
- Used to specify initialization parameters for a servlet.
- Format: @WebInitParam(name = "param1", value = "value1")
- Example:
@WebInitParam(name = "dbname", value = "mydatabase")

Mnemonics: Init params are set before init() method, so think WebInitParam initializes parameters.

#### @MultipartConfig
- Used to specify that the servlet accepts multipart/form-data (file uploads).
- Format: @MultipartConfig(location = "", fileSizeThreshold = 4096, maxFileSize = 4096, maxRequestSize = 4096)
- Example:
@MultipartConfig(location = "/temp", fileSizeThreshold = 1024)

Advantages: Directives decouple deployment descriptors (web.xml) from servlet code.
Disadvantages: If incorrect, errors only detected at deployment time.

Applications: Used in all servlets to specify metadata and configuration.