### Introduction to Recursive Function Theory

- Recursive function theory is a branch of mathematical logic that studies the properties and limitations of computable functions on natural numbers.
- A function is computable if there is an effective method or algorithm to compute its value for any given input. For example, the factorial function `n! = n * (n-1) * ... * 1` is computable because there is a simple algorithm to calculate it using repeated multiplication.
- There are different models of computation that can be used to define computable functions, such as Turing machines, lambda calculus, register machines, etc. These models are equivalent in the sense that they can compute exactly the same class of functions, which are called the recursive functions or the computable functions .
- A recursive function can be defined in two ways: by primitive recursion or by general recursion .
  - Primitive recursion is a form of recursion that uses only basic arithmetic operations and a special function called the zero function, which returns zero for any input. A function is primitive recursive if it can be obtained from the zero function and the successor function (which adds one to its input) by applying composition and primitive recursion. Composition means applying one function to the result of another function, and primitive recursion means defining a function by specifying its value for zero and its value for the successor of any input. For example, the factorial function can be defined by primitive recursion as follows:

    ```
    f(0) = 1
    f(n+1) = (n+1) * f(n)
    ```

  - General recursion is a form of recursion that allows the use of an additional function called the minimization function, which returns the smallest natural number that satisfies a given condition. A function is general recursive if it can be obtained from the zero function, the successor function, and the minimization function by applying composition and primitive recursion. For example, the function that returns the greatest common divisor of two numbers can be defined by general recursion as follows:

    ```
    g(0, y) = y
    g(x, 0) = x
    g(x, y) = g(y, x mod y)
    h(x, y) = μz. (g(x, y) = z)
    ```

    where `μz` means the minimization function and `mod` means the remainder operation.

- The class of recursive functions is closed under composition and primitive recursion, meaning that applying these operations to recursive functions always results in another recursive function. However, the class of recursive functions is not closed under general recursion, meaning that applying the minimization function to recursive functions may result in a non-recursive function .
- A function is called total recursive if it is defined for every input, or equivalently, if it can be computed by a Turing machine that always halts. A function is called partial recursive if it is defined for some inputs, but may be undefined for others, or equivalently, if it can be computed by a Turing machine that may not halt. The class of total recursive functions is a proper subset of the class of partial recursive functions, which is a proper subset of the class of recursive functions .
- There is no effective method to decide whether a given recursive function is total or partial, or whether a given partial recursive function is defined for a given input. These problems are undecidable, meaning that there is no recursive function that can solve them. This is related to the famous halting problem, which asks whether there is a recursive function that can determine whether a given Turing machine halts on a given input. The halting problem is also undecidable, and in fact, it is equivalent to many other undecidable problems in recursive function theory and computability theory .
- Recursive function theory also studies the structure and properties of the recursively enumerable sets, which are the sets of natural numbers that can be enumerated by a recursive function. For example, the set of prime numbers is recursively enumerable, because there is a recursive function that can generate all the prime numbers in some order. A set is called recursive or decidable if there is a recursive function that can decide whether a given number belongs to the set or not. For example, the set of even numbers is recursive, because there is a recursive function that can check whether a given number is divisible by two or not. The class of recursive sets is a proper subset of the class of recursively enumerable sets, and there are