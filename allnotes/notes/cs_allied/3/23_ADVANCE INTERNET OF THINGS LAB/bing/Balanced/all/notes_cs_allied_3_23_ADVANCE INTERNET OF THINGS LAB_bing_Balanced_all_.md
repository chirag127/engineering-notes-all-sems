

# ADVANCED INTERNET OF THINGS LAB

- The Advanced Internet of Things Lab is a course that aims to provide students with the knowledge and skills to design, implement, and evaluate IoT applications and systems.
- The course covers the following topics:
  - IoT concepts, architectures, and protocols
  - IoT devices, sensors, and actuators
  - IoT communication technologies, such as WiFi, Bluetooth, ZigBee, LoRa, and 5G
  - IoT cloud platforms, such as AWS IoT, Azure IoT, and Google Cloud IoT
  - IoT data processing, analytics, and visualization
  - IoT security, privacy, and ethics
  - IoT applications and use cases, such as smart home, smart city, smart health, and smart agriculture
- The course consists of lectures, labs, quizzes, assignments, and a final project.
- The lectures provide the theoretical background and introduce the relevant technologies and tools for IoT development.
- The labs provide hands-on experience with various IoT devices, platforms, and services, and require students to complete tasks and challenges using the provided hardware and software.
- The quizzes test the students' understanding of the lecture materials and the lab exercises.
- The assignments require students to design and implement their own IoT applications and systems, and to document and demonstrate their work.
- The final project is a capstone project that integrates the knowledge and skills acquired throughout the course, and requires students to propose, develop, and present an innovative IoT solution for a real-world problem or opportunity.
- The course requires students to have a basic knowledge of programming, networking, and web development, and to have access to a laptop and an internet connection.
- The course also provides students with a starter kit that includes an Arduino board, a Raspberry Pi, a breadboard, a set of sensors and actuators, and a WiFi dongle.



## Unit 1 - Understanding the implementation of IOT

- IOT stands for Internet of Things, which is a network of physical devices, sensors, actuators, and software that can communicate and exchange data over the internet.
- IOT enables various applications and services that can improve the efficiency, convenience, and quality of life for people and businesses.
- Some examples of IOT applications are smart homes, smart cities, smart agriculture, smart healthcare, smart manufacturing, smart transportation, and smart energy.
- To implement IOT, there are four main components: devices, connectivity, platforms, and applications.
  - Devices are the hardware that can sense, actuate, or compute data. They can be embedded in objects, such as sensors, cameras, RFID tags, or wearables, or standalone, such as smartphones, tablets, or laptops.
  - Connectivity is the network that enables the devices to communicate and transfer data over the internet. It can be wired, such as Ethernet, or wireless, such as Wi-Fi, Bluetooth, cellular, or satellite.
  - Platforms are the software that provide the infrastructure and services to manage, store, process, and analyze the data from the devices. They can be cloud-based, such as AWS, Azure, or Google Cloud, or edge-based, such as Raspberry Pi, Arduino, or Jetson Nano.
  - Applications are the software that provide the user interface and functionality to interact with the devices and data. They can be web-based, such as browsers, or mobile-based, such as apps. They can also use artificial intelligence, machine learning, or big data analytics to provide insights and solutions.



# Wearable Computer With Temperature Distance Sensors

- A wearable computer is a device that can be worn on the body and can perform computing tasks such as processing, storing, and displaying information.
- A wearable computer with temperature distance sensors is a type of wearable computer that can measure the temperature and distance of objects or environments using sensors such as lidar and thermocouple.
- Some applications of wearable computer with temperature distance sensors are:
  - Contactless temperature sensing for medical, industrial, or environmental purposes.
  - Contactless and accurate distance measurement for navigation, obstacle detection, or mapping.
  - Smart and easy to carry wearable computer for personal or professional use.
- A possible design and implementation of wearable computer with temperature distance sensors is:
  - Using a Raspberry Pi controller as the main computing unit, which can run various operating systems and applications.
  - Using a battery as the power source, which can be recharged or replaced as needed.
  - Using a touch screen display as the user interface, which can show the temperature and distance readings, as well as other information or functions.
  - Using a lidar sensor as the distance sensor, which can emit laser pulses and measure the time of flight to calculate the distance of objects.
  - Using a temperature sensor as the temperature sensor, which can measure the temperature of objects or environments using electrical resistance or voltage changes.
  - Mounting all the components in a compact way over a wrist strap, which can be worn on the wrist like a watch or bracelet.



# Weather Imaging CubeSat with Telemetry Transmission

- A CubeSat is a type of miniaturized satellite that has a standard size of 10x10x10 cm and a mass of up to 1.33 kg. CubeSats can be deployed in low Earth orbit for various applications, such as communication, GPS, remote sensing, and scientific research .
- A weather imaging CubeSat is a CubeSat that is equipped with a camera or a radiometer to capture images or measurements of the Earth's atmosphere and surface, such as clouds, precipitation, temperature, humidity, and pressure  .
- A telemetry transmission CubeSat is a CubeSat that is able to send data back to the ground station using a radio or a laser link. The data can be used for analysis, prediction, and forecasting of weather conditions .
- A weather imaging CubeSat with telemetry transmission is a CubeSat that combines both functions of weather imaging and telemetry transmission. It can provide real-time or near-real-time information about the weather phenomena and their evolution over time  .
- Some examples of weather imaging CubeSats with telemetry transmission are:
  - CubIXSS: A CubeSat that will measure the solar irradiance and the Earth's reflected radiation using a miniaturized spectrometer. It will help improve the understanding of the solar variability and its impact on the Earth's climate.
  - SunCET: A CubeSat that will monitor the solar coronal mass ejections (CMEs) and their effects on the Earth's magnetosphere using a compact coronagraph. It will help improve the forecasting of space weather events and their potential hazards.
  - TEMPEST-D: A CubeSat that has demonstrated a five-frequency, millimeter-wave imaging radiometer to observe the clouds and precipitation processes. It has provided high-resolution data on the vertical structure and evolution of storms and tropical systems.



# IOT Water Pollution Monitor RC Boat

- IOT Water Pollution Monitor RC Boat is a project that aims to measure and transmit water quality data using an RC boat equipped with sensors and an IOT module  .
- The project is remote-operated and controlled by an RC remote using which it can be maneuvered accordingly, a motorized propeller system to provide the forward and backward motion and a rudder to provide direction.
- The boat carries relevant sensors to measure water quality parameters such as pH, turbidity, temperature, dissolved oxygen, etc. and transmit them wirelessly to a remote control terminal or an IOT server online  .
- The project can help to monitor water pollution in real-time and alert the authorities or the public about the water condition and the need for remedial actions  .
- The project can also be used for educational purposes, research and development, environmental awareness, etc.  .



# Mountain Climber Health & GPS Tracker

## Introduction

- Mountain climbing is a challenging and adventurous activity that requires physical fitness, mental toughness and proper equipment.
- Mountain climbers face various risks such as altitude sickness, hypothermia, frostbite, avalanches, rock falls and injuries.
- To ensure the safety and well-being of mountain climbers, it is important to monitor their health and location in real time using smart devices and Internet of Things (IoT) technology.

## Objectives

- To design and implement a smart mountain climber system that can track the vitals and location of climbers using sensors, GPS and IoT.
- To display the live data of the climbers on a web dashboard and send alerts in case of any abnormality or emergency.
- To compare and evaluate different GPS trackers and altimeter watches for mountain climbers based on their features, accuracy, battery life and usability.

## Methodology

- The smart mountain climber system consists of the following components:

  - A wearable device that measures the heart rate, blood pressure, body temperature and oxygen saturation of the climber using sensors and sends the data to a microcontroller via Bluetooth.
  - A microcontroller that processes the sensor data and communicates with a GPS module to get the location coordinates of the climber.
  - A GSM module that transmits the data and location of the climber to a cloud server using cellular network.
  - A cloud server that stores and analyzes the data and location of the climber and displays them on a web dashboard using IoT protocols.
  - A web dashboard that shows the live vitals and location of the climber on a map and allows the user to set upper and lower limits for the vitals and send SMS alerts in case of limit crossings or emergency.

- The GPS trackers and altimeter watches for mountain climbers are evaluated based on the following criteria:

  - Features: The number and type of features that the device offers, such as GPS, barometer, altimeter, compass, thermometer, stopwatch, timer, alarm, backlight, etc.
  - Accuracy: The precision and reliability of the device in measuring the altitude, location, pressure, temperature and other parameters.
  - Battery life: The duration and frequency of the device's operation and charging.
  - Usability: The ease and convenience of using the device in different environments and conditions, such as wet, frozen, dark, etc.

## Results and Discussion

- The smart mountain climber system can successfully track the vitals and location of the climber and display them on a web dashboard in real time.
- The system can also send SMS alerts to the user or the emergency contacts in case of any abnormality or emergency.
- The system can be customized and scaled up for multiple climbers and different regions and terrains.
- The GPS trackers and altimeter watches for mountain climbers vary in their features, accuracy, battery life and usability.
- Some of the best GPS trackers and altimeter watches for mountain climbers are:

  - Suunto Spartan Sport Wristwatch: A GPS tracker and wristwatch that offers multiple features such as heart rate monitor, barometer, altimeter, compass, thermometer, stopwatch, timer, alarm, backlight, etc. It has a battery life of 10 hours in GPS mode and 14 days in watch mode. It is easy to use and has a touchscreen and LED backlight.
  - Garmin Oregon 650t: A handheld GPS tracker that features a three-inch touchscreen and LED backlight. It has a battery life of 16 hours and can be operated with gloves on. It has a barometer, altimeter, compass, thermometer, camera, etc. It is accurate and reliable in measuring the altitude and location.
  - Casio GW9400: An altimeter watch that has a solar-powered battery that can last for 7 months. It has a barometer, altimeter, compass, thermometer, stopwatch, timer, alarm, backlight, etc. It is accurate and durable in measuring the altitude and pressure. It is easy to use and has a digital display and buttons.



# Contactless IOT Doorbell

- A contactless IOT doorbell is a device that uses internet of things (IOT) technology to perform various functions such as ringing a bell, scanning the temperature, recognizing the face, and sending alerts to the house owner when a visitor arrives at the door.
- A contactless IOT doorbell can help prevent the spread of Covid-19 and other infectious diseases by avoiding physical contact and detecting fever symptoms in the visitors.
- A contactless IOT doorbell can also enhance the security and convenience of the house owner by allowing them to monitor and communicate with the visitors remotely through a mobile app or a web interface.
- A contactless IOT doorbell typically consists of the following components:
  - A microcontroller such as NodeMCU or Raspberry Pi that acts as the brain of the device and controls the communication and processing of data.
  - A non-contact infrared temperature sensor such as MLX90614 that measures the body temperature of the visitor without touching them.
  - A camera module that captures the image of the visitor and performs face recognition using machine learning algorithms.
  - A speaker that plays a voice message or a sound to greet the visitor and inform them of the temperature reading.
  - A wireless module such as Wi-Fi or Bluetooth that connects the device to the internet and enables data transmission and reception.
  - A power supply such as a battery or a solar panel that provides the necessary voltage and current to the device.
  - A buzzer or a LED that acts as a visual or an audible indicator of the device status and the visitor arrival.
- A contactless IOT doorbell works as follows:
  - When a visitor approaches the door, the device detects their presence using a motion sensor or a proximity sensor and activates the camera and the temperature sensor.
  - The device captures the image of the visitor and sends it to a cloud server or a local server for face recognition and identification.
  - The device also measures the temperature of the visitor and compares it with a threshold value to determine if they have fever or not.
  - The device plays a voice message or a sound to welcome the visitor and inform them of the temperature reading and the face recognition result.
  - The device sends the data and the image of the visitor to the house owner's mobile app or web interface through the internet and alerts them of the visitor arrival.
  - The house owner can view the data and the image of the visitor and decide whether to open the door or not. They can also communicate with the visitor through the speaker or send a text message or an email to them.
  - The device logs all the data and the images of the visitors in a database for future reference and analysis.



# IOT Smart Parking Using RFID

- IOT (Internet of Things) is the interconnection of physical devices, sensors, and actuators over the internet to exchange data and perform tasks.
- RFID (Radio Frequency Identification) is a technology that uses radio waves to identify objects by attaching tags to them. Tags contain a unique identifier and some data that can be read by a reader device.
- IOT Smart Parking Using RFID is a system that aims to improve the efficiency and convenience of parking management by using RFID tags and readers to monitor the availability and occupancy of parking spaces.
- The system consists of the following components:
  - RFID tags: These are attached to the vehicles or the entry cards of the users. They store the vehicle or user information and communicate with the RFID readers.
  - RFID readers: These are installed at the entry and exit points of the parking area. They scan the RFID tags and send the data to the central server.
  - Central server: This is the main controller of the system. It receives the data from the RFID readers and updates the database of the parking status. It also communicates with the mobile app and the display boards.
  - Mobile app: This is an application that allows the users to check the availability of parking spaces, reserve a slot, pay the parking fee, and get directions to the parking area.
  - Display boards: These are electronic boards that show the number of vacant and occupied parking spaces in the parking area. They also guide the users to their reserved slots.
- The system works as follows:
  - When a user arrives at the parking area, the RFID reader scans the RFID tag of the vehicle or the entry card and sends the data to the central server.
  - The central server checks the database and assigns a parking slot to the user. It also updates the display boards and the mobile app with the parking status.
  - The user can use the mobile app to reserve a slot, pay the parking fee, and get directions to the parking area.
  - When the user leaves the parking area, the RFID reader scans the RFID tag again and sends the data to the central server.
  - The central server updates the database and the display boards and the mobile app with the parking status. It also calculates the parking duration and the parking fee for the user.
- The benefits of the system are:
  - It reduces the parking search time and traffic congestion by providing real-time information and guidance to the users.
  - It optimizes the parking space utilization by allocating the slots according to the demand and availability.
  - It enhances the security and safety of the vehicles and the users by using RFID tags and readers to identify and monitor them.
  - It improves the user experience and satisfaction by offering convenience and flexibility in parking management.



# IOT Contactless Covid Testing Booth Automation

## Unit 1 - Understanding the implementation of IOT in the subject of ADVANCE INTERNET OF THINGS LAB

- IOT stands for Internet of Things, which is a network of physical devices, sensors, actuators, and software that can communicate and exchange data over the internet.
- IOT can be used to create smart and connected solutions for various domains, such as healthcare, agriculture, transportation, manufacturing, etc.
- IOT Contactless Covid Testing Booth Automation is an example of an IOT application that aims to reduce the risk of infection and human error in the covid testing process.
- The main features of this application are:

  - It uses RFID technology to register and identify the person who wants to undergo the covid test.
  - It uses a microcontroller to control the booth operations, such as opening and closing the door, activating the swab mechanism, sending the test sample to the lab, etc.
  - It uses MATLAB to process the image of the person's face and detect if they are wearing a mask or not.
  - It uses GSM modem to send the test result and other information to the person's mobile phone via SMS.
  - It uses a web server to store and display the test data and statistics on a dashboard.

- The main benefits of this application are:

  - It reduces the contact between the person and the health worker, thus minimizing the chance of cross-contamination.
  - It automates the covid testing process, thus saving time and resources.
  - It provides instant and accurate test results, thus enhancing the efficiency and reliability of the covid testing system.
  - It collects and analyzes the test data, thus enabling better monitoring and management of the covid situation.



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



# IOT Covid Patient Health Monitor in Quarantine

- IOT stands for Internet of Things, which is a network of physical devices, sensors, actuators, and software that can collect and exchange data over the internet.
- Covid-19 is a highly contagious respiratory disease caused by a novel coronavirus that emerged in late 2019 and has spread worldwide, causing a global pandemic.
- Covid-19 patients who have mild or moderate symptoms are often advised to isolate themselves at home or in designated quarantine facilities to prevent further transmission of the virus and to reduce the burden on the health care system.
- However, these patients still need to monitor their vital signs, such as body temperature, pulse rate, blood oxygen saturation, and blood pressure, which are indicators of their health condition and potential complications.
- IOT Covid Patient Health Monitor in Quarantine is a system that uses wearable or portable devices, such as smart watches, bracelets, thermometers, oximeters, and blood pressure monitors, that can measure and transmit the vital signs of the patients to a cloud server or a mobile application via wireless communication protocols, such as Bluetooth, Wi-Fi, or cellular networks.
- The system allows the patients to self-monitor their health status and to receive alerts or feedback from the system or the medical staff if their vital signs are abnormal or out of range.
- The system also enables the medical staff, such as doctors, nurses, or health workers, to remotely monitor multiple patients simultaneously and to access their health data in real-time or in historical trends, using a web portal or a mobile application.
- The system can also provide analytics, visualization, and decision support tools to help the medical staff to diagnose, treat, and manage the patients more effectively and efficiently.
- The system can also integrate with other IOT devices, such as smart speakers, cameras, or door locks, to provide additional services, such as voice assistance, video consultation, or contactless delivery, to the patients in quarantine.
- The system can also leverage artificial intelligence, machine learning, or big data techniques to enhance the accuracy, reliability, and scalability of the system and to provide personalized and predictive health care solutions to the patients.
- The system can also support interoperability, security, and privacy standards to ensure the compatibility, safety, and confidentiality of the system and the health data.
- The system can also be customized and adapted to different scenarios, such as home, hotel, hospital, or community, and to different regions, cultures, or regulations, to meet the diverse and dynamic needs of the patients and the medical staff.



# IOT based Manhole Detection and Monitoring System

- IOT based Manhole Detection and Monitoring System is a project that aims to improve the safety and efficiency of the drainage system in urban areas by using sensors, GSM, GPS and cloud computing technologies.
- The main objectives of this project are:
  - To detect and alert the authorities about the open or broken manholes that can cause accidents or injuries to the pedestrians and vehicles.
  - To monitor and measure the water level and flow rate in the drainage pipes and manholes to prevent blockage and overflow that can lead to flooding and contamination of fresh water sources.
  - To collect and store the data from the sensors in the cloud server for analysis and visualization of the drainage system performance and status.
- The main components of this project are:
  - Sensors: Water level sensor, water flow sensor, ultrasonic sensor, gas sensor, temperature sensor and humidity sensor are used to measure the physical parameters of the drainage system and manhole environment.
  - Arduino: Arduino Uno is used as the microcontroller to process the sensor data and communicate with the GSM and GPS modules.
  - GSM and GPS modules: GSM module is used to send SMS alerts to the authorities and GPS module is used to provide the location of the manhole.
  - Cloud server: Firebase is used as the cloud platform to store and retrieve the sensor data and display it on a web dashboard.
  - Web dashboard: A web application is developed using HTML, CSS and JavaScript to visualize the sensor data and show the status and location of the manholes on a map.



# IOT based Smart Energy Meter Monitoring with Theft Detection

- IOT based Smart Energy Meter Monitoring with Theft Detection is a system that aims to reduce the energy crisis and power theft by properly monitoring the energy consumption and avoiding energy wastage.
- The system uses smart energy meters that are connected to the Internet of Things (IoT) platform to send and receive data from the distribution end and the consumer end.
- The system can detect power theft by using statistical regression methods to compare the data from the smart meters and identify any anomalies or discrepancies.
- The system can also alert the authorities and the consumers about the power theft and the energy consumption through mobile applications or web interfaces .
- The system can improve the efficiency and reliability of the power distribution network and reduce the losses and costs due to power theft.



# IOT Weather Station Airship

- An IOT weather station airship is a device that can measure and transmit atmospheric data using wireless communication and internet of things (IOT) technologies.
- It consists of a balloon or a drone that carries sensors, a microcontroller, a battery, a solar panel, and a wireless module.
- The sensors can measure parameters such as temperature, humidity, pressure, wind speed, wind direction, and UV radiation.
- The microcontroller can process the sensor data and send it to a cloud platform or a web portal using the wireless module, which can be based on Wi-Fi, LoRaWAN, or cellular networks.
- The battery can provide power to the device and the solar panel can recharge it.
- The device can be controlled remotely by the user to adjust the height, location, and frequency of data transmission.
- The device can provide real-time and accurate weather information for various applications, such as agriculture, climate research, disaster management, and weather forecasting.



# IOT based Three Phase Power Failure Monitoring with SMS Alerts

- This is a system that monitors the status of a three-phase power supply and alerts the authorized person via SMS in case of a phase loss or failure   .
- A phase loss occurs when one of the three phases of a three-phase system gets disconnected or damaged, resulting in a single phasing condition  .
- A phase loss can cause serious damage to the equipment and appliances connected to the power supply, as well as increase the risk of fire and electric shock  .
- The system consists of the following components:
  - A microcontroller that controls the logic and communication of the system .
  - A GSM module that sends and receives SMS messages to and from the authorized person   .
  - A LCD display that shows the voltage values of the three phases .
  - A voltage sensor that measures the voltage of each phase and sends it to the microcontroller .
  - A relay that switches on and off the power supply to the load.
- The system works as follows:
  - The voltage sensor continuously monitors the voltage of each phase and sends it to the microcontroller .
  - The microcontroller compares the voltage values with a predefined threshold and determines if there is a phase loss or failure .
  - If there is a phase loss or failure, the microcontroller sends a SMS message to the authorized person with the details of the fault   .
  - The microcontroller also displays the voltage values and the fault status on the LCD display .
  - The microcontroller can also switch off the power supply to the load using the relay to prevent further damage.
  - The authorized person can send a SMS message to the system to check the status of the power supply or to reset the system  .
- The system is an example of the implementation of IOT (Internet of Things) in the field of power monitoring and management   .
- IOT is the concept of connecting physical devices and objects to the internet and enabling them to communicate and exchange data   .
- IOT can provide various benefits such as remote control, automation, efficiency, safety, and convenience   .



# IOT based Intelligent Gas Leakage Detector Using Arduino

- This is a project that uses Internet of Things (IoT) technology to detect gas leakage in the surroundings and send data to an IOT module.
- IoT is the networking of physical things that can communicate with the help of sensors, electronics, software, and connectivity.
- Arduino is a microcontroller board that can be programmed to control various devices and sensors.
- The main components of this project are:
  - MQ5 gas sensor: This sensor can detect LPG gas and other combustible gases in the air. It has a high sensitivity and fast response time. It outputs an analog voltage that varies with the concentration of gas.
  - ESP8266 module: This module is a low-cost Wi-Fi chip that can connect to the internet and send or receive data. It can be interfaced with Arduino using serial communication.
  - Buzzer: This device produces a loud sound when activated. It can be used to alert the user or the nearby people about the gas leakage.
  - LED: This device emits light when powered. It can be used to indicate the status of the system or the gas level.
  - LCD: This device displays alphanumeric characters on a screen. It can be used to show the gas concentration or other messages to the user.
- The working of this project is as follows:
  - The MQ5 gas sensor is connected to the analog input of the Arduino. The sensor continuously monitors the level of LPG gas present in the air and outputs a voltage that is proportional to the gas concentration.
  - The Arduino reads the analog voltage from the sensor and converts it to a digital value using analog-to-digital conversion (ADC). The Arduino then calculates the gas concentration in parts per million (ppm) using a formula.
  - The Arduino sends the gas concentration data to the ESP8266 module using serial communication. The ESP8266 module connects to the internet using Wi-Fi and uploads the data to a cloud platform or a web server.
  - The Arduino also displays the gas concentration on the LCD and turns on the LED and the buzzer if the gas level exceeds a predefined threshold. This threshold can be set by the user according to the safety standards or the application requirements.
  - The user can access the gas leakage data from anywhere using a web browser or a mobile app. The user can also receive notifications or alerts if the gas level is too high or if there is any malfunction in the system.



# 360° Aerial Surveillance UAV With IOT Camera

- Aerial surveillance is the key to security and military based operations. It provides real-time information on enemy movements which plays a key role in precision strikes  .
- Aerial surveillance can be performed by using unmanned aerial vehicles (UAVs) or drones, which are remotely controlled or autonomous aircraft that can carry cameras, sensors, and other payloads  .
- A 360° aerial surveillance UAV with IOT camera is a type of drone that can capture and stream 360-degree video from the air, providing a panoramic view of the surroundings   .
- IOT stands for Internet of Things, which is a network of physical devices, sensors, and software that can communicate and exchange data over the internet   .
- A 360° aerial surveillance UAV with IOT camera can be used for various applications, such as:
  - Military and defense: to monitor enemy activities, detect threats, and coordinate attacks   .
  - Law enforcement and security: to prevent and respond to crimes, track suspects, and provide evidence   .
  - Disaster management and rescue: to assess the damage, locate survivors, and deliver aid   .
  - Environmental and wildlife protection: to observe and protect endangered species, habitats, and ecosystems   .
  - Media and entertainment: to capture and broadcast immersive and interactive videos   .
- A 360° aerial surveillance UAV with IOT camera consists of the following components  :
  - A drone frame: the structure that supports the propellers, motors, battery, and other components.
  - A flight controller: the brain of the drone that controls the stability, navigation, and communication of the drone.
  - A 360-degree camera: the device that captures and streams spherical video from the drone.
  - A wireless transmitter and receiver: the devices that enable the communication between the drone and the ground station or the internet.
  - A battery: the power source of the drone that determines the flight time and range of the drone.
  - A ground station: the device that receives the video and data from the drone and displays it on a screen or a headset.
  - A software application: the program that allows the user to control the drone, view the video, and access the data from the drone.



# IOT Garbage Segregator & Bin Level Indicator

- IOT Garbage Segregator & Bin Level Indicator is a system that uses sensors and microcontrollers to automatically segregate different types of waste and monitor the level of garbage in a bin.
- The system consists of the following components:
  - A dustbin with multiple compartments for different types of waste, such as organic, plastic, metal, paper, etc.
  - A sensor module that detects the type of waste and opens the corresponding compartment of the dustbin.
  - A level sensor that measures the amount of garbage in each compartment and sends the data to a microcontroller.
  - A microcontroller that processes the data and transmits it to an IOT platform over the internet.
  - An IOT platform that displays the bin level data and alerts the authorities when the bins need to be emptied.
- The system aims to achieve the following objectives:
  - To reduce the manual labor and human error involved in waste segregation and management.
  - To improve the efficiency and hygiene of waste collection and disposal.
  - To promote recycling and environmental awareness among the public.
  - To reduce the landfill space and greenhouse gas emissions caused by improper waste disposal.



# IOT Temperature & Mask Scan Entry System

- An IOT temperature and mask scan entry system is a device that uses a contactless temperature scanner and a camera to detect the body temperature and the presence of a mask on a person who wants to enter a building or a facility.
- The device is connected to a gate or a barrier that controls the entry based on the temperature and mask scan results. If a person has a high temperature or no mask, the entry is denied and an alert is generated. If a person has a normal temperature and a mask, the entry is allowed and a record is stored.
- The device uses a thermal and video camera, a temperature sensor, a Raspberry Pi system, a 7 inch touch screen, and an IOT module to perform the temperature and mask scan and communicate with the gate or the barrier and a cloud server.
- The device can be placed in or in front of buildings such as offices, schools, hospitals, malls, etc. to prevent the spread of COVID-19 and other infectious diseases.
- The device can also be integrated with other features such as face recognition, QR code scanning, attendance tracking, etc. to enhance the security and convenience of the entry system.



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



# IOT Based Automatic Vehicle Accident Detection and Rescue System

- This system is an application of Internet of Things (IoT) that aims to reduce the response time and human errors in the case of vehicle accidents.
- The system consists of a vibration sensor, a GPS module, a WiFi module, and a microcontroller that are installed in the vehicle.
- The vibration sensor detects the impact of an accident and sends a signal to the microcontroller.
- The microcontroller then obtains the location coordinates from the GPS module and sends them to a web server or a mobile application via the WiFi module.
- The web server or the mobile application can display the location of the accident on a map and alert the nearest rescue team or emergency service.
- The system can also send an SMS to a predefined number with the location information and a link to the map.
- The system can improve the safety and security of the vehicle and the passengers, as well as reduce the traffic congestion and environmental pollution caused by accidents.
- The system can be implemented using Arduino Nano, ESP8266 WiFi module, SW-420 vibration sensor, and NEO-6M GPS module   .



# Greenhouse Monitoring and Control System using IOT Project

- A greenhouse is a structure where plants such as flowers and vegetables are grown in a controlled environment.
- Greenhouses need to maintain optimal conditions for plant growth, such as temperature, humidity, light intensity, soil moisture, and soil pH.
- IOT (Internet of Things) is a technology that enables devices to communicate and exchange data over the internet or a network.
- IOT based greenhouse monitoring and control system project is a system that uses sensors, microcontrollers, actuators, and cloud services to monitor and control the environmental parameters in a greenhouse remotely and automatically.
- The main components of the system are:

  - Sensors: These are devices that measure the physical quantities of the environment, such as temperature, humidity, light intensity, soil moisture, and soil pH. The sensors are connected to a microcontroller, such as Arduino, which processes the sensor data and sends it to the cloud service.
  - Microcontroller: This is a small computer that controls the sensors and actuators. It also communicates with the cloud service using a Wi-Fi module or a GSM module. The microcontroller can be programmed using Arduino IDE or other software tools.
  - Actuators: These are devices that perform actions based on the sensor data and the commands from the cloud service, such as turning on or off fans, heaters, lights, water pumps, or valves. The actuators are connected to the microcontroller, which controls them according to the logic and rules defined in the code.
  - Cloud service: This is a platform that provides storage, processing, and visualization of the sensor data and the actuator commands. It also enables the user to access and control the system from anywhere using a web browser or a mobile app. The cloud service can be a third-party service, such as ThingSpeak, Blynk, or Firebase, or a custom-built service using web technologies, such as HTML, CSS, JavaScript, PHP, or Python.

- The main advantages of the system are:

  - It improves the productivity and quality of the plants by providing optimal conditions for their growth.
  - It reduces the human intervention and labor cost by automating the monitoring and control of the environment.
  - It saves water and energy by using them efficiently and avoiding wastage.
  - It provides real-time data and alerts to the user, which helps in decision making and troubleshooting.
  - It is scalable and flexible, as more sensors and actuators can be added or removed according to the needs and preferences of the user.



# IOT Based Coal Mine Safety Monitoring and Alerting System

- IOT based coal mine safety monitoring and alerting system is a project that aims to improve the safety and security of coal miners and detect the hazards inside a coal mine .
- The system consists of sensors, an IoT gateway, an LCD screen, and a cloud platform.
- The sensors are installed in the transmitter module, which is attached to the helmet of the coal miner. The sensors can measure the temperature, smoke, methane, and other parameters in the coal mine .
- The transmitter module also has an RF transmitter, which can send the sensor data to the IoT gateway using a low power communication protocol such as LoRa.
- The IoT gateway is a device that collects and analyzes the sensor data from the transmitter module. It can also display the data on the LCD screen or send it to the cloud platform through the internet.
- The cloud platform is a web application that can store, process, and visualize the sensor data from the IoT gateway. It can also provide alerts and notifications to the authorities or the rescue team in case of any emergency or abnormal situation in the coal mine .
- The system can help to monitor and control various parameters in the coal mine, such as leakage of gas, earthquake, water level, and fire ignition . It can also improve the communication and coordination between the coal miners and the outside world.
- The system can reduce the risk of accidents and fatalities in the coal mine, and enhance the efficiency and productivity of the coal mining industry .



# IOT Based Heart Monitoring System Using ECG

- IOT (Internet of Things) is a network of physical devices that can communicate and exchange data over the internet.
- ECG (Electrocardiogram) is a test that measures the electrical activity of the heart and shows how well it is working.
- IOT Based Heart Monitoring System Using ECG is a system that uses an ECG sensor, a microcontroller, a wireless module and a cloud platform to monitor the heart condition of a patient remotely and in real-time.
- The system works as follows:
  - The ECG sensor is attached to the patient's chest and detects the electrical signals generated by the heartbeats.
  - The microcontroller processes the ECG signals and calculates the heart rate and other parameters such as PQRST wave and QRS complex intervals.
  - The wireless module sends the ECG data to the cloud platform via the internet.
  - The cloud platform stores, analyzes and displays the ECG data on a web or mobile application.
  - The doctor or the patient can access the ECG data anytime and anywhere and get alerts if there is any abnormality or emergency.
- The advantages of the system are:
  - It is portable, low-cost and easy to use.
  - It provides continuous and accurate monitoring of the heart condition.
  - It enables early diagnosis and prevention of heart diseases.
  - It reduces the need for hospital visits and saves time and money.
  - It improves the quality of life and health care of the patient.
- The challenges of the system are:
  - It requires a reliable and secure internet connection and cloud service.
  - It may face interference or noise from other wireless devices or sources.
  - It may have privacy and security issues regarding the ECG data transmission and storage.
  - It may need calibration and maintenance of the ECG sensor and the microcontroller.
- The applications of the system are:
  - It can be used for home-based or remote health care of patients with heart problems or risks.
  - It can be used for fitness and wellness tracking of healthy individuals.
  - It can be used for research and education purposes in medical and engineering fields.



# IOT based Anti-theft Flooring System using Raspberry Pi

- This system is designed to secure and guard the house in the absence of the owner by monitoring the entire floor for movement  .
- The system consists of secure flooring tiles connected with IOT, piezo sensors, a camera, a wifi modem, and a Raspberry Pi controller .
- The system can be turned on or off by the owner through a web interface .
- When the system is turned on, any step on the floor is detected by the piezo sensors and the information is sent to the Raspberry Pi controller  .
- The controller processes the signal and moves the camera to the area where the movement was detected  .
- The camera captures the image of the intruder and transmits it over the internet to the owner's email address  .
- The owner can check the image and take appropriate action  .
- The system is based on the concept of IOT, which is the interconnection of devices and objects over the internet for data exchange and communication  .
- The system uses Raspberry Pi as the main controller, which is a low-cost, credit-card sized computer that can run various operating systems and perform various tasks  .
- The system is an example of the implementation of IOT in the field of home security and automation  .



# Raspberry Pi based Weather Reporting Over IOT

- This system can be used to monitor and update weather conditions over the internet using Raspberry Pi and various sensors.
- The system monitors three parameters namely temperature, humidity and rainfall and displays them on LCD and also updates them over the IoT gecko.
- IoT gecko is a web service that allows users to create dashboards and widgets to visualize and control data from various sources.
- The system uses DHT11 sensor for temperature and humidity, rain sensor for rainfall and BMP180 sensor for atmospheric pressure.
- The sensors are connected to the Raspberry Pi through GPIO pins and the data is read using Python scripts.
- The data is then sent to the IoT gecko server using HTTP requests and the user can access the data from any device with internet connection.
- The system is cost effective and has low power consumption as compared to conventional weather stations.
- The system provides accurate and precise weather-related data of a specific area as opposed to the generic type regional weather forecasts.
- The system can be useful for farmers, travelers, researchers and anyone who wants to know the weather conditions of a particular location.



# IOT Early Flood Detection & Avoidance

- Floods are natural disasters that can cause severe damage to property and lives.
- Early detection and avoidance of floods can help reduce the impact and save lives.
- IOT (Internet of Things) is a technology that connects devices and sensors to the internet and enables data collection and communication.
- IOT can be used to implement a system that monitors various natural factors that can indicate a flood, such as rainfall, water level, soil moisture, etc.
- The system can use wireless sensor networks (WSN) to deploy sensor nodes at specific flood-prone locations and collect real-time data.
- The data can be transmitted to a cloud server or a central station, where it can be processed and analyzed using algorithms and models.
- The system can generate alerts and warnings based on the data analysis and send them to the authorities and the public through various channels, such as SMS, email, social media, etc.
- The system can also provide guidance and suggestions for evacuation and rescue operations, such as optimal routes, safe zones, etc.
- The system can improve the accuracy and timeliness of flood prediction and response, and help mitigate the risks and losses caused by floods.



# IOT Garbage Monitoring Using Raspberry Pi

- IOT Garbage Monitoring Using Raspberry Pi is a project that aims to monitor and manage the waste level of garbage bins using ultrasonic sensors, Raspberry Pi, and a remote server.
- The project uses two ultrasonic sensors to measure the distance between the sensor and the waste in the bins. The sensors work on the principle of Doppler's effect, which means they emit sound waves and detect the reflected waves from the waste. The distance is inversely proportional to the waste level.
- The project uses a Raspberry Pi as a digital controller that receives the distance data from the sensors and sends it to a remote server using the Internet. The Raspberry Pi also displays the data on an LCD screen for local monitoring. The remote server can be accessed by the user through a web browser or a mobile app to view the waste level of the bins and get alerts when the bins are full.
- The project can be used for the monitoring and management of garbage in big organizations and industries where dozens of bins are present. It can also be used in homes for the purpose of automatic garbage disposal reminders. The project can help reduce the environmental impact of waste and improve the efficiency of waste collection and disposal.  
- The project can also be extended to classify the waste into different categories, such as recyclable, compostable, or garbage, using a camera and a machine learning model. The camera can capture the image of the waste and send it to the Raspberry Pi, which can run the machine learning model to identify the type of waste. The model can be trained using online tools or platforms, such as Teachable Machine or Edge Impulse, without any coding. The Raspberry Pi can then display the classification result on the LCD screen or send it to the remote server. The project can help promote waste segregation and recycling.



# IOT Circuit Breaker Project

## Unit 1 - Understanding the implementation of IOT in the subject of ADVANCE INTERNET OF THINGS LAB

- The IOT Circuit Breaker Project is a system that provides a password based circuit breaker system using IOT .
- The project aims to solve the issue of fatal accidents that happen with line men due to electric shocks, which are a result of miscoordination or miscommunication between line men and substations .
- The project uses the interconnection network (internet) to control electrical loads with high response time .
- The project uses a wifi module paired with Atmega328p microcontroller locally to connect to the internet .
- The project allows the user to remotely switch on or off the circuit breaker using a web page or a mobile app .
- The project also allows the user to set a password for the circuit breaker, which can be changed or reset as per the user's convenience .
- The project uses a relay driver circuit to control the circuit breaker, which is connected to the microcontroller through digital pins .
- The project uses a 16x2 LCD display to show the status of the circuit breaker, the password, and the wifi connection .
- The project uses a buzzer to alert the user in case of any error or unauthorized access .
- The project can be extended to use wireless solutions for smart circuit breakers, which offer best-in-class RF performance and can extend wireless connectivity across harsh environments.
- The project can also be integrated with other IoT applications, such as home automation, smart irrigation, smart building, smart water monitoring, and automated street lighting.



# IOT Mining Tracking & Worker Safety Helmet

- IOT or the internet of things is a technology that enables us to control hardware devices through the internet.
- Mining is one of the most dangerous jobs in the world, as it involves working in hazardous environments with high risks of accidents, injuries, and fatalities.
- IOT Mining Tracking & Worker Safety Helmet is a system that aims to improve the safety and efficiency of mining operations by using IOT devices on the worker helmets.
- The system consists of the following components:
  - A smart helmet that has sensors to detect temperature, humidity, gas, and collision, as well as an RF transmitter to send the data to the tracker circuit.
  - A tracker circuit that has an RF receiver to receive the data from the helmet nodes, an ATmega microcontroller to process the data, and a Wi-Fi module to send the data to the cloud server over IOT.
  - A cloud server that stores and analyzes the data, and provides a web interface for the mining manager to monitor the status and location of the workers in real time.
- The system works as follows:
  - The worker wears the smart helmet and enters the mining site.
  - The helmet sensors continuously measure the environmental and physical parameters and transmit them to the tracker circuit using RF signals.
  - The tracker circuit receives the signals and converts them into digital data using the microcontroller. It also assigns a unique ID to each helmet node based on the RF frequency.
  - The tracker circuit sends the data along with the ID to the cloud server using the Wi-Fi module and the internet connection.
  - The cloud server stores and analyzes the data, and displays it on a web dashboard for the mining manager to access from any device.
  - The mining manager can view the current location, health, and safety status of each worker on a map, and also get alerts and notifications in case of any emergency or abnormal situation.
  - The system can also trigger an alarm or a rescue operation if the worker is in danger or needs help.



# IOT Prison Break Monitoring & Alerting System

- The system is designed to keep a proper monitoring system on the inmates and track their location on regular basis using IOT and RF technology  .
- The system consists of a microcontroller based circuit, a RF transmitter and a RF receiver .
- The RF transmitter is installed on each inmate and transmits a unique prisoner code wirelessly .
- The RF receiver is connected to the microcontroller and scans through all the inmates as per the data fed to it .
- The microcontroller also communicates with an online alerting portal using IOTGecko .
- The online alerting portal displays the prisoner details and sends out instant alerts and alarms through the internet .
- The system detects the presence of the inmates in the premises and validates their location using RF signals  .
- If an inmate is out of his/her validated location, the system sends an alert signal to the online portal and also throughout the jail  .
- The system aims to prevent prison breaks and enhance the security and safety of the prison  .



# Raspberry Pi Air and Noise Pollution Monitoring System Over IOT

- This system is a project that uses Raspberry Pi and Internet of Things (IOT) to monitor and check the air quality index and the sound pollution of a region in real time.
- The system consists of two main modules: the air quality index monitoring module and the sound intensity detection module.
- The air quality index monitoring module uses sensors to measure the levels of carbon dioxide, methane, and other pollutants in the air. The data is then sent to the Raspberry Pi, which processes and displays it on a LCD screen.
- The sound intensity detection module uses a microphone to capture the ambient noise level and sends it to the Raspberry Pi, which calculates and displays the decibel value on the LCD screen.
- The Raspberry Pi also uploads the data to a cloud server, where it can be accessed and analyzed by authorized users through a web interface. The cloud server can also send alerts to the users if the air quality or noise level exceeds a certain threshold.



## Unit 2 - Solving Societal Problems with the Help of IoT

- IoT stands for Internet of Things, which refers to the network of physical devices, sensors, actuators, and software that can collect, process, and exchange data over the internet.
- IoT can help solve various societal problems by providing smart solutions that can improve efficiency, safety, convenience, and quality of life for people and communities.
- Some examples of societal problems that can be solved with the help of IoT are:

  - **Smart Cities**: IoT can enable smart urban planning and management, such as optimizing traffic flow, reducing pollution, enhancing public safety, and providing better services to citizens.
  - **Smart Healthcare**: IoT can enable remote monitoring and diagnosis, personalized medicine, wearable devices, and telemedicine, which can improve health outcomes, reduce costs, and increase access to healthcare.
  - **Smart Agriculture**: IoT can enable precision farming, smart irrigation, soil and crop monitoring, and livestock tracking, which can increase productivity, reduce waste, and conserve resources.
  - **Smart Energy**: IoT can enable smart grid, smart metering, demand response, and renewable energy integration, which can improve energy efficiency, reliability, and sustainability.
  - **Smart Education**: IoT can enable adaptive learning, gamification, virtual and augmented reality, and collaborative learning, which can enhance student engagement, motivation, and performance.



# Wearable Computer With Temperature Distance Sensors

- A wearable computer is a device that can be worn on the body and can perform various functions such as computing, sensing, communicating, displaying, etc.
- A wearable computer with temperature distance sensors is a specific type of wearable computer that can measure the temperature and distance of objects or environments using contactless sensors.
- Some of the applications of wearable computer with temperature distance sensors are:
  - Health monitoring: The device can monitor the body temperature of the wearer or other people and alert them of any abnormality or fever. It can also measure the distance between the wearer and other people or objects and help them maintain social distancing or avoid collisions.
  - Industrial safety: The device can detect the temperature and distance of machines, equipment, materials, etc. and warn the wearer of any potential hazards or risks. It can also help the wearer to control or operate the machines remotely using the touch screen display.
  - Education and entertainment: The device can provide interactive and immersive learning and gaming experiences by using the temperature and distance sensors to create realistic and dynamic environments. It can also display various information and multimedia content on the screen.
- The main components of a wearable computer with temperature distance sensors are:
  - Raspberry Pi controller: This is the brain of the device that runs the software and processes the data from the sensors and the display. It is a small and low-cost computer that can be programmed using various languages and frameworks.
  - Battery: This is the power source of the device that provides the required voltage and current to the controller and the sensors. It can be rechargeable or replaceable depending on the design and usage of the device.
  - Touch screen display: This is the interface of the device that allows the wearer to interact with the computer and the sensors. It can be a LCD, OLED, or e-ink display that can show various graphics, text, icons, etc.
  - Lidar sensor: This is the distance sensor of the device that uses laser light to measure the distance and speed of objects or environments. It can be a single-point or multi-point sensor that can provide accurate and high-resolution data.
  - Temperature sensor: This is the temperature sensor of the device that uses infrared radiation to measure the temperature of objects or environments. It can be a thermocouple, thermistor, or pyrometer sensor that can provide fast and reliable data.



# Weather Imaging CubeSat with Telemetry Transmission

- A CubeSat is a type of miniaturized satellite that has a standard size of 10 cm x 10 cm x 10 cm and a mass of up to 1.33 kg. CubeSats can be deployed in low Earth orbit for various purposes, such as communication, GPS, remote sensing, and scientific research .
- Weather imaging CubeSats are used to transmit data about weather parameters, such as temperature, humidity, pressure, wind speed, cloud cover, and precipitation, that can be used for prediction and forecasting systems .
- Weather imaging CubeSats typically use a camera or a radiometer to capture images of the Earth's atmosphere and surface at different wavelengths, such as visible, infrared, or microwave . The images can provide information about the structure, dynamics, and evolution of weather systems, such as storms, hurricanes, and tropical cyclones.
- Weather imaging CubeSats also use a telemetry system to transmit the data back to the ground station, where it can be processed, analyzed, and distributed to users. The telemetry system consists of a transmitter, a receiver, an antenna, and a power source. The transmitter encodes the data into a radio signal and sends it to the receiver via the antenna. The receiver decodes the signal and stores the data in a memory device. The power source provides the energy for the telemetry system to operate .
- Weather imaging CubeSats can offer several advantages over conventional weather satellites, such as lower cost, shorter development time, easier launch, and higher spatial and temporal resolution. However, they also face some challenges, such as limited payload capacity, shorter lifespan, orbital decay, and interference from other CubeSats or space debris .
- Weather imaging CubeSats can help solve societal problems related to weather and climate, such as natural disasters, food security, water resources, health, and energy. They can provide timely and accurate data for weather monitoring, forecasting, and warning, as well as for climate research and education  .



# IOT Water Pollution Monitor RC Boat

- IOT Water Pollution Monitor RC Boat is a project that aims to measure and transmit water quality data to an online server using Internet of Things (IOT) technology.
- The project consists of a remote-controlled (RC) boat that carries various sensors to detect parameters such as pH, turbidity, temperature, dissolved oxygen, etc. of the water.
- The boat is controlled by an RC remote that can maneuver it in different directions and speeds. The boat also has a motorized propeller system to provide the forward thrust and a rudder to steer the boat.
- The sensors are connected to an Arduino microcontroller that processes the data and sends it to a Wi-Fi module. The Wi-Fi module connects to the internet and uploads the data to an IOT server such as ThingSpeak or Blynk.
- The data can be accessed and visualized by the user through a web browser or a mobile app. The user can also monitor the location and status of the boat using GPS and battery indicators.
- The project can help to monitor and maintain the water quality of various water bodies such as lakes, rivers, ponds, etc. It can also help to identify the sources and causes of water pollution and take appropriate actions to prevent or reduce it.



# Mountain Climber Health & GPS Tracker

- Mountain climbing is a challenging and risky activity that requires physical fitness, mental strength, and proper equipment.
- Mountain climbers face various hazards such as altitude sickness, hypothermia, frostbite, avalanches, rock falls, and wildlife attacks.
- To ensure the safety and well-being of mountain climbers, it is essential to monitor their health and location in real time and provide timely assistance in case of emergencies.
- Internet of Things (IoT) is a technology that enables the interconnection and communication of devices, sensors, and systems over the internet.
- IoT can be used to create a smart mountain climber health and GPS tracker system that can provide the following benefits:

  - Live heartbeat monitoring: A wearable device such as a smartwatch or a chest strap can measure the heart rate of the climber and send the data to a cloud server via a wireless network. The server can display the live vitals of the climber on a web or mobile application and alert the rescue team if the heart rate exceeds or falls below a predefined threshold.
  - Upper and lower limit settings: The climber or the rescue team can set the upper and lower limits for the heart rate, blood pressure, oxygen saturation, body temperature, and other vital parameters. The system can compare the measured values with the limits and trigger an alarm if any parameter goes out of range.
  - IoT live vitals display: The system can display the live vitals of the climber on a web or mobile application that can be accessed by the climber, the rescue team, or the family members. The system can also show the historical data and trends of the vitals for analysis and diagnosis.
  - GPS location tracking: A GPS module can be attached to the climber's backpack or helmet to track the location and altitude of the climber. The GPS data can be sent to the cloud server and displayed on a map on the web or mobile application. The system can also show the route and distance covered by the climber and alert the rescue team if the climber deviates from the planned path or stops moving for a long time.
  - Added SMS alert in case of limit crossings: The system can send an SMS alert to the rescue team or the family members if any vital parameter crosses the limit or if the GPS location indicates a potential danger. The SMS alert can include the climber's name, ID, location, and the parameter that triggered the alarm.
  - Automatic operation: The system can operate automatically without requiring any manual intervention from the climber or the rescue team. The system can also be powered by a battery or a solar panel to ensure uninterrupted operation.

- The smart mountain climber health and GPS tracker system can be implemented using various IoT devices, sensors, and platforms such as Arduino, Raspberry Pi, ESP8266, Bluetooth, Wi-Fi, GSM, GPS, heart rate sensor, blood pressure sensor, temperature sensor, oxygen sensor, etc.
- The system can help to solve the societal problem of mountain climbing accidents and fatalities by providing real-time health and location monitoring, early warning, and emergency response. The system can also enhance the experience and enjoyment of mountain climbing by providing feedback and guidance.



# Contactless IOT Doorbell

- A contactless IOT doorbell is a device that uses internet of things (IOT) technology to alert the house owner about the arrival of a visitor without requiring any physical contact.
- A contactless IOT doorbell can also perform other functions, such as scanning the temperature of the visitor, recognizing the face of the visitor, sending online notifications to the house owner, and providing voice assistance to the visitor.
- A contactless IOT doorbell can help solve societal problems such as preventing the spread of infectious diseases like Covid-19, enhancing the security and safety of the house, and improving the convenience and accessibility of the doorbell system.
- A contactless IOT doorbell typically consists of the following components:
  - A microcontroller, such as NodeMCU or Raspberry Pi, that acts as the brain of the device and controls the communication and processing of data.
  - A camera module, such as Pi Camera or USB Camera, that captures the image of the visitor and sends it to the microcontroller for face recognition and online streaming.
  - A temperature sensor, such as MLX90614 or DHT11, that measures the body temperature of the visitor and sends it to the microcontroller for fever detection and online logging.
  - A speaker, such as PAM8403 or LM386, that plays a pre-recorded voice message or a synthesized voice to guide the visitor and provide feedback.
  - A button, such as TTP223 or Push Button, that triggers the doorbell system when the visitor touches or approaches it.
  - A wireless module, such as Wi-Fi or Bluetooth, that connects the device to the internet and enables the communication with the house owner and the online database.
  - A power supply, such as battery or adapter, that provides the required voltage and current to the device.
- A contactless IOT doorbell can be implemented using various software tools and platforms, such as:
  - Blynk, which is a mobile app that allows the house owner to view the temperature and image of the visitor, and control the doorbell system remotely.
  - Firebase, which is an online database that stores and retrieves the data of the doorbell system, such as temperature readings, face images, and timestamps.
  - OpenCV, which is a computer vision library that performs face recognition and face detection on the image of the visitor.
  - Google Text-to-Speech, which is a service that converts text to speech and generates a synthetic voice for the speaker.
  - Arduino IDE, which is an integrated development environment that allows the programming and uploading of the code to the microcontroller.



# IOT Smart Parking Using RFID

- IOT Smart Parking Using RFID is a system that aims to replace the traditional parking system with a high technological, IoT based smart parking system by using RFID (radio-frequency identification) technology  .
- RFID is a wireless technology that uses radio waves to identify and track objects. RFID tags are attached to the vehicles and RFID readers are installed at the entry and exit points of the parking area. The RFID readers can read the information stored in the RFID tags and communicate with a central server via the internet  .
- The central server can store and process the data related to the parking status, such as the availability of parking slots, the duration of parking, the payment details, etc. The server can also send notifications to the users via a mobile app or a web portal  .
- The users can use the mobile app or the web portal to check the availability of parking slots, book a parking slot, pay the parking fee, and get directions to the parking area. The users can also use a smart card to access the parking slot. The smart card can store the user's identity and payment information and can be scanned by the RFID readers at the entry and exit points  .
- The advantages of IOT Smart Parking Using RFID are:

  - It can reduce the time and fuel consumption of the users by avoiding the search for parking slots.
  - It can improve the security and safety of the vehicles by preventing unauthorized access and theft.
  - It can optimize the utilization of parking space and generate revenue for the parking operators.
  - It can provide real-time data and analytics for the parking management and planning.
  - It can enhance the user experience and satisfaction by offering convenience and transparency  .

- The disadvantages of IOT Smart Parking Using RFID are:

  - It can be costly and complex to implement and maintain the RFID hardware and software components.
  - It can be vulnerable to hacking and data breaches that can compromise the privacy and security of the users and the system.
  - It can be affected by environmental factors and interference that can reduce the accuracy and reliability of the RFID communication  .

- The applications of IOT Smart Parking Using RFID are:

  - It can be used in various public and private parking areas, such as shopping malls, airports, hospitals, offices, universities, etc.
  - It can be integrated with other smart city solutions, such as traffic management, pollution monitoring, emergency response, etc.
  - It can be extended to other domains, such as logistics, inventory management, asset tracking, etc.  .



# IOT Contactless Covid Testing Booth Automation

- IOT Contactless Covid Testing Booth Automation is a project that aims to design a completely automated instant contactless covid testing booth system by which person details is monitored using RFID technology .
- The system utilizes microcontroller, MATLAB, GSM modem, RFID reader, RFID tags, LCD display, buzzer, and swab collection kit .
- The system works as follows:
  - The person who wants to get tested has to register online and get an RFID tag with a unique ID.
  - The person has to scan the RFID tag at the entrance of the booth and the system will display the person's name, contact number, and address on the LCD screen .
  - The system will also send a confirmation message to the person's mobile number using GSM modem .
  - The person has to enter the booth and follow the instructions on the LCD screen to collect the swab sample using the swab collection kit .
  - The person has to place the swab sample in a sealed container and exit the booth.
  - The system will send the swab sample to the lab for testing and notify the person about the test result via SMS .
- The advantages of this system are:
  - It reduces the human contact and the risk of spreading the virus in the covid testing centers .
  - It saves time and resources by automating the registration and testing process .
  - It provides a safe and convenient covid testing environment for the people .
- The challenges of this system are:
  - It requires a reliable internet connection and power supply for the system to work properly .
  - It depends on the availability and accuracy of the RFID tags and the swab collection kits .
  - It may face technical issues or malfunctions that could affect the system performance and the test results .



# IOT Social Distancing & Monitoring Robot For Queue

- IOT Social Distancing & Monitoring Robot For Queue is a project that aims to prevent the spread of COVID-19 by enforcing social distancing rules in public places where people form queues, such as banks, malls, schools, theatres, etc.
- The project uses a four-wheel robot that follows a line on the ground and moves along with the queue. The robot has a camera, an ultrasonic sensor, a buzzer, and an LCD display. The camera is used to capture the images of the people in the queue and send them to a cloud server. The ultrasonic sensor is used to measure the distance between the robot and the person in front of it. The buzzer is used to alert the person if they are too close to the robot or the person behind them. The LCD display is used to show the distance and the number of people in the queue.
- The cloud server uses a machine learning algorithm to detect the faces of the people in the images and count them. It also uses a database to store the images and the data. The cloud server can send the data to a web application or a mobile application that can be accessed by the authorities or the public to monitor the queue status and the social distancing violations.
- The project has the following advantages:
  - It can help reduce the risk of COVID-19 transmission by ensuring that people maintain a safe distance from each other in queues.
  - It can provide real-time data and feedback to the people and the authorities about the queue situation and the social distancing compliance.
  - It can improve the efficiency and the management of the queues by avoiding overcrowding and chaos.
  - It can be easily deployed and operated in various public places with minimal infrastructure and cost.



# IOT Covid Patient Health Monitor in Quarantine

- IOT stands for Internet of Things, which is a network of physical devices, sensors, actuators, and software that can collect and exchange data over the internet.
- Covid-19 is a highly contagious respiratory disease caused by a novel coronavirus that emerged in late 2019 and has spread worldwide, causing a global pandemic.
- Quarantine is a public health measure that restricts the movement and contact of people who have been exposed to a contagious disease, such as Covid-19, to prevent further transmission.
- IOT Covid Patient Health Monitor in Quarantine is a system that uses IOT devices and sensors to measure and monitor the vital signs of Covid-19 patients who are isolated at home or in designated facilities, and to transmit the data to a remote server or cloud platform where medical professionals can access and analyze it.
- The main objectives of the system are:
  - To reduce the risk of infection and exposure for medical staff and other patients by minimizing physical contact and visits.
  - To provide real-time and continuous health monitoring and alerting for Covid-19 patients who may develop complications or deteriorate rapidly.
  - To optimize the use of limited health resources and facilities by prioritizing the patients who need urgent care and intervention.
  - To improve the quality of care and outcomes for Covid-19 patients by enabling timely diagnosis, treatment, and follow-up.
- The main components of the system are:
  - IOT devices and sensors: These are wearable or non-wearable devices that can measure various health parameters of Covid-19 patients, such as body temperature, pulse rate, blood pressure, oxygen saturation, respiratory rate, etc. Some examples are smart watches, smart bands, thermometers, pulse oximeters, blood pressure monitors, etc. These devices and sensors are connected to the internet via Wi-Fi, Bluetooth, cellular, or other wireless technologies.
  - Remote server or cloud platform: This is the central hub that receives, stores, processes, and displays the data collected from the IOT devices and sensors. It also provides various functions and features, such as data analysis, visualization, dashboard, alerting, notification, reporting, etc. The server or cloud platform can be accessed by authorized medical professionals or caregivers via web or mobile applications.
  - Web or mobile applications: These are the interfaces that allow the medical professionals or caregivers to view and interact with the data and functions provided by the server or cloud platform. They can also communicate with the patients via text, voice, or video calls, and provide feedback, guidance, or instructions. The applications can be accessed via web browsers or mobile devices, such as smartphones or tablets.



# IOT based Manhole Detection and Monitoring System

- IOT based Manhole Detection and Monitoring System is a project that aims to solve the societal problem of accidents, deaths, and floods caused by open, broken, or blocked manholes in urban areas    .
- The project uses sensors, Arduino, GSM, and GPS modules to create a drainage monitoring system that can detect and alert the authorities and the public about the status of the manholes in real time   .
- The project has the following objectives:
  - To prevent accidents and deaths of manual scavengers who clean the underground drainage system by providing them with safety information and equipment .
  - To prevent accidents and injuries of pedestrians and vehicles who may fall into open or broken manholes by providing them with warning signals and barriers  .
  - To prevent contamination of fresh water and urban floods due to sewage overflow by providing them with drainage blockage detection and control   .
- The project has the following components:
  - Sensors: The project uses different types of sensors to measure the water level, water flow, gas concentration, and manhole cover status in the drainage system   . Some of the sensors used are ultrasonic sensor, water flow sensor, MQ-2 gas sensor, and reed switch sensor  .
  - Arduino: The project uses Arduino microcontroller to process the sensor data and send it to the GSM and GPS modules   . Arduino also controls the actuators such as buzzer, LED, and servo motor to provide feedback and action  .
  - GSM: The project uses GSM module to send SMS alerts to the authorities and the public about the manhole status and location using the GPS coordinates   . GSM also enables remote monitoring and control of the system using a mobile phone  .
  - GPS: The project uses GPS module to obtain the accurate location of the manhole and send it to the GSM module   . GPS also helps in mapping and tracking the manholes in a smart city  .
- The project has the following advantages:
  - It is low cost, low maintenance, and easy to install    .
  - It is reliable, accurate, and fast in detecting and reporting the manhole status    .
  - It is scalable, adaptable, and compatible with different types of manholes and drainage systems    .
  - It is beneficial for the health, safety, and environment of the society    .



# IOT based Smart Energy Meter Monitoring with Theft Detection

- IOT based Smart Energy Meter Monitoring with Theft Detection is a system that aims to reduce the energy crisis and the power theft by using smart meters and Internet of Things (IOT) technology.
- The system consists of smart energy meters that are installed at the consumer end and the distribution end, and a master unit that is located at the distribution pole site.
- The smart energy meters can measure the energy consumption, voltage, current, power factor, and other parameters of the electrical load, and send the data to the master unit and a cloud server using wireless communication.
- The master unit can monitor the data from all the smart meters in a section, and compare the total energy consumption at the consumer end and the distribution end. If there is a mismatch, it indicates a possible power theft, and the master unit can alert the authorities and take appropriate actions.
- The cloud server can store the data from all the smart meters and the master unit, and provide a web interface and an android application for the users and the utility company to access the data and control the smart meters remotely.
- The system can also provide features such as billing, load management, demand response, outage detection, and fault diagnosis, using the data from the smart meters and the IOT technology.
- The system can help to reduce the energy wastage, improve the energy efficiency, enhance the reliability and security of the power grid, and prevent the power theft.



# IOT Weather Station Airship

- An IOT weather station airship is a device that can fly in the upper atmosphere and collect data about the weather conditions using sensors and wireless communication.
- It can be used to solve societal problems such as improving weather forecasting, monitoring climate change, detecting natural disasters, and providing emergency services.
- Some of the features and benefits of an IOT weather station airship are:

  - It can reach any height as controlled by the user, and cover a large area of observation.
  - It can measure atmospheric pressure, temperature, humidity, wind direction and speed, and other parameters using sensors such as DHT22, BMP180, and UV sensor.
  - It can send the data to an online portal for analysis and visualization using IOT connectivity such as LoRaWAN, WiFi, or cellular network.
  - It can be powered by a solar panel and a battery, and have a long endurance and low maintenance cost.
  - It can be controlled remotely using a web dashboard or a mobile app, and have features such as GPS, camera, and LED display.

- Some of the challenges and limitations of an IOT weather station airship are:

  - It can be affected by weather conditions such as rain, snow, fog, and lightning, and may require protection and stabilization mechanisms.
  - It can face interference and security issues from other wireless devices and networks, and may require encryption and authentication methods.
  - It can have legal and ethical implications such as privacy, ownership, and regulation, and may require compliance and consent from authorities and stakeholders.



# IOT based Three Phase Power Failure Monitoring with SMS Alerts

- IOT based Three Phase Power Failure Monitoring with SMS Alerts is a system that monitors the status of three-phase power supply and alerts the authorized person via SMS in case of any failure  .
- The system consists of the following components:
  - Three-phase transformer: It converts the high voltage AC power to low voltage AC power for the system.
  - Voltage sensors: They measure the voltage of each phase and send the data to the microcontroller.
  - Microcontroller: It processes the data from the voltage sensors and compares it with the predefined threshold values. It also controls the LCD display and the GSM module.
  - LCD display: It shows the voltage values of each phase and the status of the power supply.
  - GSM module: It communicates with the mobile phone of the authorized person and sends SMS alerts in case of any failure.
- The system works as follows:
  - The three-phase transformer provides low voltage AC power to the system.
  - The voltage sensors measure the voltage of each phase and send the data to the microcontroller.
  - The microcontroller processes the data and compares it with the predefined threshold values. If the voltage of any phase is below the threshold, it indicates a power failure in that phase.
  - The microcontroller then sends a command to the GSM module to send an SMS alert to the authorized person with the details of the failure.
  - The microcontroller also updates the LCD display with the voltage values and the status of the power supply.
- The system has the following advantages:
  - It can detect and report power failures in real time and prevent damage to the equipment and appliances connected to the three-phase power supply.
  - It can reduce the downtime and maintenance costs of the power supply system.
  - It can improve the safety and reliability of the power supply system.
  - It can be easily implemented and configured using IOT devices and GSM technology.
- The system has the following applications:
  - It can be used in industrial, commercial, and residential sectors where three-phase power supply is required.
  - It can be used in remote and rural areas where power supply is unreliable and prone to failures.
  - It can be used in critical and sensitive areas where power supply is essential and failure can cause serious consequences.



# IOT based Intelligent Gas Leakage Detector Using Arduino

- This is a project that uses Internet of Things (IoT) and Arduino to detect gas leakage in the surroundings and send data to an IOT module.
- IoT is the networking of physical things that can communicate with the help of sensors, electronics, software, and connectivity.
- Arduino is an open-source platform that consists of a microcontroller and a software environment that can be used to program and control the microcontroller.
- The main components of this project are:
  - MQ5 gas sensor: This is a sensor that can detect various gases such as LPG, methane, alcohol, etc. It has a high sensitivity and fast response time. It outputs an analog voltage that varies according to the concentration of the gas in the air.
  - ESP8266: This is a low-cost Wi-Fi module that can connect to the internet and send or receive data. It can be programmed using Arduino IDE or other software tools.
  - Buzzer: This is a device that can produce a loud sound when activated by an electric signal. It can be used to alert the user or the authorities in case of a gas leakage.
  - LED: This is a light-emitting diode that can emit different colors of light when powered by an electric current. It can be used to indicate the status of the system or the level of gas leakage.
  - LCD: This is a liquid crystal display that can show alphanumeric characters or graphics on a screen. It can be used to display the gas concentration or other information to the user.
- The working principle of this project is as follows:
  - The MQ5 gas sensor is connected to the analog input pin of the Arduino. The sensor continuously monitors the level of gas in the air and outputs a voltage that corresponds to the gas concentration.
  - The Arduino reads the analog voltage from the sensor and converts it to a digital value using an analog-to-digital converter (ADC). The Arduino then compares the digital value with a predefined threshold value and determines if there is a gas leakage or not.
  - If there is a gas leakage, the Arduino activates the buzzer and the LED to alert the user. The Arduino also sends the gas concentration data to the ESP8266 module using a serial communication protocol.
  - The ESP8266 module connects to the internet using Wi-Fi and uploads the data to an IOT platform such as ThingSpeak, Blynk, Firebase, etc. The IOT platform can store, process, and visualize the data and also send notifications or alerts to the user or the authorities via email, SMS, or mobile app.
  - The LCD is connected to the Arduino using a parallel or serial interface. The LCD displays the gas concentration or other information to the user.
- The advantages of this project are:
  - It can detect gas leakage in real-time and prevent accidents or disasters caused by gas explosion or suffocation.
  - It can send data to the internet and enable remote monitoring and control of the system.
  - It can alert the user or the authorities in case of a gas leakage and facilitate quick response and action.
  - It can display the gas concentration or other information to the user and enhance the user experience and awareness.
  - It can be easily implemented using low-cost and readily available components and software tools.



# 360° Aerial Surveillance UAV With IOT Camera

- Aerial surveillance is the key to security and military based operations. It provides real time information on enemy movements which plays a key role in precision strikes  .
- Large drones are very large in size which can be easily detected by enemy radars and also require large runways for takeoff and landing.
- Small drones are more suitable for covert operations as they can fly at low altitudes and avoid detection. However, they have limited field of view and battery life.
- 360° Aerial Surveillance UAV With IOT Camera is a project that aims to develop a small drone that can capture 360-degree images and videos and transmit them to a remote server using IOT technology .
- The drone consists of the following components  :
  - A quadcopter frame with four propellers and motors
  - A flight controller board with sensors and GPS module
  - A Raspberry Pi 3 as the main processing unit
  - A 360-degree camera module attached to the bottom of the frame
  - A Wi-Fi module for wireless communication
  - A battery pack for power supply
- The drone can be controlled by a smartphone app or a web interface that allows the user to view the live feed from the camera and send commands to the drone .
- The drone can also perform autonomous tasks such as following a predefined path, hovering at a fixed location, or returning to the base station .
- The drone can be used for various applications such as  :
  - Border security and surveillance
  - Disaster management and rescue operations
  - Traffic monitoring and management
  - Crowd surveillance and face recognition
  - Wildlife conservation and research
  - Entertainment and tourism
- The drone has the following advantages over conventional drones :
  - It can capture a complete view of the surroundings without any blind spots
  - It can transmit high-quality images and videos in real time
  - It can operate in low-light and adverse weather conditions
  - It can fly at low altitudes and avoid detection
  - It can be easily deployed and retrieved
  - It can be integrated with other IOT devices and platforms
- The drone also has some challenges and limitations such as :
  - It requires a stable and secure wireless connection
  - It consumes more power and has a shorter battery life
  - It has a limited payload and range
  - It may face legal and ethical issues regarding privacy and safety



# IOT Garbage Segregator & Bin Level Indicator

- IOT Garbage Segregator & Bin Level Indicator is a system that uses Internet of Things (IoT) technology to automate the process of garbage segregation and level monitoring in dustbins.
- The system consists of multiple smart dustbins that are equipped with sensors, microcontrollers, and wireless modules to detect the type and level of garbage in each bin.
- The system can segregate the garbage into different categories, such as organic, plastic, metal, paper, etc., based on the weight, color, or shape of the waste items.
- The system can also measure the level of garbage in each bin and transmit the data to an online platform, such as IOT gecko, that displays the bin level data over the internet.
- The system can alert the authorities or the waste management service providers when the garbage bins need to be emptied, thus reducing the overflow of waste and improving the efficiency of waste collection and disposal.
- The system can help to solve the societal problems of waste management, such as environmental pollution, health hazards, resource depletion, and landfill crisis, by promoting recycling and reducing waste generation.



# IOT Temperature & Mask Scan Entry System

- An IOT Temperature & Mask Scan Entry System is a device that uses a contactless temperature scanner and a camera to capture images of people who want to enter a building or a facility.
- The device is connected to a gate-like structure that prevents entry if a high temperature or the absence of a mask is detected.
- The device is also connected to a cloud server that stores the data of the scanned people and sends alerts to the authorities if any abnormality is found.
- The device aims to increase COVID-19 indoor safety by screening people for fever and mask compliance, which are two of the main symptoms and preventive measures of the disease.
- The device can be placed in or in front of buildings, such as universities, offices, hospitals, malls, etc., to control the access of people and reduce the risk of infection.
- The device uses a temperature sensor and a camera connected to a Raspberry Pi system, which runs a machine learning algorithm to detect the face, measure the temperature, and identify the mask status of the person.
- The device also uses a 7 inch touch screen to display the results and instructions to the person, and a thermal and video camera to improve the accuracy and quality of the image.
- The device can be powered by a battery or a power supply, and can communicate with the cloud server via Wi-Fi or cellular network.
- The device can be customized according to the needs and preferences of the user, such as the temperature threshold, the mask requirement, the gate type, the alert mode, etc.



# IOT based Smart Agriculture Monitoring System Project

- This project is an application of the Internet of Things (IoT) in the domain of smart agriculture.
- The project aims to use IoT sensors and devices to monitor and control various parameters that affect the growth and yield of crops, such as temperature, humidity, light, soil moisture, and water level.
- The project consists of the following components:
  - Sensors: The project uses four types of sensors to measure the environmental conditions in the agricultural field. These are:
    - Temperature sensor: This sensor measures the ambient temperature and sends the data to the controller.
    - Humidity sensor: This sensor measures the relative humidity and sends the data to the controller.
    - Light sensor: This sensor measures the intensity of light and sends the data to the controller.
    - Soil moisture sensor: This sensor measures the moisture level in the soil and sends the data to the controller.
  - Controller: The project uses an Arduino board as the controller that receives the data from the sensors and processes it according to the predefined logic. The controller also sends commands to the actuators based on the sensor data.
  - Actuators: The project uses two types of actuators to perform actions based on the controller's commands. These are:
    - Water pump: This actuator controls the water supply to the field based on the soil moisture level and the water level in the tank.
    - LED strip: This actuator provides artificial light to the plants based on the light sensor data and the time of the day.
  - Communication module: The project uses a GSM modem or a Wi-Fi module to communicate with the cloud server or the user's mobile device. The communication module sends the sensor data and the controller status to the cloud server or the user's mobile device and receives commands or queries from them.
  - Cloud server or user's mobile device: The project uses a cloud server or a user's mobile device to store and display the sensor data and the controller status. The cloud server or the user's mobile device also allows the user to remotely monitor and control the system through a web or mobile application.
- The project has the following advantages:
  - It improves the efficiency and productivity of agriculture by providing optimal conditions for the crops.
  - It reduces the human intervention and labor cost by automating the irrigation and lighting system.
  - It saves water and energy by using them only when needed.
  - It enables the user to access the system from anywhere and anytime through the internet.
  - It provides real-time data and alerts to the user about the system status and any anomalies.



# IOT Based Automatic Vehicle Accident Detection and Rescue System

- This system is a solution for solving the societal problem of delayed rescue operations for vehicle accidents.
- It uses Internet of Things (IoT) technology to detect accidents and communicate information to rescue teams via SMS, web applications, or Android mobile applications  .
- It consists of the following components:
  - A vibration sensor that is attached to the vehicle and produces a digital pulse output when an accident or collision occurs .
  - A microcontroller (such as Arduino Nano) that receives the sensor output and triggers the communication module .
  - A communication module (such as GSM or Wifi) that sends the accident location and other details to the rescue team or emergency contacts   .
  - A GPS module that provides the accurate location of the vehicle    .
  - A power supply that provides the necessary voltage and current to the system .
- The system works as follows:
  - When an accident occurs, the vibration sensor detects the impact and sends a signal to the microcontroller .
  - The microcontroller activates the communication module and the GPS module .
  - The communication module sends an SMS or a web or mobile notification to the rescue team or the emergency contacts with the accident location and other details   .
  - The rescue team can access the location and other details through a web or mobile application and reach the accident site as soon as possible .
- The benefits of this system are:
  - It reduces the response time and saves lives of the accident victims  .
  - It provides accurate and reliable information to the rescue team   .
  - It is easy to install and operate .
  - It is cost-effective and energy-efficient .



# Greenhouse Monitoring and Control System using IOT Project

- A greenhouse is a structure where plants such as flowers and vegetables are grown under controlled environmental conditions.
- Greenhouse monitoring and control system using IOT project is a system that uses sensors, actuators, microcontrollers, and internet connectivity to monitor and control the environmental parameters inside the greenhouse, such as temperature, humidity, light intensity, and soil moisture.
- The main objectives of this project are:
  - To improve the productivity and quality of plants by providing optimal conditions for their growth.
  - To reduce the manual labor and human errors involved in greenhouse management.
  - To enable remote access and control of the greenhouse system using a web or mobile application.
- The main components of this project are:
  - Sensors: These are devices that measure the physical quantities of the environment, such as temperature, humidity, light intensity, and soil moisture. They send the data to the microcontroller using analog or digital signals.
  - Microcontroller: This is a small computer that processes the data from the sensors and sends commands to the actuators using logic and algorithms. It also communicates with the internet using a Wi-Fi or Ethernet module.
  - Actuators: These are devices that perform actions based on the commands from the microcontroller, such as turning on or off fans, heaters, lights, water pumps, etc. They control the environmental parameters inside the greenhouse.
  - Internet: This is a network that connects the microcontroller to a web or mobile application, where the user can view the data from the sensors, set the desired values for the parameters, and control the actuators remotely.
- The main steps of this project are:
  - Designing and assembling the hardware components, such as sensors, microcontroller, actuators, power supply, etc.
  - Programming the microcontroller using Arduino IDE or any other suitable platform, to read the data from the sensors, apply the logic and algorithms, send the commands to the actuators, and communicate with the internet.
  - Developing the web or mobile application using HTML, CSS, JavaScript, PHP, or any other suitable languages, to display the data from the sensors, allow the user to set the desired values for the parameters, and control the actuators remotely.
  - Testing and debugging the system, to ensure its functionality and reliability.



# IOT Based Coal Mine Safety Monitoring and Alerting System

- IOT based coal mine safety monitoring and alerting system is a project that aims to improve the safety and security of coal miners and detect the hazards inside a coal mine .
- The system consists of sensors, an IoT gateway, an LCD screen, an RF transmitter, and a cloud platform .
- The sensors are installed in the transmitter module, which is carried by the coal miners or placed in strategic locations inside the mine .
- The sensors can measure parameters such as temperature, smoke, methane, water level, and fire ignition  .
- The transmitter module sends the sensor data to the IoT gateway using a low power communication protocol such as LoRa or Zigbee.
- The IoT gateway analyzes the data and displays it on the LCD screen. It also sends the data to the cloud platform using the internet .
- The cloud platform can store, process, and visualize the data, and provide alerts and notifications to the authorities and the miners in case of any emergency or abnormal situation .
- The system can help to prevent accidents, save lives, and reduce environmental damage caused by coal mining.



# IOT Based Heart Monitoring System Using ECG

- ECG (Electrocardiogram) is a technique that records the electrical activity of the heart over a period of time using electrodes attached to the skin.
- ECG can be used to diagnose various heart conditions, such as arrhythmias, heart attacks, and heart failure.
- IOT (Internet of Things) is a network of physical devices, sensors, and software that can communicate and exchange data over the internet.
- IOT can be used to enhance the health care system by enabling remote monitoring, diagnosis, and treatment of patients using telemedicine and cloud computing.
- IOT Based Heart Monitoring System Using ECG is a system that combines ECG and IOT technologies to measure and transmit the ECG signals of a patient to a remote server or a cloud platform, where they can be analyzed and displayed in real-time.
- IOT Based Heart Monitoring System Using ECG can provide the following benefits:
  - It can reduce the cost and time of health care by eliminating the need for physical visits to the hospital or clinic.
  - It can improve the quality and accuracy of health care by providing continuous and comprehensive data of the heart condition of the patient.
  - It can enhance the accessibility and availability of health care by allowing the patient to monitor their own heart health at home or anywhere with an internet connection.
  - It can facilitate the early detection and prevention of heart diseases by alerting the patient or the doctor of any abnormality or emergency in the ECG signals.
- IOT Based Heart Monitoring System Using ECG consists of the following components:
  - An ECG sensor that measures the electrical activity of the heart using electrodes attached to the chest, arms, or legs of the patient.
  - An IOT device that collects, processes, and transmits the ECG data from the sensor to the internet using a wireless communication protocol, such as Wi-Fi, Bluetooth, or cellular network.
  - A cloud platform or a web server that receives, stores, and analyzes the ECG data from the IOT device using various algorithms and techniques, such as signal processing, machine learning, and artificial intelligence.
  - A web or a mobile application that displays the ECG waveform, parameters, and alerts to the patient or the doctor in real-time using a graphical user interface (GUI).
- IOT Based Heart Monitoring System Using ECG can be implemented using various hardware and software tools, such as Arduino, NodeMCU, AD8232, AWS, Ubidots, etc.



# IOT based Anti-theft Flooring System using Raspberry Pi

- This system is designed to secure and guard the house in the absence of the owner by monitoring the entire floor for movement  .
- The system consists of secure flooring tiles connected with IOT, piezo sensors, a camera, a wifi modem, and a Raspberry Pi controller .
- The system can be turned on or off by the owner through a web interface.
- When the system is turned on, any step on the floor is detected by the piezo sensors and the information is sent to the Raspberry Pi controller .
- The controller processes the signal and moves the camera to the area where the movement was detected .
- The camera captures the image of the intruder and transmits it over the internet to the owner's email .
- The owner can check the image and take appropriate action, such as calling the police or alerting the neighbors .
- The system is based on IOT, which enables remote monitoring and control of the house security  .
- The system is cost-effective, easy to install, and scalable to cover larger areas.
- The system can also be integrated with other sensors, such as smoke detectors, gas leak detectors, or motion sensors, to enhance the safety of the house.



# Raspberry Pi based Weather Reporting Over IOT

- This system can be used to monitor and update weather conditions over the internet using Raspberry Pi and various sensors.
- The system monitors three parameters namely temperature, humidity and rainfall. These values are then displayed on LCD and also updated over the IoT gecko.
- The system uses DHT11 sensor for temperature and humidity, rain sensor for rainfall and BMP180 sensor for atmospheric pressure.
- The system uses Raspberry Pi as a base station that collects data from the sensors and sends it to the IoT gecko server using Wi-Fi module.
- The IoT gecko server provides a web interface for the user to view the weather data in real time and also generate graphs and reports.
- The system is cost effective and has low power consumption in order to save money as well as power utilization.
- The system can provide accurate and precise weather-related data of a specific area as opposed to the generic type regional weather forecasts.
- The system can be useful for farmers, meteorologists, travelers and general public who want to know the weather conditions of their location.



# IOT Early Flood Detection & Avoidance

- Floods are natural disasters that can cause severe damage to property and lives.
- Early detection and avoidance of floods can help reduce the impact and save lives.
- IOT (Internet of Things) is a technology that connects devices and sensors to the internet, enabling data collection and communication.
- IOT can be used to monitor various natural factors that can indicate a flood, such as rainfall, water level, soil moisture, etc.
- IOT can also be used to alert the authorities and the public about the flood risk and provide guidance for evacuation and rescue.
- IOT-based early flood detection and avoidance system consists of the following components   :
  - Sensor nodes: These are devices that measure the natural factors and send the data to the cloud or a central server. They can be deployed at strategic locations such as rivers, dams, bridges, etc. They can use wireless communication protocols such as Wi-Fi, Bluetooth, ZigBee, etc.
  - Cloud or central server: This is the platform that receives, stores, and processes the data from the sensor nodes. It can use machine learning algorithms to analyze the data and predict the flood risk. It can also send alerts and notifications to the authorities and the public through various channels such as SMS, email, social media, etc.
  - User interface: This is the application or website that displays the data and the flood risk to the users. It can also provide maps, directions, and instructions for evacuation and rescue. It can be accessed through smartphones, tablets, laptops, etc.
- IOT-based early flood detection and avoidance system can provide the following benefits   :
  - Real-time monitoring and detection of flood events
  - Early warning and notification of flood risk
  - Guidance and assistance for evacuation and rescue
  - Reduction of property damage and loss of lives
  - Improvement of disaster management and response



# IOT Garbage Monitoring Using Raspberry Pi

- IOT Garbage Monitoring Using Raspberry Pi is a project that aims to solve the problem of waste management and disposal by using sensors, internet, and Raspberry Pi.
- The project uses ultrasonic sensors to measure the level of garbage in the bins and sends the data to a remote server or a user via internet  .
- The project also uses a Raspberry Pi as a digital controller that processes the sensor data and displays it on an LCD screen.
- The project can also use a machine learning model to classify the type of trash (recyclable, compostable, or garbage) by using a camera and a Raspberry Pi.
- The project can help in reducing the environmental impact of waste, improving the efficiency of waste collection and disposal, and raising awareness among the users about the importance of proper waste segregation  .



# IOT Circuit Breaker Project

- IOT Circuit Breaker Project is a project that aims to provide a password based circuit breaker system using IOT .
- The project is motivated by the problem of fatal accidents that happen with line men due to electric shocks, which are a result of miscoordination or miscommunication between line men and substations .
- The project uses a wifi module paired with Atmega328p microcontroller locally to connect to the internet and control electrical loads .
- The project also uses a relay driver circuit to switch on or off the electrical loads based on the commands received from the internet .
- The project allows the user to enter a password through a web page to access the circuit breaker system and view the status of the electrical loads .
- The project also sends an SMS alert to the line men and the substation when the circuit breaker is switched on or off .
- The project demonstrates the use of IOT for solving societal problems such as improving the safety and efficiency of electrical systems .
- The project also showcases the use of wireless solutions for smart circuit breakers that offer high response time, best-in-class RF performance, and extended wireless connectivity across harsh environments.
- The project can be further enhanced by adding features such as voice control, energy monitoring, fault detection, and remote diagnosis.



# IOT Mining Tracking & Worker Safety Helmet

- IOT or the internet of things is a technology that enables us to control hardware devices through the internet.
- Mining is one of the most dangerous jobs in the world, as miners face various risks such as gas explosions, cave-ins, fires, etc .
- IOT Mining Tracking & Worker Safety Helmet is a system that aims to improve the safety and efficiency of miners by using a microcontroller-based circuit on the worker helmet  .
- The system has the following features and benefits:
  - The helmet is integrated with an RF based tracking system that helps map the current location of workers through the entire mining site .
  - The helmet also has sensors to monitor the environmental parameters such as temperature, humidity, gas, etc and alert the workers and the control room in case of any abnormality .
  - The helmet can communicate with other helmets and the control room through wireless communication modules such as Zigbee, Bluetooth, Wi-Fi, etc .
  - The helmet can also provide audio and visual feedback to the workers through speakers, LEDs, LCD, etc .
  - The system can provide data over IOT to a web server or a cloud platform where it can be accessed and analyzed by authorized users .
  - The system is cost-effective, practical, eco-friendly, and reliable .
- The system can help reduce the accidents and fatalities in the mining industry, as well as increase the productivity and efficiency of the workers  .



# IOT Prison Break Monitoring & Alerting System

- The system is designed to prevent and detect prison breaks by tracking the location and activities of the inmates using radio frequency (RF) technology and Internet of Things (IOT).
- The system consists of the following components:
  - RF trackers: These are small devices attached to each inmate that transmit a unique code wirelessly to the central monitoring units. The RF trackers can also detect the movement and orientation of the inmates.
  - Central monitoring units: These are microcontroller-based circuits that scan and receive the signals from the RF trackers and compare them with the predefined data of the inmates. The central monitoring units can also control the alert signals and the communication with the online portal.
  - Online portal: This is a web-based application that displays the status and location of each inmate on a map and alerts the authorities in case of any prison break. The online portal is developed using IOTGecko, a cloud platform for IOT applications.
- The system works as follows:
  - The RF trackers continuously send their codes and location data to the central monitoring units, which store them in a database.
  - The central monitoring units compare the received data with the predefined data of the inmates, such as their names, cell numbers, and valid locations.
  - If the central monitoring units detect any discrepancy or anomaly in the data, such as an inmate being out of his/her valid location, they send an alert signal to the online portal and also to the speakers and sirens installed in the prison.
  - The online portal receives the alert signal and displays the details of the inmate who is trying to escape, such as his/her name, photo, and location on a map. The online portal also sends a notification to the authorities, such as the prison officers and the police, via email or SMS.
  - The authorities can then take immediate action to stop the prison break and capture the inmate before he/she escapes from the prison premises.
- The system has the following advantages:
  - It enhances the security and safety of the prison by preventing and detecting prison breaks in real time.
  - It reduces the manpower and cost required for monitoring and guarding the inmates.
  - It provides accurate and reliable information about the location and activities of the inmates.
  - It improves the accountability and transparency of the prison management.
  - It facilitates the communication and coordination between the prison authorities and the police.



# Raspberry Pi Air and Noise Pollution Monitoring System Over IOT

- This is a project that uses an IOT-based method to monitor and check the air quality index and the sound pollution of a region using Raspberry Pi    .
- The system consists of two main modules: the air quality index monitoring module and the sound intensity detection module .
- The air quality index monitoring module uses sensors to measure the levels of carbon dioxide, methane, and other gases in the air that are harmful to human health and the environment .
- The sound intensity detection module uses a microphone to measure the noise level in decibels and detect any abnormal sounds that may indicate a disturbance or an emergency  .
- The data collected from the sensors and the microphone is continuously fed to a controller, which is a Raspberry Pi board, that processes and stores the data .
- The Raspberry Pi board also connects to the internet via Wi-Fi and sends the data to a cloud-based platform, such as ThingSpeak or Firebase, where it can be accessed and visualized by authorized users  .
- The cloud-based platform also provides an anomaly notification module that alerts the users via email or SMS if the air quality index or the sound intensity exceeds a predefined threshold or shows an unusual pattern .
- The system can be deployed in various locations, such as industrial areas, residential areas, schools, hospitals, etc., to monitor and control the air and noise pollution levels and improve the quality of life and the environment    .



## Unit 3 - Problem Analysis and Designing a Solution

- In this unit, you will learn how to analyze a given problem and design a solution using various tools and techniques.
- Problem analysis is the process of identifying the nature, scope, and causes of a problem, and defining the goals and constraints of a solution.
- Designing a solution is the process of creating a plan or a blueprint for implementing a solution, using appropriate methods and tools.
- Some of the tools and techniques for problem analysis and designing a solution are:

  - Flowcharts: A flowchart is a diagram that shows the steps of a process or an algorithm using symbols and arrows. Flowcharts can help visualize the logic and structure of a solution, and identify errors or inefficiencies.
  - Pseudocode: Pseudocode is a way of writing the steps of an algorithm using natural language and basic programming concepts. Pseudocode can help translate the flowchart into a more detailed and readable form, and prepare for coding.
  - Data structures: Data structures are ways of organizing and storing data in a program, such as arrays, lists, stacks, queues, trees, graphs, etc. Data structures can help optimize the performance and functionality of a solution, and handle complex data types and operations.
  - Modular design: Modular design is a way of breaking down a large and complex problem into smaller and simpler subproblems, and solving them separately. Modular design can help reduce the complexity and redundancy of a solution, and improve the readability and maintainability of the code.
  - Testing and debugging: Testing and debugging are ways of checking and correcting the errors or bugs in a solution, using various tools and techniques. Testing and debugging can help ensure the correctness and quality of a solution, and prevent or fix potential problems.



# Wearable Computer With Temperature Distance Sensors

## Introduction

- A wearable computer is a device that can be worn on the body and provides computing and communication capabilities.
- A wearable computer with temperature distance sensors is a device that can measure the temperature and distance of objects or people in the environment using contactless sensors.
- A wearable computer with temperature distance sensors can be used for various applications, such as health monitoring, security, navigation, gaming, education, etc.

## Problem Analysis

- The main problem is to design and implement a wearable computer with temperature distance sensors that is compact, portable, user-friendly, accurate, and reliable.
- The subproblems are:
  - How to select the appropriate hardware components, such as the controller, battery, display, lidar sensor, and temperature sensor, for the wearable computer?
  - How to integrate the hardware components and mount them on a wrist strap or a similar wearable accessory?
  - How to program the controller to interface with the sensors and the display, and to perform the required computations and communications?
  - How to test and evaluate the performance and functionality of the wearable computer with temperature distance sensors?

## Designing a Solution

- The possible steps for designing a solution are:
  - Conduct a literature review and market survey to identify the existing solutions and the user requirements for a wearable computer with temperature distance sensors.
  - Choose the hardware components based on the specifications, availability, cost, and compatibility. For example, a Raspberry Pi controller with a battery, touch screen display, lidar sensor, and temperature sensor can be used .
  - Design a circuit diagram and a layout for connecting the hardware components and mounting them on a wrist strap or a similar wearable accessory.
  - Write a program code for the controller using a suitable programming language, such as Python, to interface with the sensors and the display, and to perform the required computations and communications. The program code should include the following functions:
    - Initialize the sensors and the display, and set the parameters, such as the sampling rate, the measurement range, the calibration factors, etc.
    - Read the sensor data and convert them to the appropriate units, such as degrees Celsius, meters, etc.
    - Display the sensor data and the graphical representations, such as the temperature trend, the distance map, etc., on the touch screen display.
    - Transmit the sensor data and the graphical representations to a remote device, such as a smartphone or a computer, using Bluetooth or Wi-Fi connectivity.
    - Receive the commands and the feedback from the remote device, and adjust the settings or the functions of the wearable computer accordingly.
  - Test and evaluate the performance and functionality of the wearable computer with temperature distance sensors using various scenarios and metrics, such as the accuracy, the precision, the response time, the battery life, the user satisfaction, etc.



# Weather Imaging CubeSat with Telemetry Transmission

- A CubeSat is a type of miniaturized satellite that has a standard size of 10x10x10 cm and a mass of up to 1.33 kg. CubeSats can be deployed in low Earth orbit for various applications, such as communication, GPS, remote sensing, and scientific research .
- A weather imaging CubeSat is a CubeSat that is equipped with a camera or a radiometer to capture images or measurements of the Earth's atmosphere, clouds, and precipitation. These data can be used for weather prediction and forecasting systems  .
- A telemetry transmission CubeSat is a CubeSat that is capable of transmitting data back to the ground station using a radio or a laser link. The data can include the CubeSat's status, location, orientation, and payload information .
- A weather imaging CubeSat with telemetry transmission is a CubeSat that combines both functions of weather imaging and data transmission. It can collect and send weather data to the Earth for analysis and monitoring .
- The advantages of using weather imaging CubeSats with telemetry transmission are:
  - They are low-cost, lightweight, and easy to launch compared to conventional satellites .
  - They can provide high-resolution, real-time, and global coverage of weather phenomena .
  - They can enhance the accuracy and reliability of weather forecasting and warning systems .
  - They can support scientific research and education on atmospheric processes and climate change .
- The challenges of designing and operating weather imaging CubeSats with telemetry transmission are:
  - They have limited power, memory, and communication resources .
  - They have to withstand harsh environmental conditions, such as radiation, temperature, and orbital decay .
  - They have to comply with the regulations and standards of the space agencies and the frequency spectrum authorities .
  - They have to ensure the quality and security of the data transmission and reception .



# IOT Water Pollution Monitor RC Boat

- IOT Water Pollution Monitor RC Boat is a project that aims to measure and transmit water quality data using an RC boat equipped with sensors and an IOT module.
- The project consists of the following components:
  - An RC boat with a motorized propeller system, a battery, and a wireless receiver.
  - A remote control unit with a wireless transmitter and a joystick to maneuver the boat.
  - A water quality sensor module with a pH sensor, a turbidity sensor, a temperature sensor, and a conductivity sensor.
  - An IOT module with a microcontroller, a Wi-Fi module, and an LCD display.
  - An IOT server that receives and stores the water quality data from the IOT module and displays it on a web page or a mobile app.
- The project works as follows:
  - The user controls the RC boat using the remote control unit and drives it into the water area for sample collection.
  - The water quality sensor module measures the pH, turbidity, temperature, and conductivity of the water and sends the data to the IOT module.
  - The IOT module processes the data and displays it on the LCD screen. It also connects to the Wi-Fi network and uploads the data to the IOT server.
  - The IOT server stores the data in a database and displays it on a web page or a mobile app that can be accessed by the user or other stakeholders.
  - The user can monitor the water quality data in real-time and identify the sources and levels of pollution in the water.
- The project has the following advantages:
  - It is a low-cost and portable solution that can be used in various water bodies such as rivers, lakes, ponds, etc.
  - It is a remote-operated and wireless system that does not require physical contact with the water or manual sampling.
  - It is an IOT-based system that enables real-time and online monitoring of water quality and pollution.
  - It is a scalable and modular system that can be extended with more sensors and features as per the user's requirements.



# Mountain Climber Health & GPS Tracker

## Problem Analysis

- Mountain climbing is a challenging and risky activity that requires physical fitness, mental toughness, and proper equipment.
- Mountain climbers face various hazards such as altitude sickness, hypothermia, frostbite, avalanches, rock falls, and crevasses.
- Mountain climbers need to monitor their health and location constantly to avoid accidents and emergencies.
- Mountain climbers also need to communicate with their team members and base camp to coordinate their movements and report their status.
- Conventional devices such as smartphones, watches, and radios may not work well in harsh mountain environments due to low battery life, poor signal, or extreme weather conditions.

## Designing a Solution

- A possible solution is to design a smart mountain climber device that can track the vitals and location of climbers in real time and transmit the data to a cloud server via the Internet of Things (IoT) technology.
- The device can be worn as a wristband or a chest strap that can measure the heart rate, blood pressure, oxygen saturation, and body temperature of the climber using sensors.
- The device can also have a GPS module that can pinpoint the exact location of the climber on a map and display the altitude, speed, and distance traveled.
- The device can have a wireless communication module that can connect to a smartphone or a satellite phone via Bluetooth or Wi-Fi and send the data to a web application or a mobile app that can be accessed by the team members and the base camp.
- The device can have a battery that can last for several days or weeks and can be recharged by solar power or kinetic energy.
- The device can have a display that can show the climber's vitals and location, as well as the time, date, weather, and notifications.
- The device can have a button that can trigger an emergency alert in case of danger or distress, which can send a message and a sound to the team members and the base camp, as well as activate a flashing light and a siren on the device.
- The device can have a software that can analyze the data and provide feedback and guidance to the climber, such as warning them of potential hazards, advising them to rest or descend, or suggesting the best route to take.



# Contactless IOT Doorbell

- A contactless IOT doorbell is a device that uses internet of things (IOT) technology to alert the house owner about the arrival of a visitor without requiring any physical contact.
- A contactless IOT doorbell can also provide additional features such as temperature scanning, face recognition, voice interaction, security camera, and online alerts.
- A contactless IOT doorbell can help prevent the spread of Covid-19 and other infectious diseases by avoiding direct contact between the visitor and the doorbell or the house owner.
- A contactless IOT doorbell can also enhance the security and convenience of the house owner by allowing them to monitor and communicate with the visitor remotely.

## Problem Analysis and Designing a Solution

- The main problem that a contactless IOT doorbell aims to solve is the risk of transmission of Covid-19 and other infectious diseases through physical contact with the doorbell or the house owner.
- The secondary problem that a contactless IOT doorbell aims to solve is the lack of security and convenience for the house owner when dealing with visitors.
- The main objectives of a contactless IOT doorbell are:
  - To detect the presence of a visitor using a motion sensor or a proximity sensor.
  - To measure the temperature of the visitor using a non-contact infrared temperature sensor.
  - To alert the house owner about the arrival of the visitor using a speaker, a buzzer, or a mobile app.
  - To display the temperature of the visitor on a LCD screen or a mobile app.
  - To identify the visitor using a camera and a face recognition algorithm.
  - To interact with the visitor using a microphone and a speaker or a mobile app.
  - To record and stream the video of the visitor using a camera and a cloud service.
  - To sound an alarm or notify the authorities in case of abnormal or suspicious behavior of the visitor.
- The main components of a contactless IOT doorbell are:
  - A microcontroller or a microcomputer such as NodeMCU or Raspberry Pi that acts as the brain of the device and controls the other components.
  - A motion sensor or a proximity sensor that detects the presence of a visitor.
  - A non-contact infrared temperature sensor that measures the temperature of the visitor.
  - A speaker or a buzzer that alerts the house owner about the arrival of the visitor.
  - A LCD screen that displays the temperature of the visitor.
  - A camera that captures the image of the visitor.
  - A face recognition algorithm that identifies the visitor.
  - A microphone and a speaker that enable voice interaction with the visitor.
  - A cloud service such as Firebase or Blynk that stores and streams the video of the visitor and provides a mobile app for the house owner.
  - A wireless communication module such as Wi-Fi or Bluetooth that connects the device to the internet and the mobile app.
  - A power supply such as a battery or a solar panel that provides electricity to the device.
- The main steps of designing a contactless IOT doorbell are:
  - Define the problem statement and the objectives of the device.
  - Research the existing solutions and technologies related to the device.
  - Select the appropriate components and tools for the device.
  - Design the circuit diagram and the layout of the device.
  - Write the code for the microcontroller or the microcomputer that controls the device.
  - Test and debug the device and the code.
  - Deploy and evaluate the device and the code.



# IOT Smart Parking Using RFID

- IOT (Internet of Things) is the interconnection of devices and objects through the internet, enabling data collection and exchange.
- RFID (Radio Frequency Identification) is a technology that uses radio waves to identify and track objects, such as vehicles, using tags and readers.
- IOT Smart Parking Using RFID is a system that aims to improve the efficiency and convenience of parking management, by using RFID tags and readers to monitor the availability and occupancy of parking spaces, and by providing information and guidance to drivers and administrators through mobile applications and web portals.
- The main components of the system are:
  - RFID tags: These are attached to the vehicles and contain unique identification numbers and other information, such as the owner's name, vehicle type, etc.
  - RFID readers: These are installed at the entry and exit points of the parking area and can read the RFID tags of the vehicles passing by, and communicate with a central server.
  - Central server: This is the core of the system that stores and processes the data from the RFID readers, and provides the parking status and other services to the users and administrators.
  - Mobile application: This is a smartphone app that allows the drivers to check the availability of parking spaces, reserve a spot, pay the parking fee, and get directions to the parking area and the assigned spot.
  - Web portal: This is a website that allows the administrators to monitor and manage the parking system, such as setting the parking rates, generating reports, etc.
- The main benefits of the system are:
  - Reduced parking search time and traffic congestion, as the drivers can easily find and access the available parking spaces.
  - Increased parking revenue and security, as the system can prevent unauthorized parking, enforce parking rules, and collect parking fees automatically.
  - Enhanced user satisfaction and convenience, as the system can provide a seamless and hassle-free parking experience for the drivers.
  - Improved environmental sustainability, as the system can reduce the fuel consumption and emissions from the vehicles.



# IOT Contactless Covid Testing Booth Automation

## Introduction
- Covid-19 is a highly contagious disease that has caused a global pandemic.
- Covid testing is a key measure to control the spread of the virus and identify infected individuals.
- Covid testing booths are designed to provide a safe and isolated environment for collecting samples from suspected cases.
- However, the conventional testing process involves manual registration of personal details, physical contact with health workers, and potential exposure to the virus.
- Therefore, there is a need for an advanced system that can automate and contactless the covid testing process using IOT technology.

## Problem Analysis
- The main problem of the conventional covid testing process is the risk of cross-infection and human error.
- The manual registration of personal details is time-consuming, prone to mistakes, and requires paper and pen that can be contaminated.
- The physical contact with health workers and other patients can increase the chance of transmission of the virus.
- The lack of real-time monitoring and feedback can delay the diagnosis and treatment of positive cases.
- The main objectives of the proposed system are to:
  - Reduce the human intervention and contact in the covid testing process.
  - Improve the efficiency and accuracy of data collection and management.
  - Enhance the safety and convenience of the patients and health workers.
  - Provide instant and remote notification of test results and health status.

## Designing a Solution
- The proposed system is an IOT-based contactless covid testing booth automation that consists of the following components:
  - An RFID reader and tag that are used to identify and register the patient's details automatically.
  - A microcontroller that acts as the brain of the system and controls the other components.
  - A temperature sensor and a pulse oximeter that are used to measure the patient's vital signs and detect any symptoms of covid-19.
  - A swab robot that is used to collect the nasal or oral sample from the patient without any human contact.
  - A GSM modem that is used to send the test result and health status to the patient's mobile phone via SMS.
  - A MATLAB software that is used to analyze the data and generate a graphical user interface for the health workers.
- The working of the system is as follows:
  - The patient enters the testing booth and scans the RFID tag that contains his/her personal details.
  - The microcontroller reads the RFID tag and displays the patient's name and contact number on the LCD screen.
  - The microcontroller also activates the temperature sensor and the pulse oximeter that measure the patient's body temperature and blood oxygen level respectively.
  - The microcontroller compares the readings with the normal range and displays the result on the LCD screen.
  - If the readings are abnormal, the microcontroller triggers an alarm and alerts the health workers.
  - The microcontroller also activates the swab robot that moves towards the patient and collects the sample from the nose or mouth.
  - The sample is then sent to the laboratory for further testing.
  - The microcontroller also sends the test result and health status to the patient's mobile phone via SMS using the GSM modem.
  - The microcontroller also stores the data in the MATLAB software that analyzes the data and generates a graphical user interface for the health workers.
  - The health workers can monitor the testing process and access the patient's information remotely using the MATLAB software.



# IOT Social Distancing & Monitoring Robot For Queue

- The aim of this project is to design a robot that can monitor and enforce social distancing in queues, such as in banks, malls, schools, etc.   
- The robot uses a 4-wheel drive system and a line-following principle to move along with the queue and detect any violations of social distancing norms. 
- The robot is equipped with an ultrasonic sensor to measure the distance between individuals in the queue and a buzzer to alert them if they are too close.  
- The robot also has a camera and a Wi-Fi module to stream the video of the queue to a web server, where it can be accessed by the authorities or the public.  
- The robot can be controlled remotely using a mobile app or a web interface, where the user can adjust the parameters such as the minimum distance, the buzzer sound, the speed, etc.  
- The robot is powered by a rechargeable battery and can run for up to 8 hours on a single charge. 
- The robot is based on Arduino Uno and ESP8266 microcontrollers and uses Firebase as the cloud platform.  
- The robot is a low-cost and effective solution to prevent the spread of Covid-19 by ensuring social distancing in public places.



# IOT Covid Patient Health Monitor in Quarantine

- IoT stands for Internet of Things, which is a network of physical devices, sensors, and actuators that can communicate and exchange data over the internet.
- Covid-19 is a highly contagious respiratory disease caused by a novel coronavirus that emerged in late 2019 and has spread worldwide, causing a global pandemic.
- Covid-19 patients who have mild or moderate symptoms are advised to isolate themselves at home or in designated quarantine facilities to prevent further transmission of the virus and to reduce the burden on the health care system.
- However, these patients still need to monitor their vital signs, such as body temperature, pulse rate, blood oxygen saturation, and blood pressure, which are indicators of their health condition and potential complications.
- IoT-based health monitoring systems can provide a solution for remote and real-time monitoring of Covid-19 patients in quarantine, by using wearable or non-invasive sensors that can measure the vital signs and transmit the data to a cloud server or a mobile application, where the medical staff, doctors, or family members can access and analyze the data and provide timely feedback or intervention if needed.
- IoT-based health monitoring systems can also alert the patients or the caregivers if the vital signs exceed the normal or safe ranges, or if there are any abnormal patterns or trends in the data, which may indicate a worsening of the condition or a need for hospitalization.
- IoT-based health monitoring systems can benefit both the patients and the health care providers, by reducing the risk of exposure and infection, improving the quality and efficiency of care, enhancing the patient's comfort and compliance, and saving the cost and resources of the health care system.
- Some examples of IoT-based health monitoring systems for Covid-19 patients in quarantine are:

  - IoT Based Covid Patient Health Monitor in Quarantine by Nevon Projects, which uses a heartbeat sensor, a temperature sensor, and a blood pressure sensor to measure the vital signs and send the data to an online server, where the medical staff can monitor multiple patients remotely and receive alerts if the values are abnormal.
  - IoT Based COVID Patient Health Monitoring System in Quarantine by R.Yoganapriya et al., which uses a pulse oximeter, a temperature sensor, and a blood pressure sensor to measure the vital signs and send the data to a mobile application, where the doctor can monitor the patient and provide feedback or prescription through a chatbot.
  - IoT-Based Smart Health Monitoring System for COVID-19 by M. Alsharif et al., which uses a smart wristband, a smart thermometer, and a smart blood pressure monitor to measure the vital signs and send the data to a cloud server, where the medical staff can monitor the patient and provide guidance or intervention through a web application.



# IOT based Manhole Detection and Monitoring System

- A drainage monitoring system plays a significant role in keeping towns and cities healthy and clean. Most of the manholes are open without any observations that cause accidents. In India, many cities adopted emptying underground system because it is vital.
- IOT based manhole detection and monitoring system is a project that aims to prevent such accidents and improve the management and maintenance of the manholes. It uses sensors to detect and send alerts to authorities via GSM and GPS module when any manhole crosses its threshold values .
- The system consists of the following components:
  - Arduino Uno: It is the microcontroller that controls the sensors and the communication modules.
  - Ultrasonic sensor: It is used to measure the water level in the manhole and detect any blockage or overflow.
  - Gas sensor: It is used to detect any toxic gases in the manhole and alert the workers or the public.
  - Temperature sensor: It is used to measure the temperature in the manhole and prevent any fire hazards.
  - GSM module: It is used to send SMS alerts to the authorities or the workers with the location and the status of the manhole.
  - GPS module: It is used to get the coordinates of the manhole and send them along with the SMS alerts.
  - LCD display: It is used to show the readings of the sensors and the status of the manhole.
  - Buzzer: It is used to produce an audible alarm when any threshold value is crossed.
- The system works as follows:
  - The sensors are installed in the manhole and connected to the Arduino Uno.
  - The Arduino Uno reads the data from the sensors and compares them with the predefined threshold values.
  - If any threshold value is crossed, the Arduino Uno activates the buzzer and the GSM module.
  - The GSM module sends an SMS alert to the predefined number with the location and the status of the manhole.
  - The GPS module provides the location of the manhole by sending the coordinates to the GSM module.
  - The LCD display shows the readings of the sensors and the status of the manhole.
- The advantages of the system are:
  - It reduces the death risk of manual scavengers who clean the underground drainage and also benefits the public.
  - It prevents urban floods caused by poor management and monitoring of the manholes.
  - It saves time and resources by providing real-time information and alerts to the authorities.
  - It is low cost, low maintenance, and easy to install .



# IOT based Smart Energy Meter Monitoring with Theft Detection

- IOT based Smart Energy Meter Monitoring with Theft Detection is a system that aims to reduce the energy crisis and prevent the power theft by using smart meters and Internet of Things (IoT) technology.
- The system consists of smart energy meters that are installed at the consumer end and the distribution end, and a master unit that is located at the distribution pole site. The smart energy meters can measure the energy consumption, voltage, current, power factor, and other parameters of the sections. The smart energy meters can also communicate with the master unit and the cloud server via wireless or wired network.
- The master unit can collect the data from the smart energy meters and compare them with the predefined threshold values. If there is any discrepancy or abnormality in the data, such as power loss, power theft, or tampering, the master unit can send an alert to the cloud server and the authorized personnel. The master unit can also control the power supply of the sections by switching on or off the relays.
- The cloud server can store and process the data from the master unit and the smart energy meters. The cloud server can also provide a web interface or a mobile application for the users and the authorities to monitor and manage the energy consumption and the power theft detection. The cloud server can also generate reports and statistics for the analysis and optimization of the energy distribution system.
- The system can provide the following benefits:
  - It can reduce the energy wastage and the energy cost by providing real-time feedback and control of the energy consumption.
  - It can detect and prevent the power theft and the tampering by using smart meters and IoT technology.
  - It can improve the reliability and the efficiency of the energy distribution system by using data analysis and optimization techniques.
  - It can enhance the customer satisfaction and the transparency by providing user-friendly interface and services.



# IOT Weather Station Airship

- An IOT weather station airship is a device that can measure and transmit atmospheric data using wireless communication and internet of things (IOT) technologies.
- It consists of a balloon or a drone that carries sensors, a microcontroller, a battery, a solar panel, and a wireless module.
- The sensors can measure parameters such as temperature, humidity, pressure, wind speed, wind direction, and UV radiation.
- The microcontroller can process the sensor data and send it to a cloud platform or a web portal using the wireless module, which can be based on LoRaWAN, WiFi, GSM, or other protocols.
- The battery can provide power to the device and the solar panel can recharge it.
- The device can be controlled remotely by the user to adjust the height, location, and frequency of data transmission.
- The device can provide real-time and accurate weather information for various applications, such as agriculture, meteorology, environmental monitoring, disaster management, and research.



# IOT based Three Phase Power Failure Monitoring with SMS Alerts

- IOT based Three Phase Power Failure Monitoring with SMS Alerts is a system that monitors the status of three-phase power supply and alerts the authorized person via SMS in case of any failure    .
- The system consists of the following components:
  - Three-phase power supply: This is the source of power for the system and the load. It has three phases: R, Y, and B.
  - Voltage sensors: These are devices that measure the voltage of each phase and send the data to the microcontroller.
  - Microcontroller: This is the brain of the system that processes the data from the voltage sensors and compares it with a threshold value. If any phase voltage falls below the threshold, it triggers the GSM module to send an SMS alert.
  - GSM module: This is a device that connects the system to the cellular network and enables the communication via SMS. It has a SIM card and an antenna.
  - LCD display: This is a device that displays the voltage values of each phase and the status of the system.
  - Buzzer: This is a device that produces a sound when there is a power failure.
  - Load: This is the device or equipment that consumes the power from the three-phase supply.
- The system works as follows:
  - The system is powered by the three-phase supply and the load is connected to it.
  - The voltage sensors measure the voltage of each phase and send the data to the microcontroller.
  - The microcontroller displays the voltage values on the LCD display and checks if any phase voltage is below the threshold value.
  - If all the phase voltages are above the threshold, the system is normal and no action is taken.
  - If any phase voltage is below the threshold, the system detects a power failure and activates the buzzer and the GSM module.
  - The GSM module sends an SMS alert to the authorized person with the details of the failed phase and the location of the system.
  - The authorized person can take the necessary action to restore the power supply or to protect the load from damage.
- The system has the following advantages:
  - It can monitor the three-phase power supply remotely and in real-time.
  - It can alert the authorized person quickly and accurately in case of any power failure.
  - It can prevent the damage or malfunction of the load due to single phasing or phase imbalance.
  - It can reduce the downtime and maintenance cost of the system and the load.
  - It can improve the safety and reliability of the system and the load.
- The system has the following limitations:
  - It depends on the availability and quality of the cellular network for the communication via SMS.
  - It may not be able to detect the power failure if the voltage sensors or the microcontroller are damaged or faulty.
  - It may not be able to send the SMS alert if the GSM module or the SIM card are damaged or faulty.
  - It may not be able to prevent the power failure if the three-phase supply is interrupted or disconnected.



# IOT based Intelligent Gas Leakage Detector Using Arduino

- This is a project that uses an Arduino board, an MQ5 gas sensor, an ESP8266 Wi-Fi module, and a buzzer to detect and alert the presence of LPG gas leakage in the air  .
- The MQ5 gas sensor is a metal oxide semiconductor sensor that can sense various gases such as methane, butane, LPG, smoke, alcohol, etc. It has a high sensitivity and fast response time. It outputs an analog voltage that varies according to the concentration of the gas .
- The Arduino board is a microcontroller that can read the analog voltage from the MQ5 sensor, process it, and send the data to the ESP8266 module via serial communication  .
- The ESP8266 module is a low-cost Wi-Fi chip that can connect to the internet and send or receive data from a cloud server or a web page . It can also act as a web server and host a web page that displays the gas level and status.
- The buzzer is a device that can produce a loud sound when the Arduino board sends a signal to it. It is used to alert the user when the gas level exceeds a certain threshold .
- The project works as follows:
  - The MQ5 sensor continuously monitors the level of LPG gas in the air and outputs a voltage that is proportional to it  .
  - The Arduino board reads the voltage from the MQ5 sensor and converts it to a gas concentration value using a formula  .
  - The Arduino board sends the gas concentration value and the status (normal or alert) to the ESP8266 module via serial communication  .
  - The ESP8266 module connects to the internet and sends the data to a cloud server or a web page, where it can be viewed by the user from anywhere .
  - The ESP8266 module also hosts a web page that displays the gas level and status on a gauge and a LED.
  - The Arduino board also activates the buzzer when the gas level exceeds a predefined threshold, indicating a gas leakage .
  - The user can also set the minimum and maximum parameters for the gas level according to their preference.
- The advantages of this project are:
  - It can detect and alert the user about gas leakage in real time and remotely  .
  - It can prevent fire accidents and health hazards caused by gas leakage  .
  - It can save energy and money by avoiding wastage of gas  .
  - It can be installed in homes, hotels, LPG gas storage areas, and other places where gas is used  .
  - It is low-cost, easy to build, and uses widely available components  .
- The challenges of this project are:
  - It requires a stable internet connection and power supply for the ESP8266 module to work properly .
  - It may not be able to detect other types of gases that are not compatible with the MQ5 sensor .
  - It may have some errors or inaccuracies in the gas level measurement due to environmental factors or sensor calibration .
  - It may need regular maintenance and testing to ensure its functionality and reliability .

