##### 8. Determination of efficiency of a dc shunt motor by load test

- The efficiency of a dc shunt motor is the ratio of output power to input power. It can be determined by direct or indirect methods of testing.
- The direct method of testing involves loading the motor with a brake or a dynamometer and measuring the input and output power. This method is accurate but requires a large amount of power and a suitable load.
- The indirect method of testing involves running the motor at no load and measuring the losses. The efficiency at any load can be pre-determined by subtracting the losses from the input power. This method is simple and economical but assumes that the losses are constant at all loads.
- One of the indirect methods of testing is the Swinburne's test, which is applicable to shunt and compound dc machines with constant flux. In this test, the motor is run at rated voltage and no load, and the following parameters are measured:
  - The no-load current (I_0) and the no-load power (P_0) drawn by the motor.
  - The armature resistance (R_a) and the shunt field resistance (R_sh) of the motor.
- The losses in the motor can be calculated as follows:
  - The shunt field loss (P_sh) is the power dissipated in the shunt field winding, which is given by P_sh = V^2/R_sh, where V is the rated voltage.
  - The armature copper loss (P_cu) is the power dissipated in the armature winding due to the resistance, which is given by P_cu = I_a^2 R_a, where I_a is the armature current.
  - The constant losses (P_c) are the sum of the iron losses, friction losses, and windage losses, which are assumed to be constant at all loads. They can be obtained by subtracting the shunt field loss and the armature copper loss from the no-load power, i.e., P_c = P_0 - P_sh - P_cu.
- The efficiency of the motor at any load can be pre-determined by using the following formula:

  - η = (P_o - P_c)/(P_i - P_c) x 100%, where P_o is the output power, P_i is the input power, and P_c is the constant losses.
  - Alternatively, the efficiency can be expressed in terms of the output torque (T) and the speed (N) as follows:

  - η = (T x N x 2π/60)/(V x I) x 100%, where V is the rated voltage and I is the total current drawn by the motor.

- The advantages of the Swinburne's test are:
  - It is simple and economical, as it does not require a large amount of power or a suitable load.
  - It can be performed on both motor and generator modes of operation.
  - It can be used to determine the efficiency at any load and speed.
- The disadvantages of the Swinburne's test are:
  - It assumes that the losses are constant at all loads, which may not be true in practice.
  - It does not account for the stray load losses, which are the additional losses due to the load current and the magnetic saturation of the core.
  - It does not give the actual performance of the motor under load conditions.

- A mnemonic to remember the formula for the efficiency of the motor is:

  - **E**fficiency = (**O**utput - **C**onstant)/(**I**nput - **C**onstant) x 100%
  - **E**OC/**I**OC x 100%
  - This can be pronounced as "E-O-C over I-O-C times hundred".