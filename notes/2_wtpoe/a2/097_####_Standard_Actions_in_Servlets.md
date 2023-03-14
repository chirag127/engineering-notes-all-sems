 Here is the content in markdown format for the topic - #### Standard Actions in Servlets:

#### Standard Actions in Servlets

The standard actions supported by servlets are -

1. init() - This method is called by the container once when the servlet is loaded. It is used to initialize resources like database connections, etc.
Mnemonic - *First time setup* - think of init() as the first time setup method called when the servlet is loaded.

2. service() - This is the primary method that handles requests and provides responses. It determines the HTTP request type (GET, POST, etc.) and calls doGet(), doPost(), etc. accordingly.
Mnemonic - * Main worker* - think of service() as the main worker method that handles requests and provides responses.

3. doGet() - This method handles GET requests and provides responses.
Mnemonic - *Gets request* - think of doGet() as the method that gets the GET request.

4. doPost() - This method handles POST requests and provides responses.
Mnemonic - *Posts response* - think of doPost() as the method that posts the response.

5. destroy() - This method is called by the container when the servlet is unloaded. It is used to release resources like database connections, etc.
Mnemonic - *Cleanup* - think of destroy() as the cleanup method called when the servlet is unloaded to release resources.

Advantages of using standard servlet actions -

- Code reuse - The standard actions can be reused across servlets.
- Easy to understand - The names of the standard actions are self-explanatory making them easy to understand.
- Less coding - We don't have to write a lot of code for common tasks like initializing resources, handling requests, etc. as standard servlet actions can be used.

Disadvantages of using standard servlet actions -

- Limited functionality - The standard servlet actions provide limited functionality. For complex tasks, we may have to write our own methods.
- Additional methods may be required - Although standard servlet actions handle common tasks, we may have to write additional methods for our specific requirements.

Examples and applications of standard servlet actions -

- init() is commonly used to initialize database connections.
- service() handles GET and POST requests and calls the appropriate doGet() or doPost() method.
- doGet() and doPost() handle GET and POST requests respectively and build appropriate responses.
- destroy() is commonly used to close database connections and release other resources.

Servlets use the standard actions to handle common tasks in a reusable and efficient manner. The standard actions can be overridden to customize the servlet behavior if required.