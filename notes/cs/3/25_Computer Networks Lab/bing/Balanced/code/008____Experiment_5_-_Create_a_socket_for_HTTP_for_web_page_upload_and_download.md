## Experiment 5 - Create a socket for HTTP for web page upload and download

- A socket is an endpoint of a communication channel between two processes or devices over a network.
- HTTP (Hypertext Transfer Protocol) is a protocol that defines how web servers and web browsers communicate and exchange data.
- To create a socket for HTTP, we need to use the socket module in Python, which provides a low-level interface to the network layer.
- The steps to create a socket for HTTP are:

  1. Import the socket module: `import socket`
  2. Create a socket object: `s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)`
  3. Specify the host and port of the web server: `host = 'www.example.com'` and `port = 80`
  4. Connect the socket to the server: `s.connect((host, port))`
  5. Send an HTTP request to the server: `s.send(b'GET /index.html HTTP/1.1\r\nHost: www.example.com\r\n\r\n')`
  6. Receive the HTTP response from the server: `data = s.recv(1024)`
  7. Close the socket: `s.close()`
  8. Print the data: `print(data.decode())`

- To upload and download a web page, we need to use the requests module in Python, which provides a high-level interface to the HTTP protocol.
- The steps to upload and download a web page are:

  1. Import the requests module: `import requests`
  2. Specify the URL of the web page: `url = 'http://www.example.com/index.html'`
  3. Download the web page using the GET method: `r = requests.get(url)`
  4. Check the status code of the response: `r.status_code`
  5. Save the web page content to a file: `with open('index.html', 'wb') as f: f.write(r.content)`
  6. Modify the web page content as desired: `# edit the index.html file`
  7. Upload the web page using the PUT method: `r = requests.put(url, data=open('index.html', 'rb'))`
  8. Check the status code of the response: `r.status_code`