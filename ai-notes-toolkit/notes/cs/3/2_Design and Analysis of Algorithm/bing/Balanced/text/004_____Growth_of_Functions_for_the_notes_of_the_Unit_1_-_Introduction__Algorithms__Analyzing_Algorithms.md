### Growth of Functions

- Growth of functions is a concept that helps us to compare the efficiency of different algorithms based on their running time or space requirements as a function of the input size.
- Growth of functions is also useful for describing the asymptotic behavior of algorithms, that is, how they perform in the limit of large inputs.
- Growth of functions can be expressed using different notations, such as big O, big Omega, big Theta, little o, and little omega. These notations capture the order of magnitude, the lower bound, the tight bound, the upper bound, and the strict upper bound of a function, respectively.
- Growth of functions can be classified into different classes, such as constant, logarithmic, linear, polynomial, exponential, and factorial. These classes represent the common patterns of how the running time or space requirements of an algorithm grow with the input size.
- Growth of functions can be compared using some basic rules, such as:

  - If f(n) and g(n) are two functions, then f(n) + g(n) is O(max(f(n), g(n))).
  - If f(n) and g(n) are two functions, then f(n) * g(n) is O(f(n) * g(n)).
  - If f(n) is a function and c is a constant, then c * f(n) is O(f(n)).
  - If f(n) is a function and k is a positive integer, then f(n)^k is O(f(n)^k).
  - If f(n) and g(n) are two functions, then f(g(n)) is O(f(n)) if g(n) is O(n).

- Growth of functions can be analyzed using some common techniques, such as:

  - The loop rule: If a loop runs for n iterations and each iteration takes O(f(n)) time, then the loop takes O(n * f(n)) time.
  - The recursion rule: If a recursive function calls itself a times with input size n/b, and each call takes O(f(n)) time, then the recursive function takes O(f(n) + a * T(n/b)) time, where T(n) is the time complexity of the function.
  - The master theorem: If a recursive function calls itself a times with input size n/b, and each call takes O(f(n)) time, where f(n) is asymptotically positive, then the recursive function takes O(n^log_b(a) * f(n)) time if f(n) is O(n^log_b(a)), O(f(n)) time if f(n) is O(n^log_b(a) / log n), and O(n^log_b(a)) time if f(n) is O(n^log_b(a) / polylog n), where polylog n is any polynomial function of log n.