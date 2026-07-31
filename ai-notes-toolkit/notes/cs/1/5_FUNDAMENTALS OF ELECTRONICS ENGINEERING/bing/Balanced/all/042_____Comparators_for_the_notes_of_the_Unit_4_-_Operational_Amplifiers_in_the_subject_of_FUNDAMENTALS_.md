# Comparators for the notes of the Unit 4 - Operational Amplifiers in the subject of FUNDAMENTALS OF ELECTRONICS ENGINEERING

- A comparator is a circuit that uses an operational amplifier to compare two voltages and output a high or low signal depending on which voltage is larger .
- A comparator can be used for various applications, such as polarity identification, analog to digital conversion, switch driving, wave generation, and pulse detection .
- A comparator can be configured by using an operational amplifier in its open-loop state, that is, without any feedback resistor.
- A comparator has two inputs, a non-inverting input (+) and an inverting input (-), and one output. The output voltage is determined by the following rules:
  - If V+ > V-, then the output voltage is equal to the positive supply voltage (Vcc).
  - If V+ < V-, then the output voltage is equal to the negative supply voltage (Vee).
  - If V+ = V-, then the output voltage is undefined and may oscillate between Vcc and Vee.
- A comparator can be classified into different types based on the number and values of the reference voltages used to compare the input voltage:
  - A zero-crossing detector is a comparator that uses zero volts as the reference voltage. It can be used to detect the polarity of the input voltage or to convert a sinusoidal wave into a square wave.
  - A level detector is a comparator that uses a fixed reference voltage other than zero volts. It can be used to check whether the input voltage has reached a certain threshold or to generate a pulse when the input voltage crosses the reference voltage.
  - A window detector is a comparator that uses two reference voltages, an upper reference voltage and a lower reference voltage. It can be used to check whether the input voltage is within a certain range or window of values. A window detector requires two comparators connected in parallel, one for the upper reference voltage and one for the lower reference voltage. The output of the window detector is high only when the input voltage is between the two reference voltages.