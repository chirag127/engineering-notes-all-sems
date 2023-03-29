
### Redirecting Requests to Other Resources

1. A servlet is a Java class that is used to process requests and generate responses.
2. A servlet can be used to redirect requests to other resources by using the `sendRedirect()` method.
3. The `sendRedirect()` method takes a URL as a parameter and sends a response to the client with the status code `302` and the new location.
4. The `sendRedirect()` method is a convenient way to forward requests to other resources, but it does not allow for any other processing.
5. The `sendRedirect()` method should be used when the response from the resource is not needed, such as when redirecting to an external website.
6. The `forward()` method is another way to redirect requests to other resources.
7. The `forward()` method takes a request and response as parameters and forwards the request to another resource.
8. The `forward()` method allows for additional processing to be done before the request is forwarded.
9. The `forward()` method should be used when the response from the resource is needed, such as when redirecting to an internal resource.