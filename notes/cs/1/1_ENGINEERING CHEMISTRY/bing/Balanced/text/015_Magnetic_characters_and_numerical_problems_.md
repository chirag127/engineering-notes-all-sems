# Magnetic Characteristics and Numerical Problems

Magnetic characteristics are the properties of a material that determine its behavior in a magnetic field. Some of the important magnetic characteristics are:

- Magnetic permeability: The ratio of the magnetic flux density (B) to the magnetic field intensity (H) in a material. It measures how easily a material can be magnetized by an external field. The magnetic permeability of free space (vacuum) is denoted by μ0 and has a value of 4π × 10^-7 H/m. The magnetic permeability of a material is denoted by μ and is equal to μ0 times the relative permeability (μr) of the material. The relative permeability is a dimensionless quantity that depends on the type and composition of the material. For example, the relative permeability of iron is about 5000, while that of air is about 1.00000037.
- Magnetic susceptibility: The ratio of the magnetization (M) to the magnetic field intensity (H) in a material. It measures how much a material is magnetized by an external field. The magnetic susceptibility of a material is denoted by χ and is equal to μr - 1. The magnetic susceptibility is a dimensionless quantity that can be positive, negative, or zero depending on the type of material. For example, the magnetic susceptibility of iron is about 4999, while that of diamagnetic materials (such as copper, silver, or water) is negative and very small (about -10^-5).
- Magnetic hysteresis: The phenomenon of retaining some magnetization even after the external field is removed. It is observed in ferromagnetic materials (such as iron, nickel, or cobalt) that have domains of aligned magnetic moments. When an external field is applied, the domains tend to align with the field, resulting in a net magnetization. When the field is removed, some of the domains remain aligned, creating a residual magnetization or remanence. To demagnetize the material completely, a reverse field of sufficient strength must be applied. The strength of the reverse field required to reduce the magnetization to zero is called the coercivity. The loop formed by plotting the magnetization versus the applied field is called the hysteresis loop. The area enclosed by the loop represents the energy loss due to hysteresis.

Numerical problems involving magnetic characteristics can be solved by applying the following formulas:

- B = μH
- M = χH
- χ = μr - 1
- μ = μ0μr
- μ0 = 4π × 10^-7 H/m

Some examples of numerical problems are:

- What is the magnetic flux density in a material with a relative permeability of 1000 when a magnetic field intensity of 0.5 A/m is applied?
  - Solution: B = μH = μ0μrH = (4π × 10^-7)(1000)(0.5) = 6.28 × 10^-4 T
- What is the magnetization of a material with a magnetic susceptibility of 0.01 when a magnetic field intensity of 100 A/m is applied?
  - Solution: M = χH = (0.01)(100) = 1 A/m
- What is the relative permeability of a material with a magnetic susceptibility of -0.00001?
  - Solution: χ = μr - 1 => μr = χ + 1 = -0.00001 + 1 = 0.99999
- What is the coercivity of a material that has a remanence of 0.1 T when the applied field is reduced to zero?
  - Solution: The coercivity is the reverse field required to reduce the magnetization to zero. Using the formula B = μH, we can find the value of H that corresponds to B = 0.1 T. Assuming that the material has a constant relative permeability of 1000, we have:
    - 0.1 = μH = μ0μrH => H = 0.1 / (μ0μr) = 0.1 / [(4π × 10^-7)(1000)] = 795.77 A/m
    - The coercivity is the negative of this value, so Hc = -795.77 A/m.