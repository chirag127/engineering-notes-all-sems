### IOT Circuit Breaker Project

In this project, we will be implementing an Internet of Things (IoT) based circuit breaker system. The project will demonstrate how IoT can be used to remotely control and monitor circuit breakers.

#### Objectives

The objectives of this project are as follows:

- To design and implement a circuit breaker system that can be remotely controlled and monitored using IoT.
- To demonstrate the use of IoT in controlling and monitoring electrical appliances.
- To gain hands-on experience in working with IoT devices and software.

#### Materials Required

The following materials are required to complete this project:

- ESP32 development board
- Relay module
- Circuit breaker
- Jumper wires
- Power supply
- Breadboard
- Smartphone or computer with internet connectivity

#### Circuit Diagram

The following circuit diagram shows the connections between the ESP32 development board, relay module, and circuit breaker:

```
ESP32 GPIO 14 --> Relay IN1
Relay COM --> Circuit breaker LINE
Relay NC --> Circuit breaker LOAD
ESP32 GND --> Relay GND
```

#### Software Requirements

The following software is required to complete this project:

- Arduino IDE (Integrated Development Environment)
- ESP32 board package for Arduino IDE
- Blynk IoT platform

#### Working

The circuit breaker system is controlled and monitored using the Blynk IoT platform. The ESP32 development board is connected to the internet using Wi-Fi. The Blynk app is installed on a smartphone or computer, and the device is connected to the same Wi-Fi network as the ESP32 board.

The user can turn the circuit breaker on or off using the Blynk app. When the user presses the button in the app, a signal is sent to the ESP32 board through the internet. The ESP32 board then activates or deactivates the relay module, which in turn controls the circuit breaker.

The status of the circuit breaker can also be monitored using the Blynk app. The app displays the current status of the circuit breaker, whether it is on or off.

#### Conclusion

In this project, we have successfully implemented an IoT based circuit breaker system. We have demonstrated how IoT can be used to remotely control and monitor electrical appliances. This project provides a good starting point for further exploration and development of IoT based systems.