#### c) Get the status of a bulb at a remote place (on the LAN) through web.

- To get the status of a bulb at a remote place (on the LAN) through web, the following steps are required:

  - The bulb should be connected to a microcontroller that can communicate with the LAN using a wired or wireless interface. The microcontroller should also have a web server that can handle HTTP requests and responses.

  - The microcontroller should be able to read the state of the bulb (on or off) using a digital input pin and send it as a response to the web server.

  - The web server should have a URL that can be accessed by any device on the LAN using a web browser. The URL should return the status of the bulb as a plain text or a JSON object.

  - The device that wants to get the status of the bulb should send a GET request to the URL of the web server using the web browser. The web browser should display the response from the web server, which is the status of the bulb.

- An example of a possible implementation is:

  - The bulb is connected to a NodeMCU board, which is a microcontroller with a built-in WiFi module. The NodeMCU board is connected to the LAN using WiFi.

  - The NodeMCU board runs a web server using the Arduino IDE and the ESP8266WebServer library. The web server listens on port 80 and has a URL /status that returns the state of the bulb.

  - The NodeMCU board reads the state of the bulb using a digital input pin D1 and sends it as a response to the web server. The response is a JSON object with a key "state" and a value "on" or "off".

  - The device that wants to get the status of the bulb sends a GET request to the URL http://nodemcu.local/status using the web browser. The web browser displays the response from the web server, which is a JSON object with the state of the bulb.

- The code for the NodeMCU board is:

```c
#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

// WiFi credentials
const char* ssid = "your-ssid";
const char* password = "your-password";

// Web server object
ESP8266WebServer server(80);

// Bulb pin
const int bulbPin = D1;

// Setup function
void setup() {
  // Initialize serial monitor
  Serial.begin(115200);

  // Initialize bulb pin as input
  pinMode(bulbPin, INPUT);

  // Connect to WiFi
  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println();
  Serial.print("WiFi connected. IP address: ");
  Serial.println(WiFi.localIP());

  // Handle /status URL
  server.on("/status", handleStatus);

  // Start web server
  server.begin();
  Serial.println("Web server started.");
}

// Loop function
void loop() {
  // Handle web server requests
  server.handleClient();
}

// Handle /status URL function
void handleStatus() {
  // Read bulb state
  int bulbState = digitalRead(bulbPin);

  // Send response as JSON
  server.send(200, "application/json", "{\"state\":\"" + String(bulbState ? "on" : "off") + "\"}");
}
```