Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn or discuss. You have asked me to write the content on the topic of change of variables for the notes of the Unit 2 - Differential Calculus- I in the subject of Engineering Mathematics-I. Here is the content I have written in markdown format:

### Change of variables

- Change of variables is a technique that allows us to transform a complicated function or integral into a simpler one by using a suitable substitution.
- The idea is to replace the original variable(s) with new variable(s) that are related by some function(s).
- The advantage of change of variables is that it can simplify the algebraic expressions, the limits of integration, or the integrand itself.
- Change of variables can be applied to functions of one variable or functions of several variables.
- For functions of one variable, change of variables is also known as u-substitution or integration by substitution. The general formula is:

$$\int f(g(x))g'(x)dx = \int f(u)du$$

where $u = g(x)$ and $du = g'(x)dx$.

- For functions of several variables, change of variables is also known as coordinate transformation or Jacobian substitution. The general formula is:

$$\int_{R} f(x,y) dxdy = \int_{S} f(g(u,v),h(u,v)) \left| \frac{\partial (x,y)}{\partial (u,v)} \right| dudv$$

where $(x,y) = (g(u,v),h(u,v))$ and $\left| \frac{\partial (x,y)}{\partial (u,v)} \right|$ is the absolute value of the determinant of the Jacobian matrix of the transformation.

- Some common examples of change of variables are:

  - Polar coordinates: $(x,y) = (r\cos \theta, r\sin \theta)$ and $\left| \frac{\partial (x,y)}{\partial (r,\theta)} \right| = r$.
  - Cylindrical coordinates: $(x,y,z) = (r\cos \theta, r\sin \theta, z)$ and $\left| \frac{\partial (x,y,z)}{\partial (r,\theta,z)} \right| = r$.
  - Spherical coordinates: $(x,y,z) = (\rho \sin \phi \cos \theta, \rho \sin \phi \sin \theta, \rho \cos \phi)$ and $\left| \frac{\partial (x,y,z)}{\partial (\rho,\phi,\theta)} \right| = \rho^2 \sin \phi$.
  - Exponential substitution: $x = e^u$ and $dx = e^u du$.
  - Trigonometric substitution: $x = \sin u$, $x = \cos u$, or $x = \tan u$ and $dx = \cos u du$, $dx = -\sin u du$, or $dx = \sec^2 u du$, respectively.