# Slip-torque characteristics of induction motor

- The slip-torque characteristic of an induction motor is the relationship between the torque produced by the motor and the slip of the rotor with respect to the synchronous speed.
- The slip of the rotor is defined as the difference between the synchronous speed and the rotor speed, expressed as a fraction of the synchronous speed.
- The slip-torque characteristic can be derived from the equivalent circuit of the induction motor, by equating the mechanical power output to the electrical power input to the rotor.
- The slip-torque characteristic can be represented by a rectangular hyperbola, as shown in the figure below.

![Slip-torque characteristic](https://circuitglobe.com/wp-content/uploads/2016/07/Torque-Slip-Characteristic-of-an-Induction-Motor.png)

- The slip-torque characteristic can be divided into three regions, depending on the value of the slip:

  - Low slip region: This is the region where the slip is very small, and the rotor speed is near the synchronous speed. In this region, the torque is proportional to the slip, and the rotor resistance is negligible compared to the rotor reactance. The torque is given by:

    $$T = \frac{3V^2_sR_2}{sX^2_0}$$

    where $V_s$ is the stator voltage, $R_2$ is the rotor resistance, $s$ is the slip, and $X_0$ is the standstill reactance of the motor.

  - Medium slip region: This is the region where the slip is moderate, and the rotor speed is lower than the synchronous speed. In this region, the torque is not linearly proportional to the slip, and the rotor resistance is comparable to the rotor reactance. The torque is given by:

    $$T = \frac{3V^2_sR_2/s}{(R_2/s)^2 + X^2_0}$$

    The torque reaches its maximum value when $R_2/s = X_0$, which corresponds to the slip value of:

    $$s_{max} = \frac{R_2}{X_0}$$

    The maximum torque is independent of the stator voltage, and is given by:

    $$T_{max} = \frac{3V^2_s}{2X_0}$$

  - High slip region: This is the region where the slip is large, and the rotor speed is much lower than the synchronous speed. In this region, the torque decreases as the slip increases, and the rotor resistance is much larger than the rotor reactance. The torque is given by:

    $$T = \frac{3V^2_sX_0}{(R_2/s)^2 + X^2_0}$$

    The torque becomes zero when the slip is equal to one, which means the rotor is stationary.

- The slip-torque characteristic can be modified by changing the rotor resistance, either by inserting external resistors in the rotor circuit, or by using a wound rotor with slip rings. By increasing the rotor resistance, the maximum torque can be increased, and the slip at which the maximum torque occurs can be shifted to a higher value. This can improve the starting torque and the speed regulation of the motor. However, increasing the rotor resistance also increases the rotor losses and reduces the efficiency of the motor.