Hello, I am Sydney, your AI assistant. I can help you with your study material for Engineering Mathematics-I. Here is the content for the topic of change of order of integration for the notes of Unit 4 - Multiple integration.

# Change of order of integration

- Sometimes, it is easier to evaluate a double integral by changing the order of integration.
- The order of integration is the sequence in which we integrate with respect to the variables.
- For example, the order of integration for $\int_{a}^{b} \int_{c}^{d} f(x,y) dy dx$ is first with respect to $y$ and then with respect to $x$.
- To change the order of integration, we need to find the new limits of integration for each variable in terms of the other variable.
- The new limits of integration should cover the same region of integration as the original one.
- The region of integration can be represented by a graph or an equation in the $xy$-plane.
- There are two common cases of changing the order of integration:

## Case 1: The region of integration is bounded by two curves

- If the region of integration is bounded by two curves $y=g_1(x)$ and $y=g_2(x)$, where $g_1(x) \leq g_2(x)$ for $a \leq x \leq b$, then the order of integration can be changed as follows:

$$\int_{a}^{b} \int_{g_1(x)}^{g_2(x)} f(x,y) dy dx = \int_{c}^{d} \int_{h_1(y)}^{h_2(y)} f(x,y) dx dy$$

- where $c$ and $d$ are the minimum and maximum values of $y$ in the region, and $h_1(y)$ and $h_2(y)$ are the inverse functions of $g_1(x)$ and $g_2(x)$, respectively.
- For example, consider the following double integral:

$$\int_{0}^{1} \int_{x^2}^{x} e^{y^3} dy dx$$

- The region of integration is bounded by the curves $y=x^2$ and $y=x$ for $0 \leq x \leq 1$, as shown in the graph below:

![region1](region1.png)

- To change the order of integration, we need to find the new limits of integration for $x$ in terms of $y$.
- The minimum and maximum values of $y$ in the region are $0$ and $1$, respectively.
- The inverse functions of $y=x^2$ and $y=x$ are $x=\sqrt{y}$ and $x=y$, respectively.
- Therefore, the new order of integration is:

$$\int_{0}^{1} \int_{x^2}^{x} e^{y^3} dy dx = \int_{0}^{1} \int_{\sqrt{y}}^{y} e^{y^3} dx dy$$

## Case 2: The region of integration is bounded by two curves

- If the region of integration is bounded by two curves $x=h_1(y)$ and $x=h_2(y)$, where $h_1(y) \leq h_2(y)$ for $c \leq y \leq d$, then the order of integration can be changed as follows:

$$\int_{c}^{d} \int_{h_1(y)}^{h_2(y)} f(x,y) dx dy = \int_{a}^{b} \int_{g_1(x)}^{g_2(x)} f(x,y) dy dx$$

- where $a$ and $b$ are the minimum and maximum values of $x$ in the region, and $g_1(x)$ and $g_2(x)$ are the inverse functions of $h_1(y)$ and $h_2(y)$, respectively.
- For example, consider the following double integral:

$$\int_{0}^{2} \int_{y}^{2y} \sin(x^2) dx dy$$

- The region of integration is bounded by the curves $x=y$ and $x=2y$ for $0 \leq y \leq 2$, as shown in the graph below:

![region2](region2.png)

- To change the order of integration, we need to find the new limits of integration for $y$ in terms of $x$.
- The minimum and maximum values of $x$