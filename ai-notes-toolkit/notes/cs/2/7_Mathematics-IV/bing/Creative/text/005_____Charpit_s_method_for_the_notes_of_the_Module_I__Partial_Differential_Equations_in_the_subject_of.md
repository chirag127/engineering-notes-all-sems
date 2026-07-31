### Charpit's method

- Charpit's method is a general method for finding the complete solution of non-linear partial differential equation of the first order of the form $f(x,y,z,p,q)=0$, where $p=\frac{\partial z}{\partial x}$ and $q=\frac{\partial z}{\partial y}$ are the partial derivatives of $z$ with respect to $x$ and $y$ respectively.
- The main idea of Charpit's method is to introduce auxiliary variables $\lambda$ and $\mu$ such that $p=\frac{dx}{d\lambda}$ and $q=\frac{dy}{d\mu}$, and then to find a relation between $\lambda$ and $\mu$ that makes the equation $f(x,y,z,p,q)=0$ identically satisfied.
- The steps of Charpit's method are as follows :
  - Write the given equation in the form $f(x,y,z,p,q)=0$ and assume that $z$ is a function of $x$ and $y$.
  - Introduce the auxiliary variables $\lambda$ and $\mu$ such that $p=\frac{dx}{d\lambda}$ and $q=\frac{dy}{d\mu}$, and write the total differential of $z$ as $dz=pdx+qdy$.
  - Differentiate the given equation partially with respect to $x$, $y$, $z$, $p$, and $q$, and obtain five equations by equating the coefficients of $dx$, $dy$, $dz$, $dp$, and $dq$ to zero.
  - These five equations are called Charpit's equations, and they can be written in the form
    $$\frac{dx}{F_p}=\frac{dy}{F_q}=\frac{dz}{pF_p+qF_q}=\frac{dp}{-F_x+pF_u}=\frac{dq}{-F_y+qF_u}$$
    where $F_u=\frac{\partial F}{\partial z}$.
  - Solve Charpit's equations for $x$, $y$, $z$, $p$, and $q$ in terms of $\lambda$ and $\mu$, and eliminate $\lambda$ and $\mu$ to obtain the complete solution of the given equation.
  - If the complete solution is not obtained, find a particular solution by assigning suitable values to the arbitrary constants or functions.

- Here is an example of applying Charpit's method to solve the equation $p^2+q^2=1$:
  - The given equation is already in the form $f(x,y,z,p,q)=0$, where $f(x,y,z,p,q)=p^2+q^2-1$.
  - Introducing the auxiliary variables $\lambda$ and $\mu$ such that $p=\frac{dx}{d\lambda}$ and $q=\frac{dy}{d\mu}$, we have $dz=pdx+qdy$.
  - Differentiating the given equation partially with respect to $x$, $y$, $z$, $p$, and $q$, we obtain
    $$\begin{aligned}
    F_x&=0\\
    F_y&=0\\
    F_z&=0\\
    F_p&=2p\\
    F_q&=2q\\
    F_u&=0
    \end{aligned}$$
  - Charpit's equations are
    $$\begin{aligned}
    \frac{dx}{2p}&=\frac{dy}{2q}=\frac{dz}{2p^2+2q^2}=\frac{dp}{0}=\frac{dq}{0}
    \end{aligned}$$
  - From the last two equations, we get $dp=0$ and $dq=0$, which imply that $p$ and $q$ are constants. Since $p^2+q^2=1$, we can write $p=\cos\alpha$ and $q=\sin\alpha$, where $\alpha$ is an arbitrary constant.
  - Substituting these values of $p$ and $q$ into the first three equations, we get
    $$\begin{aligned}
    \frac{dx}{2\cos\alpha}&=\frac{dy}{2\sin\alpha}=\frac{dz}{2}\\
    \end{aligned}$$