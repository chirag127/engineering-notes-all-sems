### Solution by changing independent variable for the notes of the Unit 1 - Ordinary Differential Equation of Higher Order in the subject of ENGINEERING MATHEMATICS-II

- Sometimes, it is possible to simplify a differential equation by changing the independent variable to a new one.
- This method is useful when the differential equation contains a function of the independent variable only, such as $x$, $y$, or $z$.
- The general procedure is as follows:
  - Let the new independent variable be $p$, and express the old independent variable in terms of $p$.
  - Find the relation between the derivatives of the dependent variable with respect to the old and new independent variables, using the chain rule.
  - Substitute the new independent variable and the derivatives in the original differential equation, and simplify the resulting equation.
  - Solve the new differential equation for the dependent variable in terms of the new independent variable.
  - Express the solution in terms of the old independent variable, using the inverse relation between $p$ and the old independent variable.

- For example, consider the differential equation
$$
y'' + \frac{2}{x}y' + y = 0
$$
- This equation contains a function of $x$ only, so we can try to change the independent variable to $p = \ln x$.
- Then, we have $x = e^p$, and by the chain rule, we get
$$
\frac{dy}{dx} = \frac{dy}{dp} \frac{dp}{dx} = \frac{dy}{dp} \frac{1}{x} = \frac{dy}{dp} e^{-p}
$$
and
$$
\frac{d^2y}{dx^2} = \frac{d}{dx} \left( \frac{dy}{dp} e^{-p} \right) = \frac{d}{dp} \left( \frac{dy}{dp} e^{-p} \right) \frac{dp}{dx} = \left( \frac{d^2y}{dp^2} e^{-p} - \frac{dy}{dp} e^{-p} \right) \frac{1}{x} = \left( \frac{d^2y}{dp^2} - \frac{dy}{dp} \right) e^{-2p}
$$
- Substituting these expressions in the original differential equation, we get
$$
\left( \frac{d^2y}{dp^2} - \frac{dy}{dp} \right) e^{-2p} + \frac{2}{x} \frac{dy}{dp} e^{-p} + y = 0
$$
- Simplifying, we obtain
$$
\frac{d^2y}{dp^2} - \frac{dy}{dp} + 2 \frac{dy}{dp} + y = 0
$$
or
$$
\frac{d^2y}{dp^2} + \frac{dy}{dp} + y = 0
$$
- This is a second-order linear differential equation with constant coefficients, which can be solved by the method of characteristic equation.
- The characteristic equation is
$$
r^2 + r + 1 = 0
$$
which has complex roots
$$
r = -\frac{1}{2} \pm \frac{\sqrt{3}}{2} i
$$
- Therefore, the general solution of the new differential equation is
$$
y = e^{-\frac{p}{2}} \left( c_1 \cos \frac{\sqrt{3}}{2} p + c_2 \sin \frac{\sqrt{3}}{2} p \right)
$$
where $c_1$ and $c_2$ are arbitrary constants.
- To express the solution in terms of the old independent variable, we use the inverse relation $p = \ln x$, and get
$$
y = e^{-\frac{\ln x}{2}} \left( c_1 \cos \frac{\sqrt{3}}{2} \ln x + c_2 \sin \frac{\sqrt{3}}{2} \ln x \right)
$$
or
$$
y = x^{-\frac{1}{2}} \left( c_1 \cos \frac{\sqrt{3}}{2} \ln x + c_2 \sin \frac{\sqrt{3}}{2} \ln x \right)
$$
- This is the general solution of the original differential equation in terms of $x$.