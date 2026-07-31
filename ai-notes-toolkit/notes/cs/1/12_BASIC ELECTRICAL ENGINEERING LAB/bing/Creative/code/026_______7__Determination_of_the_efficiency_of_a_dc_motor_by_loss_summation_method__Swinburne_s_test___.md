##### 7. Determination of the efficiency of a dc motor by loss summation method (Swinburne's test).

- The efficiency of a dc motor is defined as the ratio of output (mechanical) power to input (electrical) power.
- The output power of a dc motor can be measured by using a dynamometer or a brake, which applies a torque and measures the rotational speed of the motor shaft.
- The input power of a dc motor can be measured by using a power analyzer, which measures the voltage and current supplied to the motor.
- The efficiency of a dc motor can be calculated by using the formula:

  `Efficiency = Output power / Input power`

- However, measuring the output power of a dc motor on load requires a suitable load device, which may not be available or convenient for large motors.
- An alternative method of measuring the efficiency of a dc motor is to determine its losses (instead of measuring the output power on load) and then use the formula:

  `Efficiency = (Input power - Losses) / Input power`

- This method is called the loss summation method or the Swinburne's test.
- The loss summation method enables the determination of losses without actually loading the motor. The power is required to supply the losses only, so there is no difficulty in applying this method even to very large motors.
- The losses in a dc motor can be classified into two types: constant losses and variable losses .
- Constant losses are those losses that do not vary with the load, such as core loss, friction loss and windage loss .
- Variable losses are those losses that vary with the load, such as copper loss in the armature and the field winding .
- The loss summation method involves the following steps :

  - Run the motor at no load and measure the input power, the no-load current and the speed.
  - Calculate the constant losses by multiplying the input power by the efficiency at no load, which can be assumed to be 0.8 for shunt motors and 0.75 for compound motors.
  - Calculate the copper loss in the field winding by multiplying the field resistance and the square of the field current, which can be assumed to be constant for shunt and compound motors.
  - Calculate the copper loss in the armature at no load by multiplying the armature resistance and the square of the no-load current.
  - Calculate the variable loss at any load by multiplying the armature resistance and the square of the load current, which can be obtained from the no-load current and the rated current of the motor.
  - Calculate the total loss at any load by adding the constant loss and the variable loss.
  - Calculate the efficiency at any load by subtracting the total loss from the input power and dividing by the input power.

- The advantages of the loss summation method are:

  - It is simple and convenient to perform, as it does not require a load device or a dynamometer.
  - It is economical, as it consumes less power than the direct method.
  - It is applicable to any size of motor, as it does not depend on the availability of a suitable load.

- The disadvantages of the loss summation method are:

  - It is not very accurate, as it involves some assumptions and approximations, such as the efficiency at no load, the field current and the armature resistance.
  - It does not account for the stray load losses, which are the additional losses due to the distortion of the magnetic field and the eddy currents in the armature at high loads.
  - It does not provide the actual output power and torque of the motor on load, which may be required for some applications.