### ADC

Analog-to-digital converter (ADC) is a circuit that converts a continuous voltage value (analog) to a binary value (digital) that can be understood by a digital device which could then be used for digital computation. ADCs are essential for wearable computing, mixed reality and internet of everything applications, as they enable the processing and communication of analog signals such as sound, light, temperature, pressure, etc.

Some of the main characteristics of ADCs are:

- Resolution: the number of bits used to represent the digital output. Higher resolution means higher accuracy and dynamic range, but also higher power consumption and cost.
- Sampling rate: the frequency at which the analog input is sampled and converted to digital. Higher sampling rate means higher bandwidth and faster response, but also higher power consumption and noise.
- Power consumption: the amount of energy required by the ADC to operate. Lower power consumption means longer battery life and less heat generation, but also lower performance and quality.

Some of the main types of ADCs are:

- Successive approximation ADC: a type of ADC that uses a binary search algorithm to find the digital output that matches the analog input. It consists of a comparator, a digital-to-analog converter (DAC), and a register. It is fast, accurate, and widely used, but it requires a clock signal and a reference voltage.
- Pipelined ADC: a type of ADC that uses a series of stages, each consisting of a sample-and-hold circuit, a sub-ADC, and a sub-DAC, to convert the analog input to digital. It is faster than successive approximation ADC, but it has higher power consumption and latency.
- Delta-sigma ADC: a type of ADC that uses a feedback loop to oversample and filter the analog input, and then decimate the output to obtain the desired resolution. It has high resolution, low noise, and low power consumption, but it has lower bandwidth and higher latency.

Some of the main applications of ADCs in wearable computing, mixed reality and internet of everything are:

- Wearable electrocardiogram (ECG) sensors: a type of wearable device that measures the electrical activity of the heart and transmits it to a smartphone or a cloud server for analysis and diagnosis. ADCs are used to convert the analog ECG signals to digital for processing and communication. A low-power delta-modulation-based ADC is proposed for this application, which achieves a power consumption of 0.8 μW and a signal-to-noise-and-distortion ratio (SNDR) of 38.8 dB.
- Mixed reality headsets: a type of device that combines virtual and augmented reality to create immersive and interactive experiences. ADCs are used to convert the analog signals from the sensors (such as cameras, microphones, accelerometers, etc.) and the user inputs (such as voice, gestures, etc.) to digital for processing and rendering. A high-speed pipelined ADC is suitable for this application, which can achieve a sampling rate of up to 1 GSPS and a resolution of up to 12 bits.
- Internet of things (IoT) devices: a type of device that connects to the internet and other devices to collect and exchange data. ADCs are used to convert the analog signals from the sensors (such as temperature, humidity, light, etc.) and the actuators (such as motors, LEDs, etc.) to digital for processing and communication. A low-power successive approximation ADC is suitable for this application, which can achieve a power consumption of less than 1 mW and a resolution of up to 16 bits.

: https://components101.com/articles/analog-to-digital-adc-converters
: https://ieeexplore.ieee.org/document/9790719/
: https://www.microchip.com/en-us/about/media-center/blog/2021/understanding-the-function-of-analog-to-digital-adc-drivers
: https://www.semanticscholar.org/paper/Asynchronous-Level-Crossing-ADC-Design-for-Wearable-Antony-Paulson/e9f322f7c196a1a7e7caf47f5802583951fceb54