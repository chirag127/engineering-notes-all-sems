# IOT based Smart Agriculture Monitoring System Project

## Unit 1 - Understanding the implementation of IOT in the subject of ADVANCE INTERNET OF THINGS LAB

- The IOT based Smart Agriculture Monitoring System Project is a project that aims to use the Internet of Things (IOT) technology and wireless sensor networks to monitor and control various parameters of the agricultural field, such as temperature, humidity, light, soil moisture, and water level  .
- The project consists of the following components:
  - Sensors: The project uses four sensors to measure the environmental factors that affect the crop growth. These sensors are:
    - Temperature sensor: This sensor measures the ambient temperature of the field and sends the data to the controller. The project uses a DHT11 sensor, which is a digital temperature and humidity sensor.
    - Humidity sensor: This sensor measures the relative humidity of the air and sends the data to the controller. The project uses the same DHT11 sensor as the temperature sensor.
    - Light sensor: This sensor measures the intensity of the sunlight and sends the data to the controller. The project uses a light dependent resistor (LDR), which is a resistor whose resistance varies with the amount of light falling on it.
    - Soil moisture sensor: This sensor measures the moisture content of the soil and sends the data to the controller. The project uses a capacitive soil moisture sensor, which is a sensor that measures the dielectric permittivity of the soil, which is related to the water content.
    - Water level sensor: This sensor measures the water level in the water tank and sends the data to the controller. The project uses a float switch, which is a switch that closes or opens a circuit depending on the position of a floating ball.
  - Controller: The project uses an Arduino controller to receive the data from the sensors and process it. The project uses an Arduino Uno, which is a microcontroller board based on the ATmega328P chip.
  - Communication module: The project uses a communication module to send the data from the controller to the cloud and receive commands from the user. The project uses a NodeMCU, which is a development board that integrates the ESP8266 Wi-Fi chip and a microcontroller.
  - Cloud platform: The project uses a cloud platform to store and display the data from the controller and allow the user to access and control the system remotely. The project uses the Blynk app, which is a platform that enables the creation of IOT applications using a drag-and-drop interface.
  - Actuators: The project uses two actuators to control the irrigation and lighting of the field based on the data from the sensors and the commands from the user. These actuators are:
    - Water pump: This actuator pumps water from the water tank to the field when the soil moisture level is low or when the user commands it. The project uses a 12V DC water pump, which is a pump that runs on direct current and can be controlled by a relay .
    - LED strip: This actuator provides artificial light to the field when the sunlight intensity is low or when the user commands it. The project uses a 12V LED strip, which is a strip of light emitting diodes that can be controlled by a transistor.
- The project works as follows:
  - The sensors collect the data from the field and send it to the Arduino controller.
  - The Arduino controller processes the data and sends it to the NodeMCU module.
  - The NodeMCU module connects to the Wi-Fi network and sends the data to the Blynk app on the cloud.
  - The Blynk app displays the data on a dashboard and allows the user to view and control the system from a smartphone or a web browser.
  - The user can send commands to the NodeMCU module through the Blynk app to turn on or off the water pump and the LED strip.
  - The NodeMCU module receives the commands from the Blynk app and sends them to the Arduino controller.
  - The Arduino controller activates or deactivates the water pump and the LED strip according to the commands from the NodeMCU module or the data from the sensors.
- The benefits of the project are:
  - It improves the efficiency and productivity of the agriculture by providing optimal conditions for the crop growth.
  - It reduces the water and energy consumption by automating the irrigation