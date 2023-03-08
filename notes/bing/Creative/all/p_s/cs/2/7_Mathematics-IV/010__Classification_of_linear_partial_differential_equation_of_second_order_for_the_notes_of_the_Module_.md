### Classification of linear partial differential equation of second order

A linear partial differential equation (PDE) of second order is an equation of the form

$$a(x,y)u_{xx} + 2b(x,y)u_{xy} + c(x,y)u_{yy} + d(x,y)u_{x} + e(x,y)u_{y} + f(x,y)u = g(x,y)$$

where $u$ is the unknown function of $x$ and $y$, and $a,b,c,d,e,f,g$ are given functions of $x$ and $y$. The coefficients $a,b,c$ determine the type of the PDE, which can be classified into three categories:

- **Elliptic PDE**: If $b^2 - ac < 0$, the PDE is elliptic. This means that the solutions of the PDE are smooth and have no singularities. Examples of elliptic PDEs are Laplace's equation and Poisson's equation, which model steady-state phenomena such as heat conduction and electrostatics.

- **Parabolic PDE**: If $b^2 - ac = 0$, the PDE is parabolic. This means that the solutions of the PDE are smooth in one direction and have singularities in the other direction. Examples of parabolic PDEs are the heat equation and the diffusion equation, which model transient phenomena such as heat transfer and diffusion of substances.

- **Hyperbolic PDE**: If $b^2 - ac > 0$, the PDE is hyperbolic. This means that the solutions of the PDE have singularities in both directions and propagate along characteristic curves. Examples of hyperbolic PDEs are the wave equation and the transport equation, which model wave phenomena such as sound and light.

The classification of a linear PDE of second order can be visualized by considering the equation

$$au_{xx} + 2bu_{xy} + cu_{yy} = 0$$

and making a change of variables

$$\xi = x + \lambda y, \quad \eta = x - \lambda y$$

where $\lambda$ is a constant. Then, the equation becomes

$$(a - b\lambda + c\lambda^2)u_{\xi\xi} + (a + b\lambda + c\lambda^2)u_{\eta\eta} = 0$$

The coefficients of this equation depend on the choice of $\lambda$. If we can find a value of $\lambda$ that makes one of the coefficients zero, then the equation reduces to a first-order PDE. This value of $\lambda$ is called a **characteristic value**, and the corresponding curve $\xi = x + \lambda y = \text{constant}$ is called a **characteristic curve**. The characteristic values are the roots of the equation

$$a - b\lambda + c\lambda^2 = 0$$

which is a quadratic equation with discriminant $b^2 - ac$. Depending on the sign of the discriminant, we have three cases:

- If $b^2 - ac < 0$, the equation has no real roots, and the PDE is elliptic. There are no characteristic curves, and the solutions are smooth in all directions.

- If $b^2 - ac = 0$, the equation has one repeated root, and the PDE is parabolic. There is one family of characteristic curves, and the solutions are smooth in one direction and have singularities in the other direction.

- If $b^2 - ac > 0$, the equation has two distinct real roots, and the PDE is hyperbolic. There are two families of characteristic curves, and the solutions have singularities in both directions and propagate along these curves.

Mnemonics are memory tricks that can help you remember new information by connecting it to something you already know. There are different types of mnemonics, such as rhymes, acronyms, diagrams, or images. For example, you can use the acronym HOMES to remember the names of the Great Lakes: Huron, Ontario, Michigan, Erie, and Superior. Or you can use the rhyme "Thirty days hath September, April, June, and November" to remember how many days are in each month.

Some tips for using mnemonics are:

- Choose the right mnemonic for your situation. For example, if you want to learn how to spell a word, you can use a spelling mnemonic, such as "i before e except after c".
- Practice the mnemonic several times to help you remember it. You can write it down, say it out loud, or quiz yourself on it.
- Repeat the mnemonic to others or teach it to someone else. This can help you reinforce the information and check your understanding.
- Use mnemonics that are funny, creative, or exaggerated. These are easier to remember than boring or plain ones. For example, you can use the sentence "My very eager mother just served us nine pizzas" to remember the order of the planets: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, and Pluto.