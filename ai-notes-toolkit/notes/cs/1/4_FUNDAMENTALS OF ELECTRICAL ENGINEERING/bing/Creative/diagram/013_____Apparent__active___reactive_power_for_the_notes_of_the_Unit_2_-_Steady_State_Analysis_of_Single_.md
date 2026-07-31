### Apparent, active and reactive power

- Apparent power is the product of the RMS voltage and current in an AC circuit, without reference to the phase angle between them. It is measured in volt-amperes (VA) and symbolized by S. It represents the total power supplied to the circuit, but not all of it may be useful for doing work.  
- Active power is the component of the apparent power that is in phase with the voltage and does work in the circuit. It is measured in watts (W) and symbolized by P. It represents the average power transferred to the load, such as a resistor, a motor, or a lamp.    
- Reactive power is the component of the apparent power that is out of phase with the voltage and does not do work in the circuit. It is measured in volt-amperes reactive (VAR) and symbolized by Q. It represents the power that is stored and released by the reactive elements in the circuit, such as a capacitor or an inductor.    

- The relationship between apparent, active and reactive power can be expressed by the power triangle, as shown below:

![power triangle](https://control.com/wp-content/uploads/2021/08/Power-Triangle-1.png)

- The power triangle shows that the apparent power is the hypotenuse of the right triangle, and the active and reactive powers are the adjacent and opposite sides, respectively. The angle between the apparent and active powers is the power factor angle, which indicates how much the current lags or leads the voltage in the circuit.   
- The power triangle can be used to calculate the apparent, active and reactive powers using the following formulas:

  - S = Vrms * Irms
  - P = S * cos(θ) = Vrms * Irms * cos(θ)
  - Q = S * sin(θ) = Vrms * Irms * sin(θ)

- Alternatively, the apparent, active and reactive powers can be represented by a complex number, called the complex power, as shown below:

![complex power](https://www.electronicshub.org/wp-content/uploads/2015/06/Complex-Power.jpg)

- The complex power is symbolized by S and has a real part (P) and an imaginary part (Q). The magnitude of the complex power is the apparent power, and the angle of the complex power is the power factor angle. 
- The complex power can be calculated using the following formula:

  - S = P + jQ = Vrms * Irms * (cos(θ) + j sin(θ)) = Vrms * Irms * ∠θ

- The complex power can also be expressed in terms of the complex voltage and current, as shown below:

  - S = V * I* = Vrms * ∠φ * Irms * ∠(-ψ) = Vrms * Irms * ∠(φ - ψ)

  - where V and I are the phasors of the voltage and current, respectively, and φ and ψ are their phase angles. The asterisk (*) denotes the complex conjugate.