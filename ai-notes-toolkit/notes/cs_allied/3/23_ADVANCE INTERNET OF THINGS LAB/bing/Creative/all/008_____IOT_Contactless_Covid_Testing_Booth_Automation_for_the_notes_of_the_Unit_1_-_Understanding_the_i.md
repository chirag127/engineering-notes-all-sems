# IOT Contactless Covid Testing Booth Automation

## Unit 1 - Understanding the implementation of IOT in the subject of ADVANCE INTERNET OF THINGS LAB

- IOT stands for Internet of Things, which is a network of physical devices, sensors, actuators, and software that can communicate and exchange data over the internet.
- IOT can be used to create smart and connected solutions for various domains, such as healthcare, agriculture, transportation, manufacturing, etc.
- IOT Contactless Covid Testing Booth Automation is an example of an IOT application that aims to reduce the risk of infection and human error in the covid testing process.
- The main components of this system are:
  - A microcontroller, such as Arduino, that acts as the brain of the system and controls the logic and communication.
  - An RFID reader and tags, that are used to identify and register the person who wants to get tested.
  - A GSM modem, that is used to send the test results and other information to the person's mobile phone via SMS.
  - A MATLAB software, that is used to process the image of the person's face and detect the presence of mask and fever.
  - A servo motor and a syringe, that are used to collect the nasal swab sample from the person automatically.
  - A thermal printer, that is used to print the test report and a QR code for verification.
- The main steps of the system are:
  - The person scans their RFID tag at the entrance of the booth and enters their mobile number on a keypad.
  - The system verifies the person's identity and checks if they have already been tested or not.
  - The person enters the booth and faces the camera, which captures their image and sends it to MATLAB for analysis.
  - MATLAB detects if the person is wearing a mask and if they have fever, and sends the results back to the microcontroller.
  - If the person is wearing a mask and has no fever, the system proceeds to the next step. Otherwise, the system alerts the person and asks them to leave the booth.
  - The system instructs the person to tilt their head back and open their mouth, and then activates the servo motor and the syringe to collect the nasal swab sample from the person.
  - The system sends the sample to a nearby lab for testing and waits for the results.
  - The system receives the results from the lab and prints the test report and a QR code on a thermal paper, and also sends the results and the QR code to the person's mobile phone via SMS.
  - The person exits the booth and scans the QR code at the exit to verify their identity and test status.
- The advantages of this system are:
  - It reduces the contact between the person and the medical staff, and thus lowers the risk of infection and cross-contamination.
  - It automates the covid testing process and eliminates the need for manual registration, data entry, and sample collection, and thus reduces the human error and the waiting time.
  - It provides a fast and accurate test result and a digital record of the person's identity and test status, and thus improves the efficiency and the reliability of the covid testing system.