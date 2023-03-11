 Here is the content in markdown format for the given topic:

### Handling HTTP get Requests

To handle HTTP get requests in servlets, we need to do the following:

1. Override the doGet() method of HttpServlet class. This is where the get request is handled.
2. Parse the request - We can get the request parameters using methods like getParameter(), getParameterValues(), getQueryString() etc. We can also get request headers, cookies, session objects, etc.
3. Perform business logic or retrieve data as per the get request - This could be getting some data from the database, performing calculations etc.
4. Generate the response - We can set the content type, status code and send the response data. This can be HTML, XML, JSON data etc.

Advantages of using get requests:

- Idempotent - Repeated get requests have no additional effect.
- Can be bookmarked - Get requests can be bookmarked and shared as they are safe and idempotent.
- Cached - Get requests can be cached by proxies, browsers thereby improving performance.
- Have length restrictions - Get requests have length restrictions which makes them suitable for retrieval of data.

Disadvantages:

- Not suitable for requests that change state - As get requests are idempotent, they are not suitable for requests that change state. Post requests should be used in such cases.
- Exposure of data - Since the parameters are in the URL, the data gets exposed which can lead to security issues.

[Include diagrams and code snippets if required to explain the concepts]

Applications of GET requests via servlets:

- Retrieving data from databases - We can have servlets to handle get requests to retrieve data from databases.
- Getting information - We can have servlets to send information/details on the server in response to get requests. For example, to get server stats or get a web page.
- REST APIs - GET requests are commonly used in REST APIs to retrieve resources/data.