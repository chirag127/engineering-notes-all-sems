## Experiment 5 - Create a socket for HTTP for web page upload and download

1. **Objective:** The objective of this experiment is to create a socket for HTTP to enable the upload and download of web pages.

2. **Background:** HTTP (Hypertext Transfer Protocol) is the protocol used for transmitting web pages over the internet. A socket is an endpoint for sending or receiving data across a computer network.

3. **Procedure:**
    1. Create a socket using the `socket()` function.
    2. Connect the socket to a server using the `connect()` function.
    3. Send an HTTP request to the server using the `send()` function.
    4. Receive the server's response using the `recv()` function.
    5. Close the socket using the `close()` function.

4. **Expected Outcome:** After completing this experiment, you should be able to create a socket for HTTP and use it to upload and download web pages.

5. **Further Reading:** For more information on sockets and HTTP, you can refer to the following resources:
    - [Python Socket Programming](https://docs.python.org/3/library/socket.html)
    - [HTTP Made Really Easy](https://www.jmarshall.com/easy/http/)