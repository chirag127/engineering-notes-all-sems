 Here is the formal content in Markdown format without any emojis or external links for the given topic:

### IOT based Three Phase Power Failure Monitoring with SMS Alerts

1. Problem Statement: To monitor three phase power supply and send SMS alerts in case of power failure in any phase.
2. Components Required:
    - NodeMCU ESP8266
    - Three single phase energy meters to measure voltage and current of each phase
    - SIM800L GSM GPRS Module
    - Jumper wires
    - Power supply
3. Working Explanation:
    - The voltage and current of each phase is measured by the respective energy meters.
    - The analog outputs of energy meters are connected to the analog inputs of NodeMCU.
    - The NodeMCU is programmed to continuously monitor the voltage and current values.
    - In case the voltage or current of any phase goes below a threshold value, it indicates a power failure. The NodeMCU sends an SMS alert through the connected SIM800L GSM GPRS module.
    - The SMS alert will contain the information about which phase has failed.
4. Applications:
    - The system can be used in industries and offices to monitor three phase power supply and send alerts in case of failure for taking backup actions.
    - It can help in reducing the losses due to power failures by taking immediate actions after failure detection.