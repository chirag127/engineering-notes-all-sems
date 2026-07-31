# IOT Social Distancing & Monitoring Robot For Queue

- IOT Social Distancing & Monitoring Robot For Queue is a project that aims to prevent the spread of COVID-19 by enforcing social distancing rules in public places where people form queues, such as banks, malls, schools, etc.
- The project uses a four-wheel robot that follows a line on the ground and moves along with the queue. The robot has an ultrasonic sensor that measures the distance between the robot and the person in front of it. If the distance is less than the recommended 6 feet, the robot will alert the person by a buzzer and a display message to maintain the distance.
- The project also uses a camera and a Raspberry Pi to capture the images of the queue and send them to a cloud server. The cloud server uses a machine learning model to count the number of people in the queue and estimate the waiting time. The server also sends the data to a mobile app that can be used by the authorities or the customers to monitor the queue status and plan their visit accordingly.
- The project uses the following components and technologies:
  - Arduino Uno: A microcontroller board that controls the robot's movement and sensor data.
  - Ultrasonic sensor: A sensor that emits and receives sound waves to measure the distance between the robot and the person in front of it.
  - Buzzer: A device that produces a loud sound to alert the person to maintain the distance.
  - LCD display: A screen that shows the distance and the message to the person.
  - Motor driver: A module that controls the speed and direction of the four motors attached to the wheels of the robot.
  - Line follower sensor: A sensor that detects the line on the ground and guides the robot to follow it.
  - Raspberry Pi: A mini-computer that processes the camera images and sends them to the cloud server.
  - Camera: A device that captures the images of the queue and sends them to the Raspberry Pi.
  - Cloud server: A remote server that hosts the machine learning model and the database for the queue data.
  - Machine learning model: A model that uses computer vision techniques to count the number of people in the queue and estimate the waiting time.
  - Mobile app: An application that displays the queue data and allows the users to check the queue status and plan their visit.