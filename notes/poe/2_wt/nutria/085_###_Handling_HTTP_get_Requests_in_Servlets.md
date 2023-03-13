
### Handling HTTP get Requests in Servlets

* HTTP Get requests are used to request data from a specified resource.
* The request contains a header and a body. The header contains the request type, the resource to be requested, and other information such as the type of content being requested.
* The body of the request contains additional information such as the data to be sent, the type of data being sent, and other parameters.
* In Servlets, HTTP get requests are handled using the doGet() method. This method takes an HttpServletRequest and HttpServletResponse object.
* The HttpServletRequest object contains the request information such as the request type, the resource requested, and the parameters sent in the body.
* The HttpServletResponse object is used to send the response back to the client.
* In the doGet() method, the request is checked for validity. If the request is valid, the appropriate action is taken and the response is sent back to the client.
* Mnemonics and Learning Tricks:
    * G - Get Request
    * R - Request Information
    * V - Validity Check
    * A - Action
    * R - Response
* Advantages of using HTTP Get Requests:
    * Fast response time
    * Easy to implement
    * Can be cached
    * Can be bookmarked
* Disadvantages of using HTTP Get Requests:
    * Limited amount of data can be sent
    * Security risks
* Examples of applications which use HTTP Get Requests:
    * Web browsers
    * Search engines
    * Online shopping websites
    * Social media websites