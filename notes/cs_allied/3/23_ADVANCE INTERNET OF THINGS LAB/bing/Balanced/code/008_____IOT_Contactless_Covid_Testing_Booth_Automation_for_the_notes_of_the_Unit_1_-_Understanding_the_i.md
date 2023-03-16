# IOT Contactless Covid Testing Booth Automation

## Unit 1 - Understanding the implementation of IOT in the subject of ADVANCE INTERNET OF THINGS LAB

- IOT stands for Internet of Things, which is a network of physical devices, sensors, actuators, and software that can communicate and exchange data over the internet.
- IOT can be used to create smart applications and systems that can improve efficiency, safety, convenience, and quality of life.
- One of the applications of IOT is contactless covid testing booth automation, which is a system that can perform covid testing without human contact and manual registration.
- The main aim of this system is to reduce the risk of infection and transmission of the virus in the covid testing centers, and to speed up the testing process and results delivery.
- The system consists of the following components:
  - A microcontroller, such as Arduino, that acts as the brain of the system and controls the other components.
  - A RFID reader and tags, that are used to identify and register the person who wants to undergo the testing. The RFID tag contains the person's details, such as name, contact number, and address, and can be scanned by the RFID reader without physical contact.
  - A thermal camera and a pulse oximeter, that are used to measure the body temperature and the oxygen saturation level of the person, which are two of the indicators of covid infection.
  - A swab robot, that is used to collect the nasal or oral sample from the person, without human intervention. The robot is equipped with a camera and a servo motor, that can adjust the angle and depth of the swab according to the person's face.
  - A GSM modem, that is used to send the test results to the person's mobile phone via SMS, and to upload the data to a cloud server for further analysis and monitoring.
  - A MATLAB software, that is used to process the images from the thermal camera and the swab robot, and to apply machine learning algorithms to detect the presence of covid infection.
- The system works as follows:
  - The person who wants to undergo the testing enters the booth and scans their RFID tag on the RFID reader.
  - The microcontroller reads the person's details from the RFID tag and displays them on a LCD screen.
  - The microcontroller activates the thermal camera and the pulse oximeter, and measures the person's body temperature and oxygen saturation level.
  - The microcontroller compares the measurements with the predefined thresholds, and determines if the person has any symptoms of covid infection.
  - The microcontroller activates the swab robot, and instructs the person to position their face in front of the camera.
  - The swab robot captures the image of the person's face, and uses MATLAB to calculate the coordinates of the nostril or the mouth.
  - The swab robot moves the swab to the calculated coordinates, and inserts it into the nostril or the mouth, and collects the sample.
  - The swab robot retracts the swab, and places it into a test tube, and seals it with a cap.
  - The test tube is labeled with the person's details, and is sent to a laboratory for further testing.
  - The microcontroller sends the test results to the person's mobile phone via SMS, and uploads the data to the cloud server for further analysis and monitoring.