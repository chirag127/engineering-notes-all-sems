### IOT Social Distancing & Monitoring Robot For Queue

- This is a project that aims to prevent the spread of COVID-19 by enforcing social distancing rules in public places where queues are formed, such as banks, malls, schools, etc.  
- The project uses a four-wheel robot that follows a line on the ground and moves along with the queue. The robot has an ultrasonic sensor that measures the distance between the robot and the person in front of it. If the distance is less than the recommended 6 feet, the robot will alert the person with a buzzer and a LED display. 
- The robot also has a camera that captures the images of the queue and sends them to a cloud server. The server uses image processing and machine learning techniques to count the number of people in the queue, estimate the waiting time, and detect any violations of social distancing rules. The server can also send notifications to the authorities or the public through a web or mobile application.  
- The project uses Arduino Uno as the microcontroller, ESP8266 as the Wi-Fi module, HC-SR04 as the ultrasonic sensor, OV7670 as the camera, and 16x2 LCD as the display. The project also uses Firebase as the cloud platform, OpenCV as the image processing library, and TensorFlow as the machine learning framework.  
- The project has the following advantages:
  - It can help reduce the risk of COVID-19 transmission by enforcing social distancing rules in queues.
  - It can provide real-time information and feedback to the people in the queue and the authorities about the queue status and the social distancing compliance.
  - It can improve the efficiency and management of the queue system by reducing the waiting time and the human intervention.