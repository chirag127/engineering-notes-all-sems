#### c) Get the status of a bulb at a remote place (on the LAN) through web.

To get the status of a bulb at a remote place (on the LAN) through web, the following steps are required:

- The bulb should be connected to a microcontroller that can communicate with the LAN using a wired or wireless interface. The microcontroller should also have a web server that can handle HTTP requests and responses.
- The microcontroller should be able to read the state of the bulb (on or off) using a digital input pin or a sensor, and store it in a variable or a memory location.
- The web server should be able to serve a web page that can display the status of the bulb using HTML and CSS. The web page should also have a refresh button that can send a new HTTP request to the web server to update the status of the bulb.
- The user should be able to access the web page using a web browser on a device that is connected to the same LAN as the microcontroller. The user should enter the IP address or the hostname of the microcontroller in the web browser's address bar, and the web page should load and show the status of the bulb.
- The user should be able to click on the refresh button to get the latest status of the bulb from the microcontroller. The web page should update the status of the bulb accordingly.

The following is a possible example of the code for the microcontroller and the web page:

```c
// Code for the microcontroller (Arduino)

// Include the libraries for the network interface and the web server
#include <Ethernet.h>
#include <WebServer.h>

// Define the MAC address and the IP address of the microcontroller
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
IPAddress ip(192, 168, 1, 100);

// Create an instance of the web server
WebServer server(80);

// Define the pin number for the bulb
#define BULB_PIN 2

// Define a variable to store the status of the bulb
int bulbStatus = 0;

// Setup function
void setup() {
  // Initialize the network interface and the web server
  Ethernet.begin(mac, ip);
  server.begin();

  // Initialize the bulb pin as an input
  pinMode(BULB_PIN, INPUT);
}

// Loop function
void loop() {
  // Read the status of the bulb and store it in the variable
  bulbStatus = digitalRead(BULB_PIN);

  // Handle the incoming HTTP requests
  server.processRequest();
}

// Function to handle the root path of the web server
void handleRoot() {
  // Send the HTTP response header
  server.sendHeader("Content-Type", "text/html");
  server.sendHeader("Connection", "close");
  server.endHeaders();

  // Send the HTML code for the web page
  server.print("<html>");
  server.print("<head>");
  server.print("<title>Bulb Status</title>");
  server.print("</head>");
  server.print("<body>");
  server.print("<h1>Bulb Status</h1>");
  server.print("<p>The bulb is ");
  // Display the status of the bulb using a conditional statement
  if (bulbStatus == HIGH) {
    server.print("ON");
  } else {
    server.print("OFF");
  }
  server.print("</p>");
  // Display a refresh button that can send a new HTTP request to the web server
  server.print("<button onclick=\"window.location.reload();\">Refresh</button>");
  server.print("</body>");
  server.print("</html>");
}
```

```html
<!-- Code for the web page -->

<html>
<head>
  <title>Bulb Status</title>
</head>
<body>
  <h1>Bulb Status</h1>
  <p>The bulb is ON</p>
  <button onclick="window.location.reload();">Refresh</button>
</body>
</html>
```