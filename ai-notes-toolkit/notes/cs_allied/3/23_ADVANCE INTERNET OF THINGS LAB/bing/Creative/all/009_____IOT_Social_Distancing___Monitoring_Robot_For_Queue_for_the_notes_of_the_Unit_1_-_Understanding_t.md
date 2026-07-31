# IOT Social Distancing & Monitoring Robot For Queue

- IOT Social Distancing & Monitoring Robot For Queue is a project that aims to prevent the spread of COVID-19 by enforcing social distancing rules in public places where people form queues, such as banks, malls, schools, etc.
- The project uses a four-wheeled robot that follows a line on the ground and moves along with the queue. The robot is equipped with an ultrasonic sensor that measures the distance between the robot and the person in front of it. If the distance is less than the recommended 6 feet, the robot will alert the person with a buzzer and a LED display. The robot will also send the data to a web server using an ESP8266 module, where the queue length and the number of violations can be monitored in real time.
- The project has the following objectives:
  - To design and implement a line-following robot using Arduino, motor driver, and IR sensors.
  - To interface an ultrasonic sensor with Arduino to measure the distance between the robot and the person in front of it.
  - To interface an ESP8266 module with Arduino to send the data to a web server using MQTT protocol.
  - To create a web dashboard using Node-RED to display the queue length and the number of violations.
  - To test the performance and accuracy of the robot in different scenarios and environments.