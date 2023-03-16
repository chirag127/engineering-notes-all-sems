### IOT Prison Break Monitoring & Alerting System

- The system is designed to prevent and detect prison breaks by tracking the location and activities of the inmates using radio frequency (RF) technology and Internet of Things (IoT).
- The system consists of the following components:
  - RF trackers: These are small devices attached to each inmate that transmit a unique code wirelessly to the central monitoring units. The RF trackers can also detect the movement and orientation of the inmates.
  - Central monitoring units: These are microcontroller-based circuits that scan and receive the signals from the RF trackers and compare them with the predefined data of the inmates. The central monitoring units can also control the alert signals and communicate with the online portal.
  - Online portal: This is a web-based application that displays the status and location of each inmate on a map and alerts the authorities in case of any prison break. The online portal is developed using IoTGecko, a cloud platform for IoT applications.
- The system works as follows:
  - The RF trackers continuously send their codes and location data to the central monitoring units, which store them in a database.
  - The central monitoring units compare the received data with the predefined data of the inmates, such as their names, cell numbers, and valid locations.
  - If the central monitoring units detect any mismatch or anomaly in the data, such as an inmate being out of his/her valid location, they trigger an alert signal and send the details of the inmate to the online portal.
  - The online portal receives the alert signal and displays the inmate's name, code, and location on a map. It also sounds an alarm and notifies the authorities via email or SMS.
  - The authorities can then take immediate action to catch the inmate and prevent the prison break.
- The system has the following advantages:
  - It enhances the security and safety of the prison by preventing and detecting prison breaks in real time.
  - It reduces the manpower and cost required for monitoring the inmates manually.
  - It provides a reliable and accurate tracking system that works even in low-light or noisy conditions.
  - It allows the authorities to access the status and location of the inmates remotely and conveniently through the online portal.