# Arduino for the notes of the Unit 4 - ADVANCED I/O INTERFACING

- Arduino is an open-source platform that consists of a microcontroller board and a software IDE that can be used to write and upload code to the board.
- Arduino can interface with various external devices and sensors using its digital and analog input/output (I/O) pins.
- Some of the advanced I/O functions that Arduino provides are:
  - `tone()` and `noTone()` : These functions can be used to generate a square wave of a specified frequency and duration on a digital pin. This can be useful for interfacing with buzzers, speakers, or other sound devices.
  - `shiftOut()` and `shiftIn()` : These functions can be used to shift out or shift in a byte of data one bit at a time on a pair of digital pins. This can be useful for interfacing with shift registers, serial-to-parallel converters, or other devices that use serial communication.
  - `pulseIn()` : This function can be used to measure the duration of a pulse (high or low) on a digital pin. This can be useful for interfacing with ultrasonic sensors, infrared receivers, or other devices that use pulse-width modulation (PWM).
  - `analogReference()` : This function can be used to set the reference voltage for the analog inputs. By default, the reference voltage is the same as the operating voltage of the board (5V or 3.3V), but it can be changed to an external source or an internal source (1.1V or 2.56V) depending on the board.
  - `analogReadResolution()` and `analogWriteResolution()` : These functions can be used to change the resolution of the analog inputs and outputs. By default, the resolution is 10 bits (0 to 1023), but it can be changed to a higher or lower value depending on the board.
- To use the advanced I/O functions, some of the things to consider are :
  - The maximum current that the digital pins can source or sink is 40 mA, so external devices may need additional components such as resistors, transistors, or relays to protect the board and the devices.
  - The maximum frequency that the digital pins can generate or read is 8 MHz, so external devices may need additional components such as capacitors, filters, or amplifiers to improve the signal quality and accuracy.
  - The analog inputs can measure voltages from 0 to the reference voltage, so external devices may need additional components such as voltage dividers, potentiometers, or op-amps to scale the input range and avoid damaging the board or the devices.
  - The analog outputs can generate PWM signals from 0 to 100% duty cycle, so external devices may need additional components such as low-pass filters, drivers, or motors to convert the PWM signals to analog voltages or currents.