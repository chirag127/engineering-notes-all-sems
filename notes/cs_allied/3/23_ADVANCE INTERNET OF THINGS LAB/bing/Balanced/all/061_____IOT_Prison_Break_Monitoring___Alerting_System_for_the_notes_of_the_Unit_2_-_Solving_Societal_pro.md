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