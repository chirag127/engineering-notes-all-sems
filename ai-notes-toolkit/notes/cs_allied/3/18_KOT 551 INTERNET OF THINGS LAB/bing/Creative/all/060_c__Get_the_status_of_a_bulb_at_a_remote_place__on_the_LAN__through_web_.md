# Get the status of a bulb at a remote place (on the LAN) through web

- To get the status of a bulb at a remote place (on the LAN) through web, one needs to have a web server, a web client, and a network connection between them.
- A web server is a software program that listens for requests from web clients and responds with the requested data or actions. A web client is a software program that sends requests to web servers and displays the received data or actions. A network connection is a physical or wireless link that allows data to be transferred between web servers and web clients.
- A bulb at a remote place can be controlled by a web server if it is connected to a device that can communicate with the web server, such as a microcontroller, a computer, or a smart plug. The device can act as an interface between the web server and the bulb, sending and receiving signals to turn the bulb on or off, or to change its brightness or color.
- To get the status of a bulb at a remote place, the web client needs to send a request to the web server, asking for the current state of the bulb. The web server needs to receive the request, query the device that is connected to the bulb, and send back the response to the web client. The web client needs to display the response, showing whether the bulb is on or off, or its brightness or color.
- The request and response can be formatted using a standard protocol, such as HTTP (Hypertext Transfer Protocol), which defines the rules and syntax for exchanging data over the web. The request and response can also contain data in a structured format, such as JSON (JavaScript Object Notation), which is a lightweight and human-readable way of representing data objects.
- An example of a request and response using HTTP and JSON is shown below:

```
Request:

GET /bulb/status HTTP/1.1
Host: webserver.com

Response:

HTTP/1.1 200 OK
Content-Type: application/json

{
  "bulb": {
    "state": "on",
    "brightness": 80,
    "color": "white"
  }
}
```

- The request uses the GET method, which means that the web client is asking for data from the web server. The request also specifies the path /bulb/status, which means that the web client is asking for the status of the bulb. The request also includes the Host header, which identifies the web server by its domain name.
- The response uses the 200 OK status code, which means that the web server has successfully processed the request and is sending back the data. The response also specifies the Content-Type header, which indicates that the data is in JSON format. The response also contains the data in JSON format, which shows the state, brightness, and color of the bulb.