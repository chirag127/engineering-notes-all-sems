### Double integral

- A double integral is a way to integrate over a two-dimensional area. It can be used to find the volume under a surface, the area of a region, the average value of a function, and other applications.
- A double integral of a function of two variables, say f(x,y), over a region R in the xy-plane is denoted by:

```
∬R f(x,y) dA
```

- where dA is a small element of area in the region R. The double integral can be interpreted as the sum of the values of f(x,y) times the area dA over the region R.
- A double integral can be evaluated by iterated integration, which means integrating first with respect to one variable and then with respect to the other variable. For example, if R is a rectangular region with boundaries a ≤ x ≤ b and c ≤ y ≤ d, then the double integral can be written as:

```
∬R f(x,y) dA = ∫c^d ∫a^b f(x,y) dx dy = ∫a^b ∫c^d f(x,y) dy dx
```

- The order of integration can be changed if the region R is simple enough. The limits of integration must be adjusted accordingly to match the region R.
- A double integral can also be evaluated by changing to polar coordinates, which are more suitable for regions that are circular or symmetric about the origin. The polar coordinates of a point (x,y) are given by:

```
x = r cos θ
y = r sin θ
```

- where r is the distance from the origin and θ is the angle measured from the positive x-axis. The element of area in polar coordinates is given by:

```
dA = r dr dθ
```

- The double integral in polar coordinates can be written as:

```
∬R f(x,y) dA = ∬R f(r cos θ, r sin θ) r dr dθ
```

- The limits of integration for r and θ depend on the shape of the region R.