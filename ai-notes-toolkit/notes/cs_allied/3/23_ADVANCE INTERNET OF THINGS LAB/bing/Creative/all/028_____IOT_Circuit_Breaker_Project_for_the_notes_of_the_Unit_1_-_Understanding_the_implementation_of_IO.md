# IOT Circuit Breaker Project

The IOT Circuit Breaker Project is a system that provides a password-based circuit breaker system using IOT. The system aims to prevent fatal accidents with line men due to electric shocks, which are a result of miscoordination or miscommunication between line men and substations. The system uses the interconnection network (internet) to control electrical loads remotely and securely. The system consists of the following components:

- A wifi module paired with Atmega328p microcontroller locally to connect to the internet and send/receive commands.
- A relay driver circuit to switch on/off the electrical loads based on the commands received from the wifi module.
- A keypad and LCD display to enter and show the password for authentication.
- A web server to host the user interface for controlling the circuit breaker from any device with internet access.

The system works as follows:

- The user enters the password on the keypad and the microcontroller verifies it with the web server. If the password is correct, the LCD display shows "Access Granted" and the user can control the circuit breaker from the web server. If the password is incorrect, the LCD display shows "Access Denied" and the user cannot control the circuit breaker.
- The user can access the web server from any device with internet access and see the status of the electrical loads. The user can also switch on/off the electrical loads by clicking on the corresponding buttons on the web server.
- The web server sends the commands to the wifi module, which in turn sends them to the microcontroller. The microcontroller then activates/deactivates the relay driver circuit to switch on/off the electrical loads accordingly.
- The system also provides feedback to the user by showing the current status of the electrical loads on the web server and the LCD display.

The IOT Circuit Breaker Project is a system that demonstrates the implementation of IOT in controlling electrical loads remotely and securely. The system can be used to improve the safety and efficiency of line men and substations. The system can also be modified to include other features such as current and voltage sensors, overload protection, power consumption monitoring, etc.