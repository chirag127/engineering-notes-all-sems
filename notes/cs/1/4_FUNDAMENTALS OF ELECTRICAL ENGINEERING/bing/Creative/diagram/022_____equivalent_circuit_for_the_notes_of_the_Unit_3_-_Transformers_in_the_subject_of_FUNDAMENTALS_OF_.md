### Equivalent Circuit of a Transformer

An equivalent circuit of a transformer is a simplified representation of a practical transformer that shows all the electrical parameters such as winding resistance, leakage reactance, magnetizing current, core losses, etc. The equivalent circuit helps to analyze the performance and efficiency of a transformer under different operating conditions.

The equivalent circuit of a transformer can be derived from the following steps:

- Assume that the primary and secondary windings have some resistance and leakage reactance, denoted by R1, X1, R2, and X2 respectively. These parameters account for the copper losses and leakage flux in the windings.
- Refer the secondary parameters to the primary side by multiplying them with the square of the turns ratio, denoted by K = N1/N2. The referred parameters are R2', X2', E2', and I2'.
- Draw the primary and referred secondary circuits in series, as shown in the figure below. This is the exact equivalent circuit of a transformer.

![Exact equivalent circuit of a transformer](https://www.electricalclassroom.com/wp-content/uploads/2017/11/Exact-equivalent-circuit-of-transformer.png)

- Assume that the no-load current I0 consists of two components: the magnetizing current Im that produces the flux in the core, and the core loss component Ic that accounts for the hysteresis and eddy current losses in the core. These components are in quadrature with each other, as shown in the figure below.

![No-load current components](https://www.electricalclassroom.com/wp-content/uploads/2017/11/No-load-current-components.png)

- Represent the magnetizing current Im by a magnetizing reactance Xm in parallel with the primary winding, and the core loss component Ic by a core loss resistance Rc in parallel with the primary winding. These parameters are calculated from the no-load test of the transformer.
- Draw the parallel branch of Rc and Xm in parallel with the series branch of R1, X1, R2', and X2', as shown in the figure below. This is the approximate equivalent circuit of a transformer.

![Approximate equivalent circuit of a transformer](https://www.electricalclassroom.com/wp-content/uploads/2017/11/Approximate-equivalent-circuit-of-transformer.png)

- To simplify the analysis, the parallel branch of Rc and Xm can be moved to the left of the series branch, as shown in the figure below. This is the simplified equivalent circuit of a transformer.

![Simplified equivalent circuit of a transformer](https://www.electricalclassroom.com/wp-content/uploads/2017/11/Simplified-equivalent-circuit-of-transformer.png)

- To further simplify the analysis, the series branch of R1, X1, R2', and X2' can be replaced by a single equivalent resistance Req and a single equivalent reactance Xeq, as shown in the figure below. This is the most simplified equivalent circuit of a transformer.

![Most simplified equivalent circuit of a transformer](https://www.electricalclassroom.com/wp-content/uploads/2017/11/Most-simplified-equivalent-circuit-of-transformer.png)

The equivalent circuit of a transformer can be used to calculate the voltage regulation, efficiency, power factor, and other performance parameters of a transformer. The equivalent circuit can also be drawn on the secondary side by referring the primary parameters to the secondary side by dividing them with the square of the turns ratio. The equivalent circuit can also be modified to include the effect of frequency, load, and temperature variations on the transformer parameters.