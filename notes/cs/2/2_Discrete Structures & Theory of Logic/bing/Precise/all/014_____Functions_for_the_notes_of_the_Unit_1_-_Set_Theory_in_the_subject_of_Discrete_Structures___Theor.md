# Functions

A function is a relation between two sets that associates each element of the first set with exactly one element of the second set. The first set is called the domain, and the second set is called the codomain. The set of all possible outputs of a function is called its range.

- **Definition:** A function `f` from a set `A` to a set `B` is a rule that assigns to each element `x` in `A` exactly one element `f(x)` in `B`. We write `f: A -> B` to indicate that `f` is a function from `A` to `B`.

- **Domain:** The domain of a function `f` is the set of all possible inputs to the function. It is denoted by `Dom(f)`.

- **Codomain:** The codomain of a function `f` is the set of all possible outputs of the function. It is denoted by `Cod(f)`.

- **Range:** The range of a function `f` is the set of all actual outputs of the function. It is denoted by `Ran(f)`.

- **One-to-one function:** A function `f` is said to be one-to-one (or injective) if different elements in the domain have different images in the codomain. In other words, if `f(x) = f(y)` for some `x` and `y` in the domain, then `x = y`.

- **Onto function:** A function `f` is said to be onto (or surjective) if every element in the codomain has a preimage in the domain. In other words, for every `y` in the codomain, there exists an `x` in the domain such that `f(x) = y`.

- **Bijective function:** A function `f` is said to be bijective if it is both one-to-one and onto. A bijective function has an inverse function, which is also a bijection.

- **Inverse function:** The inverse function of a bijective function `f` is a function `f^(-1)` such that `f^(-1)(f(x)) = x` for all `x` in the domain of `f`, and `f(f^(-1)(y)) = y` for all `y` in the codomain of `f`.

- **Composition of functions:** The composition of two functions `f` and `g` is a new function `g o f` defined by `(g o f)(x) = g(f(x))` for all `x` in the domain of `f`. The domain of `g o f` is the set of all `x` in the domain of `f` such that `f(x)` is in the domain of `g`.
