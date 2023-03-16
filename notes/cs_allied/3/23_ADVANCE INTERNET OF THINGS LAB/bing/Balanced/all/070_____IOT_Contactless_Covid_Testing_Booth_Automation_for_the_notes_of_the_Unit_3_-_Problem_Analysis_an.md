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