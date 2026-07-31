### IOT based Intelligent Gas Leakage Detector Using Arduino

- IOT based Intelligent Gas Leakage Detector Using Arduino is a project that aims to detect and alert the presence of LPG gas in the air using MQ5 gas sensor, Arduino microcontroller, ESP8266 Wi-Fi module and Blynk app.
- MQ5 gas sensor is a metal oxide semiconductor sensor that can detect various gases such as methane, propane, butane, LPG, smoke, etc. It has high sensitivity and fast response time. The sensor's output is an analog voltage that varies depending on the gas concentration.
- Arduino microcontroller is a programmable device that can read the analog voltage from the MQ5 sensor, process it and send it to the ESP8266 Wi-Fi module using serial communication.
- ESP8266 Wi-Fi module is a low-cost device that can connect to the internet and communicate with the Blynk app using MQTT protocol. MQTT is a lightweight and publish-subscribe messaging protocol that is suitable for IOT applications.
- Blynk app is a mobile application that can be used to create a user interface for IOT projects. It can display the gas level, send notifications, and control actuators such as buzzer, LED, relay, etc.
- The working principle of the project is as follows:
  - The MQ5 sensor continuously monitors the air for LPG gas and produces an analog voltage that is proportional to the gas concentration.
  - The Arduino reads the analog voltage and converts it to a digital value using analog-to-digital converter (ADC).
  - The Arduino sends the digital value to the ESP8266 module using serial communication.
  - The ESP8266 module connects to the internet and publishes the digital value to the Blynk app using MQTT protocol.
  - The Blynk app receives the digital value and displays it on a gauge widget. It also compares the digital value with a predefined threshold and sends an alert message to the user if the gas level exceeds the threshold.
  - The user can also control the buzzer, LED, relay, etc. using the Blynk app to indicate the gas leakage or to turn off the gas supply.