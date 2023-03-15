Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of change of order of integration.

### Change of order of integration

- Sometimes, it is easier to evaluate a double integral by changing the order of integration.
- The order of integration is the sequence in which we integrate with respect to the variables.
- For example, if we have a double integral of the form $\int_a^b \int_{g_1(x)}^{g_2(x)} f(x,y) dy dx$, the order of integration is $dy dx$, meaning we integrate with respect to $y$ first, then with respect to $x$.
- To change the order of integration, we need to find the equivalent limits of integration for the other order, which is $dx dy$ in this case.
- To do this, we need to sketch the region of integration in the $xy$-plane, and identify the curves that bound the region.
- Then, we need to express the curves as functions of $y$, instead of $x$, and find the values of $y$ that span the region.
- The new limits of integration will be $\int_c^d \int_{h_1(y)}^{h_2(y)} f(x,y) dx dy$, where $c$ and $d$ are the minimum and maximum values of $y$, and $h_1(y)$ and $h_2(y)$ are the functions of $y$ that bound the region.
- The value of the double integral will be the same regardless of the order of integration, as long as the region of integration is the same.
- Here is an example of changing the order of integration:

![Example of changing the order of integration](https://i.imgur.com/9X8wW0a.png)

- The original double integral is $\int_0^2 \int_{x/2}^x e^{y^2} dy dx$, with the order of integration $dy dx$.
- The region of integration is bounded by the curves $y=x/2$, $y=x$, $x=0$, and $x=2$.
- To change the order of integration to $dx dy$, we need to express the curves as functions of $y$, and find the values of $y$ that span the region.
- The curves $y=x/2$ and $y=x$ can be rewritten as $x=2y$ and $x=y$, respectively.
- The values of $y$ that span the region are from $0$ to $2$.
- The new limits of integration are $\int_0^2 \int_{2y}^y e^{y^2} dx dy$, with the order of integration $dx dy$.
- The value of the double integral is the same for both orders of integration, which is $\frac{1}{2}(e^4 - 1)$.