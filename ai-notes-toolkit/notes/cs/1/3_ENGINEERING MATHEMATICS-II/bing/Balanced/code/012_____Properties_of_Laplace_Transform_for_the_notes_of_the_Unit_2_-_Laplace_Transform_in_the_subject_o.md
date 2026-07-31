Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some properties of Laplace transform for the notes of the Unit 2 - Laplace Transform in the subject of Engineering Mathematics-II.

### Properties of Laplace Transform

- Laplace transform is a linear operator, which means that if `f(t)` and `g(t)` are two functions and `a` and `b` are two constants, then

```
L{a f(t) + b g(t)} = a L{f(t)} + b L{g(t)}
```

- Laplace transform is also a one-to-one operator, which means that if `f(t)` and `g(t)` are two functions that have the same Laplace transform, then they are equal except for a finite number of points.

- Laplace transform has the property of differentiation in the `s`-domain, which means that if `f(t)` is a function and `n` is a positive integer, then

```
L{f^(n)(t)} = s^n L{f(t)} - s^(n-1) f(0) - s^(n-2) f'(0) - ... - f^(n-1)(0)
```

- Laplace transform has the property of integration in the `s`-domain, which means that if `f(t)` is a function, then

```
L{∫f(t) dt} = 1/s L{f(t)} + c/s
```

where `c` is an arbitrary constant.

- Laplace transform has the property of multiplication by `t^n`, which means that if `f(t)` is a function and `n` is a positive integer, then

```
L{t^n f(t)} = (-1)^n d^n/ds^n L{f(t)}
```

- Laplace transform has the property of division by `t`, which means that if `f(t)` is a function, then

```
L{f(t)/t} = ∫s^∞ L{f(u)} du
```

- Laplace transform has the property of shifting in the `t`-domain, which means that if `f(t)` is a function and `a` is a positive constant, then

```
L{f(t-a) u(t-a)} = e^(-as) L{f(t)}
```

where `u(t)` is the unit step function.

- Laplace transform has the property of shifting in the `s`-domain, which means that if `f(t)` is a function and `a` is a constant, then

```
L{e^(at) f(t)} = L{f(t)} | s -> s-a
```

- Laplace transform has the property of scaling in the `t`-domain, which means that if `f(t)` is a function and `a` is a positive constant, then

```
L{f(at)} = 1/a L{f(t)} | s -> s/a
```

- Laplace transform has the property of scaling in the `s`-domain, which means that if `f(t)` is a function and `a` is a positive constant, then

```
L{f(t)/a} = L{f(t)} | s -> as
```

- Laplace transform has the property of convolution, which means that if `f(t)` and `g(t)` are two functions, then

```
L{f(t) * g(t)} = L{f(t)} L{g(t)}
```

where `*` denotes the convolution operation.