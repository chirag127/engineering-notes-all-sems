### Slip-torque characteristics of induction motor

- The slip-torque characteristic of an induction motor is the relationship between the torque produced by the motor and the slip of the rotor with respect to the synchronous speed.
- The slip of the rotor is defined as the difference between the synchronous speed and the rotor speed, expressed as a fraction of the synchronous speed.
- The slip-torque characteristic can be derived from the equivalent circuit of the induction motor, by equating the mechanical power output to the electrical power input to the rotor.
- The slip-torque characteristic can be represented by a rectangular hyperbola, as shown in the figure below.

![Slip-torque characteristic](https://circuitglobe.com/wp-content/uploads/2016/05/Torque-Slip-Characteristic-of-an-Induction-Motor.png)

- The slip-torque characteristic can be divided into three regions, depending on the value of the slip:

  - Low slip region: This is the region where the slip is very small, and the rotor speed is near the synchronous speed. In this region, the torque is proportional to the slip, and the rotor resistance is negligible compared to the rotor reactance. The torque is given by:

    `T = (3/2) * (V^2 / X^2) * (R2 / s)`

    where V is the stator voltage, X2 is the rotor reactance, R2 is the rotor resistance, and s is the slip.

  - Medium slip region: This is the region where the slip is moderate, and the rotor speed is lower than the synchronous speed. In this region, the torque is not linearly proportional to the slip, and the rotor resistance is comparable to the rotor reactance. The torque is given by:

    `T = (3/2) * (V^2 / X^2) * (R2 / (R2^2 + (sX2)^2))`

    The torque reaches its maximum value at a certain slip, called the critical slip, given by:

    `s = R2 / X2`

    The maximum torque, also called the breakdown torque or the pull-out torque, is given by:

    `Tmax = (3/4) * (V^2 / X^2)`

  - High slip region: This is the region where the slip is large, and the rotor speed is much lower than the synchronous speed. In this region, the torque decreases as the slip increases, and the rotor resistance is dominant over the rotor reactance. The torque is given by:

    `T = (3/2) * (V^2 / X^2) * (s / R2)`

    The torque becomes zero when the slip is equal to one, which means the rotor is stationary.

- The slip-torque characteristic can be modified by changing the rotor resistance, either by adding external resistors or by using a wound rotor with slip rings. Increasing the rotor resistance shifts the critical slip to a higher value, and increases the maximum torque. However, it also increases the rotor losses and reduces the efficiency of the motor.