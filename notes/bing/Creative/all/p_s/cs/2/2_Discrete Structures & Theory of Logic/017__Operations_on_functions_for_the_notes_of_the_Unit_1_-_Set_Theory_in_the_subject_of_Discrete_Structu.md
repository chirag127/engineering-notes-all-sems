### Operations on functions

- A function is a rule that assigns to each element of a set, called the domain, exactly one element of another set, called the codomain.
- Operations on functions are ways of combining functions to create new functions, such as addition, subtraction, multiplication, division, and composition.
- If f and g are two functions with overlapping domains, then the sum, difference, product, and quotient of f and g are defined as follows:

  - (f + g)(x) = f(x) + g(x)
  - (f - g)(x) = f(x) - g(x)
  - (f * g)(x) = f(x) * g(x)
  - (f / g)(x) = f(x) / g(x), g(x) ≠ 0

- For example, if f(x) = x^2 and g(x) = 2x + 1, then

  - (f + g)(x) = x^2 + 2x + 1
  - (f - g)(x) = x^2 - 2x - 1
  - (f * g)(x) = 2x^3 + x^2
  - (f / g)(x) = x / (2x + 1), x ≠ -1/2

- The composition of two functions f and g, written as g ∘ f, is a function that maps an element x in the domain of f to the element g(f(x)) in the codomain of g.
- For example, if f(x) = x + 1 and g(x) = x^2, then

  - (g ∘ f)(x) = g(f(x)) = (x + 1)^2
  - (f ∘ g)(x) = f(g(x)) = x^2 + 1

- Note that the composition of functions is not commutative, that is, g ∘ f ≠ f ∘ g in general.
- Some properties of functions that are useful to know are:

  - A function f is one-to-one (or injective) if different elements in the domain map to different elements in the codomain, that is, f(x) = f(y) implies x = y.
  - A function f is onto (or surjective) if every element in the codomain is mapped by some element in the domain, that is, for every y in the codomain, there exists x in the domain such that f(x) = y.
  - A function f is bijective if it is both one-to-one and onto, that is, it is a one-to-one correspondence between the domain and the codomain.
  - The inverse of a bijective function f, written as f^-1, is a function that maps an element y in the codomain of f to the element x in the domain of f such that f(x) = y, that is, f^-1(f(x)) = x and f(f^-1(y)) = y.
  - For example, if f(x) = 2x + 1, then f is a bijective function with inverse f^-1(x) = (x - 1) / 2.

- Functions are important in discrete mathematics because they can be used to model various phenomena, such as the computational complexity of algorithms, the counting of objects, the study of sequences and strings, and so on.

Some possible mnemonics and learning tricks for the topic are:

- To remember the order of composition of functions, use the acronym FOG, which stands for First Outer, then Inner, then G, that is, (g ∘ f)(x) = g(f(x)).
- To remember the definition of a bijective function, use the acronym BOI, which stands for Both One-to-one and Onto, or Injective and Surjective.
- To remember the formula for the inverse of a function, use the acronym SWAP, which stands for Switch x and y, then solve for y. For example, if f(x) = 2x + 1, then to find f^-1(x), we swap x and y and get x = 2y + 1, then solve for y and get y = (x - 1) / 2, which is f^-1(x).