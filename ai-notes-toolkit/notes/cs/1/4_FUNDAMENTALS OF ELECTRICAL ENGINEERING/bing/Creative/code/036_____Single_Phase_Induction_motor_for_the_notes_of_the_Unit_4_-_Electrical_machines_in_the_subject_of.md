# Single Phase Induction Motor

- A single phase induction motor is a type of AC motor that operates on single phase power supply .
- It has a stator with distributed single phase winding and a rotor with a cage winding .
- There is a uniform air gap between the stator and the rotor, but no electrical connection between them.
- The stator produces a pulsating magnetic field, rather than a rotating one as in a three phase motor .
- This means there is no starting torque in a single phase induction motor, as the rotor does not experience any rotating force .
- To make the motor self-starting, various methods are used to create a rotating magnetic field at least at starting, such as:
  - Split-phase method: The stator has two windings, a main winding and an auxiliary winding, connected in parallel. The auxiliary winding is connected to a capacitor or a resistor, which creates a phase difference between the currents in the two windings. This results in a rotating magnetic field that induces a torque in the rotor.
  - Capacitor-start method: Similar to the split-phase method, but the capacitor is connected only at starting and disconnected once the motor reaches a certain speed. This improves the power factor and reduces the losses in the auxiliary winding.
  - Permanent-split capacitor method: Similar to the capacitor-start method, but the capacitor remains connected throughout the operation. This eliminates the need for a centrifugal switch and reduces the noise and vibration in the motor. However, the starting torque is lower than the capacitor-start method .
  - Shaded-pole method: The stator has a single winding with a small portion of each pole shaded by a copper ring. The shaded portion of the pole creates a phase difference between the currents in the shaded and unshaded parts, resulting in a rotating magnetic field. This method is simple and cheap, but has low efficiency and power factor.
- The speed of a single phase induction motor depends on the frequency of the supply voltage and the number of poles in the stator. The synchronous speed is given by:

  ```
  N_s = 120f / P
  ```

  where N_s is the synchronous speed in rpm, f is the frequency in Hz, and P is the number of poles.

- The slip of a single phase induction motor is the difference between the synchronous speed and the actual speed of the rotor, expressed as a fraction of the synchronous speed. The slip is given by:

  ```
  s = (N_s - N_r) / N_s
  ```

  where s is the slip, N_s is the synchronous speed, and N_r is the rotor speed.

- The torque of a single phase induction motor is proportional to the square of the slip, and reaches a maximum value at a certain slip called the pull-out slip. The torque-slip curve is shown below:

  ![torque-slip curve](https://www.allaboutcircuits.com/uploads/articles/SinglePhaseInductionMotorTorqueSlipCurve.png)

- The power output of a single phase induction motor is the product of the torque and the angular speed of the rotor. The power input is the product of the voltage and the current drawn by the motor. The efficiency of the motor is the ratio of the power output to the power input.

- The advantages of a single phase induction motor are:
  - It is simple and cheap to manufacture and maintain.
  - It is reliable and durable, as it has no brushes or commutators.
  - It can operate on single phase power supply, which is widely available in domestic and commercial applications.
- The disadvantages of a single phase induction motor are:
  - It has low starting torque and power factor.
  - It has low efficiency and speed regulation.
  - It requires additional devices to make it self-starting.