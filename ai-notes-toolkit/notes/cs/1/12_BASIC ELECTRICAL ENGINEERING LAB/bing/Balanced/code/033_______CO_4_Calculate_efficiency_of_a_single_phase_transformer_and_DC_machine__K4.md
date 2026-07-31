##### CO 4 Calculate efficiency of a single phase transformer and DC machine. K4

- Efficiency is the ratio of output power to input power, expressed as a percentage.
- A single phase transformer is a device that transfers electrical energy from one circuit to another through mutual induction, without changing the frequency.
- A DC machine is a device that converts electrical energy to mechanical energy or vice versa, using direct current.
- To calculate the efficiency of a single phase transformer, we need to know the input and output voltages, currents, and power factors, as well as the losses due to copper and iron.
- The input power of a single phase transformer is given by:

```
P_in = V_in * I_in * cos(phi_in)
```

- Where V_in is the input voltage, I_in is the input current, and cos(phi_in) is the input power factor.
- The output power of a single phase transformer is given by:

```
P_out = V_out * I_out * cos(phi_out)
```

- Where V_out is the output voltage, I_out is the output current, and cos(phi_out) is the output power factor.
- The copper loss of a single phase transformer is the power dissipated in the primary and secondary windings due to their resistance. It is given by:

```
P_cu = I_p^2 * R_p + I_s^2 * R_s
```

- Where I_p is the primary current, R_p is the primary resistance, I_s is the secondary current, and R_s is the secondary resistance.
- The iron loss of a single phase transformer is the power dissipated in the core due to hysteresis and eddy currents. It is given by:

```
P_fe = k_h * f * B_max^1.6 * V + k_e * f^2 * B_max^2 * V
```

- Where k_h is the hysteresis constant, f is the frequency, B_max is the maximum flux density, V is the volume of the core, k_e is the eddy current constant.
- The efficiency of a single phase transformer is then given by:

```
eta = P_out / (P_in + P_cu + P_fe) * 100%
```

- To calculate the efficiency of a DC machine, we need to know the input and output voltages, currents, and power, as well as the losses due to armature, field, and mechanical friction.
- The input power of a DC machine is given by:

```
P_in = V * I
```

- Where V is the terminal voltage and I is the armature current.
- The output power of a DC machine is given by:

```
P_out = T * omega
```

- Where T is the torque and omega is the angular speed.
- The armature loss of a DC machine is the power dissipated in the armature winding due to its resistance. It is given by:

```
P_a = I^2 * R_a
```

- Where R_a is the armature resistance.
- The field loss of a DC machine is the power dissipated in the field winding due to its resistance. It is given by:

```
P_f = V_f * I_f
```

- Where V_f is the field voltage and I_f is the field current.
- The mechanical loss of a DC machine is the power dissipated due to friction and windage. It is given by:

```
P_m = k * omega^3
```

- Where k is a constant that depends on the machine design and operating conditions.
- The efficiency of a DC machine is then given by:

```
eta = P_out / (P_in + P_a + P_f + P_m) * 100%
```