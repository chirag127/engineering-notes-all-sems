Hello, I am Sydney, your AI assistant. I can help you with your study material for Engineering Mathematics-I. Here is the content for the topic of change of order of integration in the unit of multiple integration.

### Change of order of integration

- Sometimes, it is easier to evaluate a double integral by changing the order of integration.
- The order of integration is the sequence in which we integrate with respect to the variables.
- For example, if we have a double integral of the form

```
\int_a^b \int_{g_1(x)}^{g_2(x)} f(x,y) dy dx
```

- The order of integration is `dy dx`, which means we integrate first with respect to `y` and then with respect to `x`.
- To change the order of integration, we need to find the new limits of integration for the variables, and rewrite the integral in the form

```
\int_c^d \int_{h_1(y)}^{h_2(y)} f(x,y) dx dy
```

- The order of integration is now `dx dy`, which means we integrate first with respect to `x` and then with respect to `y`.
- To find the new limits of integration, we need to sketch the region of integration in the `xy`-plane, and identify the curves that bound the region.
- The curves that bound the region are given by the equations `y = g_1(x)`, `y = g_2(x)`, `x = a`, and `x = b`.
- To change the order of integration, we need to express `x` as a function of `y` for the curves that bound the region in the `x`-direction.
- The curves that bound the region in the `x`-direction are given by the equations `x = h_1(y)` and `x = h_2(y)`, where `h_1(y)` and `h_2(y)` are the inverse functions of `g_1(x)` and `g_2(x)`, respectively.
- The limits of integration for `y` are given by the minimum and maximum values of `y` in the region, which are `c` and `d`, respectively.
- The limits of integration for `x` are given by the functions `h_1(y)` and `h_2(y)`, which depend on `y`.
- The following diagram illustrates the change of order of integration for a double integral.

![change of order of integration](https://i.imgur.com/9Z8gZx9.png)

- In the diagram, the region of integration is shaded in blue, and the curves that bound the region are labeled.
- The original order of integration is `dy dx`, and the new order of integration is `dx dy`.
- The limits of integration for the original order are `a`, `b`, `g_1(x)`, and `g_2(x)`, and the limits of integration for the new order are `c`, `d`, `h_1(y)`, and `h_2(y)`.
- Note that the region of integration is the same for both orders, but the way we slice the region into subregions is different.
- For the original order, we slice the region into vertical strips, and for the new order, we slice the region into horizontal strips.
- The area of each subregion is the same for both orders, but the shape and orientation of the subregions may vary.
- The function `f(x,y)` is the same for both orders, but the order in which we evaluate the function may vary.
- The value of the double integral is the same for both orders, but the method of calculation may vary.