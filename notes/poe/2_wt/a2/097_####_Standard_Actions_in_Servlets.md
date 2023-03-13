 Here is the content in markdown format for the topic - #### Standard Actions in Servlets:

#### Standard Actions in Servlets

The following are the standard actions supported by servlets:

1. Init(): This method is called when the servlet is loaded by the container. It is used to initialize the servlet. Resources can be initialized here.
2. Service(): This method is called by the container each time a request is received from a client. The servlet's task is defined in this method. It determines the kind of request and calls methods for handling the request and sending response.
3. Destroy(): This method is called when the servlet is unloaded from the container. It is used to perform cleanup activities and free allocated resources.

**Mnemonics:**

- Init() - Initialize the servlet
- Service() - Service the client request
- Destroy() - Destroy the servlet instance

**Learning Tricks:**

- Remember 'I' in Init() stands for Initialize
- Service() is at the core of a servlet's functionality
- Destroy() frees all resources taken by the servlet, just like destroying an object

Advantages of servlets:
- Platform independent (run on servers)
- Faster (no separate interpreter required unlike CGI)
- Share resources efficiently
- Session tracking capabilities

Disadvantages of servlets:
- Complex architecture
- Thread safety issues
- Extra overload on server

Servlets are mainly used to handle dynamic requests in web applications and to generate dynamic web pages. They provide an alternative to CGI and are a key component of Java EE architecture.