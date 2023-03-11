 Here is the content in markdown format for the given topic:

### URL Connection for the notes of the Unit 3 - Scripting in the subject of Web Technology

1. URL or Uniform Resource Locator is the address of a resource on the Internet. It contains the protocol, hostname and path to access the resource.
2. The basic structure of a URL is:
<protocol>://<hostname>/<path>

For example: https://www.example.com/page.html

- Protocol: https
- Hostname: www.example.com
- Path: /page.html

3. To access the resource on a URL, we need to establish a connection to the server hosting the resource. This is done using programming languages like JavaScript.
4. The steps to establish a URL connection are:

1. Create an XMLHttpRequest object.
2. Create a callback function to receive the response.
3. Open a connection to the URL - specify method (GET/POST) and async (true/false).
4. Send the request.
5. Receive the response in the callback function.
6. Process the response.

5. Advantages of URL connection:
- Fetch data from servers without page refresh.
- Read responses incrementally.
- Send requests in background.
- Make requests across domains (with CORS).

6. Disadvantages of URL connection:
- Limited to HTTP.
- Callback hell if multiple nested requests are made.
- Security restrictions with CORS.

7. Examples and applications:
- Fetching JSON data from APIs.
- Reading incremental data updates.
- Building single page applications.
- Performing AJAX calls.

[Detailed diagrams and codes can be included here if required to explain the concepts]