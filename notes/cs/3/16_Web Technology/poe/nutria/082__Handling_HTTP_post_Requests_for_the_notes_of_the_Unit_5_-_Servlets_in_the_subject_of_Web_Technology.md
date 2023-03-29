
### Handling HTTP Post Requests for the Notes of Unit 5 - Servlets in Web Technology

1. HTTP post requests are sent from the client to the server in order to send data to the server for processing.
2. The data sent in a post request is not visible in the URL and is sent as part of the request body.
3. The post request body can contain data in various formats such as plain text, HTML, XML, JSON and more.
4. The server can access the data sent in the post request using the request object.
5. The request object can be used to access the data sent in the post request body as well as the headers and other information.
6. The post request body can be accessed using the `getParameter()` method of the request object.
7. This method takes the name of the parameter as an argument and returns the value of the parameter.
8. The post request body can also be accessed using the `getReader()` method of the request object.
9. This method returns a `BufferedReader` object which can be used to read the data in the request body.
10. The post request body can also be accessed using the `getInputStream()` method of the request object.
11. This method returns an `InputStream` object which can be used to read the data in the request body.
12. The post request body can also be accessed using the `getParameterMap()` method of the request object.
13. This method returns a `Map` object which contains the parameters sent in the post request.
14. Finally, the post request body can also be accessed using the `getParameterNames()` method of the request object.
15. This method returns an `Enumeration` object which contains the names of the parameters sent in the post request.