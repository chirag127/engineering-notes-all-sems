### EMF equation of generator and torque equation of motor

- A generator is a device that converts mechanical energy into electrical energy by inducing an electromotive force (EMF) in a coil of wire that rotates in a magnetic field.
- A motor is a device that converts electrical energy into mechanical energy by applying a torque to a coil of wire that rotates in a magnetic field.
- The EMF equation of a generator relates the generated EMF to the number of turns in the coil, the magnetic flux, the speed of rotation, and the number of poles in the generator.
- The torque equation of a motor relates the applied torque to the current in the coil, the magnetic flux, the number of turns in the coil, and the number of poles in the motor.

#### EMF equation of a generator

- The EMF equation of a generator can be derived by applying Faraday's law of electromagnetic induction, which states that the induced EMF is equal to the negative rate of change of magnetic flux through the coil.
- Consider a coil of N turns that rotates with an angular velocity ω in a uniform magnetic field B. The area of the coil is A and the angle between the normal to the coil and the magnetic field is θ.
- The magnetic flux through the coil is given by Φ = B A cos θ, where θ = ω t, and t is the time.
- The induced EMF in the coil is given by E = - N dΦ / dt, where dΦ / dt is the rate of change of magnetic flux.
- Substituting the expression for Φ and using the chain rule, we get E = - N dΦ / dt = - N (- B A ω sin θ) dθ / dt = N B A ω^2 sin θ cos θ
- The maximum value of E occurs when sin θ cos θ = 1/2, which happens when θ = π/4 or 3π/4. The maximum value of E is E_max = N B A ω^2 / 2
- The frequency of the EMF is f = ω / 2π, and the number of poles in the generator is P = 2π / ω. Therefore, E_max = N B A P f / 2
- The average value of E over one cycle is E_avg = 2 E_max / π, since the EMF is a sinusoidal function. Therefore, E_avg = 4 N B A P f / π^2
- The EMF equation of a generator can be written as E = K N Φ P f, where K is a constant that depends on the units of the quantities, and Φ is the magnetic flux per pole, given by Φ = B A / P.
- The EMF equation of a generator can also be written in terms of the speed of rotation N, where N = 60 f / P, and f is the frequency in Hz and N is the speed in rpm. Therefore, E = K N Φ Z, where Z is the total number of conductors in the coil, given by Z = N P.

#### Torque equation of a motor

- The torque equation of a motor can be derived by applying the Lorentz force law, which states that the force on a current-carrying conductor in a magnetic field is given by F = I L x B, where I is the current, L is the length of the conductor, and B is the magnetic field.
- Consider a coil of N turns that carries a current I and rotates with an angular velocity ω in a uniform magnetic field B. The area of the coil is A and the angle between the normal to the coil and the magnetic field is θ.
- The torque on the coil is given by τ = F r sin θ, where F is the force on one side of the coil, r is the radius of the coil, and θ is the angle between the force and the radius.
- Substituting the expression for F and using the fact that L = 2 r, we get τ = I (2 r) x B r sin θ = 2 I r^2 B sin θ
- The maximum value of τ occurs when sin θ = 1, which happens when θ = π/2 or 3π/2. The maximum value of τ is τ_max = 2 I r^2 B
- The average value of τ over one cycle is τ_avg = 2 τ_max /