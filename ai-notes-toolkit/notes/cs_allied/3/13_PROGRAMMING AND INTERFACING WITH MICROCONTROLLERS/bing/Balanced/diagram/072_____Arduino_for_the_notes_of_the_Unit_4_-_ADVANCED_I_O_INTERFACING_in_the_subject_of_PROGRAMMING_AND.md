### Arduino for the notes of the Unit 4 - ADVANCED I/O INTERFACING

- Arduino is an open-source platform that consists of a microcontroller board and a software IDE that can be used to program the board.
- Arduino can interface with various external devices and sensors using its digital and analog input/output (I/O) pins.
- Advanced I/O functions in Arduino allow more control and flexibility over the I/O operations, such as generating tones, shifting bits, and manipulating interrupts.
- Some of the advanced I/O functions in Arduino are:

  - `tone()` and `noTone()`: These functions can be used to generate a square wave of a specified frequency and duration on a digital pin. This can be useful for creating sounds or driving a buzzer.
  - `shiftOut()` and `shiftIn()`: These functions can be used to shift out or shift in a byte of data one bit at a time on a pair of data and clock pins. This can be useful for interfacing with shift registers or other serial devices.
  - `attachInterrupt()` and `detachInterrupt()`: These functions can be used to attach or detach an interrupt service routine (ISR) to an external interrupt pin. This can be useful for responding to events or signals that require immediate attention.

- To use the advanced I/O functions, some considerations are:

  - The Arduino board must be configured to draw power from either the USB connection or an external power supply, depending on the model.
  - The Arduino board must have a common ground with the external devices or sensors that are connected to its I/O pins.
  - The Arduino board must use the appropriate voltage level and current rating for the external devices or sensors that are connected to its I/O pins.
  - The Arduino board must set the analog reference to EXTERNAL before calling the `analogRead()` function if using an external reference on the AREF pin.
  - The Arduino board must avoid using the same pins for multiple functions, such as serial communication, PWM, and interrupts.