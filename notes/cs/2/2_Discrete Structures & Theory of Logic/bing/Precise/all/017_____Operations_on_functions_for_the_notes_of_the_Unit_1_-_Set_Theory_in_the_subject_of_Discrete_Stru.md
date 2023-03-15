# Operations on Functions

In the context of Set Theory, a function is a relation between two sets that associates every element of the first set to exactly one element of the second set. The first set is called the domain of the function, and the second set is called the codomain. The set of all possible outputs of the function is called the range.

There are several operations that can be performed on functions, including:

1. **Composition**: Given two functions `f` and `g`, the composition of `f` and `g`, denoted by `f ∘ g`, is a new function defined as `(f ∘ g)(x) = f(g(x))`. The domain of `f ∘ g` is the set of all `x` in the domain of `g` such that `g(x)` is in the domain of `f`.

2. **Inverse**: Given a function `f`, the inverse of `f`, denoted by `f^(-1)`, is a function that "undoes" the action of `f`. In other words, for every `y` in the range of `f`, `f^(-1)(y)` is the unique `x` in the domain of `f` such that `f(x) = y`. The inverse of a function exists if and only if the function is one-to-one (injective) and onto (surjective).

3. **Restriction**: Given a function `f` and a subset `A` of its domain, the restriction of `f` to `A`, denoted by `f|A`, is a new function defined as `f|A(x) = f(x)` for all `x` in `A`. The domain of `f|A` is `A`.

4. **Image**: Given a function `f` and a subset `A` of its domain, the image of `A` under `f`, denoted by `f(A)`, is the set of all `f(x)` such that `x` is in `A`. In other words, `f(A) = {f(x) | x ∈ A}`.

5. **Preimage**: Given a function `f` and a subset `B` of its codomain, the preimage of `B` under `f`, denoted by `f^(-1)(B)`, is the set of all `x` in the domain of `f` such that `f(x)` is in `B`. In other words, `f^(-1)(B) = {x | f(x) ∈ B}`.

These are some of the basic operations that can be performed on functions in the context of Set Theory. Understanding these operations is essential for further study in Discrete Structures and Theory of Logic.