### Practical Op-Amp Circuits

An operational amplifier (op-amp) is a versatile device that can be used to amplify signals, filter signals, perform mathematical operations and more. Op-amps are usually used in conjunction with passive components such as resistors and capacitors to create various circuits with different functions. Here are some of the most common and useful op-amp circuits that you should know:

1. **Voltage Follower**: This is the simplest op-amp circuit, as it does not require any external components. It is also called a buffer, as it isolates the input from the output and provides a high input impedance and a low output impedance. The output voltage is equal to the input voltage, as shown by the equation:

    `Vout = Vin`

    The voltage follower can be used to prevent loading effects, drive low-impedance loads, or interface different stages of a circuit.

    The circuit diagram of a voltage follower is shown below:

    ```
    +Vcc
     |
     |
     |    Vin
     |-----|\
     |     | \
     |     |  \
     |     |   \_______Vout
     |     |   /
     |     |  /
     |     | /
     |-----|/
     |
     |
    -Vcc
    ```

2. **Inverting Op-Amp**: This circuit uses a resistor (R2) to feed back the output to the negative or inverting input of the op-amp. The input signal is applied to the positive or non-inverting input through another resistor (R1). The output voltage is inverted and proportional to the input voltage, as shown by the equation:

    `Vout = -R2/R1 * Vin`

    The inverting op-amp can be used to amplify or attenuate signals, invert signals, or perform mathematical operations such as subtraction or integration.

    The circuit diagram of an inverting op-amp is shown below:

    ```
    +Vcc
     |
     |
     |    Vin
     |-----/\/\/\/\----|\
     |     R1          | \
     |                 |  \
     |                 |   \_______Vout
     |                 |   /
     |                 |  /
     |                 | /
     |                 |/
     |                 |
     |                 /\/\/\/\
     |                 R2
     |                 |
     |                 |
    -Vcc
    ```

3. **Non-inverting Op-Amp**: This circuit uses a resistor (R2) to feed back the output to the positive or non-inverting input of the op-amp. The input signal is applied to the negative or inverting input through another resistor (R1). The output voltage is in phase and proportional to the input voltage, as shown by the equation:

    `Vout = (1 + R2/R1) * Vin`

    The non-inverting op-amp can be used to amplify or attenuate signals, buffer signals, or perform mathematical operations such as addition or differentiation.

    The circuit diagram of a non-inverting op-amp is shown below:

    ```
    +Vcc
     |
     |
     |    Vin
     |-----/\/\/\/\----|\
     |     R1          | \
     |                 |  \
     |                 |   \_______Vout
     |                 |   /
     |                 |  /
     |                 | /
     |                 |/
     |                 |
     |                 |
     |                 /\/\/\/\
     |                 R2
     |                 |
     |                 |
     |-----------------|
     |
    -Vcc
    ```

4. **Non-inverting Summing Amplifier**: This circuit uses a resistor (Rf) to feed back the output to the positive or non-inverting input of the op-amp. The input signals are applied to the negative or inverting input through resistors (R1, R2, R3, ...). The output voltage is in phase and proportional to the sum of the input voltages, as shown by the equation:

    `Vout = Rf/R1 * V1 + Rf/R2 * V2 + Rf/R3 * V3 + ...`

    The non-inverting summing amplifier can be used to add signals, mix signals, or perform weighted averaging.

    The circuit diagram of a non-inverting summing amplifier is shown below:

    ```
    +Vcc
     |
     |
     |    V1
     |-----