# EMF equation of generator and torque equation of motor

## EMF equation of generator

- A generator is a device that converts mechanical energy into electrical energy by rotating a coil in a magnetic field.
- The emf induced in the coil is given by the Faraday's law of electromagnetic induction, which states that the emf is equal to the rate of change of magnetic flux linkage.
- The magnetic flux linkage is the product of the magnetic flux and the number of turns in the coil, and it depends on the angle between the coil and the magnetic field.
- The emf equation of a generator can be derived by considering a single loop of wire with N turns and area A, rotating with a constant angular speed ω in a uniform magnetic field B.
- The magnetic flux through the loop is given by Φ = B A cos θ, where θ is the angle between the normal to the loop and the magnetic field.
- The flux linkage is then N Φ = N B A cos θ, and the emf is the negative of the rate of change of flux linkage, i.e.,

  E = - d/dt (N Φ) = - N B A d/dt (cos θ)

- Since the loop is rotating with a constant angular speed ω, the angle θ changes with time as θ = ω t, and the derivative of cos θ is - ω sin θ. Therefore, the emf is

  E = N B A ω sin θ = N B A ω sin (ω t)

- This equation shows that the emf is a sinusoidal function of time, with a frequency equal to the angular speed of the loop, and an amplitude equal to N B A ω, which is also called the peak emf, E0. Thus, the emf equation of a generator can be written as

  E = E0 sin (ω t)

- For a DC generator, the coil is connected to a commutator, which reverses the direction of the current every half cycle, so that the output emf is always positive. The emf equation of a DC generator is then

  E = E0 |sin (ω t)|

## Torque equation of motor

- A motor is a device that converts electrical energy into mechanical energy by passing a current through a coil in a magnetic field, so that a torque is exerted on the coil, and it starts to rotate.
- The torque on the coil is given by the Lorentz force law, which states that the force on a current-carrying wire in a magnetic field is F = I l B sin θ, where I is the current, l is the length of the wire, B is the magnetic field, and θ is the angle between the wire and the magnetic field.
- The torque is then the product of the force and the perpendicular distance from the pivot to the wire, i.e.,

  τ = r F sin θ = I l B r sin θ sin θ = I l B r sin^2 θ

- For a single loop of wire with N turns and area A, the length of the wire is l = 2 π r, where r is the radius of the loop, and the area is A = π r^2. Therefore, the torque is

  τ = I N B A sin^2 θ = I N B π r^3 sin^2 θ

- This equation shows that the torque is a sinusoidal function of the angle θ, with a maximum value of I N B π r^3 when θ = 90°, and a zero value when θ = 0° or 180°. The torque equation of a motor can be written as

  τ = τ0 sin^2 θ

  where τ0 = I N B π r^3 is the peak torque.

- For a DC motor, the coil is connected to a commutator, which keeps the current in the same direction as the magnetic field, so that the torque is always positive. The torque equation of a DC motor is then

  τ = τ0 |sin θ|