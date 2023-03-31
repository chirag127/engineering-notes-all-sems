
### Distance Measures for Quantum Information
1. The **trace distance** is a measure of the distinguishability of two quantum states, $\rho_1$ and $\rho_2$. It is defined as:
$$D(\rho_1, \rho_2) = \frac{1}{2}\text{Tr}\left| \rho_1 - \rho_2 \right|$$
where $\left| \cdot \right|$ denotes the absolute value of a matrix.

2. The **Fidelity** is a measure of the similarity of two quantum states, $\rho_1$ and $\rho_2$. It is defined as:
$$F(\rho_1, \rho_2) = \text{Tr} \left(\sqrt{\sqrt{\rho_1} \rho_2 \sqrt{\rho_1}}\right)$$

3. The **Bures distance** is a measure of the distance between two quantum states, $\rho_1$ and $\rho_2$. It is defined as:
$$D_B(\rho_1, \rho_2) = \sqrt{2-2F(\rho_1, \rho_2)}$$

4. The **Hilbert-Schmidt distance** is a measure of the distance between two quantum states, $\rho_1$ and $\rho_2$. It is defined as:
$$D_{HS}(\rho_1, \rho_2) = \sqrt{\text{Tr}\left(\left(\rho_1 - \rho_2\right)^2\right)}$$