 Here is the content in Markdown format without any emojis or external links:

### Handling HTTP post Requests

1. An HTTP POST method sends data to the server for processing - to create/update a resource.
2. The POST request body contains the data being sent to the server.
3. To handle a POST request in a servlet:
* Get the request body - use `getReader()` or `getInputStream()`
* Parse the data - if form data, use `getParameter()` or for XML/JSON, parse appropriately
* Process the data
* Generate a response - often a redirect to another page or a JSON/XML response

4. The Post Request is often used to send sensitive data (as the data is in the request body and not the URL) or to upload files (the file data is sent in the request body).
5. Ensure that the POST request is handled by a doPost() method in the servlet (a doGet() method will not get the request body).

The above points should cover the key aspects to understanding and handling HTTP POST requests in servlets. The requests send data in the request body which needs extracting and processing, often for database inserts or file uploads. The doPost() method should be used to handle POST requests (not doGet()).