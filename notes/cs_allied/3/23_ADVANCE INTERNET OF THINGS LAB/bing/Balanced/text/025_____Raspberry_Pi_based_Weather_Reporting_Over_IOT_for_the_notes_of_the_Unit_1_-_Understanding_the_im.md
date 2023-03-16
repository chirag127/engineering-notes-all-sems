### Raspberry Pi based Weather Reporting Over IOT

- This system can be used to monitor and update weather conditions over the internet using a Raspberry Pi device and various sensors.
- The system monitors three parameters namely temperature, humidity and rainfall. These values are then displayed on LCD and also updated over the IoT gecko platform.
- The IoT gecko platform is a web service that allows users to create dashboards and widgets to visualize and control data from various sources.
- The system uses the following components:
  - Raspberry Pi: A low-cost, single-board computer that can run Linux and Python. It acts as the base station and the controller of the system .
  - DHT11 sensor: A digital sensor that measures temperature and humidity. It is connected to the GPIO pins of the Raspberry Pi .
  - Rain sensor: A sensor that detects the presence and intensity of rainfall. It consists of a rain board and a control board. The rain board has parallel wires that are exposed to raindrops. The control board has a potentiometer to adjust the sensitivity and an LED to indicate the output. The sensor is connected to the analog input of the Raspberry Pi using an ADC module .
  - LCD display: A 16x2 character LCD display that shows the weather data. It is connected to the Raspberry Pi using an I2C module .
- The system works as follows:
  - The Raspberry Pi reads the data from the sensors using Python scripts .
  - The Raspberry Pi sends the data to the IoT gecko platform using an API key and a device ID.
  - The IoT gecko platform updates the data on the dashboard and the widgets.
  - The Raspberry Pi also displays the data on the LCD screen .
- The system has the following advantages:
  - It provides accurate and precise weather data of a specific area as opposed to the generic type regional weather forecasts.
  - It is cost-effective and has low power consumption in order to save money and energy .
  - It is easy to carry around and work with as it uses wireless communication and IoT technology .
  - It can be used for various applications such as agriculture, smart cities, disaster management, etc .