# CO-5 Estimate the rate constant of reaction K3

- The rate constant of a reaction is a proportionality factor that relates the reaction rate to the concentrations of the reactants.
- The rate constant depends on the temperature, the activation energy, and the frequency factor of the reaction.
- The rate constant can have different units depending on the order of the reaction.
- For a termolecular reaction, such as A + B + C → products, the reaction rate is described by r = k3[A][B][C], where k3 is a termolecular rate constant.
- To estimate the rate constant of a termolecular reaction, one can use the Arrhenius equation: k3 = A3 exp(-Ea3/RT), where A3 is the frequency factor, Ea3 is the activation energy, R is the gas constant, and T is the temperature.
- Alternatively, one can use experimental data to plot the natural logarithm of the rate constant versus the inverse of the temperature, and obtain the slope and the intercept of the linear regression. The slope is equal to -Ea3/R and the intercept is equal to ln(A3).
- For example, a reaction takes place in three steps with an individual rate constant and activation energy, as given below :

| Step | Rate constant | Activation energy |
|------|---------------|-------------------|
| 1    | k1            | Ea1 = 180 kJ/mol  |
| 2    | k2            | Ea2 = 80 kJ/mol   |
| 3    | k3            | Ea3 = 50 kJ/mol   |

- The overall rate constant k is given by k = k2k1k3.
- If the temperature is 300 K, the frequency factors are A1 = 10^13 s^-1, A2 = 10^9 L/mol s, and A3 = 10^6 L^2/mol^2 s, then the rate constant of the third step can be estimated as:

k3 = A3 exp(-Ea3/RT) = 10^6 L^2/mol^2 s * exp(-50000 J/mol / 8.314 J/mol K * 300 K) = 0.0036 L^2/mol^2 s