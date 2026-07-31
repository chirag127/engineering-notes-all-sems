### IOT Prison Break Monitoring & Alerting System

- This system is designed to track the location and activities of the inmates in a prison and alert the authorities in case of any prison break attempt using IoT technology.
- The system consists of the following components:
  - **RF trackers**: These are small devices attached to each inmate that transmit a unique code wirelessly to the central monitoring unit. The RF trackers use radio frequency (RF) technology to communicate with the receiver.
  - **Central monitoring unit**: This is a microcontroller based circuit that scans through all the RF trackers and detects their presence in the premises. The central monitoring unit also connects to the internet and sends the data to the officer's portal.
  - **Officer's portal**: This is an online platform that receives the data from the central monitoring unit and displays the status and location of each inmate. The officer's portal also alerts the authorities with an alarm and a message if any inmate is out of the validated location or tries to escape the facility. The officer's portal is developed using IoTGecko, a web service for IoT applications.
- The system works as follows:
  - The RF trackers are installed on each inmate and assigned a unique code that corresponds to their identity and location.
  - The central monitoring unit continuously scans through all the RF trackers and receives their codes. The central monitoring unit also validates the location of each inmate based on the predefined boundaries of the facility.
  - The central monitoring unit sends the data to the officer's portal via the internet. The officer's portal displays the status and location of each inmate on a map or a table.
  - If any inmate is out of the validated location or tries to escape the facility, the central monitoring unit detects the anomaly and sends an alert signal to the officer's portal. The officer's portal then triggers an alarm and a message to notify the authorities and prevent the prison break.
- The system has the following advantages:
  - It enhances the security and safety of the prison by monitoring the inmates and preventing prison breaks.
  - It reduces the manpower and cost required for manual surveillance and tracking of the inmates.
  - It provides real-time and accurate data on the status and location of the inmates to the authorities.
  - It uses IoT technology to enable remote and online access to the data and alerts.