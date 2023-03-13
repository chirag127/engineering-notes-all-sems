A Parametric Productivity Model (PPM) in Software Project Management (SPM) is a method of estimating the cost and effort required to develop software based on various parameters, such as size, complexity, hardware/software requirements, etc. One example of a PPM is the Constructive Cost Model (COCOMO), which uses a basic equation to calculate the effort as a function of the size of the software, and then applies different coefficients and exponents to adjust the equation for different modes of development (organic, semi-detached, or embedded) and different levels of detail (basic, intermediate, or detailed) .

The following diagram illustrates the basic architecture of a PPM in SPM using ASCII art:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Input Data     |---->|  PPM Equation   |---->|  Output Data    |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Size           |     |  Effort = a *   |     |  Effort         |
|  Complexity     |     |          (Size)^b *   |  Cost           |
|  Hardware/      |     |          M1 * M2 * ...|  Schedule       |
|  Software       |     |                 |     |  Quality        |
|  Requirements   |     |  a, b =         |     |                 |
|                 |     |  coefficients    |     |                 |
|                 |     |  M1, M2, ... =  |     |                 |
|                 |     |  multipliers     |     |                 |
+-----------------+     +-----------------+     +-----------------+
```