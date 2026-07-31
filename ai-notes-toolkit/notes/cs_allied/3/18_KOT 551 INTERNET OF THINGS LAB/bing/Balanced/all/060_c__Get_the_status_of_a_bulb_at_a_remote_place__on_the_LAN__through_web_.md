# Get the status of a bulb at a remote place (on the LAN) through web

- To get the status of a bulb at a remote place (on the LAN) through web, the following steps are required:

  - The bulb should be connected to a microcontroller that can communicate with the LAN using a wired or wireless interface. The microcontroller should also have a digital input pin to read the state of the bulb (on or off).

  - The microcontroller should run a web server that can handle HTTP requests from other devices on the LAN. The web server should have a URL that returns the status of the bulb as a plain text or JSON response.

  - The device that wants to get the status of the bulb should send an HTTP GET request to the web server's URL using a web browser or a web client library. The device should parse the response and display the status of the bulb accordingly.

- An example of a possible implementation is as follows:

  - The bulb is connected to a NodeMCU board that has a built-in WiFi module. The NodeMCU board is powered by a USB cable and has a digital input pin D1 connected to the bulb's switch.

  - The NodeMCU board runs a web server using the Arduino IDE and the ESP8266WebServer library. The web server has a URL `/status` that returns the state of the bulb as a plain text response (`ON` or `OFF`).

  - The code for the web server is:

  ```c
  #include <ESP8266WiFi.h>
  #include <ESP8266WebServer.h>

  // WiFi credentials
  const char* ssid = "your-ssid";
  const char* password = "your-password";

  // Web server object
  ESP8266WebServer server(80);

  // Pin for the bulb switch
  const int bulbPin = D1;

  // Setup function
  void setup() {
    // Initialize serial monitor
    Serial.begin(9600);

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

    // Handle web requests
    server.on("/status", handleStatus); // Return the status of the bulb
    server.begin(); // Start the web server
    Serial.println("Web server started.");
  }

  // Loop function
  void loop() {
    // Handle web requests
    server.handleClient();
  }

  // Function to handle the /status request
  void handleStatus() {
    // Read the state of the bulb
    int bulbState = digitalRead(bulbPin);

    // Send the response as plain text
    server.send(200, "text/plain", (bulbState == HIGH) ? "ON" : "OFF");
  }
  ```

  - The device that wants to get the status of the bulb can use a web browser or a web client library to send an HTTP GET request to the web server's URL, for example: `http://192.168.1.10/status`. The device should parse the response and display the status of the bulb accordingly.