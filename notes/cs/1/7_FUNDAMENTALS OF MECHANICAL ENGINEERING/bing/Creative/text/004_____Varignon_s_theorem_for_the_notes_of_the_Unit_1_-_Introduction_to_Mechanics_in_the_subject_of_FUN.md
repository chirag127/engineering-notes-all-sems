### Varignon's theorem

- Varignon's theorem is a useful tool in scalar moment calculations for concurrent forces .
- It states that the moment of the resultant of several concurrent forces about any point is equal to the sum of the moments of the individual forces about the same point  .
- It can also be stated as the moment of a force about a point equals the sum of the moments of its components about the same point  .
- Mathematically, it can be expressed as:

$$\vec{M}_O = \vec{M}_{OA} + \vec{M}_{OB}$$

where $\vec{M}_O$ is the moment of the resultant force $\vec{R}$ about point O, $\vec{M}_{OA}$ and $\vec{M}_{OB}$ are the moments of the component forces $\vec{A}$ and $\vec{B}$ about point O, respectively.

- Varignon's theorem can be applied to any number of concurrent forces, as long as they have a common point of application  .
- Varignon's theorem can be used to simplify the calculation of moments when the perpendicular distance from the point to the line of action of the force is hard to determine  .
- Varignon's theorem can also be used to find the resultant force by equating the moments of the individual forces and the resultant force about two different points .
- Varignon's theorem has applications in engineering, such as finding the reactions at the supports of a beam, or the tension in the cables of a crane .

- An example of applying Varignon's theorem is shown below:

![Example of Varignon's theorem](https://eng.libretexts.org/@api/deki/files/1383/Varignon_Example.png)

In this example, three concurrent forces $\vec{F}_1$, $\vec{F}_2$, and $\vec{F}_3$ act on a point O. The moment of the resultant force $\vec{R}$ about point A can be found by using Varignon's theorem:

$$\vec{M}_A = \vec{M}_{A1} + \vec{M}_{A2} + \vec{M}_{A3}$$

where $\vec{M}_{A1}$, $\vec{M}_{A2}$, and $\vec{M}_{A3}$ are the moments of the individual forces about point A, respectively. The moments can be calculated by using the cross product of the position vector and the force vector:

$$\vec{M}_{A1} = \vec{r}_{A1} \times \vec{F}_1$$
$$\vec{M}_{A2} = \vec{r}_{A2} \times \vec{F}_2$$
$$\vec{M}_{A3} = \vec{r}_{A3} \times \vec{F}_3$$

where $\vec{r}_{A1}$, $\vec{r}_{A2}$, and $\vec{r}_{A3}$ are the position vectors from point A to the point of application of the forces, respectively. The position vectors can be found by using the coordinates of the points:

$$\vec{r}_{A1} = (0.5 \hat{i} + 0.5 \hat{j}) \text{ m}$$
$$\vec{r}_{A2} = (0.5 \hat{i} - 0.5 \hat{j}) \text{ m}$$
$$\vec{r}_{A3} = (-0.5 \hat{i} - 0.5 \hat{j}) \text{ m}$$

The force vectors are given by:

$$\vec{F}_1 = (2 \hat{i} + 2 \hat{j}) \text{ kN}$$
$$\vec{F}_2 = (-2 \hat{i} + 2 \hat{j}) \text{ kN}$$
$$\vec{F}_3 = (-2 \hat{i} - 2 \hat{j}) \text{ kN}$$

The cross products can be computed by using the determinant of a matrix:

$$\vec{M}_{A1} = \