# DAC

DAC stands for Digital-to-Analog Converter. It is an integrated analog peripheral that provides a variable voltage reference that is ratio metric with an input source. DACs are used to generate custom analog signals from digital data, such as precision voltages, waveforms, voice synthesis, etc.

## DACs in Microcontrollers

Some microcontrollers have DACs on-chip for frequency or voltage generation. For many applications, this provides additional functionality while saving board space. However, applications might require specialized DAC functionality not found in microcontrollers. In such cases, external DACs can be used to extend the microcontroller functionality.

## DACs Parameters

DACs are defined by their bit resolution, which indicates how many selectable voltage levels are possible between the positive and negative voltage sources. For example, a 10-bit DAC can produce 1024 discrete voltage levels. The resolution determines the accuracy and granularity of the analog output.

Another parameter of DACs is the sampling rate, which indicates how fast the DAC can update its output voltage. The sampling rate is measured in samples per second (SPS) or mega samples per second (MSPS). The sampling rate determines the bandwidth and frequency response of the analog output.

## DACs Types

There are different types of DACs based on their architecture, performance, and application. Some of the common types are:

- R-2R ladder DAC: This is a simple and low-cost DAC that uses a network of resistors to divide the input voltage into discrete levels. The output voltage is determined by the combination of bits that are switched on or off by the digital input.
- Sigma-delta DAC: This is a high-resolution and low-noise DAC that uses a feedback loop to modulate the input signal into a high-frequency pulse train. The output voltage is obtained by filtering the pulse train with a low-pass filter.
- Current-steering DAC: This is a high-speed and high-power DAC that uses a network of current sources to generate the output voltage. The output voltage is determined by the combination of current sources that are switched on or off by the digital input.

## DACs Applications

DACs are used in various applications that require analog signals from digital data, such as:

- Audio and video: DACs are used to convert digital audio and video signals into analog signals that can be played by speakers, headphones, monitors, etc.
- Communication: DACs are used to modulate digital data into analog signals that can be transmitted by radio, optical, or wired channels.
- Instrumentation: DACs are used to generate analog signals that can be used for testing, calibration, or control of other devices or systems.
- Industrial: DACs are used to control analog devices or processes, such as motors, valves, heaters, etc.