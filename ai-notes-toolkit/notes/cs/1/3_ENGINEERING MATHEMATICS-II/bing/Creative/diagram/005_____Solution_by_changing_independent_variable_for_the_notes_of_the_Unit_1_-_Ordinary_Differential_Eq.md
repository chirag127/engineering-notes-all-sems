### Solution by changing independent variable for the notes of the Unit 1 - Ordinary Differential Equation of Higher Order in the subject of ENGINEERING MATHEMATICS-II

- A differential equation is an equation that relates a function and its derivatives.
- The order of a differential equation is the highest order of the derivative that appears in the equation .
- A linear differential equation is one that can be written in the form L(y) = g(t), where L is a linear operator and g is a given function.
- A homogeneous linear differential equation is one that has g(t) = 0.
- A solution of a differential equation is a function that satisfies the equation.
- To solve a differential equation, we need to find a general solution that contains arbitrary constants, and then use initial or boundary conditions to find a particular solution that fits the given situation.
- Sometimes, it is convenient to change the independent variable in a differential equation to simplify the equation or to match the physical context.
- For example, if we have a differential equation of the form y'' + p(t)y' + q(t)y = 0, where p and q are functions of t, we can change the independent variable to x = f(t), where f is a given function, and obtain a new differential equation of the form y'' + P(x)y' + Q(x)y = 0, where P and Q are functions of x.
- To do this, we need to use the chain rule and the inverse function theorem to express the derivatives of y with respect to t in terms of the derivatives of y with respect to x.
- For example, if x = f(t), then dx/dt = f'(t) and dt/dx = 1/f'(t). Therefore, dy/dt = (dy/dx)(dx/dt) = f'(t)dy/dx and d^2y/dt^2 = (d/dt)(dy/dt) = (d/dt)(f'(t)dy/dx) = f''(t)dy/dx + f'(t)d^2y/dx^2.
- By substituting these expressions into the original differential equation, we can obtain a new differential equation in terms of x and y.
- The advantage of changing the independent variable is that we may be able to reduce the order of the differential equation, or to transform it into a standard form that can be solved by known methods.
- For example, if we have a differential equation of the form y'' + y = 0, we can change the independent variable to x = sin(t) and obtain a new differential equation of the form y'' + y = 0, which is a first order differential equation that can be solved by separation of variables.
- Another example is if we have a differential equation of the form y'' + 2y' + y = 0, we can change the independent variable to x = e^t and obtain a new differential equation of the form y'' + y = 0, which is a second order differential equation with constant coefficients that can be solved by the characteristic equation method.
- To find the solution of the original differential equation, we need to substitute back the original independent variable in terms of the new independent variable.
- For example, if we have a solution of the form y = c1cos(x) + c2sin(x) for the differential equation y'' + y = 0, where x = sin(t), we can substitute x = sin(t) and obtain a solution of the form y = c1cos(sin(t)) + c2sin(sin(t)) for the differential equation y'' + y = 0, where t is the original independent variable.
- Another example is if we have a solution of the form y = c1e^x + c2e^-x for the differential equation y'' + y = 0, where x = e^t, we can substitute x = e^t and obtain a solution of the form y = c1e^e^t + c2e^-e^t for the differential equation y'' + 2y' + y = 0, where t is the original independent variable.
- In summary, changing the independent variable in a differential equation can be a useful technique to simplify the equation or to match the physical context, but we