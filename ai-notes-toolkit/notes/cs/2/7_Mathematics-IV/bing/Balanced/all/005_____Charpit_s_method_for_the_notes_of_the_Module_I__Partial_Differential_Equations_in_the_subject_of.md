# Charpit's Method

Charpit's method is a general method for finding the complete solution of nonlinear partial differential equation of the first order of the form

$$f(x,y,z,p,q) = 0$$

where $p = \frac{\partial z}{\partial x}$ and $q = \frac{\partial z}{\partial y}$ are the partial derivatives of $z$ with respect to $x$ and $y$ respectively.

The main steps of Charpit's method are:

- Assume that there exists a function $\phi(x,y,z,p,q) = 0$ that defines the solution surface $z = z(x,y)$ implicitly.
- Differentiate $\phi$ with respect to $x$ and $y$ and equate them to $p$ and $q$ respectively, i.e.

$$\frac{\partial \phi}{\partial x} = p \frac{\partial \phi}{\partial z}$$

$$\frac{\partial \phi}{\partial y} = q \frac{\partial \phi}{\partial z}$$

- Eliminate $\frac{\partial \phi}{\partial z}$ from the above equations and obtain

$$\frac{dx}{p} = \frac{dy}{q} = \frac{dz}{p \frac{\partial \phi}{\partial p} + q \frac{\partial \phi}{\partial q}}$$

- These are called the Charpit's equations. They are a system of ordinary differential equations that can be solved to obtain $x$, $y$, $z$, $p$ and $q$ in terms of two arbitrary parameters $s$ and $t$.
- Substitute the expressions for $p$ and $q$ in terms of $s$ and $t$ into the original equation $f(x,y,z,p,q) = 0$ and obtain a relation between $s$ and $t$, i.e.

$$F(s,t) = 0$$

- This is called the complete integral of the partial differential equation. It contains two arbitrary constants of integration, which can be chosen as $s$ and $t$.
- To find the particular integral, we need to impose two conditions on $s$ and $t$, such as

$$s = g(x,y)$$

$$t = h(x,y)$$

where $g$ and $h$ are given functions of $x$ and $y$.

- Substitute these conditions into the complete integral and obtain the particular integral, i.e.

$$z = Z(x,y)$$

where $Z$ is a function of $x$ and $y$ obtained by eliminating $s$ and $t$ from $F(s,t) = 0$, $s = g(x,y)$ and $t = h(x,y)$.