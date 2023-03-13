The Poynting vector and Poynting theorem are concepts in electromagnetics that describe the flow and conservation of electromagnetic energy. The Poynting vector is defined as the cross product of the electric field and the magnetic field vectors at any point in space. It represents the direction and magnitude of the electromagnetic power per unit area. The Poynting theorem states that the net electromagnetic power flowing into a region of space may be either dissipated, or used to change the energy stored in electric and magnetic fields within that region.

The following diagram illustrates the Poynting vector and Poynting theorem using ASCII characters:

```
    +---------------------+
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    +---------------------+
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    +---------------------+
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    +---------------------+
    ^                     ^
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    E                     E
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    v                     v
    +---------------------+
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    +---------------------+
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    +---------------------+
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    |                     |
    +---------------------+
    <--------------------->
    H                     H
    <--------------------->
```

In this diagram, the electric field E is pointing vertically and the magnetic field H is pointing horizontally. The Poynting vector S is given by S = E x H, which means it is pointing out of the page. The boxes represent regions of space where the electromagnetic energy is flowing. The Poynting theorem states that the net power entering or leaving a region is equal to the change in energy stored in the fields plus the power dissipated in the region. Mathematically, this can be written as:

```
dW/dt = - integral(S dot n) dA - integral(J dot E) dV
```

where W is the energy stored in the fields, S is the Poynting vector, n is the unit normal vector to the surface of the region, A is the surface area, J is the current density, E is the electric field, and V is the volume of the region. The first term on the right-hand side represents the net power flowing across the boundary of the region, and the second term represents the power dissipated by Joule heating in the region. If the region is lossless, the second term is zero and the net power is equal to the change in energy stored in the fields. This means that the electromagnetic energy is conserved in the region.