##### 10. To determine the value of acceleration due to gravity (g) using compound pendulum.

- A compound pendulum is a rigid body that can oscillate about a horizontal axis passing through it.
- The time period of a compound pendulum depends on the length of the pendulum, the mass distribution of the pendulum, and the acceleration due to gravity.
- The equation for the time period of a compound pendulum is:

  $$T = 2\pi \sqrt{\frac{I}{mgd}}$$

  where $T$ is the time period, $I$ is the moment of inertia of the pendulum about the axis of oscillation, $m$ is the mass of the pendulum, $g$ is the acceleration due to gravity, and $d$ is the distance of the center of mass of the pendulum from the axis of oscillation.
- To determine the value of $g$ using a compound pendulum, the following steps are followed:

  - Measure the mass ($m$) and the length ($L$) of the pendulum.
  - Choose different points along the length of the pendulum to suspend it from a rigid support and mark them as $O_1, O_2, ..., O_n$.
  - Measure the distance of each point from the center of mass of the pendulum and denote them as $d_1, d_2, ..., d_n$.
  - For each point of suspension, set the pendulum into small oscillations and measure the time taken for 20 oscillations using a stopwatch. Divide this time by 20 to get the average time period ($T_1, T_2, ..., T_n$) for each point of suspension.
  - Calculate the moment of inertia ($I_1, I_2, ..., I_n$) of the pendulum about each point of suspension using the parallel axis theorem:

    $$I_i = I_{cm} + md_i^2$$

    where $I_{cm}$ is the moment of inertia of the pendulum about its center of mass, which can be calculated using the formula for a uniform rod:

    $$I_{cm} = \frac{1}{12}mL^2$$
  - Plot a graph of $T_i^2$ versus $d_i$ and draw the best fit straight line. The slope of this line is equal to $\frac{4\pi^2}{g}$, and the intercept is equal to $\frac{4\pi^2I_{cm}}{mg}$.
  - Find the value of $g$ from the slope of the graph using the formula:

    $$g = \frac{4\pi^2}{\text{slope}}$$
  - Find the percentage error in the value of $g$ by comparing it with the standard value of $g$ (9.81 m/s$^2$) using the formula:

    $$\text{percentage error} = \frac{|g - g_0|}{g_0} \times 100\%$$

    where $g_0$ is the standard value of $g$.