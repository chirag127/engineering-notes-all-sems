 Here is the content in markdown format without any emojis or external links, written in a formal tone with points:

### Recursively defined functions for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

1. A function f(x) is said to be recursively defined if its definition involves the function itself.
2. A common form of recursive definition is:
f(x) = x if p(x)
f(x) = g(f(x')) if not p(x)
where x' < x and p(x) and g(x) are given conditions.
3. Examples:
a) The factorial function:
f(x) = x if x = 1
f(x) = x * f(x-1) if x > 1
b) The Fibonacci sequence:
f(x) = 1 if x = 1 or 2
f(x) = f(x-1) + f(x-2) if x > 2
4. A recursive function must have a base case in addition to recursive calls in order to ensure termination. The base case is the conditional part (p(x) in the general form) where the function returns a value without recursion.
5. A recursive function may have multiple base cases. Also, the recursive call may be for a value other than one less than the original input.
6. Recursive functions can be very efficient for solving problems that exhibit self-similarity or repetition. However, recursion is not always the most computationally efficient approach if the function makes many repeated calls with the same inputs. In such cases, an iterative approach may be better.