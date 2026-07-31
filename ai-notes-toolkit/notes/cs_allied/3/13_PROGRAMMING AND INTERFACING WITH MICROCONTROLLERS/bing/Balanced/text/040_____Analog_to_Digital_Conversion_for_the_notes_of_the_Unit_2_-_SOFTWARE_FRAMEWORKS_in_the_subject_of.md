### Analog to Digital Conversion

- Analog to digital conversion (ADC) is an electronic process that converts a continuous analog signal, such as a sound wave or a voltage level, into a discrete digital signal, such as a binary code, without altering its essential content.
- ADC is a common feature of many devices that interface with the real world, such as digital cameras, microphones, radars, thermometers, and pressure sensors  .
- ADC allows digital circuits, such as microcontrollers, to process, manipulate, compute, transmit, or store analog signals in a digital form.
- ADC consists of three main components: a sampler, a quantizer, and an encoder.
  - The sampler takes samples of the analog signal at regular intervals, called the sampling rate, and holds them for a short time.
  - The quantizer assigns a discrete value, called a quantization level, to each sample, based on its amplitude. The quantization levels are usually evenly spaced and represent the resolution of the ADC.
  - The encoder converts each quantization level into a binary code, called a digital word, and outputs it to the digital circuit.
- ADC has some limitations and sources of error, such as aliasing, quantization noise, non-linearity, and offset  .
  - Aliasing occurs when the sampling rate is too low to capture the variations of the analog signal, resulting in a distorted digital signal.
  - Quantization noise is the difference between the actual analog signal and the quantized digital signal, resulting from the finite resolution of the ADC.
  - Non-linearity is the deviation of the ADC output from the ideal linear relationship between the analog input and the digital output, resulting from the imperfections of the ADC components.
  - Offset is the constant error that is added to or subtracted from the ADC output, resulting from the mismatch of the ADC components or the external interference.