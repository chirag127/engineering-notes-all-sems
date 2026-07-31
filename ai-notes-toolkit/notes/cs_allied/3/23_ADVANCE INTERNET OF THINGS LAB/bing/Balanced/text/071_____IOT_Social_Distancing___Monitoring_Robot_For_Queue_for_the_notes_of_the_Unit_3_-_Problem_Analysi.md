### IOT Social Distancing & Monitoring Robot For Queue

- This is a project that aims to design and implement a robot that can monitor and enforce social distancing rules in public places, such as queues, markets, malls, etc.
- The robot uses a camera and a distance sensor to detect the presence and distance of people in its vicinity, and alerts them with a voice message or a buzzer if they are too close to each other or to the robot.
- The robot also uses a temperature sensor to measure the body temperature of the people and warns them if they have a fever, which is a possible symptom of COVID-19 or other infectious diseases.
- The robot can be controlled remotely via a web or mobile application, which allows the user to view the live video feed from the camera, adjust the parameters of the sensors, and send commands to the robot.
- The robot can also send the data collected by the sensors to a cloud server, which can be used for further analysis and visualization of the social distancing and health status of the people in the area.
- The robot is based on the Arduino platform, which is a low-cost and open-source hardware and software system that can be easily programmed and customized for various applications.
- The robot uses the following components:
  - Arduino Uno board: This is the main controller of the robot, which communicates with the sensors and the motors, and executes the logic of the program.
  - ESP8266 Wi-Fi module: This is a wireless module that connects the Arduino board to the internet, and enables the remote control and data transmission features of the robot.
  - HC-SR04 ultrasonic sensor: This is a distance sensor that emits and receives ultrasonic waves, and calculates the distance of an object based on the time difference between the emission and reception.
  - MLX90614 infrared thermometer: This is a temperature sensor that measures the surface temperature of an object using infrared radiation, and does not require physical contact.
  - OV7670 camera module: This is a camera module that captures images and videos, and sends them to the Arduino board via a serial interface.
  - L298N motor driver: This is a module that controls the speed and direction of the DC motors that drive the wheels of the robot.
  - DC motors and wheels: These are the components that enable the movement of the robot on the ground.
  - Buzzer and speaker: These are the components that produce sound signals to alert and communicate with the people.
  - LED and LCD display: These are the components that show visual indicators and messages to the people.
  - Battery and power supply: These are the components that provide the electrical energy to the robot and its components.
- The robot follows the following steps to perform its task:
  1. The robot is powered on and connected to the internet via the Wi-Fi module.
  2. The robot receives the commands and parameters from the user via the web or mobile application, and updates its settings accordingly.
  3. The robot moves around the area using the motors and wheels, and scans the environment using the camera and the distance sensor.
  4. The robot detects the presence and distance of the people using the camera and the distance sensor, and compares them with the predefined threshold values.
  5. If the robot finds that the people are too close to each other or to the robot, it alerts them with a voice message or a buzzer, and asks them to maintain a safe distance.
  6. The robot measures the body temperature of the people using the temperature sensor, and compares it with the normal range.
  7. If the robot finds that the people have a fever, it warns them with a voice message or a buzzer, and advises them to seek medical attention.
  8. The robot sends the data collected by the sensors to the cloud server via the Wi-Fi module, and the user can access and visualize the data via the web or mobile application.
  9. The robot repeats the steps 3 to 8 until it is powered off or receives a stop command from the user.